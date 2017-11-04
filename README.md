# twitter-things
:baby_chick: Other code and things for twitter.

#### twitter_user.py
```python (2.7, 3.6)``` ```tweepy (3.5.0)``` ```prettytable (0.7.2)```
```sh
$ python twitter_user.py -u @halsey
+------------------------------------+----------------------------------------+
| Attribute                          | Value                                  |
+------------------------------------+----------------------------------------+
| contributors_enabled               | False                                  |
| created_at                         | 2009-06-08 23:58:35                    |
| default_profile                    | False                                  |
| default_profile_image              | False                                  |
| description                        | true, I talk of dreams. which are the .|
| favourites_count                   | 4716                                   |
| follow_request_sent                | False                                  |
| followers_count                    | 6839030                                |
| following                          | False                                  |
| friends_count                      | 2948                                   |
...
```

#### twitter_app_resources.py
```python (2.7, 3.6)``` ```tweepy (3.5.0)``` ```prettytable (0.7.2)```
```sh
usage: twitter_app_resources.py [-h] [-a] [-l]

optional arguments:
  -h, --help   show this help message and exit
  -a, --all    print list of all resources even if unused
  -l, --local  print reset time as local instead of utc
  
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
```python (2.7, 3.6)``` ```tweepy (3.5.0)``` ```prettytable (0.7.2)```
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
