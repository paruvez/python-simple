#import file
import random

#inputs
subjects=[
    "Amir Khan",
    "Rajesh Khanna",
    "Sanjay Datta",
    "Virat Kholi",
    "Tom Curuise",
    "mamta Didi",
    "DMK"
]
actions=[
    "Launce",
    "Cancel",
    "Dances",
    "Break-up with",
    "Scam",
    "order"

]
place_or_things=[
    "at kolkata",
    "in Wb Metro train",
    "a plate of briyani",
    "inside Nabanna"
    "while Acting",
    "in street"
]

#Headline Gen Loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(place_or_things)
    headlines=f" Breaking News:{subject} {action} {place_or_thing}"
    print("\n" + headlines)
    user_input= input("\nDo you want anoyther headline?").strip().lower()
    if user_input=="no":
                 break
print("\nGood Bye")
