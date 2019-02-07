from itertools import count
from requests import get
from bs4 import BeautifulSoup

done = False

results = []

for num in count(1):
    url = f'https://developers.whatismybrowser.com/useragents/explore/hardware_type_specific/computer/{num}'
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    table = html_soup.find('tbody')

    if table is not None:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            results.append(tds[0].text)
    else:
        done = True
        break

with open(f"ua_list.txt", 'w') as text_file:
    text_file.write("\n".join(results))

print(f'UA Scraping Complete. {len(results)} User-Agents scraped.')
