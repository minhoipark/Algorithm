from itertools import permutations #조합을 만들어 출력해 준다.
from functools import reduce

def solution(numbers): #스트링 형태이다.
    answer =[]
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            a = ''.join(j)
            answer.append(int(a))
    rm_dup = tuple(set(filter(lambda x: int(x)%2 == 1 and x != 1  if  int(x) !=2 else x , answer)))
    cnt=0

    for i in rm_dup:
        for j in range(2,int(i)):
            if int(i) % j == 0:
                break
        else:
            cnt +=1
    return cnt
