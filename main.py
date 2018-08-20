from time import sleep
from random import randint

fridge_contents = 50  # food items
tiredness = 0
sleep_hours = 7  # hours
code = False
cup_contents = 1000  # ml

food = 1
food_delivery = 50

coffee = 50
coffee_delivery = 1000
alive = True


def consume(consumable, availability, delivery):
    available_consumable = availability - consumable
    if available_consumable < 1:
        print("Delivery Received!")
        available_consumable = delivery
    return available_consumable


while alive:

    fridge_contents = consume(food, fridge_contents, food_delivery)
    print("Consumed Food! Food Remaining in Fridge: " + str(fridge_contents))

    for hour in range(sleep_hours):
        sleep(1)
        print("Sleeping!")

    for hour in range(24 - sleep_hours):
        code = True
        print("Coding = " + str(code))

        cup_contents = consume(coffee, cup_contents, coffee_delivery)
        print("Consumed Coffee! Coffee Remaining in Cup: " + str(cup_contents))

    code = False
    print("Coding = " + str(code))

    death = randint(1, 260001)  # http://www.spencergreenberg.com/2013/10/which-risks-of-dying-are-worth-taking/
    if death == 42:
        alive = False
    else:
        print("There is only one thing we say to Death: 'not today'")