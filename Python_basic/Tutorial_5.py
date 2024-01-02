import pandas as pd
import numpy as np

#dataframes
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Column1","Column2","Column3","Column4"])
df.head()

## Accessing the elements
df.loc['Row1']
df.iloc[0:3,0:2]

## Take the elements from the Column2
df.iloc[:,1:]

#convert Dataframes into array
df.iloc[:,1:].values

