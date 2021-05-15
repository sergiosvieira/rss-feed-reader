import sys
import feedparser

def get_feed(url):
    parser = feedparser.parse(url)
    for feed in parser.entries:
        print(feed.published)
        print(feed.title)
        print(feed.description)
        print(feed.link)
        max_len = max(len(feed.description), len(feed.title))
        print("-" * max_len)

def usage():
    print("Usage: python main.py <url feed list>")
    print("Example: python main.py http://feeds.bbci.co.uk/news/england/london/rss.xml http://feeds.bbci.co.uk/sport/england/london/rss.xml")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        usage()
        exit
    else:
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            get_feed(arg)
