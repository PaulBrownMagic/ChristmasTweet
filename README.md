# Christmas Tweet

This code will filter the Twitter streaming API for keywords and twinkle the corresponding 
light on the [Pi Hut Christmas Tree](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi).

Requires Tweepy:

```sh
sudo pip3 install tweepy
```

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
