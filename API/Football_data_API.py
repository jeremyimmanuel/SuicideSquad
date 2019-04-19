#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json


# In[9]:


API_KEY = '4915aca12c724fa2ae27a0230086ef1d'
ENDPOINT = 'https://api.football-data.org/v2/competitions/' #/v2/competitions/


# In[10]:


headers = {'X-Auth-Token' : API_KEY}
response = requests.get(ENDPOINT, headers = headers, )


# In[11]:


response.json()


# In[ ]:




