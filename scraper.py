import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.body)
# print(soup.body.content)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find(id='score_20514755))

# need to use .titleline instead of .storylink and .titleline > a is used because a tag is under titleline element

# print(soup.select('a'))
# print(soup.select('div))
# print(soup.select(.score))
# print(soup.select(#score_20514755))
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes[0].get('id'))

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        hn.append({'title': title, 'link': href})
    return hn

create_custom_hn(links, votes)