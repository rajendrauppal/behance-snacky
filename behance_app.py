#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Behance client application in Python
'''


__author__ = 'Rajendra Kumar Uppal'


from behance_python.api import API


API_KEY = 'krFXz0JBgKT5OVYaVRrh9ouWEHSwqycu'


def behance_client():
    behance = API(API_KEY)
    projects = behance.project_search('dog', 'cat', filter_key='')
    owner = projects[0].owners[0].first_name + ' ' + projects[0].owners[0].last_name
    print owner

    users = behance.user_search('dude', '', filter_key='')
    for user in users:
        user_details = behance.get_user(user.username)
        print user_details.first_name
        
        #user_projects = user_details.get_projects(filter_key='')
        #for user_project in user_projects:
        #    print user_project.name

        user_wips = user_details.get_wips(filter_key='')
        for user_wip in user_wips:
            print '[WIP]: ' + user_wip.title


def main():
    behance_client()


if __name__ == '__main__':
    main()
