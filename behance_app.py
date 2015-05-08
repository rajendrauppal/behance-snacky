#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Behance client application in Python
'''


__author__ = 'Rajendra Kumar Uppal'
__copyright__ = "Copyright 2015, Rajendra Kumar Uppal"
__credits__ = ["Rajendra Kumar Uppal"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Rajendra Kumar Uppal"
__email__ = "rajen.iitd@gmail.com"
__status__ = "Production"


from behance_python.api import API


# Register your Behance app at https://www.behance.net/dev/register 
# and generate API key
API_KEY = 'your api key'


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
