#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests


# In[ ]:





# In[9]:


urls = ['https://covid19.who.int/WHO-COVID-19-global-data.csv',
        'https://covid19.who.int/who-data/vaccination-data.csv']


# In[ ]:





# In[10]:


for i, url in enumerate(urls):
    
    req = requests.get(url)
    url_content = req.content
    
    csv_file = open('downloaded'+str(i)+'.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
    


# In[ ]:





# In[11]:


print('files extracted successfully!!!')


# In[ ]:




