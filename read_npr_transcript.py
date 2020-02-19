import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    for line in fileinput.input():
        with urllib.request.urlopen(line) as response:
            html = response.read()
            f = open('npr_transcripts/' + os.path.basename(line), 'w')
            soup = bs4.BeautifulSoup(html, 'html.parser')
            str = soup.select('div.transcript')[0].find_all('p')
            f.write('\n'.join([s.get_text() for s in str][1:-2]))
