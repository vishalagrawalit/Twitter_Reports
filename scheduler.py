import schedule
import time
from prettytable import PrettyTable
import json
import ast
from collections import Counter
import pandas as pd
# from .tweets import get_tweets

def get_unique_words(count):
    dfr = pd.DataFrame.from_dict(count, orient='index')
    return dfr.head(10)


def job():
    print("Doing")
    columns1 = ['S.No.', 'Handle Name', 'Tweets Count']

    table1 = PrettyTable(columns1)

    with open('tweetDB4.csv') as f:
        i = 0
        words, links = [], []
        for line in f:
            if i==10:
                print("User Report")
                print(table1)
                print("Content Report")
                count_words = Counter(words)
                print(get_unique_words(count_words))
                print("Total Number of Unique Words", len(words))
                print("Link Report")
                print("Total Number of Links", len(links))
                break

            data = ast.literal_eval(line)
            table1.add_row([i+1, data["user"], data["status_count"]])
            words+=((data["unique_words"]).split(" "))
            links+=((data["links"][1:-1]).aplit(","))
            i+=1


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)