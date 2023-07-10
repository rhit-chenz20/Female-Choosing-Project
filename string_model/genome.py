from itertools import chain
from copy import deepcopy

# m=0, l=1, L=2, M=3
rules = {"S": [[1, "L"], [1, "M"]], "L": [[1], [1, "M"], [1, "L"]], "M": [[0], [0, "M"], [0, "L"]]}

def extend_one_genome(g:list):
    ge = deepcopy(g)

    for i in range(len(ge)):
        if (ge[i] in rules.keys()):
            break
    if(ge[i] in rules.keys()):
        li = rules.get(ge[i])
        ge.pop(i)
        re = []
        for j in range(len(li)):
            re.append(list(chain(ge[:i], li[j], ge[i:])))
    else:
        re = [ge]
    return re
    
def extend_all_genome(ges: list):
    re = []
    for e in ges:
        re_ge = extend_one_genome(e)
        re.extend(re_ge)
    return re

def generate_genome(size):
    re = deepcopy(rules.get("S"))
    re =extend_all_genome(re)
    
    while(len(re[len(re)-1]) < size):
        re = extend_all_genome(re)

    for i in range(len(re)):
        for j in range(len(re[i])):
            if(re[i][j] in rules.keys()):
                if(re[i][j] == "M"):
                    re[i][j] = 0
                elif(re[i][j] == "L"):
                    re[i][j] = 1
                
    return sorted(list(filter(lambda x: len(x) == size ,re)))

# print(generate_genome(4))