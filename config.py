""" This is a config file for Kite.py """

### Basic ###

# Directory path to search
directory = '~/dir/path/to/search'

# File path to store results
# Results will be stored as json file
result_file = "~/file/path/to/store/result.json"

# search dictionary to store keyword as key and regex pattern as value
# kite.py will search for all the entries of this dictionary
search = {'Hello': r'Hello'
          # , 'World': r'World'
         }

### Advanced ###

# Number of retries to get content from tika
retry = 10**5
