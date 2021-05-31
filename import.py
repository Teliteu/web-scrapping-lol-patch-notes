import requests
from bs4 import BeautifulSoup, element
import datetime

number=int(input("Number of links?: "))


while (number!=0):

     url = input("Link please: ")

     req = requests.get(url)

     soup = BeautifulSoup(req.content,"lxml")

     dateTime = soup.select("time")[0]["datetime"]
     print(dateTime)

     note=soup.find("title")
     print(note.next_element)

     lista_camp = soup.find_all("div",class_="patch-change-block white-stone accent-before")

     for lista_campp in lista_camp:
          lista = lista_campp.find_all("a",href_="")
          for lista_camppp in lista:
              for lista_campppp in lista_camppp.strings:
                print(lista_campppp)
     number=number-1
Else: print("Finish baby!")



