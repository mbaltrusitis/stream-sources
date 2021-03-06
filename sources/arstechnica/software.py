from sources.arstechnica._source import ArsSource


class Source(ArsSource):

    SOURCE = {
        'name': 'Ars Technica (Software)',
        'url': 'https://arstechnica.com',
    }

    FEED_URL = 'http://feeds.arstechnica.com/arstechnica/software'
