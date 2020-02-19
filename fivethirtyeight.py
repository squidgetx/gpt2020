import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    for index in range(50):
        with urllib.request.urlopen('https://fivethirtyeight.com/politics/features/page/' + str(index + 1) + '#episodes') as response:
            html = response.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            soup = soup.select('h2.article-title')
            links = ( s.find('a')['href'] for s in soup )
            for count, link in enumerate(links):
                with urllib.request.urlopen(link) as response:
                    html = response.read()
                    soup = bs4.BeautifulSoup(html, 'html.parser')
                    transcript = soup.select('div.entry-content')
                    if (len(transcript) == 0):
                        continue;
                    transcript = transcript[0].find_all('p')
                    text = [e.get_text() for e in transcript ]
                    f = open('fivethirtyeight_transcripts/' + str(index) + '-' + str(count), 'w')
                    f.write('\n'.join(text))
