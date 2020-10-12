import twitter
from tweetminer import TweetMiner
import pandas as pd

class TwitterConn(object): 
    def __init__(self, result_limit = 20):
        self.twitter_keys = {
            'consumer_key':        'L4sziHBqV4VUIfKezbos0JMVl',
            'consumer_secret':     'lJau6R7GIHFwoGR5wB3PlLQPXBChwzJFJ9WGXXtazcDSA1Vb1X',
            'access_token_key':    '941359629606539264-05XcmQfdwMXTbPNWS3r7cZThvbQBxCK',
            'access_token_secret': 'VdE3VJVk6oxbohQGcw7WYA5Tg4Sr8kW9duTO1wxmB6qXk'
        }
        self.api = self.set_conn()
        self.result_limit = result_limit
        self.miner = TweetMiner(self.api, result_limit)
        
    def set_conn(self):
        return twitter.Api(
            consumer_key         =   self.twitter_keys['consumer_key'],
            consumer_secret      =   self.twitter_keys['consumer_secret'],
            access_token_key     =   self.twitter_keys['access_token_key'],
            access_token_secret  =   self.twitter_keys['access_token_secret'],
            tweet_mode = 'extended'
        )

#     def get_limit(self, user = 'JoeBiden', target_minus = 3.5 * 10**16, max_minus = 5 * 10 **15):
#         self.api = self.set_conn()
#         tmp = self.api.GetUserTimeline(screen_name=user, count=1, include_rts=False)
#         tmp = [_.AsDict() for _ in tmp]

#         target_id = int(tmp[0]['id']) - target_minus
#         max_id = int(tmp[0]['id']) - max_minus

#         return target_id, max_id

    def collect_tweets(self, cand_one = 'JoeBiden', cand_two = 'realDonaldTrump', target_length = 1000):
        cand_one_tweets = self.mine_twitter(user=cand_one)
        cand_two_tweets = self.mine_twitter(user=cand_two)
        
        cand_one_train = cand_one_tweets[target_length // 10:(target_length - target_length // 10)]
        cand_two_train = cand_two_tweets[target_length // 10:(target_length - target_length // 10)]
        cand_one_test = cand_one_tweets[:target_length // 10]
        cand_two_test = cand_two_tweets[:target_length // 10]
        
        trains = []
        tests = []
        for i in range(len(cand_one_train)):
            trains.append(cand_one_train[i])
            trains.append(cand_two_train[i])
        
        for i in range(len(cand_one_test)):
            tests.append(cand_one_test[i])
            tests.append(cand_two_test[i])
        
                                       
        tweets_train = pd.DataFrame(trains)        
        tweets_test = pd.DataFrame(tests)                                         
        return tweets_train, tweets_test 

    def mine_twitter(self, user="twitter", last_tweet_id = 0, first_tweet_id = 0, mine_retweets=False, max_pages=20):
        try:
            data = self.miner.mine_user_tweets(user, last_tweet_id, first_tweet_id, mine_retweets, max_pages)
        except:
            self.api = self.set_conn()
            self.miner = TweetMiner(self.api, self.result_limit)
            data = self.miner.mine_user_tweets(user, last_tweet_id, first_tweet_id, mine_retweets, max_pages)
        return data
