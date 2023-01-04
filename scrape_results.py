import requests
from typing  import List
import pandas
import csv
from urllib.request import urlopen
from selenium import webdriver
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
class Command(BaseCommand):
    help='load data'
    def handle(self,*args, **kwargs):
     urls=self.construct_urls()
     k=1
           #you need to install pandas and selenuim  
           #link to download your chromedriver:
           #https://chromedriver.chromium.org/downloads
           #download the same  versoin of your  chrome
     driver=webdriver.Chrome('chromedriver floder path')
     for url in urls:
       driver.get(url)    
       print(url)  
       html = driver.page_source  
       df=pandas.read_html(html)
       d=df[70]
       d=d.drop([0,1,3, 5, 7,9])
       d=d.drop(d.columns[[2, 3, 4,5]], axis=1)    
       print(d)
       doc='#path were to add infos'+str(k)+'.csv'
       d.to_csv(doc,header=False,index=False)
       k=k+1
    def construct_urls(self) ->List[str]:
         
         page= requests.get("http://www.annonce-algerie.com/AnnoncesImmobilier.asp")

         soupi =BeautifulSoup (page.content, 'html.parser') 
         links= soupi.find_all('a', href=True)

         details_annonces=[]

         for link in links:


          if "DetailsAnnonceImmobilier" in link['href']: 
              details_annonces.append(f" {'http://www.annonce-algerie.com/'}{link['href']}")


         
         return details_annonces





