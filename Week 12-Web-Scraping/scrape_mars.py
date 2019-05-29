#!/usr/bin/env python
# coding: utf-8

# In[32]:


from pymongo import MongoClient
from pprint import pprint

from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs


import os
import pandas as pd
import time


# In[33]:


conn = 'mongodb://localhost:27017'
client = MongoClient(conn)


# In[34]:


db = client.pymongo_test


# In[35]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[36]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[37]:


html = browser.html
soup = bs(html, 'html.parser')

news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")


# In[38]:


featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit'
browser.visit(featured_image_url)


# In[39]:


mars_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_url)


# In[40]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")


# In[41]:


mars_weather =soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[42]:


mars_facts_url ='https://space-facts.com/mars/'
browser.visit(mars_facts_url)


# In[43]:


tables = pd.read_html(mars_facts_url)
tables


# In[44]:


type(tables)


# In[45]:


df_mars_facts = tables[0]
df_mars_facts.columns


# In[46]:


df_mars_facts = tables[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[48]:


html_table = df.to_html()
html_table


# In[ ]:


df.to_html('table.html')


# In[ ]:


get_ipython().system(' start table.html')


# In[ ]:


mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_hemispheres_url)


# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]


# In[ ]:


from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Para: {news_paragraph}")


    # In[38]:


    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit'
    browser.visit(featured_image_url)


    # In[39]:


    mars_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_url)


    # In[40]:


    html_weather = browser.html
    soup = bs(html_weather, "html.parser")


    # In[41]:


    mars_weather =soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)


    # In[42]:


    mars_facts_url ='https://space-facts.com/mars/'
    browser.visit(mars_facts_url)


    # In[43]:


    tables = pd.read_html(mars_facts_url)
    tables


    # In[44]:


    type(tables)

    df_mars_facts = tables[0]
    df_mars_facts.columns


    # In[46]:


    df_mars_facts = tables[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    df_mars_facts.set_index(["Parameter"])


    # In[48]:


    html_table = df.to_html()
    html_table

    df.to_html('table.html')

    get_ipython().system(' start table.html')


    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

    mars_data = {

    "news_title": news_title,
    "news_paragraph": news_paragraph,
    "featured_image_url": featured_image_url,
    "mars_weather": mars_weather,
    "hemisphere_image_urls": hemisphere_image_urls
    }


    browser.quit()

    return mars_data
