from bs4 import BeautifulSoup
import urllib.request

a = urllib.request.urlopen("https://www.pakwheels.com")
soup = BeautifulSoup(a, 'html.parser')

for link in soup.find_all('a', href=True):
    print(link['href'])
