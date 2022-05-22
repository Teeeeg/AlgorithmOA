from heapq import heappop, heappush


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    # 小根堆用于追踪最小投资金额
    minCapitalHeap = []
    # 大根堆用于追踪最大利润
    maxProfitHeap = []

    # 先排列好所有的投资
    for i in range(len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    availableCapital = initialCapital

    for _ in range(numberOfProjects):
        # 获取能投资的项目
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            # 把能投资的项目按最大利润排列
            heappush(maxProfitHeap, (-profits[i], i))

        if not maxProfitHeap:
            break

        availableCapital += -heappop(maxProfitHeap)[0]

    return availableCapital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
