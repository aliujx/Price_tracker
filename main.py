from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = "pakatyak@gmail.com"
password = "Na04m@j*/f"

URL = 'https://www.amazon.com/DJI-Smartphone-Stabilizer-Extension-ShotGuides/dp/B099ZXD27F/ref=sr_1_26?qid=1654962791&s=electronics&sr=1-26'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

responce = requests.get(URL, headers=headers)
soup = BeautifulSoup(responce.content, 'lxml')
#print(soup.prettify)

product_name = soup.find(id='productTitle').get_text()
print(product_name)

price_full = soup.find(name='span', class_='a-offscreen').get_text()
float_price = float(price_full.split('$')[1])
print(float_price)

if float_price > 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='aliujx@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} today ${float_price}! {URL}"
        )
