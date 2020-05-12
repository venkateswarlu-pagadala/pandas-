#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np


# In[23]:


#here we are using the particular column and apply the aggregation function
#here we are using the NamedAgg function
animals = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'],
                        'height': [9.1, 6.0, 9.5, 34.0],
                        'weight': [7.9, 7.5, 9.9, 198.0]})
    
animals.groupby(['kind',"height","weight"]).agg(
                        agg1=pd.NamedAgg(column="height",aggfunc="max"),
                        agg2=pd.NamedAgg(column="height",aggfunc="min"),
                        agg3=pd.NamedAgg(column="weight",aggfunc=np.mean))


# In[24]:


#this is the another method here we are using the overall dataset
animals.groupby("kind").agg(["max","min","mean"])
   


# In[28]:


#here we are using the normal tuple
animals.groupby("kind").agg(
    height=('height',"max"),
    weight=("height","min"),
    mean=("weight","mean"))


# In[33]:


#here we apply series datastructure on aggregate function
animals.groupby("kind").height.agg(max="max",min="min")


# In[50]:


#here we are using the many number of lambda functions
animals.groupby('kind').height.agg([lambda x:x.iloc[0],lambda x:x.iloc[-1],lambda x:x.iloc[1]])


# In[51]:


#here we are using the lambda functions and by using the mathematical functions
animals.groupby('kind').height.agg([lambda x:x.iloc[1]-x.iloc[-1],lambda x:x.iloc[0]-x.iloc[1]])


# In[58]:


#pd.MultiIndex.from_product([['a', 'abc'], range(500)])


# In[57]:


#pd.MultiIndex.from_product([['a','b','c'],range(10)])


# In[56]:


pd.MultiIndex.from_product([["venkat","nari"],range(5)])


# In[76]:


#here we are using the json instead of using the DataFrame
from pandas.io.json import json_normalize
data=[{"name":{"venkat":'python',"nari":'pyspark'},'age':{1,2,3},"marks":{1,2,3,4}}]
json_normalize(data,max_level=1)


# In[85]:


#here we are using the json instead of using the DataFrame
from pandas.io.json import json_normalize
data=[{"name":{"venkat":'python',"nari":'pyspark'},'age':{1,2,3},"marks":{1,2,3,4}}]
json_normalize(data)


# In[86]:


from pandas.io.json import json_normalize
data={"name":{"venkat","nari"},"age":{1,2},"marks":{34,33}}
pd.DataFrame(data)


# In[95]:


df = pd.DataFrame([1,2,3,4], index=['2019-01-01','2019-02-02','2019-03-03','2019-04-04'])
df


# In[106]:


df = pd.DataFrame([0,1], index=pd.DatetimeIndex(['2019-01-01','09-08-1999',], tz='US/Pacific'))
df


# pd.MultiIndex(levels=[[np.nan, None, pd.NaT, 128, 2]],
#                   codes=[[0, -1, 1, 2, 3, 4]])
#    
# 
# 
# 

# **MEDIUM PANDAS SERIES**
# 

# In[25]:


data=pd.Series([1,2,3,4,5],index=[5,6,7,8,9])
data[data>2]
data
 


# In[28]:


data=pd.Series({"name":"venkat","age":10})
data


# In[34]:


data.name="venkat"
data.index.name="nari"
data


# In[38]:


data.index=[11,22]
data


# **MEDIUM APP DATAFRAMES**

# In[50]:


df = pd.DataFrame({  'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
                     'population': [17.04, 143.5, 9.5, 45.5],
                     'square': [2724902, 17125191, 207600, 603628]})
df.index=["a","b","c","d"]
df.index.name="venkat gadu"
df


# In[41]:


df['country']


# **Row access using index can be performed in several ways:**
# **1.using .loc and providing index label**
# **2.using .iloc and providing index number**
# 

# In[55]:


df.loc["a",'country']


# In[65]:


df.loc["a":"d","country":"population"]


# In[66]:


df.iloc[1:,2:]


# In[70]:


df.loc[["a",'b',"c"],"country"]


# In[71]:


df.loc[:,["population","square"]]


# In[77]:


df[df.square>10] [["population","country",'square']]


# In[78]:


df[df["square"]>10]["population"]


# **reset index**

# In[80]:


df.reset_index()


# **CREATE NEW COLUMN**

# In[82]:


df["average"]=df['square']+df["population"]
df


# **DROP COLUMNS**

# In[87]:


df.drop(["average"],axis="columns")


# In[88]:


df.drop(["average"],axis=1)


# In[90]:


df.drop(["a"],axis="index")


# In[91]:


df.drop(["b"],axis=0)


# In[94]:


del df["square"]
df


# **RENAME COLUMNS**

# In[96]:


df.rename(columns={'country':"countries_in_the_world",'population':"world_population"})


# **PICKLE FILES**

# In[107]:


df=pd.DataFrame({"serial_no":range(5),"link":range(5)})
df


# In[109]:


data1=pd.to_pickle(df,"dummy.pkl")
data1


# In[111]:


df=pd.read_pickle("dummy.pkl")
df


# In[112]:


ds=pd.Series([1,2,3,4,5])
ds


# In[115]:


ds=pd.to_pickle(ds,"dummy1.pkl")
ds


# In[120]:


ds=pd.read_pickle("dummy1.pkl")
ds


# In[156]:


df=pd.DataFrame({"name":["venkat","nari","joo"],"age":[1,2,3],"marks":[12,12,12]})
df


# In[137]:


df.to_csv("venkat.csv")
df


# In[154]:


ds=pd.read_table("venkat.csv",sep=',')
ds


# In[ ]:




