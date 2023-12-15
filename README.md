# kite
> Python Script for Extracting Content and Parsing Using Tika and regex

This Python script uses the Tika library to extract content from various types of files and parses the extracted content using regular expressions. The script also utilizes multiprocessing and a queue model to efficiently process large numbers of files.

### Features

- Uses Tika to extract content from various types of files (e.g., PDF, Word documents, HTML)
- Parses extracted content using regular expressions
- Utilizes multiprocessing and a queue model for efficient processing of large numbers of files

## Installing
1. Getting files from github

		git clone https://github.com/fros7yx/kite.git
		cd kite

2. Environment Setup

		conda create --no-default-packages --name kite python=3.11.5
		conda activate kite
		pip install -r requirements.txt

3. Edit config.py as required

4. Run python script

- With multiprocessing

		python kite.py

- Without multiprocessing

		python kite.simple.py

