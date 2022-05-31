#Setagangas Data Scraper for https://stats.gats.io/clans/top
#Credit to my buddy vedant for giving me the idea

#Import Modules
import requests
from bs4 import BeautifulSoup

#Getting user input on how many clans and which data they want
count = 0
datatype = 0
while count <= 0 or count >= 25:
    count = int(input("Enter amount of clans to scrape (1-25):"))
while datatype <= 0 or datatype >= 6:
    datatype = int(input("Enter 1-5 if you would like ID, Tag, Name, Players, or Score:"))

#Send request to server to get data
page = requests.get("https://stats.gats.io/clans/top")
sc = page.status_code
print(f"Status code: {sc}")
print("\n")
#Check if its a-okay
if sc != 200:
    print("ERROR: Website Content could not be retrieved") #Oopsies! Data could not be retrieved!
else:
    bs = BeautifulSoup(page.content, 'html.parser')#Get entire html page
    table = bs.find(class_="rowlink")#Get specific table
    rows = table.findAll("tr")#Get all table rows

    for x in range(count): #For count number of times
        data = list(rows[x].children) #Data is a list of the children of tr (this includes stuff like <td>1</td> and "\n")
        data = [y for y in data if y != "\n"]
        print(data[datatype - 1].get_text().strip()) #Get text and strip of whitespace from data and index of var datatype - 1 (list indices start at 0)
print("\n")
