import json

from gpiozero import LEDBoard
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from christmas_tree_twitter_auth import consumer_key, consumer_secret, access_token, access_token_secret


class ChristmasTreeListener(StreamListener):
    """Stream Listener and Tree LED controller"""
    
    tree = LEDBoard(*range(2,28), pwm=True)
    # Need 26 keywords for the LEDs, the first is the star
    keywords = ["star", 
                "snow", "christmas", "santa", "merry", "xmas",
                "present", "gift", "card", "mince", "turkey",
                "joy", "tree", "light", "decoration", "carol",
                "cake", "wrap", "elves", "jingle", "reindeer",
                "festive", "holiday", "sleigh", "nativity", "peace"]
    # Associate each word with an LED via a dictionary for lookups
    lookup = {word: led for word, led in zip(keywords, tree.leds)}
    # Keep track of how many times a word has been found via a counter dictionary
    word_counter = {word: 0 for word in keywords}

    def on_data(self, data):
        """When new data is received from the Twitter stream"""
        # Parse from JSON string
        parsed_data = json.loads(data)
        # May not contain text, may be limit if the result is < 1% of tweets batch.
        if "text" in parsed_data:  # checks parsed_data's keys for "text"
            # Search for the words, if found, flip the led
            for word, led in self.lookup.items():
                if word in parsed_data["text"]: 
                    self.word_counter[word] += 1
                    led.toggle() # if on, turn off, else turn on.
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    # Authenticate with Twitter
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Setup stream
    listener = ChristmasTreeListener()
    stream = Stream(auth, listener)

    # Run filter, passing data to listener.
    # In try/except block so a keyboard interrupt will 
    # output the word counter, sorted by value
    try:
        stream.filter(track=listener.keywords)
    except KeyboardInterrupt:
        print()
        for word, value in sorted(listener.word_counter.items(), key=lambda x:x[1]):
            print(word, value)
