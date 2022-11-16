#!/usr/bin/env python
from collections import defaultdict, deque
from typing import List, Dict, Set

from challenges.utils import expect


class Solution:
    def findMinPathLength(
        self,
        stop_to_routes: Dict,
        route_to_stops: Dict,
        start_route: int,
        target_routes: Set[int],
    ) -> int | float:
        if start_route in target_routes:
            return 1

        queue = deque([(start_route, 1)])
        seen_routes = set()
        while queue:
            current_route, depth = queue.popleft()
            if current_route in target_routes:
                return depth

            seen_routes.add(current_route)

            routes_to_add = set()
            for stop in route_to_stops[current_route]:
                for route in stop_to_routes[stop]:
                    if route not in seen_routes:
                        routes_to_add.add(route)

            for route_to_add in routes_to_add:
                queue.append((route_to_add, depth + 1))

        return float("+inf")

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        route_to_stops = dict()
        target_routes = set()
        source_routes = set()

        for route, stops in enumerate(routes):
            route_to_stops[route] = stops
            for stop in stops:
                stop_to_routes[stop].add(route)
                if stop == target:
                    target_routes.add(route)
                if stop == source:
                    source_routes.add(route)

        min_buses = float("+inf")
        for source_route in source_routes:
            min_buses = min(
                min_buses,
                self.findMinPathLength(stop_to_routes, route_to_stops, source_route, target_routes),
            )

        return min_buses if min_buses < float("+inf") else -1


if __name__ == "__main__":
    obj = Solution()
    expect(obj.numBusesToDestination([[1, 2, 7], [3, 6, 7], [8, 9, 6]], 1, 6), 2)
    expect(obj.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12), -1)
    expect(obj.numBusesToDestination([[1, 7], [3, 5]], 5, 5), 0)
    expect(obj.numBusesToDestination([[2], [2, 8]], 8, 2), 1)
