import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

random_chapter = str(random.randint(1,21))
if int(random_chapter) <10:
    random_chapter = '0'+random_chapter


webpage = 'https://ebible.org/asv/JHN' + random_chapter +'.htm'
print(webpage)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

request = Request(webpage, headers=headers)
webpage = urlopen(request).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll("div", class_='main')

#print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split('.')
#print(verse_list)
    
my_verse = random.choice(verse_list[:len(verse_list)-5])

message = "Chapter: " + random_chapter + ", Verse: " +my_verse

print(message)


import keys2 as keys2
from twilio.rest import Client
client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+18585854117'

myCellPhone = '+14026191246'

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=message)
print(textmessage.status)
 