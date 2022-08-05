#Created by Setaganga on Github

#Hello! Thanks for checking out my scraper!
#I made this program because I love giving back to the r/summonsign community for their help in my endeavors.
#However, I'm not always online on the reddit, and usually someone beats me to it!
#So I made a scraper to do this and show me the first 5 posts on the new category.
#I will add onto this and have it filter out for the PS4/5 and DS3
#Reddit doesn't allow more than 30 requests per hour, so I have to not be spamming this

#importing modules and link
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
from termcolor import colored

websiteLink = "https://new.reddit.com/r/SummonSign/?f=flair_name%3A%22%3Apsx%3A%20Help%20Me!%22"

#Platforms and keywords
passablePlatforms = ["PS4", "PS5", "PS4/5"]
passableterms = [
    "DS3", 
    "Darksouls3", 
    "DKS3",
    "Vordt",
    "Greatwood",
    "Sage",
    "Deacons",
    "Abyss watchers",
    "Demon king",
    "Wolnir",
    "Pontiff",
    "Sulyvahn",
    "Aldrich",
    "Aldritch",
    "Yhorm",
    "Twin",
    "Princes",
    "Dragonslayer",
    "Cinder",
    "Oceiros",
    "Gundyr",
    "Wyvern",
    "Nameless",
    "Gravetender",
    "Friede",
    "Freide",
    "Spear",
    "Gael",
    "Midir",
    "Demon prince",
    "Pale tongue",
    "Sunlight medal",
    "Vertebrae shackle",
    "swordgrass",
    "dreg",
]

#Validate if the title is suitable
def PS_DS3_Validate(text):
    #Platform Check and Game Check
    pCheck = False
    gCheck = False
    #Search if ps4/5 in title
    for i in passablePlatforms:
        if re.search(i.lower(),text.lower()):
            pCheck = True
    #Check for keywords
    for j in passableterms:
        if re.search(j.lower(),text.lower()):
            gCheck = True
    #If both pass, it flags criteria
    if pCheck == True and gCheck == True:
        return True
    return False

#request website and make sure we fetch it correctly
print("\n")
req = requests.get(websiteLink)
sc = req.status_code
if sc != 200:
    print(colored("Could not fetch website","red"))
else:
    #Use html parser
    bs = BeautifulSoup(req.content,'html.parser')
    #Find the div with the posts
    helpmesections = bs.find(class_="rpBJOHq2PR60pnwJlUyP0")
    #Get timestamps
    timestamp = helpmesections.findAll("span")
    #Get post title
    title = helpmesections.findAll(class_="_eYtD2XCVieq6emjKBH3m")
    #Get comment count
    comments = helpmesections.findAll(class_="FHCV02u6Cp2zYL0fhQPsO")
    #Make sure timestamp has "ago" inside of it
    refinedtimestamp = [x.get_text() for x in timestamp if "ago" in x.get_text()]
    #Get text of title
    refinedtitle = [x.get_text() for x in title]
    #Get text from comments
    refinedcomments = [x.get_text() for x in comments]

    #Check if lists arent empty
    if len(refinedtitle) > 0:
        #If it has 5 or more, print out the first 5
        if len(refinedtitle) > 4:
            for i in range(5):
                #Checking for ps ds3 validation
                if PS_DS3_Validate(refinedtitle[i]):
                    #If no comments, its free to take
                    if refinedcomments[i] == "0 comments":
                        print(colored("*CRITERIA* ","green"),colored("*NOT TAKEN*","blue"),f" {refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
                    #If there IS comments, well, sad.
                    else:
                        print(colored("*CRITERIA*","green"),f" {refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
                else:
                    #Print out regular title with no flags
                    print(f"{refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
        #otherwise, print out available posts.
        else:
            for i in range(len(refinedtitle)):
                #Checking for ps ds3 validation
                if PS_DS3_Validate(refinedtitle[i]):
                    #If no comments, its free to take
                    if refinedcomments[i] == "0 comments":
                        print(colored("*CRITERIA* ","green"),colored("*NOT TAKEN*","blue"),f" {refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
                    #If there IS comments, well, sad.
                    else:
                        print(colored("*CRITERIA*","green"),f" {refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
                else:
                    #Print out regular title with no flags
                    print(f"{refinedtitle[i]}, {refinedtimestamp[i]}, {refinedcomments[i]}\n")
