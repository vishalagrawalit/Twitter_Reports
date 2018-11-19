from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
from nltk.corpus import stopwords
import re

ckey = 'iTu36JdKcsr2P2nJiDBNL0BO8'
csecret = 'coYmcooEVdRTAaVCiypfjunbtwo8bbFTVmSGXu5xnU4uH1nugO'
atoken = '759817916091031552-BFDMakQwegj80qWbsMFc2H3iHD4HcoD'
asecret = 'bxV4XtW0TkLOgrLyniUOABXgjWd8MeFGEh5naz4KYMarJ'


def get_unique_words(txt):
    s = set(stopwords.words('english'))
    s.add(" ")
    words = ""
    for i in txt.split(" "):
        if i not in s:
            words += i + " "
    return str(words)

def get_links(txt):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[! * \(\), ]|(?: % [0 - 9a - fA - F][0 - 9a - fA - F]))+', txt)
    return str(url)

class listener(StreamListener):

    def on_data(self, data):
        my_data = json.loads(data)
        my_data_ret = {}
        try:
            my_data_ret["timestamp"] = time.time()
            my_data_ret["user"] = my_data['user']['name']
            my_data_ret["status_count"] = my_data['user']['statuses_count']
            print(type(str(my_data['text'].encode("utf-8"))))
            my_data_ret["unique_words"] = get_unique_words(str(my_data['text'].encode("utf-8")))
            my_data_ret["links"] = get_links(str(my_data['text'].encode("utf-8")))
            # print(my_data_ret)

            saveFile = open("tweetDB4.csv", 'a')
            saveFile.write(str(my_data_ret))
            saveFile.write("\n")
            saveFile.close()

        except BaseException as e:
            print('Failed', str(e))
            time.sleep(5)

    def on_exception(self, exception):
        print(exception)
        return True

    def on_timeout(self):
        print("Timeout")
        return True

    def on_error(self, status_code):
        print(status_code)

with open("tweetDB4.csv", "w"):
    pass

print("Enter the keyword-")
keyword = input()

print("getting tweets")
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])
