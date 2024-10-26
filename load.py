#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3 as db


# In[ ]:





# In[7]:


database = "./covid19.sqlite"
conn = db.connect(database)


# In[ ]:





# In[5]:


transform_df = pd.read_csv("./transformed_data.csv")
transform_df.head(15)


# In[8]:


transform_df.to_sql(name = 'covid19Data', con=conn)
conn.close()


# In[ ]:





# In[10]:


con = db.connect(database)

cur = con.cursor()

for row in cur.execute('SELECT * FROM covid19Data;'):
    print(row)

con.close()


# In[ ]:




