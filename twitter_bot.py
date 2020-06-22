import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key',
                           'consumer_secret')
auth.set_access_token('access_token',
                      'access_token_secret')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)


def like_tweet(search_string, number_tweets):
    for tweet in tweepy.Cursor(api.search, search_string).items(number_tweets):
        try:
            tweet.favorite()
            print('Tweet loved.')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration as e:
            print(e)
            break


def follow_back():
    # Follow back bot
    if user.followers_count > 0:
        for follower in limit_handler(tweepy.Cursor(api.followers).items()):
            if follower.followers_count > 10000:
                follower.follow()
                break


if __name__ == '__main__':
    follow_back()
    like_tweet('python', 2)
