
class timeStars:
    def __init__(self, start, stop, time):
        self.start = start
        self.stop =stop
        self.time = time

def bellman(n, m):
    graph = []
    INF = 1e9
    for i in range(m):
        start, stop, time = map(int, input().split())
        graph.append(timeStars(start, stop, time))
    dist = [INF for i in range(n)]
    dist[graph[0].start] = 0
    for _ in range(n -1):
        for j in range(m):
            if dist[graph[j].start] != INF and dist[graph[j].start] + graph[j].time < dist[graph[j].stop]:
                dist[graph[j].stop] = dist[graph[j].start] + graph[j].time
        print(dist,"aaaaaaaa")
    print(dist,"bbbbbb")
    for j in range(m):
        if dist[graph[j].start] != INF and dist[graph[j].start] + graph[j].time < dist[graph[j].stop]:
            return True
    return False


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n, m = map(int, input().split())
        if bellman(n, m):
            print("possible")
        else:
            print("not possible")