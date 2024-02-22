import requests
from bs4 import BeautifulSoup

# url trang cần đọc
ulr_base = "https://dantri.com.vn/suc-khoe/"


#lọc toàn bộ số trang max = 30
def get_all_page(url_base):
    data_link = ["https://dantri.com.vn/suc-khoe.htm"]
    count = 1

    while True:
        count += 1
        url = url_base + f"trang-{count}.htm"
        print(url)
        page = requests.get(url=url)
        if page.status_code != 200:
            break
        data_link.append(url)

    # print(data_link)

    return data_link


get_all_page(url_base=ulr_base)