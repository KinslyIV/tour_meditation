""""
This code is just to automate the turn for for poeple in a list
"""

import json

def addMember(member):

    members = []

    with open('members.json', 'r') as file:
        members = json.load(file)

    members.append(member)
    members.sort()

    with open('members.json', 'w') as file:
        json.dump(members, file)


def get_members():
    
    members = []

    with open('members.json', 'r') as file:
        members = json.load(file)

    return members


def get_mem_week():
    members = []

    with open('members_week.json', 'r') as file:
        members = json.load(file)

    return members



def get_next(dis_memb):

    members = get_members()
    mem_week = get_mem_week()
    rem_members = mem_week - dis_memb

    

