import requests

from bs4 import BeautifulSoup

def get_content():

    soup = BeautifulSoup("<html><p>This is <b>invalid HTML</p></html>", "html.parser")

# post cần lấy thông tin ('https://dantri.com.vn/suc-khoe/tre-5-11-tuoi-tiem-vaccine-covid-19-can-luu-y-dieu-gi-20220504134833678.htm')
    req = requests.get('https://dantri.com.vn/suc-khoe/tre-5-11-tuoi-tiem-vaccine-covid-19-can-luu-y-dieu-gi-20220504134833678.htm')

    soup = BeautifulSoup(req.text, "lxml")
# lấy toàn bộ nội dung
    title = ''
    content = ''
    for idx, sub_heading in enumerate(soup.find_all('p')):
        if idx == 0:
            title = sub_heading.text
            continue

        content += sub_heading.text

    print(f"title: {title}")
    print(f"content: {content}\n")

get_content()