""" twitter api app resources using tweepy wrapper. """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import time
import datetime
import argparse
import tweepy
import prettytable

def get_app_resources(tweepy_api):
    try:
        api_rate_limits = tweepy_api.rate_limit_status()

    except tweepy.TweepError as err:
        print("tweepy_api.rate_limit_status error: ", err)
        sys.exit()

    return api_rate_limits

def get_datetime_local_offset():
    now_timestamp = time.time()
    local_offset = datetime.datetime.fromtimestamp(now_timestamp) - \
                   datetime.datetime.utcfromtimestamp(now_timestamp)

    return local_offset

def format_resource_row(resource_name, reset_time, resource_limit, resource_remaining, \
                        print_local_time):
    utc_time = datetime.datetime.utcfromtimestamp(reset_time)

    if print_local_time:
        reset_time = utc_time + get_datetime_local_offset()
        reset_time = reset_time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        reset_time = utc_time.strftime("%Y-%m-%d %H:%M:%S UTC")

    return [str(resource_name), reset_time, str(resource_limit), str(resource_remaining)]

def print_app_resources(tweepy_api, print_all_resources=False, print_local_time=False):
    """ prints a table of app resource information. """

    api_rate_limits = get_app_resources(tweepy_api)

    rate_limits_table = prettytable.PrettyTable(["twitter api resource", "reset time", "limit", \
                                                 "remaining"])
    rate_limits_table.align = "l"

    for attr, value in iter(api_rate_limits['resources'].items()):
        for sattr, svalue in iter(api_rate_limits['resources'][attr].items()):

            row = format_resource_row(sattr, svalue['reset'], svalue['limit'], \
                                      svalue['remaining'], print_local_time)

            # only print resources that have been touched
            if not print_all_resources:
                if svalue['limit'] != svalue['remaining']:
                    rate_limits_table.add_row(row)
            else:
                rate_limits_table.add_row(row)

    print(rate_limits_table)

def get_arguments():
    parser = argparse.ArgumentParser(description='print twitter app api resource usage.')
    parser.add_argument('-a', '--all', help="print list of all resources even if unused", \
                         required=False, action='store_true')
    parser.add_argument('-l', '--local', help="print reset time as local instead of utc", \
                         required=False, action='store_true')

    args = parser.parse_args()

    return args

def main():
    app_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY', 'None')
    app_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET', 'None')
    app_access_key = os.environ.get('TWITTER_ACCESS_KEY', 'None')
    app_access_secret = os.environ.get('TWITTER_ACCESS_SECRET', 'None')

    user_args = get_arguments()

    try:
        auth = tweepy.OAuthHandler(app_consumer_key, app_consumer_secret)
        auth.set_access_token(app_access_key, app_access_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,
                         compression=True)

    except tweepy.TweepError as err:
        print("tweepy.get_user error: ", err)
        sys.exit()

    print_app_resources(api, user_args.all, user_args.local)

    print("end.")

if __name__ == '__main__':
    main()
