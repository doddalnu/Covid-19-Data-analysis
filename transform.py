#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("./downloaded0.csv")
df.head(20)
df.columns


# In[ ]:





# In[4]:


df1 = pd.read_csv("./downloaded1.csv")
df1.head(20)
df1 = df1.rename(columns={'COUNTRY': 'Country'})
df1.columns


# In[ ]:





# In[5]:


merged_df = pd.merge(df, df1, on='Country', how='inner')
merged_df.head(20)
merged_df.columns


# In[ ]:





# In[6]:


req_columns = ['Country', 'TOTAL_VACCINATIONS', 'Date_reported', 'Country_code',
       'WHO_region', 'Cumulative_cases', 'Cumulative_deaths']

# ['Country', 'TOTAL_VACCINATIONS', 'Date_reported', 'Country_code',
#        'WHO_region', 'New_cases', 'Cumulative_cases', 'New_deaths',
#        'Cumulative_deaths']


# In[ ]:





# In[7]:


final_df = merged_df[req_columns]
final_df.head(20)


# In[ ]:





# In[8]:


max_dates = ['2020-12-31', '2021-12-31', '2022-12-31', '2023-10-25']

filtered_df = final_df[final_df['Date_reported'].isin(max_dates)]
filtered_df


# In[ ]:





# In[9]:


# filtered_df['Date_reported'] = filtered_df['Date_reported'].apply(lambda x: x.replace(year = pd.to_datetime(x)))

filtered_df.loc[:, ['Date_reported']] = filtered_df['Date_reported'].apply(lambda x: pd.to_datetime(x).year)
filtered_df.head(15)
# filtered_df.head(15)
# filtered_df.loc[:, ['Date_reported']] = filtered_df['Date_reported'].apply(lambda x: print(x.year))


# In[ ]:





# In[10]:


filtered_df.to_csv('transformed_data.csv', index=False)

print("transformed data sucessfully!!!")


# In[ ]:




