def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people)-1
    while left <= right:
        if(left==right):
            answer += 1
            break
        else:
            max_w = people[right]
            min_w = people[left]
            sum_w = min_w + max_w
            if sum_w <= limit:
                answer += 1
                right -= 1
                left += 1
            else:
                answer += 1
                right -= 1
    #print(people)
    return answer