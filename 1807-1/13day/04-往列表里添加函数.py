import random
def addnum():
    list = []
    while True:
        num = random.randint(1,100)
        if num not in list:
            list.append(num)
            if len(list) == 10:
               print(list)
               break
addnum()
