import requests
import re

class Source:

    def __init__(self, source):
        self.source = source 

    def getWebPage(self):
        content = requests.get(self.source)
        content = content.content
        return str(content)

    def format(self, content):
        txt = re.findall(r'<p>.+?</p>', content)
        return txt
    
    def find(self, txt, keyword):
        for phrase in txt:
            x = phrase.find(keyword)
            if x >= 0:
                return True
            else: return False

s1 = Source('https://de.wikipedia.org/wiki/Computer')
content = s1.getWebPage()
txt = s1.format(content)
value = s1.find(txt, 'Computer')
print(value)
