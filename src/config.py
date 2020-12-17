
from dataclasses import dataclass
from os import environ


@dataclass
class TweeterConfig:

    # Twitter API public and private key
    api_key = environ.get('TWITTER_API_KEY')
    api_secret = environ.get('TWITTER_API_SECRET')

    # Twitter account access token
    access_token = environ.get('TWITTER_ACCESS_TOKEN')
    access_secret = environ.get('TWITTER_ACCESS_SECRET')

    topics = [
        'Machine Learning',
        'Deep Learning',
        'Data Science',
        'genetique algorithme',
        'experimentally determinated'
    ]


@dataclass
class Config:

    twitter = TweeterConfig()


# Init a global config object
config = Config()
