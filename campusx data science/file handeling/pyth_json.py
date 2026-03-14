# load and dump

import json

# l = [1,2,3,4,5]
# with open('sample.txt','w') as f:
#     d = json.dump(l,f)
#     print(d)
#     print(type(d))

d = {
    'name':12,
    'age':24,
    'school':'sainik school'
}

with open('demo.json','w') as f:
    json.dump(d,f,indent=4)


# serializaion and deserialization
# pickling
