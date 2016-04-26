#!/usr/bin/env python
# coding=utf-8

import requests,ast

class Seebug(object):
    def __init__(self, token):

        self.token = token
        self.headers = {'Authorization': 'Token %s' % self.token}
        self.r = None

    def requestisok(self):
        if self.r.status_code == requests.codes.ok:
            return True
        else:
            return False

    def error(self):
        content = ast.literal_eval(self.r.content)
        return "Error:" + content['detail'] + "\n"

    def login(self):
        pass

    def poc_list(self):
        self.r = requests.get('https://www.seebug.org/api/user/poc_list', headers=self.headers)
        return self.requestisok()

    def seek(self, keyword):
        self.r = requests.get('https://www.seebug.org/api/user/poc_list?q=%s' % keyword, headers=self.headers, )
        return self.requestisok()

    def retrieve(self, ID):
        self.r = requests.get('https://www.seebug.org/api/user/poc_detail?id=%s' % ID, headers=self.headers, )
        return self.requestisok()

    def response(self):
        return ast.literal_eval(self.r.content)
