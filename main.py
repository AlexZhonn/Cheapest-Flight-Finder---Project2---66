import csv
from collections import defaultdict
import heapq

import csv
from collections import defaultdict
import heapq

def getCsv():
    graph = defaultdict(dict)
    with open("Aviation.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            city1 = row["city1"].strip()
            city2 = row["city2"].strip()
            fare = float(row["fare"])

            if city2 not in graph[city1] or fare < graph[city1][city2]:
                graph[city1][city2] = fare
                graph[city2][city1] = fare
    return graph


def dijkstra(graph, start, end):
    pq = [(0, start, [start])]
    dist = {start: 0}
    visited = set()

    while pq:
        cost, city, path = heapq.heappop(pq)

        if city in visited:
            continue
        visited.add(city)

        if city == end:
            return cost, path

        for neighbor, fare in graph[city].items():
            new_cost = cost + fare
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return float("inf"), []


if __name__ == "__main__":
    graph = getCsv()
    # for city, edges in list(graph.items())[:5]:
        # print(city, edges)
    print(dijkstra(graph, "Allentown/Bethlehem/Easton, PA", "Miami, FL (Metropolitan Area)"))
