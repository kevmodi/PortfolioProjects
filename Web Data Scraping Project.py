#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from a Real Website
# - Utilized pandas and web scraping techniques to extract data from a website and return the data as a csv file

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


soup.find('table', class_= 'wikitable sortable')


# In[5]:


table = soup.find_all('table')[1]


# In[6]:


print(table)


# In[7]:


world_titles = table.find_all('th')


# In[8]:


world_titles


# In[9]:


world_table_titiles = [title.text.strip() for title in world_titles]

print(world_table_titiles)


# In[10]:


import pandas as pd


# In[11]:


df = pd.DataFrame(columns = world_table_titiles)

df


# In[12]:


column_data = table.find_all('tr')


# In[13]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data


# In[14]:


df


# In[15]:


df.to_csv(r'Downloads\companies.csv', index = False)

