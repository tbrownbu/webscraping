
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
ranking = 1
for row in table_row[1:6]:
    td=row.findAll("td")
    rank=td[0].text
    if int(rank)<8:
        release = td[1].text
        gross = td[5].text
        theaters = td[6].text
        total_gross = td[7].text
        distributor = td[8].text
        print(f'Rank: {rank}\nRelease: {release}\nGross: {gross}\nTheaters: {theaters}\nTotal Gross: {total_gross}\nDistributor: {distributor}\n\n')
        #print('release: ',release)
        #print('gross: ',gross)
        #print('theaters: ',theaters)
        #print('total gross: ',total_gross)
        #print('distributor: ',distributor)
    ranking+=1

##
##
##


