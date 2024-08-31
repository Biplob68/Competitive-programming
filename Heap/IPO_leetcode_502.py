from heapq import heappop
from heapq import heappush


def maximum_capital(c, k, capital, profits):
    capital_min_heap = []
    profit_max_heap = []

    current_capital = c

    for i in range(len(capital)):
        heappush(capital_min_heap, (capital[i], i))

    while k > 0:
        while capital_min_heap and capital_min_heap[0][0] <= current_capital:
            value, index = heappop(capital_min_heap)
            heappush(profit_max_heap, -(profits[index]))

        if not profit_max_heap:
            break

        current_capital += - heappop(profit_max_heap)
        k -= 1

    return current_capital


if __name__ == '__main__':
    k = 1
    c = 0
    cap = [1, 1, 2]
    pro = [1, 2, 3]
    print(maximum_capital(c, k, cap, pro))
    print()
