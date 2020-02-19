import urllib.request
import fileinput
import pdb
import os
import bs4

if __name__ == "__main__":
    for index in range(10):
        with urllib.request.urlopen('https://slate.com/podcasts/political-gabfest/' + str(index + 1) + '#episodes') as response:
            html = response.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            soup = soup.select('a.podcast-episode-list__main')
            links = ( s['href'] for s in soup )
            for link in links:
                with urllib.request.urlopen(link) as response:
                    html = response.read()
                    soup = bs4.BeautifulSoup(html, 'html.parser')
                    transcript_links = soup.select('a.slate-megaphone__transcript')
                    if (len(transcript_links) == 0):
                        continue;
                    transcript_link = transcript_links[0]['href']
                    with urllib.request.urlopen(transcript_link) as response:
                        html = response.read()
                        soup = bs4.BeautifulSoup(html, 'html.parser')
                        text = [e.get_text() for e in soup.select('p.slate-paragraph')]
                        f = open('slate_transcripts/' + os.path.basename(transcript_link), 'w')
                        f.write('\n'.join(text))
