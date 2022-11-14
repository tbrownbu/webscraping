from urllib.request import urlopen
from bs4 import BeautifulSoup
import keys2 as keys2
from twilio.rest import Client
client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+18585854117'

myCellPhone = '+14026191246'

#webpage = 'https://www.cryptocurrencychart.com/'
webpage = 'https://www.cryptocurrencychart.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_row = soup.findAll('tr')
ranking = 1
for row in table_row[1:6]:
    td = row.findAll('td')
    rank = int(td[0].text)

    name = td[1].text
    price = td[2].text.replace('$','')
    price = price.replace(',','')
    price = float(price)
    percent_24 = td[4].text
    change = float(percent_24.replace('%',''))
    change = change/100

    price_diff = round((1-change)*price,2)

    print(f'Rank: {rank}\nName:{name}Price: ${price}\nPercent Change: %{percent_24}\nOriginal Price: ${price_diff}\n')
        
    ranking+=1
    if ranking == 1:
        if price <40000:
            message = "Bitcoin (BTC) has fallen below $40,000!"
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
            print(textmessage.status)

    if ranking == 2:
        if price < 3000:
            message = "Ethereum (ETH) has fallen below $3,000!"
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
            print(textmessage.status)




            
'''import keys2 as keys2
from twilio.rest import Client
client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+18585854117'

myCellPhone = '+14026191246'

if ranking == 1:
    if price <40000:
        message = "Bitcoin (BTC) has fallen below $40,000!"
        textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
        print(textmessage.status)

if ranking == 2:
    if price < 3000:
        message = "Ethereum (ETH) has fallen below $3,000!"
        textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
        print(textmessage.status)
        '''