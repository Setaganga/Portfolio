#This is my submission for the Hackerrank HTML Parser Challenge
#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/
from html.parser import HTMLParser

class htmParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("->",element[0],">",element[1])
        
hP = htmParser()
for x in range(int(input())):
    hP.feed(input())