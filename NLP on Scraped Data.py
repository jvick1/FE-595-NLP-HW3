#NLP on Scraped Data

import pandas as pd #for my dataframe
import nltk #for sentiment and text analysis
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet') #helps the script determine the base word
nltk.download('averaged_perceptron_tagger') #helps the script determine the context
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt

#reading in the two data files
Jake = pd.read_csv("50companyData.csv")
Zach = pd.read_csv("output.csv")

#cleaning my data
Jake.head()
#here I note I have an extra column so I only want Name and Purpose
Jake = Jake[["Name", "Purpose"]]
Jake.head()

#cleaning Zach's data
Zach.head()

#now that the data has been checked and cleaned we can combine it
data = Jake.append(Zach)

#----Part 1 
#you should be able to print out a single file with combined results
#data.to_csv("FinalDataSet.csv") 

#----Part 2
#read in purpose and get a sentiment score
#identify top and bottom 10

pos = [] #sentiment
neg = []
neu = []
freqTable = dict() #word count
stopWords=set(stopwords.words("english")) #stop words
i = 0
sia = SentimentIntensityAnalyzer()

#this loop will go row by row looking at the purpos column
#it will tokenize the words
#count the word frequency (remove stop words)
#then does a sentiment analysis (again removing stop words)
#It then stores the sia return in different list i.e. pos goes to the pos list
for index, row in data.iterrows():

    words = word_tokenize(row["Purpose"]) #breaks down each word

    #this will add to the word count
    for word in words:
        word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

    #sentiement score
    filtered_words = [w for w in words if not w in stopWords] #remove Stop words
    summary = " ".join([str(elem) for elem in filtered_words]) #back to string
    pos.append(sia.polarity_scores(summary)["pos"])
    neg.append(sia.polarity_scores(summary)["neg"])
    neu.append(sia.polarity_scores(summary)["neu"])

#now that we have pos, neg, and neu accounted for lets add it to the df
data.head()
data["Positive"] = pos
data["Negative"] = neg
data["Neutral"] = neu
data.head()

#---- top and bottom 10 (part 2 results)
#top 10 positive 
data.sort_values(by="Positive", ascending = False).head(10)

#top 10 negative 
data.sort_values(by="Negative", ascending = False).head(10)

#---- interesting findings (part 3 results)
#we also have a frequency table to id most common words (mainly for part 3)
freqTable
plt.barh(list(freqTable.keys()), freqTable.values(), color = "blue")
plt.show()

#writeup

#A few notes that I can make after looking at some of the data
#is majority of the Company Purpose write-ups tend to be positive or neutral 
#out of my groups 100 observations only 2 had negative sentiment.

#Looing at the freqTable plot I was able to identify some of the key words used
#"E-Services" 6, "Application" 5, "vortals" 5, "Functionalities" 5
#are some of the most commonly used words

#There are a lot of common Tech-Business words like action-items, roi, services,etc.
#one of the words that stand out is "Eyeballs" doesn't seem to fit in with the other companies

#to look at this further I find the purposes that contain eyeballs
FindEyes = data["Purpose"].str.find("eyeballs")
data["Eyeballs"] = FindEyes
#identify the two companies that had eyeballs
werid = data.sort_values(by="Eyeballs", ascending = False).head(2)
#print out the first and second
werid["Purpose"].values[0]
#not sure what embracing bricks-and-clicks eyeballs lol
werid["Purpose"].values[1]
#this one looked ok - talking about a good userface compelling to your eyes.

#not sure how much more you wanted to look into this but I definty thought Eyeballs didn't belong