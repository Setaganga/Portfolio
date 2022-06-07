from random import randint

nouns = ["cats", "dogs", "apples", "pizza"]
verbs = ["jumping","dancing","singing","programming"]
adjectives = ["happy","sad","content","depressed"]
masterString = ""

def noun():
    return(nouns[randint(0,len(nouns)-1)])
def verb():
    return(verbs[randint(0,len(verbs)-1)])
def adj():
    return(adjectives[randint(0,len(adjectives)-1)])

for _ in range(int(input("Enter in number of quotes to make:"))):
    SS = [
          f"The {adj()} {noun()} loves {verb()} in the park!", 
          f"I sure do love {verb()}",
          f"I feel {adj()} whenever I start {verb()}"
         ]
    masterString += SS[randint(0,len(SS)-1)]
    masterString += "\n"
print("Heres to some words of wisdom:\n" + masterString)

#I was inspired to do this via madlibs and inspirobot.me online
#I could also expand upon this to intake data from a csv file using Pandas or a Database software and just have a huge list of nouns, verbs, and adjectives
#These are also very fun when you have friends suggest words to add. 
#These can get as juvenile and inappropriate as you please, and the results from time to time are hilarious
