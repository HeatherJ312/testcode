list=[
    {'name': 'Harry', 'id': 2, 'date': 'April'}, 
    {'name': 'Chris', 'id': 34, 'date': 'May'},
    {'name': 'Heather', 'id':33, 'date': 'September'}
]


lookup = [
    {d['name']: d['name'] }
    for d in list 
]

print(lookup)