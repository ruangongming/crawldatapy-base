import requests
import lxml
from bs4 import BeautifulSoup


# url = 'https://yellowpages.com.eg/en/search/fast-food'
url2 = 'https://dantri.com.vn/suc-khoe.htm'
while True:
    r = requests.get(url2)
    soup = BeautifulSoup(r.content, "html.parser")
    # pages = soup.find_all('ul', class_='pagination center-pagination')

    pages2 = soup.find('div', {'class': 'pagination'})
    # print(pages2)
    a_data = pages2.find("a", {'class': "page-item next"})
    print("https://dantri.com.vn/" + a_data['href'])

    # print(a_data['href'])
    break
    # for page in pages2:
    #     # nextpage = page.find('li', class_='waves-effect').find('a', {'aria-label': 'Next'})
    #     nextpage2 = page.find('div', class_='pagination').find('a', {'page-item next': 'Trang tiếp'})
    #     if nextpage2:
    #         uu = nextpage2.get('href')
    #
    #         # url = 'http://www.yellowpages.com.eg' + str(uu)
    #         url2 = 'https://dantri.com.vn/suc-khoe/trang-' + str(uu)
    #         print(url2)
    #     else:
    #         break