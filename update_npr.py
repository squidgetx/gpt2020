import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    url = 'https://www.npr.org/podcasts/510310/npr-politics-podcast'
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    li = soup.select('li.audio-tool-transcript')
    links = [ l.find('a').get('href', '') for l in li]
    for line in links:
        with urllib.request.urlopen(line) as response:
            html = response.read()
            f = open('npr_transcripts/' + os.path.basename(line), 'w')
            soup = bs4.BeautifulSoup(html, 'html.parser')
            str = soup.select('div.transcript')[0].find_all('p')
            f.write('\n'.join([s.get_text() for s in str][1:-2]))
