import json
"""d={
    'Name':'Sadhu',
     'USN':'4CI22AI037'
}
f=json.dumps(d)
print(type(f))
print(f)

y=json.loads(f)
print(type(y))
print(y)"""
j='{"Name":"Sadhu","USN":"4CI22AI037"}'
x=json.loads(j)


print(type(j))
print(x)