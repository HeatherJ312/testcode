list=[
    {'name': 'Harry', 'id': 4, 'date': 'April'}, 
    {'name': 'Chris', 'id': 36, 'date': 'May'},
    {'name': 'Heather', 'id':36, 'date': 'September'}
    {'name': 'Sam', 'id':1, 'date': 'December'}
]


lookup = [
    {d['name']: d['name'] }
    for d in list 
]

print(lookup)