import csv
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
browser = webdriver.Chrome('C:\\Users\Major League Hacking\Downloads\chromedriver_win32\chromedriver')
browser.get('https://www.facebook.com/pg/secretsuchicago/posts/?ref=page_internal/')
SCROLL_PAUSE_TIME = 0.2
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    #Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#browser.execute_script("window.scrollTo(0,10000000)")
html = browser.page_source

soup = BeautifulSoup(html,'lxml')

file = open('uchicagosecrets.csv','w')
writer = csv.writer(file)

writer.writerow(['PostText','Date'])

for userContentWrapper in soup.find_all('div',class_='userContentWrapper'):
    content = userContentWrapper.find(class_='userContent').find('p').findNext('p').text
    date = userContentWrapper.find('abbr')['title']

    writer.writerow([content.encode('utf-8'),date.encode('utf-8')])

file.close()
browser.close()