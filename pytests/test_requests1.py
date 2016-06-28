#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
'''

def funDelete():
    r = requests.delete('http://www.thomas-bayer.com/sqlrest/INVOICE/26/');
    print r.headers;
    print r.status_code;
    print r.text;
    return r.status_code;

#funDelete()

def test_funDelete():
    assert funDelete() == 200;

'''
def funPut():
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <resource>
    <ID>51</ID>
    <NAME>Kelly</NAME>
    <PRICE>3.2</PRICE>
    </resource>"""
    headers = {'Content-Type':'application/xml'}
    r1 = requests.post('http://www.thomas-bayer.com/sqlrest/PRODUCT/', data = xml, headers=headers);
    print r1.status_code;
    return r1.status_code;
    #print r1.content;

def test_funPut():
    assert funPut() == 201;
#def funType():
#    r = requests.get('https://api.github.com/users/octocat/orgs');
#    return r.headers['content-type']


#def test_req():
#    print funStatus

#def test_type():
#    assert funType() == 'application/json; charset=utf-8'


# ------
# 200
# 'application/json'
