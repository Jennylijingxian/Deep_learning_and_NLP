import sys
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

def loadkeys(filename):
    """"
    load twitter api keys/tokens from CSV file with form
    consumer_key, consumer_secret, access_token, access_token_secret
    """
    with open(filename) as f:
        items = f.readline().strip().split(', ')
        return items


def authenticate(twitter_auth_filename):
    """
    Given a file name containing the Twitter keys and tokens,
    create and return a tweepy API object.
    """
    items = loadkeys(twitter_auth_filename)
    consumer_key = items[0]
    consumer_secret = items[1]
    access_token = items[2]
    access_token_secret = items[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def fetch_tweets(api, name):
    """
    Given a tweepy API object and the screen name of the Twitter user,
    create a list of tweets where each tweet is a dictionary with the
    following keys:

       id: tweet ID
       created: tweet creation date
       retweeted: number of retweets
       text: text of the tweet
       hashtags: list of hashtags mentioned in the tweet
       urls: list of URLs mentioned in the tweet
       mentions: list of screen names mentioned in the tweet
       score: the "compound" polarity score from vader's polarity_scores()

    Return a dictionary containing keys-value pairs:

       user: user's screen name
       count: number of tweets
       tweets: list of tweets, each tweet is a dictionary

    For efficiency, create a single Vader SentimentIntensityAnalyzer()
    per call to this function, not per tweet.
    """
    analyzer = SentimentIntensityAnalyzer()
    user = api.get_user(name)
    user_timeline = api.user_timeline(name, count = 100)
    ls = []
    for i in range(len(user_timeline)):
        d = {}
        d['id'] = user_timeline[i]._json['id']

        initial = user_timeline[i]._json['created_at'].split(" ")
        combine = [initial[1],initial[2],initial[-1]]
        combine_str = " ".join(combine)
        result = time.strptime(combine_str, "%b %d %Y")
        time_str = time.strftime("%Y-%m-%d",result)
        d['created'] =time_str
        #d['created'] = time[4:10] + " " + time[-4:]

        d['retweeted'] = user_timeline[i]._json['retweet_count']

        text = user_timeline[i]._json['text']
        d['text'] = text

        entities = user_timeline[i]._json['entities']
        if entities['hashtags'] == []:
            d['hashtags'] = []
        else:
            d['hashtags'] = [ele['text'] for ele in entities['hashtags']]
        if entities['urls'] == []:
            d['urls'] = []
        else:
            d['urls'] = [ele['url'] for ele in entities['urls']]
        if entities['user_mentions'] == []:
            d['mentions'] = []
        else:
            d['mentions'] = [ele['screen_name'] for ele in entities['user_mentions']]

        # d['hashtags'] = [ele['text'] for ele in user_timeline[i]._json['entities']['hashtags']]
        # d['urls'] = [ele['url'] for ele in user_timeline[i]._json['entities']['url']['urls'] if user_timeline[i]._json['entities']['url'] != []]
        # d['mentions'] = [ele['screen_name'] for ele in user_timeline[i]._json['entities']['user_mentions']]

        vs = analyzer.polarity_scores(text)
        d['score'] = vs['compound']

        ls.append(d)

    dic = {}
    dic['user'] = name
    dic['count'] = user.listed_count
    dic['tweets'] = ls

    return dic


def fetch_following(api,name):
    """
    Given a tweepy API object and the screen name of the Twitter user,
    return a a list of dictionaries containing the followed user info
    with keys-value pairs:

       name: real name
       screen_name: Twitter screen name
       followers: number of followers
       created: created date (no time info)
       image: the URL of the profile's image

    To collect data: get a list of "friends IDs" then get
    the list of users for each of those.
    """
    ls = []
    friends = api.friends_ids(name)

    for id in friends:
        d = {}
        user_info = api.get_user(id)._json
        d['name'] = user_info['name']
        d['screen_name'] = user_info['screen_name']
        d['followers'] = user_info['followers_count']

        initial = user_info['created_at'].split(" ")
        combine = [initial[1], initial[2], initial[-1]]
        combine_str = " ".join(combine)
        result = time.strptime(combine_str, "%b %d %Y")
        time_str = time.strftime("%Y-%m-%d", result)
        d['created'] = time_str

        d['image'] = user_info['profile_image_url']
        ls.append(d)

    return ls

    # ls = []
    # for i in range(len(friends)):
    #     d = {}
    #     d['name'] = friends[i]._json['name']
    #     d['screen_name'] = friends[i]._json['screen_name']
    #     d['followers'] = friends[i]._json['followers_count']
    #
    #     initial = friends[i]._json['status']['created_at'].split(" ")
    #     combine = [initial[1], initial[2], initial[-1]]
    #     combine_str = " ".join(combine)
    #     result = time.strptime(combine_str, "%b %d %Y")
    #     time_str = time.strftime("%Y-%m-%d", result)
    #     d['created'] = time_str
    #
    #     d['image'] = friends[i]._json['profile_image_url']
    #     ls.append(d)
    # return ls
