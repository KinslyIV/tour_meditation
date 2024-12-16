from head import *


with open("data.json",'r') as file:
    data = json.load(file)

data["disc_mem_last_week"] = data["disc_mem_week"]

data["disc_mem_week"] = []

data["members_week"] = data["next_week"]

data["next_week"] = []

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)