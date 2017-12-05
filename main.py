import json

from gpiozero import LEDBoard
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from christmas_tree_twitter_auth import consumer_token, consumer_secret, access_token, access_token_secret


class ChristmasTreeListener(StreamListener):
    tree = LEDBoard(*range(2,28), pwm=True)
    keywords = ["star", 
                "snow", "christmas", "santa", "merry", "xmas",
                "present", "gift", "card", "mince", "turkey",
                "joy", "tree", "light", "decoration", "carol",
                "cake", "wrap", "elves", "jingle", "reindeer",
                "festive", "holiday", "sleigh", "nativity", "peace"]
    lookup = {word: led for word, led in zip(keywords, tree.leds)}
    word_counter = {word: 0 for word in keywords}

    def on_data(self, data):
        parsed_data = json.loads(data)
        if "text" in parsed_data:
            for word, led in self.lookup.items():
                if word in parsed_data["text"]:
                    self.word_counter[word] += 1
                    led.toggle()
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    auth = OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    listener = ChristmasTreeListener()
    stream = Stream(auth, listener)

    try:
        stream.filter(track=listener.keywords)
    except KeyboardInterrupt:
        print()
        for word, value in sorted(listener.word_counter.items(), key=lambda x:x[1]):
            print(word, value)
