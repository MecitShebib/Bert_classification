import requests
from bs4 import BeautifulSoup
import pandas as pd
links = ["bilimkurgu","ekonomi","islam","polisiye","romantik","saglik","spor"]
ozetler = []
kategory = []
for h in range(len(links)):
    for j in range(22):
        url = ("https://www.kitapsepeti.com/"+links[h]+"?pg="+ str(j+1))
        print(url)
        src = requests.get(url).content
        soup = BeautifulSoup(src, "lxml")
        div = soup.find_all("div", {'class':'col-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 mb-2 product-item effect-wrapper'})
        for i in range(len(div)):
            link = ("https://www.kitapsepeti.com"+div[i].find("a").attrs['href'])
            src = requests.get(link).content
            soup = BeautifulSoup(src, "lxml")
            try:
                ozet = soup.find("div", {'class':'product-fullbody'}).text
                ozet = ozet.replace('\n', '')
                ozetler.append(ozet)
                if links[h] == "islam":
                    kategory.append("İslam")
                if links[h] == "bilimkurgu":
                    kategory.append("Bilim Kurgu")
                if links[h] == "spor":
                    kategory.append("Spor")
                if links[h] == "saglik":
                    kategory.append("Sağlık")
                if links[h] == "ekonomi":
                    kategory.append("Ekonomi")
                if links[h] == "polisiye":
                    kategory.append("Polisiye")
                if links[h] == "romantik":
                    kategory.append("Romantik")
            except:
                None
        data = {"kategory":kategory, "ozetler":ozetler}
        df=pd.DataFrame(data)
        df.to_csv('/Users/MK/Desktop/tum.csv', index=False,header=True)
