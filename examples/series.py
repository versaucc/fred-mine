from fredapi import Fred
import pandas as pd 
# import matplotlib as plt
from IPython.core.pylabtools import figsize
import dotenv, os


# Test implementation of fred data in json format 
# Params: API Key, Path to data, timeframe, filename to store
# Request formats: 
print('hello world')
dotenv.load_dotenv()
api = os.getenv("FRED_API_KEY")
fred = Fred(api) 


pd.options.display.max_colwidth = 60
figsize(20, 5)

df = fred.search_by_category('gdp').T
# df = df.iloc[[3,4,5,7,9,12,13]] # May want to keep data frame whole

df_sorted = df.loc['popularity'].sort_values(ascending=False)
df = df[df_sorted.index].T

print(df)
df.to_csv('gdp_search.csv')

