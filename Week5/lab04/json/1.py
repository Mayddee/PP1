import json
#with open('data.json', 'w') as file:
#   json.dump(data, file, indent=3)

with open('data.json', 'r') as file:
    data = json.load(file)

x = """
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""
print(x)
idata = data["imdata"]

for i in idata:
    print("{DN:50}{Speed:>29}{MTU:>7}".format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed= i["l1PhysIf"]["attributes"]["speed"], MTU=i["l1PhysIf"]["attributes"]["mtu"]))