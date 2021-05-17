def solution(answers):
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    score =[0,0,0]
    result = []

    for i, answer in enumerate(answers):
        if answer == no1[i%len(no1)]:
            score[0] += 1
        if answer == no2[i%len(no2)]:
            score[1] += 1
        if answer ==no3[i%len(no3)]:
            score[2] +=1

    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)

    return result