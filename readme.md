
# Montmere Test

There's two methods available for scraping this site in `requests` and `selenium` folders.
First one uses requests module and extract data without even login in.
Second one uses Selenium, it logs into the site and retries if there's any errors.

## Run

They can be executed with each `main.py` file contained in each folder:
```
python3 requests/main.py
```
```
python3 selenium/main.py
```

## Output

Results will be written in `output.csv` file in the current directory.


## Requirements

Requirements for creating a Python 3 enviroment for both methods are specified in `requirements.txt` file

> **Note**: For avoiding compatibilty issues **ChromeDriverManager** package for Selenium is being used.