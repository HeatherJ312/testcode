list=[
    {'name': 'Harry', 'id': 4, 'date': 'April', 'colour':'Green'}, 
    {'name': 'Chris', 'id': 36, 'date': 'May', 'colour': 'Black'},
    {'name': 'Heather', 'id':36, 'date': 'September', 'colour': 'purple'}
    {'name': 'Sam', 'id':1, 'date': 'December', 'colour': 'blue'}
]


lookup = [
    {d['name']: d['name'] }
    for d in list 
]

print(lookup)