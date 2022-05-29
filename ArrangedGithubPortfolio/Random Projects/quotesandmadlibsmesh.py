from random import randint
nouns = ["cats", "dogs", "apples", "pizza"]
verbs = ["jumping","dancing","singing","programming"]
adjectives = ["happy","sad","content","depressed"]
masterString = "" 
for _ in range(int(input("Enter in number of quotes to make:"))):
    SS = [f"The {adjectives[randint(0,len(adjectives)-1)]} {nouns[randint(0,len(nouns)-1)]} loves {verbs[randint(0,len(verbs)-1)]} in the park!"]
    masterString += SS[randint(0,len(SS)-1)] #Here this 
    masterString += "\n"
print("Heres to some words of wisdom:\n" + masterString)

#Here is an explanation of each line:

#1:Import randint
#2:List of nouns
#3:List of verbs
#4:List of adjectives
#5 MasterString holds all of the combined text you generate.

#6 for _ in range of input (specified by user)

#7:SS or Sentence Structures are blueprints. You can make any combination of arguments in the f string format 
# (it doesnt look pretty though, so you'd want to separate them by line). SS also needs to be inside the loop for it to generate new ones
#Even if you have an extensive list of text, you just wanna be sure, ya know?

#8 Add a random sentence structure to the master string
#9 Line break
#10 Finally print out words of wisdom

#I was inspired to do this via madlibs and inspirobot.me online
#I could also expand upon this to intake data from a csv file using Pandas or a database using MongoDB or some SQL using service
