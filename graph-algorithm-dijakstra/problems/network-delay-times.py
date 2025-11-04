"""Problem Link: https://leetcode.com/problems/network-delay-time"""
import heapq
from collections import defaultdict


class Solution:
    @staticmethod
    def networkDelayTimeBruteForce(times: list[list[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        max_delay = max(dist[1:])
        return -1 if max_delay == float('inf') else max_delay

    @staticmethod
    def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        # 1. Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        # 2. Priority queue: (total_time_from_k, node)
        min_heap = [(0, k)]
        # 3. Dictionary to record the shortest known arrival to each node
        min_times = {}

        while min_heap:
            time_k_to_i, node = heapq.heappop(min_heap)
            if node in min_times:
                continue  # already finalized
            min_times[node] = time_k_to_i
            for neighbor, extra_time in graph[node]:
                if neighbor not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i + extra_time, neighbor))
        # 4. If all nodes are reached, return the max time—else -1
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1

sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))