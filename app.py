import random


def excuse_generator(quien, que, cuando):
    indice_quien = random.randint(0, len(quien) - 1)
    indice_que = random.randint(0,len(que) - 1)
    indice_cuando = random.randint(0,len(cuando) - 1)
    result = f'{quien[indice_quien]} {que[indice_que]} {cuando[indice_cuando]}'
    return result


who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broke']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']
excuse = excuse_generator(who, what, when)

print(excuse)
