#!/usr/bin/env python
# coding=utf-8

from Seebug import *

def show_poc_list(content):
    for item in content:
        print "id:%s\t" % item['id'],
        print "name:%s" % item['name']

def show_poc(content):
    if content.has_key('code'):
        print content['code']
    else:
        print "status:%s\t" % content['status']
        print "message:%s" % content['message']

def main(token):
    '''init class Seebug with token'''
    z = Seebug(token)
    '''get poc_list'''
    if z.poc_list():
        print "poc_list:"
        show_poc_list(z.response())
    else:
        print z.error()
    '''seek(keyword)'''
    if z.seek(keyword="Redis"):
        print "seek:"
        show_poc_list(z.response())
    else:
        print z.error()
    '''retrieve(ID)'''
    if z.retrieve(ID="90021"):
        print "retrieve:"
        show_poc(z.response())
    else:
        print z.error()


if __name__ == '__main__':
    token = raw_input('Please input token:')
    main(token=token)