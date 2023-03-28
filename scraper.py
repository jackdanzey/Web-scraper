import requests
from bs4 import BeautifulSoup

r = requests.get(
    'https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y')

data = r.text

soup = BeautifulSoup(data, "html.parser")

print(soup.prettify())
