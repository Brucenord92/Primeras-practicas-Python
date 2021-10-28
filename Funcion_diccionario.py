import urllib.request
import re

url = 'https://web.archive.org/web/20210422170527/https://en.wikipedia.org/wiki/Wikipedia'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

matches = re.findall(r'[a-zA-Z]{3,}', text)
print(matches, len(matches))

wiki = re.findall(r'wiki', text)
print(wiki, len(wiki))

Wiki = re.findall(r'Wiki', text)
print(Wiki, len(Wiki))


def carga_lista(text):
    lista=[text]
    for lista in text:
        if lista == matches:
            print("values", lista)
    else:
        print("keys", lista)


    
