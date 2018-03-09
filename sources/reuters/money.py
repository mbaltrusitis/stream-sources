from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Reuters (Money)',
        'url': 'https://www.reuters.com',
    }

    FEED_URL = 'http://feeds.reuters.com/news/wealth'
