
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_row = soup.findAll('tr')

for row in table_row[0:4]:
    td=row.findAll("td")
    rank=row[0].text
    release = row[1].text
    gross = row[5].text
    theaters = row[6].text
    total_gross = row[7].text
    distributor = row[8].text
    print('Rank: ',rank)
    



##
##
##


