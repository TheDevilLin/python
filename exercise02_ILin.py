""" Aling Nena's Reward System
    Author: Lin I
    Description: Reward System?
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
    "Coke sakto",               # 0
    "Boy Bawang",               # 1
    "15pcs. Yucky candy",       # 2
    "15pcs. Pintura candy",     # 3
    "15PHP load",               # 4
    "3 pcs. Dove conditioner",  # 5
    "Cottonbuds",               # 6
    "One sheet of Biogesic",    # 7
    "100mL Pepper/Pintura",     # 8
]

"""Hi <Customer’s name first letters upper case>! 
You have successfully redeem reward #<reward number> - <reward>! 
Thank you for choosing Aling Nena’s Sari-sari store"""

sTemp = input('Please enter text: ')
gender = sTemp[len(sTemp)-1]
rewardNumber = int(sTemp[0])
customerName = sTemp[2: len(sTemp)-2:]


print(f'Hi {customerName.title()}! You have successfully redeem rewrad #{rewardNumber} - {rewards[rewardNumber]}! Thank you for choosing Aling Nena\'s Sari-sari store')