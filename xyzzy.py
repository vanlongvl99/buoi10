import queue

class doorway:
    def __init__(self, start, stop, energy):
        self.start = start
        self.stop = stop
        self.energy = energy
    def __lt__(self, other):
        return self.energy > other

def bellman(n, graph):
    INF = -1e9
    dist = [INF for i in range(n+1)]
    dist[1] = 100
    for i in range(n -1):
        for j in range(len(graph)):
            a = graph[j].start
            b = graph[j].stop
            c = graph[j].energy
            if dist[a] != INF and dist[a] > 0:
                if dist[a] + c > dist[b]:
                    dist[b] = dist[a] + c
    for j in range(len(graph) -1):
            a = graph[j].start
            b = graph[j].stop
            c = graph[j].energy
            if dist[a] != INF:
                if dist[a] + c > dist[b]:
                    return True
    if dist[n] > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        n =int(input())
        if n == -1:
            break
        graph = []
        for i in range(n):
            arr = list(map(int, input().split()))
            if len(arr) > 2:
                for j in range(2, len(arr)):    
                    graph.append(doorway(i+1, arr[j], arr[0]))
        if bellman(n, graph):
            print("winnable")
        else:
            print("hopeless")