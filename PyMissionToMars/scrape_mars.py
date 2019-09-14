#!/usr/bin/env python3
# coding: utf-8

import os, sys
from bs4 import BeautifulSoup
import pandas as pd
import requests, splinter

news_title = ""
news_description = ""
news_p = ""
featured_image_url = ""
mars_weather = ""
mars_facts_table = ""
hemisphere_image_urls = []

# ### NASA Mars News

# request url for mars news api
json_url=('https://mars.nasa.gov/api/v1/news_items/'
          '?page=0&per_page=10'
          '&order=publish_date+desc%2Ccreated_at+desc'
          '&search='
          '&category=19%2C165%2C184%2C204'
          '&blank_scope=Latest')

response = requests.get(json_url)
if response.status_code == 200:
    a=response.json()
    news_item = a.get('items')[0]
    news_title = news_item.get('title')
    news_description = news_item.get('description')
    news_p = BeautifulSoup(news_item.get('body'), 'html.parser').p.get_text()
    pass

print("Title:", news_title, end="\n\n")
print("Description:", news_description, end="\n\n")
print("Blurb:", news_p, end="\n\n")

# ### JPL Mars Space Images - Featured Image

# NOTE: some of the featured images didn't have associated 'hires' links; 
#   so I used the default wallpaper link

url=('https://www.jpl.nasa.gov/spaceimages/'
     '?search='
     '&category=Mars')


response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser').find('article', 'carousel_item')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.attrs['style'].split("'")[1]
    pass


print("Featured Image URL:", featured_image_url, end='\n\n')


# ### Mars Weather
url=('https://twitter.com/marswxreport'
     '?lang=en')

brws = splinter.Browser("chrome", executable_path="/home/burned/.local/bin/chromedriver")
brws.visit(url)
html = brws.html
brws.quit()

soup = BeautifulSoup(html, 'html.parser')
for s in soup.find_all('div', 'tweet'):
    # this is *dumb*... should be using twitter's retarded api (which is also *dumb*)
    #   ... so maybe this is less dumb?
    txt=s.get_text()
    if txt.find('InSight sol') >= 0:
        mars_weather = txt[txt.find('InSight sol'):txt.find('hPa')+3]
        break

print("Mars Weather:", mars_weather, end='\n\n')


# ### Mars Facts

url='https://space-facts.com/mars/'
df = pd.read_html(url)
df[0].set_index('Mars - Earth Comparison', inplace=True)
mars_facts_table = df[0].to_html()

# ### Mars Hemispheres

base_url='https://astrogeology.usgs.gov/'
url=(base_url+
     'search/results'
     '?q=hemisphere+enhanced'
     '&k1=target'
     '&v1=Mars')

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for itm in soup.find_all('div', 'item'):
        # extract title
        title = itm.find('h3').get_text().replace(' Enhanced', '')
        img_url = ""
        
        # hunt down link to original image
        download_link = base_url + itm.find('a')['href']
        resp = requests.get(download_link)
        if resp.status_code == 200:
            nsoup = BeautifulSoup(resp.text, 'html.parser')
            dls = nsoup.find('div','downloads')
            for litm in dls.find_all('li'):
                link = litm.find('a')
                # is this the link for the original?
                if link.text == 'Original':
                    # then, store it and be done with this mess.
                    img_url = link['href']
                    break
        
        print("Title:", title)
        print("Image URL:", img_url, end='\n\n')
        
        # push title and url onto the end of our growing list
        hemisphere_image_urls.append(
            dict(title=title, img_url=img_url))
    pass

