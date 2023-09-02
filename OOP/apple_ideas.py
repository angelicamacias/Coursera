class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    apple_change = martin.apples
    martin.apples = johanna.apples
    johanna.apples = apple_change

    you.apple = martin.apples
    me.apple = johanna.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    total_ideas = martin.ideas + johanna.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



