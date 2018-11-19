import schedule
import time
from prettytable import PrettyTable
import ast
from collections import Counter
import pandas as pd

def get_unique_words(count):
    dfr = pd.DataFrame.from_dict(count, orient='index')
    return dfr.head(10)


def job():
    print("Generating Reports:\n")

    current_time = time.time()

    columns1 = ['S.No.', 'Handle Name', 'Tweets Count']

    table1 = PrettyTable(columns1)

    with open('tweetDB4.csv', 'r', encoding='utf-8') as f:
        i = 0
        words, links = [], []
        for line in f:

            data = ast.literal_eval(line)

            # print(current_time, data["timestamp"], (current_time - data["timestamp"]))
            if 0 <= (current_time - data["timestamp"]) <= 300:
                table1.add_row([i+1, data["user"], data["status_count"]])
                words+=((data["unique_words"]).split(" "))
                links+=((data["links"][1:-1]).split(","))
                i+=1
            elif data["timestamp"] > current_time or not data:
                print("User Report:")
                print(table1)
                print("\nContent Report:")
                count_words = Counter(words)
                print(get_unique_words(count_words))
                print("\nTotal Number of Unique Words- ", len(words))
                print("\nLink Report:")
                print("Total Number of Links- ", len(links))
                break
            else:
                continue

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)