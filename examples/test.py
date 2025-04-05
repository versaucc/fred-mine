from audioop import findfactor
from fredapi import Fred
import pandas as pd 
# import matplotlib as plt
from IPython.core.pylabtools import figsize
import datetime, os, dotenv

pd.options.display.max_colwidth = 60
figsize(20, 5)

fred = Fred(os.getenv('FRED_API_KEY'))

def test_tag_search():
    tags = 'usa;food;oecd'
    exclude_tags = 'alcohol;quarterly'
    print('testing search_by_tags with inclusion only;')
    df = fred.search_by_tags(tags)
    print(df)
    print("testing parse_all_series.")
    df_list = fred.parse_all_series(df)
    for item in df_list:
        print(item['title'])
        # item['observation_data'].to_csv(item['series_id'] + '_data.csv' )
    print('\n\ntest 1 complete.\n\n')

    del df

def test_search():
    prompt = 'Inflation Women'
    print('testing search(): \n\n')
    df = fred.search(prompt)

    print(df)
    print('\n\ntesting parse_all_series: \n\n')
    #df_list = fred.parse_all_series(df)
    #for item in df_list:
        #print(item['title'])
        # item['observation_data'].to_csv(item['series_id'] + '_data.csv' )

    del df 

def test_all():
    # test_tag_search()
    test_search()



test_all()