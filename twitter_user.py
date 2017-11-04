""" twitter users details. """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import argparse
import textwrap
import tweepy
import prettytable

def insert_newlines(in_string, line_length):
    in_string = textwrap.fill(in_string, line_length)
    return in_string

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

def is_dict(item):
    if hasattr(item, '__dict__'):
        item = item.__dict__

    if isinstance(item, dict):
        return True

    return False

def insert_into_table(table, item, attr_line_length, value_line_length):
    if item:
        if hasattr(item, '__dict__'):
            item = item.__dict__

        if isinstance(item, dict):
            for attr, value in item.items():

                value = '{}'.format(value)
                value = insert_newlines(value, value_line_length)
                attr = insert_newlines(attr, attr_line_length)
                table.add_row([attr, value])

    return table

def print_user_details(user, attr_line_length=40, value_line_length=80):
    user_details_table = prettytable.PrettyTable(["Attribute", "Value"])
    user_details_table.align = "l"

    exclude_attributes = ['_json', '_api']
    extended_attributes = {}

    for attr, value in iter(user.__dict__.items()):
        if attr not in exclude_attributes:
            if is_dict(value):
                attr_temp = attr
                k = 0
                while attr_temp in extended_attributes:
                    attr_temp = attr_temp + "_" + str(k)
                    k += 1

                extended_attributes.update({attr_temp: value})
            else:
                value = '{}'.format(value)
                value = insert_newlines(value, value_line_length)
                attr = insert_newlines(attr, attr_line_length)
                user_details_table.add_row([attr, value])

    user_details_table.sortby = "Attribute"
    print(user_details_table)

    #exit()

    for attr, value in iter(extended_attributes.items()):

        user_details_table = prettytable.PrettyTable(["Attribute", "Value"])
        user_details_table.align = "l"

        user_details_table = insert_into_table(user_details_table, {attr: value}, \
                                               attr_line_length, value_line_length)

        user_details_table.sortby = "Attribute"

        print(user_details_table)

def get_arguments():
    parser = argparse.ArgumentParser(description='prints twitter user details.')

    parser.add_argument('-u', '--user', help="twitter user @name or id", type=valid_twitter_user, \
                        required=True)

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

        tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, \
            compression=True)
    except tweepy.TweepError as err:
        print("tweepy.get_user error: ", err)
        sys.exit()

    try:
        twitter_user = tweepy_api.get_user(user_args.user)
    except tweepy.TweepError as err:
        print("tweepy.get_user error: ", err)
        sys.exit()

    attr_line_length = 60
    value_line_length = 80

    print_user_details(twitter_user, attr_line_length, value_line_length)

    print("end.")

if __name__ == '__main__':
    main()
