import sys
import urllib.request

def getbib(code):
    url = 'http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=' + \
          code + '&data_type=BIBTEX'
    page = urllib.request.urlopen(url)
    s = 0
    for line in page:
        if s < 5:
            s += 1
        else:
            bibfile = open('many.bib','a')
            bibfile.write(str(line,'utf-8'))
            bibfile.close()


argv = sys.argv
if len(argv) == 2:
    getbib(argv[1])


