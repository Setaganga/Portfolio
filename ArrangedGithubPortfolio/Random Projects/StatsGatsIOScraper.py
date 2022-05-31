#Setagangas Data Scraper for https://stats.gats.io/clans/top
#Credit to my buddy vedant for giving me the idea

#Import Modules
import requests
from bs4 import BeautifulSoup

#Getting user input on how many clans and what data they want
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

if sc != 200:
    print("ERROR: Website Content could not be retrieved") #Oopsies! Data could not be retrieved!
else:
    bs = BeautifulSoup(page.content, 'html.parser')#Get entire html page
    table = bs.find(class_="rowlink")#Get specific table
    somedata = table.findAll("tr")#Get all table rows

    for x in range(count): #For count number of times
        data = list(somedata[x].children) #Data is a list of the children of tr (this includes stuff like <td>1</td> and "\n")
        for y in data:
            if y == "\n":
                data.remove(y) #Loop through the data and get rid of newlines
        print(data[datatype - 1].get_text().strip()) #Oh lord this is tough to explain. Data now looks something like "<td>1</td>,<td>clantag</td>,<td>clanname</td>"
        #So the reason I do minus one is because I prompted the user 1-5 and list indices start at 0.
        #So lets say I picked 3 at the start for the clan name. It gives me data[2], then removes the tags, and strips whitespace.
