import requests
import os
import random
import json
import string

raju = 'hlpzetb'
me = 'qlafenq'

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "https://www.getlinks.info/love/fool.php"
names = requests.get("https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.json").json()

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    myname = name.lower() + name_extra
    crushname = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects="False", data={
        'nameField': myname,
        'crushField': crushname,
        'ownerid': raju #whose link to send the names to, values are assigned in lines 7 and 8

    })

    print("Sending myname "+ myname + " and crush name "+ crushname)
