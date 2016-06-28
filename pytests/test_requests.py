#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def funStatus():
    r = requests.get('https://api.github.com/users/octocat/orgs');
    return r.status_code;

def funType():
    r = requests.get('https://api.github.com/users/octocat/orgs');
    return r.headers['content-type']


def test_req():
    assert funStatus() == 200

def test_type():
    assert funType() == 'application/json; charset=utf-8'


# ------
# 200
# 'application/json'
 