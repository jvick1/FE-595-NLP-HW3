# FE-595-NLP-HW3

1. Ingest the results from the previous assignment from you and all of your group members. You should be able to print out a single file that has rolled all of these results together into a single combined format. (This might involve writing a unique script for each member's contribution. This is practice for standardizing data which might come in many different formats from different sources.)

For part 1 of this homework I read in both csv files and printed the head of the two files. This was to identify any changes that would need to be made. I noticed that my file had an extra column so I removed it. Then I created a new variable called "data" and did an append to combine the two files. The "together into a single combined formate" can be found commented out around line 33 in the py code. 

2. A second script which reads the output from step 1 and sorts all of the company's purposes by sentiment. (Choose whichever method for sentiment you would like.) Report the top 10 and bottom 10 results. (Hint: learning about lambda functions might be useful here.)

For part two I add on columns to my combined dataframe. I create a few empty list which will be uesd to store my sentiement scores (pos, neg, neu). I also read in some stopwrods and I create an empty dictionary so that I can count words in the file. In my for loop I tokenize the words and create the frequency table (removing stop words). Once that frequency table is done my loop goes on to create a filtered word list which basically removes all stop words in a string then converts it back to a string. After do this I realized that words like "may", "not" and things like that got removed too so in future project I might do the sentiement on the full string and then the filtered string too. Then I append the pos score to the pos list and do this for the other scores as well. Out side of the for-loop now I create new columns for the scores in my existing data dataframe. Lines 82 and 85 print the top 10 bottom 10.

3. Report anything you notice about the data as you are working with it. I'm not looking for anything in particular here, this is simply to encourage you to engage in some tangential learning while working with this data.

I did a full write up in the code around lines 95 to 117 but to summaries:
I did a bar plot on common words in the documents. A lot had to do with tech companies. One common word that came up a lot was "Eyeballs" which did not really fit in with all of the other business terms. So I did a deeper dive into that and printed out the "purpose" which containted eyeballs and found some interesting stuff. 
