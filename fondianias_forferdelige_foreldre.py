"""
Utgave 5, 2018

Et tall er enbarnsforelder om én, og bare én, av tallets delstrenger er
delelig på antall siffer i det opprinnelige tallet.
Hva er summen av alle enbarnsforeldre fra én til én million?
"""

single_child_parents = set()

def is_single_childe_parent(num_str):
    num_len = len(num_str)
    divisible = False 
    for sub in consecutive_groups(str(n)):
        num = int(sub)
        if num % num_len == 0:
            if divisible:
                divisible = False
                break 
            else:
                divisible = True
    return divisible

def consecutive_groups(s):
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            yield s[index:index+size]


for n in range(1, 1000000):
    if is_single_childe_parent(str(n)):
        single_child_parents.add(n)
      
print(sum(single_child_parents))
"""
time pypy3 fondianias_forferdelige_foreldre.py
60195928269
pypy3 fondianias_forferdelige_foreldre.py  1.31s user 0.03s system 99% cpu 1.344 total
"""

