#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Behance client application in Python
'''


__author__ = 'Rajendra Kumar Uppal'


from behance_python.api import API


API_KEY = 'JFkguN6GZLoxQcOg2vkohmkk0165tuaS'


def behance_client():
    behance = API(API_KEY)
    projects = behance.project_search('dog', 'cat', filter_key='')
    owner = projects[0].owners[0].first_name + ' ' + projects[0].owners[0].last_name
    print owner


def main():
    behance_client()


if __name__ == '__main__':
    main()
