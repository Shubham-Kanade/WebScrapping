#!/usr/bin/env python
# coding: utf-8

# In[4]:

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.century21.com/real-estate/santa-clara-ca/LCCASANTACLARA/?sa=CCACUPERTINO")
c = r.content

soup = BeautifulSoup(c, "html.parser")

print(soup.prettify())

all = soup.select('div .infinite-item.property-card')  #"all" contains all HTML elements of the page of interest

print(len(all))


# In[5]:


li = []
for item in all:
    d = {}
    d["Price"] = item.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ", "")
    d["Address"] = item.find_all("div", {"class":["property-address","property-city"]})[0].text.replace("\n","")
    d["Locality"] = item.find_all("div", {"class":["property-address","property-city"]})[1].text.replace("\n","")
    
    try:
        d["Beds"] =item.find("div", {"class": "property-beds"}).find("strong").text
    
    except:
        #print("no beds data available")
        d["Beds"] = None
    try:
        d["Baths"] =item.find("div", {"class": "property-baths"}).find("strong").text
    
    except:
        d["Baths"] = None
    try:
        d["Half Baths"] =item.find("div", {"class": "property-half-baths"}).find("strong").text
    
    except:
        d["Half Baths"] = None
        
    try:
        d["Area(sq-ft)"] = item.find("div",{"class":"property-sqft"}).find("strong").text
    except:
        d["Area(sq-ft)"] = None
    
    li.append(d)  
li


# In[6]:


import pandas
df = pandas.DataFrame(li)
df.to_csv("Properties Report.csv")
df


# In[ ]:




