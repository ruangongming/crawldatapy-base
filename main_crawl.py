import requests
from bs4 import BeautifulSoup

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crawl_database"]

mycol = mydb["dantri_db"]


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

def get_all_article(url_page):
    result_article = []
    page = requests.get(url=url_page)
    if page.status_code != 200:
        print("can not connect to url")
        return False
    # GET soup data
    soup = BeautifulSoup(page.content, "html.parser")
    div_data = soup.find("div", {"class": "article list"})

    # show toàn bộ link có trong page
    a_data = div_data.find_all("a", href=True)
    for a in a_data:
        data = "https://dantri.com.vn/" + a['href']
        print(data)
        result_article.append(data)

    return result_article

def get_content(url):

    req = requests.get(url)

    soup = BeautifulSoup(req.text, "lxml")

    title = ''
    content = ''
    for idx, sub_heading in enumerate(soup.find_all('p')):
        if idx == 0:
            title = sub_heading.text
            continue

        content += sub_heading.text

    print(f"title: {title}")
    print(f"content: {content}")
    return {
        "tile": title,
        "content": content
    }


if __name__ == "__main__":
    ulr_base = "https://dantri.com.vn/suc-khoe/"
    data_links = get_all_page(url_base=ulr_base)
    print(data_links)
    for url in data_links:
        article_urls = get_all_article(url)
        data_insert = []
        for _url in article_urls:
            data_insert.append(get_content(_url))

        mycol.insert_many(data_insert)

    # get_all_article(url_page=ulr_base)
    # get_content()