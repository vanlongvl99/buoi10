

class move:
    def __init__(self, start, stop, busy):
        self.start = start
        self.stop = stop
        self.busy = busy
def bellman(n, m, busyness):
    graph = []
    for j in range(m):
        start, stop = map(int, input().split())
        k = (busyness[stop -1] - busyness[start -1])
        graph.append(move(start, stop, k*k*k))
    dist = [INF for i in range(n + 1)]
    dist[1] = 0
    for i in range(n):
        for j in range(m):
            if dist[graph[j].start] != INF and dist[graph[j].start] + graph[j].busy < dist[graph[j].stop]:
                dist[graph[j].stop] = dist[graph[j].start] + graph[j].busy
    return dist

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input()
        n = int(input())
        busyness = list(map(int, input().split()))
        m = int(input())
        INF = 1e9
        dist = bellman(n, m, busyness)
        q = int(input())
        print("Case " + str(i + 1) +":")
        for j in range(q):
            jun = int(input())
            if dist[jun] < 3 or dist[jun] == INF:
                print("?")
            else:
                print(dist[jun])