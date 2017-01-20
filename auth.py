#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import requests
import getpass


def login(uname, passw):
    url_1 = 'http://www.google.co.in'

    headers = \
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

    session = requests.Session()

    res = session.get(url_1, headers=headers)

    magic = res.url.split('?')[1]

    my_referer = res.url

    payload = {
        '4Tredir': 'http://google.com/',
        'magic': str(magic),
        'username': uname,
        'password': passw,
        }

    url_2 = 'http://192.168.201.6:1000/'

    res = requests.post(url_2, headers=headers, data=payload)

    if 'Failed' in res.text:
        return False
    else:
        print('Successfully authenticated. Now you may close this window. :)')
        return True


try:
    res = requests.head('http://www.google.co.in')
    print('Already connected. :)')
except requests.ConnectionError:

    if not os.path.isfile('.fgauthcred'):
        print('Enter credentials to login, for the first time. (password will be hidden.)')

        username = input('Enter your username : ').strip()
        password = getpass.getpass()

        if login(username, password):
            with open('.fgauthcred', 'w') as f:
                f.write(username + '\n' + password + '\n')
        else:
            print('Wrong cred. try again.\n')
            username = input('Enter your username : ').strip()
            password = getpass.getpass()
            login(username, password)
    else:
        with open('.fgauthcred', 'r') as f:
            (username, password) = [x.strip() for x in f]
        login(username, password)
