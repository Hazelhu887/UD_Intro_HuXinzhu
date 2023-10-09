
from bs4 import BeautifulSoup4
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
for i in range(0,1300,35):
    url = 'https://music.163.com/discover/playlist/?cat=欧美&order=hot&limit=35&offset='+str(i)
    reponse = requests.get(url=url, headers=headers)
    html = reponse.text
    #print(html)

    soup=BeautifulSoup(html,'html.parser')
    ids=soup.select('.dec a')
    #print(ids)
    lis=soup.select('#m-pl-container li')
    #print(lis)

    for j in range(35):
        url=ids[j]['href']
        title=ids[j]['title']
        print(url,title)

        with open('anny.csv','a+',encoding='utf-8-sig') as f:
            f.write(url+','+title+'\n')


