'''
import glassdoor_scraper as gs
import pandas as pd

df = gs.get_jobs('Data Scientist', 15, False, 3)
df
'''
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

PATH = '/Users/ghunemi/Desktop/datascience_salary/chromedriver'
keyword = 'data scientist'

l=list()
o={}

url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'

driver=webdriver.Chrome(PATH)

driver.get(url)

driver.maximize_window()
time.sleep(2)

resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')


count = 1
while count < 25:
    allJobsContainer = soup.find("ul", {"class": "css-7ry9k1"})

    allJobs = allJobsContainer.find_all("li")
    for job in allJobs:
        try:
            o["name-of-company"]=job.find("div",{"class":"d-flex justify-content-between align-items-start"}).text
        except:
            o["name-of-company"]=None

        try:
            o["name-of-job"]=job.find("a",{"class":"jobLink css-1rd3saf eigr9kq2"}).text
        except:
            o["name-of-job"]=None


        try:
            o["location"]=job.find("div",{"class":"d-flex flex-wrap css-11d3uq0 e1rrn5ka2"}).text
        except:
            o["location"]=None


        try:
            o["salary"]=job.find("div",{"class":"css-3g3psg pr-xxsm"}).text
        except:
            o["salary"]=None

        l.append(o)

        o={}
        count += 1

        try:
            driver.findElement(By.ID,'nextButton').click();

        except:
            print('ZBY')

df = pd.DataFrame(l)
df.to_csv('jobs.csv', index=False, encoding='utf-8')

#<button class="page  css-1hq9k8 e13qs2071" data-test="pagination-link-2" tabindex="0" type="button">2</button>

#<button class ="page  css-1hq9k8 e13qs2071" data-test="pagination-link-3" tabindex="0" type="button" > 3 < / button >
