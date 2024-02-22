import requests
from bs4 import BeautifulSoup

# Đường link cần lấy dữ liệu
url = 'https://tuyensinh.epu.edu.vn/tu-van-tuyen-sinh.html'

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công hay không (status code 200)
if response.status_code == 200:
    # Phân tích HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trích xuất thông tin cụ thể từ trang web, ví dụ:
    title = soup.title.text
    content = soup.find('div', class_='content').text

    # In ra thông tin
    print(f'Title: {title}')
    print(f'Content: {content}')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
