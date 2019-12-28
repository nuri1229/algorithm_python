def solution(stock, dates, supplies, k):

    import heapq

    answer = 0

    q = []
    dates_index = 0

    while stock < k:
        for i in range(dates_index, len(dates)):
            if(dates[i] <= stock):
                heapq.heappush(q, -supplies[i])
                dates_index += 1
            else:
                break
        stock += heapq.heappop(q) * -1
        answer += 1


    print(q)
    # date = heapq.heappop(dates)
    # supply = supplies[supplyCount]
    # while cnt < k:
    #     print(cnt, '일째 잔여량 ', stock)
    #     if stock < k-cnt:
    #         if date == cnt:
    #             stock = stock + supply
    #             supplyCount += 1
    #             date = heapq.heappop(dates)
    #             supply = supplies[supplyCount]
    #             answer += 1
    #     else:
    #         return answer
    #     stock -= 1
    #     cnt += 1
    # cnt = 0
    # index = 0
    # while cnt < k:
    #     print(cnt, '일째 잔여량', stock, '남은일수 ', k-cnt)
    #     for j in range(index, len(dates)):
    #         if dates[j] == cnt and stock < k-cnt:
    #             answer += 1
    #             stock += supplies[j]
    #             index += 1
    #     stock -= 1
    #     cnt += 1

    return answer

print(solution(4, [4,10,15], [20,5,10], 30))
