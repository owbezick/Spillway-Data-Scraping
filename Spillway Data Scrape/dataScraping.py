import requests
from bs4 import BeautifulSoup

url = 'http://my.sfwmd.gov/portal/pls/portal/realtime.pkg_rr.proc_rr?p_op=FORT_LAUDERDALE'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.text
no_new_line = text.replace('\n', '')
no_special = text.replace('\xa0', '')

import nltk
from nltk import word_tokenize
tokens = word_tokenize(no_special)

start = tokens.index("G56")
end = start + 11
G56 = tokens[start:end]
print(G56)