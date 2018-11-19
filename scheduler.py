import schedule
import time
from prettytable import PrettyTable
import ast
from collections import Counter
import pandas as pd

'''
This function will convert the CounterDict to the DataFrame and then return the top 10 words.
'''
def get_unique_words(count):
    dfr = pd.DataFrame.from_dict(count, orient='index')
    return dfr.head(10)


def job():
    print("Generating Reports:\n")

    current_time = time.time()

    columns1 = ['S.No.', 'Handle Name', 'Tweets Count']

    # Table1 is used to represent the user report in a clean manner.
    table1 = PrettyTable(columns1)

    with open('tweetDB4.csv', 'r', encoding='utf-8') as f:
        i = 0
        words, links = [], []
        for line in f:

            # This will read the line in the tweetDB4.csv file.
            data = ast.literal_eval(line)

            # print(current_time, data["timestamp"], (current_time - data["timestamp"]))

            '''
            These conditions will look check for the last 5 mins and the end of the file.
            It will generate the reports and as soon as the conditions failed, 
            it will print the report on the command prompt.
            '''
            if 0 <= (current_time - data["timestamp"]) <= 300:
                table1.add_row([i+1, data["user"], data["status_count"]])
                words+=((data["unique_words"]).split(" ")) # Concatenate the list of unique words into words list.
                links+=((data["links"][1:-1]).split(",")) # It will extract the links from a string.
                i+=1
            elif data["timestamp"] > current_time or not data:
                print("User Report:")
                print(table1) # Print the user report in table form.
                print("\nContent Report:")
                count_words = Counter(words)
                print(get_unique_words(count_words)) # Print the list of top 10 unique words with it's frequency.
                print("\nTotal Number of Unique Words- ", len(words)) # Print the total number of unique words.
                print("\nLink Report:")
                print("Total Number of Links- ", len(links)) # Print the total number of links in the tweets.
                break
            else:
                continue

# This will call the job function every minute.
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)