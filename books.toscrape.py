
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books_data = []

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    image_url = url + book.find('img')['src'].replace('../', '')
    books_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability,
        'Image URL': image_url
    })

for book in books_data:
    print("Title:", book['Title'])
    print("Price:", book['Price'])
    print("Availability:", book['Availability'])
    print("Image URL:", book['Image URL'])
    print()