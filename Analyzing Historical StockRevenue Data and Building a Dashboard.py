#!/usr/bin/env python
# coding: utf-8

# ### Analyzing Historical Stock/Revenue Data and Building a Dashboard

# In[24]:


import yfinance as yf

tesla = yf.Ticker("TSLA")

tesla_data = tesla.history(period="max")

tesla_data.head()


# In[25]:


tesla_data.tail()


# In[10]:


import requests
from bs4 import BeautifulSoup

search_url = "https://www.google.com/search?q=tesla+quarterly+revenue"
response = requests.get(search_url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))



# In[23]:


import yfinance as yf

gamestop = yf.Ticker("GME")

gamestop_data = gamestop.history(period="max")

gamestop_data.head()


# In[22]:


gamestop_data.tail()


# In[12]:


import requests
from bs4 import BeautifulSoup

search_url = "https://www.google.com/search?q=gamestop+quarterly+revenue"
response = requests.get(search_url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))


# In[15]:


import plotly.express as px

fig = px.line(tesla_data, x=tesla_data.index, y="Close", title="Tesla Stock Closing Prices Over Time")
fig.show()


# In[16]:


import plotly.express as px

fig = px.line(gamestop_data, x=gamestop_data.index, y="Close", title="GameStop Stock Closing Prices Over Time")
fig.show()


# In[ ]:




