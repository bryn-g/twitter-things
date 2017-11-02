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
#### twitter_friendship.py
```python (2.7)``` ```tweepy (3.5.0)``` ```prettytable (0.7.2)```
```sh
$ python twitter_friendship.py @halsey @katyperry
twitter friendship status of users:
+--------------------+----------------------------+-----------------------+---------+
| user               | relationship               | other user            | friends |
+--------------------+----------------------------+-----------------------+---------+
| @halsey (45709328) | follows and is followed by | @katyperry (21447363) | yes     |
+--------------------+----------------------------+-----------------------+---------+

$ python twitter_friendship.py @taylorswift13 @halsey
twitter friendship status of users:
+---------------------------+---------------------------------+--------------------+---------+
| user                      | relationship                    | other user         | friends |
+---------------------------+---------------------------------+--------------------+---------+
| @taylorswift13 (17919972) | is not following or followed by | @halsey (45709328) | no      |
+---------------------------+---------------------------------+--------------------+---------+

$ python twitter_friendship.py @taylorswift13 @gracehelbig
twitter friendship status of users:
+-------------------------+-------------------+---------------------------+---------+
| user                    | relationship      | other user                | friends |
+-------------------------+-------------------+---------------------------+---------+
| @gracehelbig (21502768) | is only following | @taylorswift13 (17919972) | no      |
+-------------------------+-------------------+---------------------------+---------+
```
```ruby
end.
```
