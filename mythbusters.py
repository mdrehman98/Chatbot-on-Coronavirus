from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
my_url='https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters'

uclient=uReq(my_url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")
info=page_soup.findAll("div",{"class":"sf-content-block content-block"})
informations=info[11:24]
filename="myth.csv"
f=open(filename,"w")
headers="query,response \n"
f.write(headers)
for information in informations:
    header=information.h2.text
    text=information.p.text
    
    print(header)
    print(text)

    f.write(header.replace(",","")+ "," +text.replace(",","")+ "\n")

f.close()    