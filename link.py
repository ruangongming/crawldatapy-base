import pandas as pd
import requests
from bs4 import BeautifulSoup

def links():
# url cần lấy link
    url = "https://dantri.com.vn/suc-khoe.htm"

    page = requests.get(url=url)
    if page.status_code != 200:
        raise("can not connect to url")

    soup = BeautifulSoup(page.content, "html.parser")

    div_data = soup.find("div", {"class": "article list"})

#show toàn bộ link có trong page
    a_data = div_data.find_all("a", href=True)
    for a in a_data:
        print("https://dantri.com.vn/" + a['href'])


    # i = range(1, len(a_data) + 1)

    # data_df = pd.DataFrame({'title': a_data}, index=None)
    # data_df.to_csv('reviews.txt', sep='\t')

    # print("Danh sách các link:", a)

link = links()