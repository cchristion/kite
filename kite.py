import re
import os
import json
import random
import requests
import multiprocessing as mp

from time import sleep
from tika import parser

from config import directory, search, retry, result_file

def queue_files(directory):
    print(f"queuing files for {directory}")
    for dirpath, _, file_group in os.walk(directory):
        for file in file_group:
            file = os.path.abspath(os.path.join(dirpath, file))
            file_q.put(file)
    print(f'files found: {file_q.qsize()}')

def get_content(file):
    content = None
    for i in range(1, retry):
        try:
            sleep(random.randint(0, i))
            if (i%10 == 0):
                print(f'On {i}th attempt...')
            content = parser.from_file(file)
            return content
        except (ConnectionError, RuntimeError
                , requests.exceptions.ConnectionError
                , requests.exceptions.ChunkedEncodingError
                , requests.exceptions.ReadTimeout
               ):
            if i <= retry:
                continue
        except Exception as e:
            print(f'file: \'{file}\'\nError type: {type(e)}\nError message: {e}\n')
        break

def search_content(file, content):
    result = {}
    for key in search:
        hit = search[key].search(str(content))
        if hit:
            if key in result:
                result[key].append(file)
            else:
                result[key] = [file]
    if result:
        result_q.put(result)

def worker(_):
    while not file_q.empty():
        file = file_q.get()
        print(f"Processing: ...{file[-100:]}")
        content = get_content(file)
        search_content(file, content)

if __name__ == "__main__":

    _ = parser.from_buffer('')

    file_q = mp.Queue()
    result_q = mp.Queue()

    for key in search:
        search[key] = re.compile(search[key], re.IGNORECASE)

    queue_files(directory)
    print('procesing...')
    with mp.Pool() as pool:
        pool.map(worker, range(len(os.sched_getaffinity(0))))

    result = {}
    while not result_q.empty():
        entry = result_q.get()
        for key in entry:
            if key in result:
                result[key] += entry[key]
            else:
                result[key] = entry[key]

    with open(result_file, 'w') as file:
        file.write(json.dumps(result))

    print('Completed.')
