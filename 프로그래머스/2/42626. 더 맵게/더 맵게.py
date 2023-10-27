import heapq

def all_ele_more_than_k(arr, K):
    for e in arr:
        if e < K:
            return False
    return True

def solution(scoville, K):
    answer = 0
    if all_ele_more_than_k(scoville, K):
        return answer
    
    heapq.heapify(scoville)
    l = []
    
    while len(scoville) > 1:
        answer += 1
        l.append(heapq.heappop(scoville))
        l.append(heapq.heappop(scoville))
        
        new_food = l[0] + (l[1] * 2)
        l.clear()
        heapq.heappush(scoville, new_food)
        
        if all_ele_more_than_k(scoville,K):
            break
    else:
        return -1
    return answer