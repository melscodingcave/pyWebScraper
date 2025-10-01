import requests
from bs4 import BeautifulSoup
import pprint
import time

base_url = 'https://news.ycombinator.com/news'

def sort_stories_by_votes(hnlist):
            return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext, min_votes=100):
            hn = []
            for idx, item in enumerate(links):
                title = item.getText()
                href = item.get('href', None)
                vote_tag = subtext[idx].select_one('.score')
                if vote_tag:
                    points = int(vote_tag.getText().replace(' points', ''))
                    if points >= min_votes:
                        hn.append({'title': title, 'link': href, 'votes': points})
            return hn

def scrape_hn(min_votes=100, target_count=20, delay=1):
    current_page = 1
    all_stories = []

    with requests.Session() as session:
        while len(all_stories) < target_count:
            url = f'{base_url}?p={current_page}'
            res = session.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')

            links = soup.select('.titleline')
            subtext = soup.select('.subtext')
            
            new_stories = create_custom_hn(links, subtext, min_votes)
            all_stories.extend(new_stories)

            more_link = soup.find('a', id='morelink')
            
            if not more_link:
                break
            
            current_page += 1
            time.sleep(delay)
            
    return sort_stories_by_votes(all_stories)[:target_count]

if __name__ == '__main__':
    stories = scrape_hn(min_votes=100, target_count=20, delay=2)
    pprint.pprint(stories)
        