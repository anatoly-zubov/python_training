import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.group_contact import Group_contact


try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o=="-n":
        n = int(a)
    elif o== "-f":
        f = a
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group_contact(firstname ="", lastname="", mobile="", email="", email2="", email3="")] + \
           [Group_contact(firstname =random_string("firstname", 10), lastname=random_string("lastname", 10),
                          mobile=random_string("mobile", 10), email=random_string("email", 10))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))
