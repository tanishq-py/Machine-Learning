import pandas as pd
import numpy as np

df=pd.read_csv('file name')
df.head()

df.info() #infro about file
df.describe() #describe different stats about file

#Get the unique category counts
df['X0'].value_counts()

df[df['y']>100]

df.corr()


lst_data=[[1,2,3],[3,4,np.nan],[5,6,np.nan],[np.nan,np.nan,np.nan]]
df=pd.DataFrame(lst_data)
df.head()
df.dropna(axis=1)


df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two', 'three'])
df.head()
df2=df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
df2.dropna(axis=0) 
pd.isna(df2['one'])
df2['one'].notna()
df2.fillna('Missing')
df2['one'].values


#CSV
from io import StringIO, BytesIO
import pandas as pd

data = ('col1,col2,col3\n'
            'x,y,1\n'
            'a,b,2\n'
            'c,d,3')
type(data) #str
# pd.read_csv(StringIO(data))

## Read from specific columns
# df=pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3'])
df.to_csv('Test.csv')

