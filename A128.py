from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
#browser = webdriver.Chrome()
#browser.get(START_URL)
browser = requests.get(START_URL)


time.sleep(10)

stars_data = []

soup = BeautifulSoup(browser.text, "html.parser")

table = soup.find_all('table',attrs={'class':'wikitable sortable'})

temp = []
array = []
rows = table[1].find_all('tr')

for tr in rows :
    tds = tr.find_all('td')
    temp = []
    for td in tds :
        row = td.text.rstrip()
        temp.append(row)
    array.append(temp)

star_names=[]
distance=[]
mass=[]
radius=[]

print(array)

for i in range (1,len(array)):
    star_names.append(array[i][0])
    distance.append(array[i][5])
    mass.append(array[i][7])
    radius.append(array[i][8])

headers = ['star_name','distance','mass','radius']

df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=headers)
df.to_csv('dwarf_stars.csv')
