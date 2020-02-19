import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    for index in range(30):
        with urllib.request.urlopen('https://www.rushlimbaugh.com/daily/category/transcripts/page/' + str(index + 1)) as response:
            html = response.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            links = ( s['href'] for s in soup.find_all('a', class_=None) )
            for count, link in enumerate(links):
                if (link.startswith('https://www.rushlimbaugh.com/daily')):
                    with urllib.request.urlopen(link) as response:
                        html = response.read()
                        soup = bs4.BeautifulSoup(html, 'html.parser')
                        transcript_div = soup.select('div.entry-content')
                        text = [e.get_text().strip() for e in transcript_div ][::-2]
                        if (len('\n'.join(text)) > 0):
                            f = open('rush_transcripts/' + str(index) + '-' + str(count) , 'w')
                            f.write('\n'.join(text))
