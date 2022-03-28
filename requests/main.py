import requests as rq
import re
import json
import pandas as pd


# Settings
START_URL = 'https://www.montmere.com/jsjs.js'
RETRY_TIMES = 2

raw_data = None
df = pd.DataFrame()

for T in range(0, RETRY_TIMES):
    # Call Javascript URL
    r = rq.get(START_URL)

    try:
        # Get raw data
        raw_data = re.findall('var data = \[(.*?)\]', r.text, re.DOTALL)
        
        # Get columns data
        makes = re.findall('make: \"(.*?)\",', raw_data[0])
        models = re.findall('model: \"(.*?)\",', raw_data[0])
        years = re.findall('year: (.*?),', raw_data[0])
        
        # Format Data
        df = pd.DataFrame(
            {'makes': makes,
            'models': models,
            'years': years
            })

        # Stop retrying if data was extracted
        if not df.empty:
            break
                
    except:
        pass

# Output to csv
if not df.empty:
    df.to_csv('output.csv')