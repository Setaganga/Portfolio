#Created by Setaganga on Github

#Hello! Thanks for checking out my scraper!
#I made this program because I love giving back to the r/summonsign community for their help in my endeavors.
#However, I'm not always online on the reddit, and usually someone beats me to it!
#So I made a scraper to do this and show me the first 5 posts on the new category.
#I will add onto this and have it filter out for the PS4/5 and DS3
#Reddit doesn't allow more than 30 requests per hour, so I have it set as 5 minute intervals just to be safe.

#importing modules and link
import requests
from bs4 import BeautifulSoup
from time import sleep
websiteLink = "https://new.reddit.com/r/SummonSign/?f=flair_name%3A%22%3Apsx%3A%20Help%20Me!%22"

#Loop
while True:
    #request website and make sure we fetch it correctly
    req = requests.get(websiteLink)
    sc = req.status_code
    if sc != 200:
        print("Could not fetch website")
        break
    #Use html parser
    bs = BeautifulSoup(req.content,'html.parser')
    #Find the div with the posts
    helpmesections = bs.find(class_="rpBJOHq2PR60pnwJlUyP0")
    #Get timestamps
    timestamp = helpmesections.findAll("span")
    #Get post title
    title = helpmesections.findAll(class_="_eYtD2XCVieq6emjKBH3m")
    #Make sure timestamp has "ago" inside of it
    refinedtimestamp = [x.get_text() for x in timestamp if "ago" in x.get_text()]
    #Get text of title
    refinedtitle = [x.get_text() for x in title]

    #Check if lists arent empty
    if len(refinedtimestamp) > 0 and len(refinedtitle) > 0:
        #If it has 5 or more, print out the first 5
        if len(refinedtimestamp) > 4 and len(refinedtitle) > 4:
            for i in range(5):
                print(f"{refinedtitle[i]}, {refinedtimestamp[i]}\n")
        #otherwise, print out available posts.
        else:
            for i in range(len(refinedtimestamp)):
                print(f"{refinedtitle[i]}, {refinedtimestamp[i]}\n")

    #wait 5 minutes
    sleep(300)