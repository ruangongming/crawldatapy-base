import requests
from bs4 import BeautifulSoup

url2 = 'https://dantri.com.vn/suc-khoe.htm'
r = requests.get(url2)
soup = BeautifulSoup(r.content, "html.parser")

pages2 = soup.find('div', {'class': 'pagination'})

a_data = pages2.find("a", {'class': "page-item next"})
print("https://dantri.com.vn" + a_data['href'])

