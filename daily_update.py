import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    file = open('daily_index.htm', 'rt')
    url = 'https://www.nytimes.com/column/the-daily'
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup = soup.select('a')
    links = ( s['href'] for s in soup )
    for link in links:
        if (link.startswith('/20')):
            url = 'https://www.nytimes.com' + link + '?showTranscript=1'
            print(url)
            with urllib.request.urlopen(url) as response:
                html = response.read()
                soup = bs4.BeautifulSoup(html, 'html.parser')
                article = soup.select('article#story')
                if (len(article) == 0):
                    print('  empty article')
                    continue;
                text_gen = article[0].select('dl')
                if (len(text_gen) == 0):
                    print('  no dl found')
                    continue;
                text_gen = text_gen[0].find_all('p')
                text_gen = [ s.get_text() for s in text_gen ]
                f = open('daily_transcripts/' + os.path.basename(link), 'w')
                f.write('\n'.join(text_gen))
