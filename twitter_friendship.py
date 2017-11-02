import os
import sys
import argparse
import tweepy
import prettytable

def valid_twitter_user(user_id):
    user_id = str(user_id)

    if user_id.isdigit():
        return user_id
    else:
        if user_id[0] != '@':
            msg = "user name must start with @."
            raise argparse.ArgumentTypeError(msg)

        if len(user_id) > 16 or len(user_id) < 2:
            msg = "user names are 16 characters or less."
            raise argparse.ArgumentTypeError(msg)

        user_name_temp = user_id[1:]
        for char in user_name_temp:
            if not char.isalnum() and char != '_':
                msg = "user name characters are alphanumeric or _."
                raise argparse.ArgumentTypeError(msg)

        return user_id

def get_follow_status(tweepy_api, user_id, other_user_id):
    try:
        user = tweepy_api.get_user(user_id)
        other_user = tweepy_api.get_user(other_user_id)

        # tuple returned from show_friendship
        friendship = tweepy_api.show_friendship(user.id, user.screen_name, \
                                                other_user.id, other_user.screen_name)

        # return user objects (since we have them) and friendship tuple
        return ([user, other_user, friendship])

    except tweepy.TweepError as err:
        print "tweepy error: " + str(err.message)
        sys.exit()

# follow_status is a tuple ([user_object, other_user_object, friendship_tuple])
def print_follow_status(follow_status):

    user, other_user, friendship = follow_status

    user_following = friendship[0].following
    other_user_following = friendship[1].following

    # format user id strings for print
    user_str = "@" + str(user.screen_name) + " (" + str(user.id) + ")"
    other_user_str = "@" + str(other_user.screen_name) + " (" + str(other_user.id) + ")"

    print "twitter friendship status of users:"

    friendship_table = prettytable.PrettyTable(["user", "relationship", "other user", "friends"], header=True)
    friendship_table.align = "l"

    if (user_following == True and other_user_following == True):
        friendship_table.add_row([user_str, "follows and is followed by", other_user_str, "yes"])

    elif (user_following == False and other_user_following == True):
        friendship_table.add_row([other_user_str, "is only following", user_str, "no"])

    elif (user_following == True and other_user_following == False):
        friendship_table.add_row([user_str, "is only following", other_user_str, "no"])

    else:
        friendship_table.add_row([user_str, "is not following or followed by", other_user_str, "no"])

    print friendship_table

def get_arguments():
    parser = argparse.ArgumentParser(description='print the twitter friendship status of two users.')
    parser.add_argument('users', metavar='@user', type=valid_twitter_user, nargs=2,
                        help='twitter user @name or id')

    args = parser.parse_args()

    return args

def main():
    app_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY', 'None')
    app_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET', 'None')
    app_access_key = os.environ.get('TWITTER_ACCESS_KEY', 'None')
    app_access_secret = os.environ.get('TWITTER_ACCESS_SECRET', 'None')

    reload(sys)
    sys.setdefaultencoding('utf-8')

    user_args = get_arguments()
    user_id, other_user_id = user_args.users

    auth = tweepy.OAuthHandler(app_consumer_key, app_consumer_secret)
    auth.set_access_token(app_access_key, app_access_secret)

    try:
        tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, \
                                compression=True)

    except tweepy.TweepError as err:
        print "tweepy error: " + str(err.message)
        sys.exit()

    # returns a tuple
    follow_status = get_follow_status(tweepy_api, user_id, other_user_id)

    print_follow_status(follow_status)

if __name__ == '__main__':
    main()
