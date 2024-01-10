import pandas as pd

# Read Json to CSV
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
pd.read_json(Data)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df.head()


# convert Json to csv
df.to_csv('wine.csv')

# convert Json to different json formats
df.to_json(orient="index")
df.to_json(orient="records")

# Reading HTML content
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)
dfs[0]

url_mcc = 'https://en.wikipedia.org/wiki/Mobile_country_code'
dfs = pd.read_html(url_mcc, match='Country', header=0)
dfs[0]

# Reading Excel Files
df_excel=pd.read_excel('Excel_Sample.xlsx')
df_excel.head()

#Pickling
df_excel.to_pickle('df_excel')
df=pd.read_pickle('df_excel')
df.head()
