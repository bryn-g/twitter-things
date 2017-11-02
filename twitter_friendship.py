import os
import sys
import argparse
import tweepy

import twitter_app_resources

def get_friendship_status(tweepy_api, user_screen_name, other_user_screen_name):
    try:
        user = tweepy_api.get_user(user_screen_name)
        other_user = tweepy_api.get_user(other_user_screen_name)

        friendship = tweepy_api.show_friendship(user.id, user.screen_name, \
                                                other_user.id, other_user.screen_name)

        # friendship object is a tuple
        return [friendship[0].following, friendship[1].following]

    except tweepy.TweepError as err:
        print "tweepy error: " + str(err.message)
        sys.exit()

def get_arguments():
    """ parse and return user supplied arguments. """

    parser = argparse.ArgumentParser(description='print the twitter friendship status of two users.')
    parser.add_argument('users', metavar='@screen_name', type=str, nargs=2,
                        help='user screen name.')
    parser.add_argument('-r', '--resources', help="print twitter api resources used", \
                        required=False, action='store_true')

    args = parser.parse_args()

    return args

def main():
    # twitter api application keys
    app_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY', 'None')
    app_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET', 'None')
    app_access_key = os.environ.get('TWITTER_ACCESS_KEY', 'None')
    app_access_secret = os.environ.get('TWITTER_ACCESS_SECRET', 'None')

    reload(sys)
    sys.setdefaultencoding('utf-8')

    user_args = get_arguments()
    user_screen_name = user_args.users[0]
    other_user_screen_name = user_args.users[1]

    auth = tweepy.OAuthHandler(app_consumer_key, app_consumer_secret)
    auth.set_access_token(app_access_key, app_access_secret)

    try:
        tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, \
                                compression=True)

    except tweepy.TweepError as err:
        print "tweepy error: " + str(err.message)
        sys.exit()

    status = get_friendship_status(tweepy_api, user_screen_name, other_user_screen_name)
    user_following = status[0]
    other_user_following = status[1]

    print "friendship status of users:"

    if (user_following == True and other_user_following == True):
        print "* both " + user_screen_name + " and " + other_user_screen_name + " are following each other."

    elif (user_following == False and other_user_following == True):
        print "* " + other_user_screen_name + " is following " + user_screen_name + " only."

    elif (user_following == True and other_user_following == False):
        print "* " + user_screen_name + " is following " + other_user_screen_name + " only."

    else:
        print "* neither " + user_screen_name + " or " + other_user_screen_name + " are following each other."

    if (user_args.resources):
        twitter_app_resources.print_app_resources(tweepy_api)

if __name__ == '__main__':
    main()
