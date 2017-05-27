"""
Aling Nena stores her soft drink stock on two refrigerators.
She stores Coke, Sprite and Royal on her Sari-sari store's refrigerator while
RC and 7UP can be found on her house's refrigerator.
Help Aling Nena to properly respond to her customer
when buying softdrinks.
The reply will depend if the soft drink brand is on the store's ref,
on the house's ref or none. If the customer buys a soft drink brand that is:
    1. stored on the store, she will respond 'Got it!'
    2. stored on the house, she will respond 'Please wait for a while!'
    3. not sold by her, she will respond 'Sorry we do not sell that. We only
    have <input here the soft drink brands>'
"""

softDrink = input('Hi! What soft drink brand do you want?')

store = [
    "Coke",
    "Sprite",
    "Royal"
]

house = [
    "RC",
    "7UP"
]

#softDrink = input('Please input here the soft drink brand: ')
isAvailable = 0

for x in store:
    if softDrink == x:
        print(f'Got it!')
        isAvailable = 1
         

for y in house:
    if softDrink == y:
        print(f'Please wait for a while!')
        isAvailable = 1
         

if isAvailable == 0:
    print(f'Sorry we do not sell that. We only have ')
    for x in store:
        print(f'{x} ')
        
    for y in house:
        print(f'{y} ')
        
    