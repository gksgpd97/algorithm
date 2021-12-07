def solution(people, limit):
    answer = 0
    break_check = 0
    people.sort()
    while len(people)!=0:
        if(len(people)==1):
            answer += 1
            break
        else:
            max_w = people[-1]
            min_w = people[0]
            sum_w = min_w + max_w
            if sum_w <= limit:
                answer += 1
                people.pop(0)
                people.pop(-1)
            else:
                answer += 1
                people.pop(-1)
    #pop떄문에 효율성 하나 통과못함
    return answer