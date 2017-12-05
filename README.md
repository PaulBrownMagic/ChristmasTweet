# Christmas Tweet

This code will filter the Twitter streaming API for keywords and twinkle the corresponding 
light on the [Pi Hut Christmas Tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi).

Requires Tweepy:

```sh
sudo pip3 install tweepy
```

Download with the command:

```sh
git clone https://github.com/PaulBrownMagic/ChristmasTweet.git
```
Then you'll need to login to your [Twitter account and create a new app for streaming](https://apps.twitter.com/). You need Consumer Key, Consumer Secret as well as Access Token and Access Token Secret. Put these into the `christmas_tree_twitter_auth.py` file and you're good to go. Your application only requires read-only permissions.

Run with the command:

```sh
python3 main.py
```

Ctrl+C KeyboardInterrupt will output the number of times a word was found to help find the
most popular words for the most twinkle. If this is not required and you wish to run the 
program as a background task, run with the command:

```sh
python3 main.py &
```

Merry Christmas!
