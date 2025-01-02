from collections import deque


def FindTheWinner(n: int, k: int) -> int:
    q = deque()
    for i in range(1, n + 1):
        q.append(i)

    while len(q) > 1:
        for i in range(k - 1):
            num = q.popleft()
            q.append(num)
        q.popleft()
    return q[0]


def FindTheWinnerOptimal(n: int, k: int) -> int:
    def helper(n: int, k: int) -> int:
        if n == 1:
            return 0
        return (helper(n - 1, k) + k) % n

    return helper(n=n, k=k) + 1


ans = FindTheWinnerOptimal(5, 2)
print("The Answer is: ", ans)
