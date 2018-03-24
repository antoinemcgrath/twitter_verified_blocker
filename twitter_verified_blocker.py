#!/usr/bin/python

#### A tool for blocking all verified users on Twitter.

#### Import dependencies
import json
import tweepy
import re
import random
import sys
import timeit

#### Define variables
start = timeit.default_timer()
exception_title = 'exceptions'
mypath = "blocked.txt"
counter = 0

#### Load API keys file 
keys_json = json.load(open('/usr/local/keys.json'))

#### Specify key dictionary wanted (generally [Platform][User][API])
Keys = keys_json["Twitter"]["ClimateCong_Bot"]["ClimateCongressBot"]

#### Access API using key dictionary definitions
auth = tweepy.OAuthHandler( Keys['Consumer Key (API Key)'], Keys['Consumer Secret (API Secret)'] )
auth.set_access_token( Keys['Access Token'], Keys['Access Token Secret'] )
#### retry_count/_delay/_errors is in anticipatation of twitter's API being over capacity (error 130) and etc
api = tweepy.API(auth, retry_count=10, retry_delay=5, retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit=True)
user = Keys['Owner']


#### Fetch the user id's of those listed in the exceptions list
def get_exceptions_list():
    listed = []
    protect_list = []
    for page in tweepy.Cursor(api.list_members, user, exception_title).pages():
        listed.extend(page)
    for x in listed:
        protect_list.append(x.id)
    return(protect_list)


def check_exceptions_list(a_user_id_2_block):
    if a_user_id_2_block in protect_list:
        #print("User is on exceptions list & will not be blocked:", a_user_id_2_block, end='\r')
        return None
    else:
        return(a_user_id_2_block)


# Calculates and returns a human readable time difference
def calc_time():
    #Stop the timer
    stop = timeit.default_timer()
    total_time = stop - start
    #Formate running time.
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    timed = str("%d:%d:%d" % (hours, mins, secs))
    return(timed)


#Check if user is already blocked, block & add to list if not
def append_to_blocked_list(a_user_id_2_block):
    with open(mypath, "r+", newline=None) as file:
        for line in file:
            if str(a_user_id_2_block) in line:
                print("Previously added to block list")
                return None
            else: # not found, we are at the eof
                pass
        file.write(str(a_user_id_2_block) + '\n') # append missing data
        api.create_block(a_user_id_2_block, wait_on_rate_limit=True)
        return("New")


def add_2_counter(counter):
    counter += 1
    if counter % 100 == 0:
        timed = calc_time()
        print("Time elapsed:", timed, " Users blocked:", str(counter))
    else:
        print(counter, end='\r')
        pass
    return(counter)


def process_a_user_id(a_user_id, counter):
    a_user_id_2_block = check_exceptions_list(a_user_id)
    if a_user_id_2_block is not None:
        #Check if user is already blocked & block if not
        new_block = append_to_blocked_list(a_user_id_2_block)
        if new_block is not None:
            counter = add_2_counter(counter)
    return(counter)


def process_a_user(a_user, counter):
    if a_user.verified == True:
        a_user_id = a_user.id
        counter = process_a_user_id(a_user_id, counter)
    else:
        pass
    return(counter)



#### Work flow

protect_list = get_exceptions_list()
print("Protect list number of entries =", len(protect_list))

#### Block verified users that are on the twitter managed verified list
for a_user_id_2_block in tweepy.Cursor(api.friends_ids, id="verified", wait_on_rate_limit=True).items():
    counter = process_a_user_id(a_user_id_2_block, counter)

#### Block verified users that are following you
for a_user in tweepy.Cursor(api.followers, screen_name=user, wait_on_rate_limit=True).items():
    counter = process_a_user(a_user, counter)

#### Block verified users that are following the user handle "Twitter"
for a_user in tweepy.Cursor(api.followers, screen_name="Twitter", wait_on_rate_limit=True).items():
    counter = process_a_user(a_user, counter)




###################################################################
#  Do not use any of the code I have written with harmful intent. #
#                                                                 #
#    By using this code you accept that everyone has the          #
#       right to choose their own gender identity.                #
###################################################################
