def solution(scoville, K):

    answer = 0

    import heapq

    heapq.heapify(scoville)
    while len(scoville) > 1:
        num = heapq.heappop(scoville)
        if num < K:
            heapq.heappush(scoville, num+ heapq.heappop(scoville) * 2)
            answer += 1
        else:
            return answer
    if heapq.heappop(scoville) < K:
        return -1


    # scoville = [scoville for scoville in scoville if scoville < K]
    # scoville.sort(reverse=True)
    # if len(scoville) == 1 and scoville[0] < K:
    #     return -1
    # elif len(scoville) == 1 or len(scoville) == 0:
    #     return 0
    # else:
    #     while len(scoville) > 1:
    #         num = scoville.pop()
    #         if num < K:
    #             num = num + scoville.pop()*2
    #             scoville.insert(0, num)
    #             answer = answer + 1

    # q = queue.PriorityQueue()
    #
    # for sco in scoville:
    #     q.put(sco)
    # while q.qsize() > 1:
    #     num = q.get()
    #     if num < K:
    #         num = num + q.get()*2
    #         q.put(num)
    #         answer = answer + 1
    #     else:
    #         return answer
    # if q.get() < K:
    #     return -1

    return answer


result = solution([1, 2, 3, 9, 10, 12], 7)
print("answer: ", result)
