#!/usr/bin/python3
"""nd the number of subs"""
import requests


def number_of_subscribers(subreddit):
    ''' get numberbcribers'''

    url = 'http://reddit.com/r/{}/about.json'
    headers = {'User-agent': 'colombiandreamm'}
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 200:
        subs = response.json()
        '''subs0 = subs['data']['subscribers']'''
        subs0 = subs.get('data').get('subscribers')
        return subs0
    else:
        return 0
