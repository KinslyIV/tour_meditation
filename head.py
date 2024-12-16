""""
This code is just to automate the turn for for poeple in a list
"""

import json
from datetime import datetime



week_days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]



def addMember(new_member, isiter=False):

    with open('data.json', 'r') as file:
        data = json.load(file)

    mem_list = data["members"]

    if(isiter):
        for mem in new_member:
            mem_list.append(mem)
    else:
        mem_list.append(new_member)
    
    mem_list.sort()

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_members():

    with open('data.json', 'r') as file:
        data = json.load(file)

    members = data["members"]

    return members


def get_mem_week():

    with open('data.json', 'r') as file:
        data = json.load(file)

    assigned_members = data["members_week"]

    return assigned_members


def ev_mem_week():
    ass_mem = get_mem_week()
    ud_mem = []
    d_mem = []
    for mem in ass_mem:
        if(not int(input(f"Did {mem} shared their meditation ? "))):
            ud_mem.append(mem)
        else:
            d_mem.append(mem)

    return (d_mem, ud_mem)


def set_dmem_week() -> list:
    ev_week_mem = ev_mem_week()
    d_mem = ev_week_mem[0]
    print(ev_week_mem[1])

    with open('data.json', 'r') as file:
        data = json.load(file)

    data["disc_mem_week"] = d_mem

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_dmem_week() -> list:
    with open('data.json', 'r') as file:
        data = json.load(file)

    return data["disc_mem_week"]


def get_udmem_week():
    mem_week = get_mem_week()
    dmem = get_dmem_week()
    udmem = []
    for mem in mem_week:
        if(mem not in dmem):
            udmem.append(mem)
    
    return udmem


def get_dmem_last_week() -> list:
    with open('data.json', 'r') as file:
        data = json.load(file)

    return data["disc_mem_last_week"]


def log(next_mem):

    sep = " "
    day = datetime.now().day

    with open("log.txt", 'w') as log:
        log.writelines([ sep.join(week_days[i] + (day + i) + next_mem[i]) for i in range(7)])


def ev_next_week_pool():

    members = get_members()
    mem_week = get_mem_week()
    dmem_week = get_dmem_week()
    dmem_last_week = get_dmem_last_week()
    next_week_pool = get_udmem_week()



    for mem in members:
        if(mem not in mem_week and mem not in dmem_last_week):
            next_week_pool.append(mem)
    
    if ( len(next_week_pool) < 7):
        dmem_last_week.reverse()
        while(len(next_week_pool) < 7):
            next_week_pool.append(dmem_last_week.pop())

    return next_week_pool


def set_next_week():

    with open('data.json', 'r') as file:
        data = json.load(file)

    data["next_week"] = ev_next_week_pool()[0:7]

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_next_week():
    with open('data.json', 'r') as file:
        data = json.load(file)

    return data["next_week"]