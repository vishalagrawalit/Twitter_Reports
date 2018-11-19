# Twitter_Reports
Generate User Reports, Link Reports &amp; Content Report of Streaming Twitter Data.

## **Stack**
Python

## **Tasks**
- [ ] User Report - Name of the Twitter user with the count of tweets.
- [ ] The total number of links (Link Report) - Count the total number of links in a tweet.
- [ ] Top 10 Domains (Link Report) - Return the top 10 domains in decreasing frequency.
- [ ] List of top words (Content Report) - Return the list of top unique words in decreasing frequency.
- [ ] The total number of unique words (Content Report) - Unique words are the words other than conjunctions, adjectives, etc.

## **How to Run?**
1- **Clone the repository**- 
	Command - _git clone https://github.com/vishuvish/Twitter_Reports_
2- **Install python packages**-
	Command - _pip install -r requirements.txt_
3- **You need to run 2 files simultaneously to generate the reports.**
	Command - _python tweets.py_ 
		- This will ask the user to input the keyword and then it will request the Twitter Streaming API and start reading the data.
	Command - _python scheduler.py_
		- This file is used to generate the reports every minute for the past 5 mins.

## **Improvements we can done-**
1- We can optimize it by not traversing to every tweets saved in tweetDB4.csv by calculating the frequency of tweets every minute.
2- It's quite possible that your local machine is doing a bunch of other things, and system processes get priority, so the tweets will back up until Twitter disconnects you. It can throw "IncompleteRead Error". So, we can push the procssing into queue and then run the process in a background. 