# twitter-things
:baby_chick: Other code and things for twitter.

#### twitter_app_resources.py
```python (2.7)``` ```tweepy (3.5.0)``` ```prettytable (0.7.2)```
```sh
$ python twitter_app_resources.py
+--------------------------------+-------------------------+-------+-----------+
| twitter api resource           | reset                   | limit | remaining |
+--------------------------------+-------------------------+-------+-----------+
| /application/rate_limit_status | 2017-10-31 04:49:26 UTC | 180   | 177       |
| /followers/list                | 2017-10-31 05:02:03 UTC | 15    | 8         |
| /followers/ids                 | 2017-10-31 05:02:03 UTC | 15    | 14        |
| /users/show/:id                | 2017-10-31 05:02:03 UTC | 900   | 897       |
+--------------------------------+-------------------------+-------+-----------+
```
### twitter_friendship.py
```python (2.7)``` ```tweepy (3.5.0)```
```sh
$ python twitter_friendship.py @halsey @katyperry
friendship status of users:
* both @halsey and @katyperry are following each other.

$ python twitter_friendship.py @taylorswift13 @halsey
friendship status of users:
* neither @taylorswift13 or @halsey are following each other.

$ python twitter_friendship.py @taylorswift13 @gracehelbig
friendship status of users:
* @gracehelbig is following @taylorswift13 only.
```
```ruby
end.
```
