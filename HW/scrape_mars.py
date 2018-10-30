
# coding: utf-8

# In[39]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
browser = Browser('chrome')


# In[40]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
url2 = 'https://space-facts.com/mars/'
url3 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url3)


# In[41]:


# Retrieve page with the requests module
response = requests.get(url)
tables = pd.read_html(url2)
html2 = browser.html
soup2 = bs(html2, 'html.parser')
imgsource = soup2.find_all('div', class_='carousel_items')
parenturl = 'https://www.jpl.nasa.gov'


# In[42]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')
df = tables[0]
df.columns = ['Fact','Value']
df.head()


# In[43]:


# Loop through returned results
for result in imgsource:
    # Error handling
    try:
        # Identify and return article title
        featured_image_url = parenturl + result.a['data-fancybox-href']

        # Print results only if title, price, and link are available
        if (featured_image_url):
            print(featured_image_url)
            
    except AttributeError as e:
        print(e)


# In[44]:


featured_image_url


# In[45]:


df.set_index('Fact', inplace=True)
df.head()


# In[46]:


html_table = df.to_html()
html_table


# In[47]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[48]:


# results are returned as an iterable list
contentresults = soup.find_all('div', class_="rollover_description_inner")
titleresults = soup.find_all('div', class_="content_title")


# In[49]:


# Loop through returned results
for result in titleresults:
    # Error handling
    try:
        # Identify and return article title
        result.find('a', class_="result-title").text = result.a.text

        # Print results only if title, price, and link are available
        if (title):
            print(title)
            
    except AttributeError as e:
        print(e)


# In[50]:


# Loop through returned results
for result in contentresults:
    # Error handling
    try:
        # Identify and return article title
        content = result.text

        # Print results only if title, price, and link are available
        if (content):
            print(content)
            
    except AttributeError as e:
        print(e)

