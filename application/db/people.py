import random


names = ['Александр', 'Анна', 'Татьяна' , 'Михаил', 'Дмитрий', 'Катерина', 'Олег']

def get_employees ():
    employees = random.choice(names)
    return employees