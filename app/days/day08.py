"""Advent of Code 2025 - Day 08"""

from scipy.cluster.hierarchy import DisjointSet
from itertools import combinations
import math


def part1(puzzle_input: str):
    boxes = parse_input(puzzle_input)
    set_sizes = find_n_shortest_connections(1000, boxes)
    return top_three_value_counts(set_sizes)


def part2(puzzle_input: str):
    pass


def parse_input(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def find_n_shortest_connections(n, junctions):
    uf = DisjointSet(junctions)
    edges = compute_all_edges(junctions)

    count = 0
    for dist, j1, j2 in edges:
        if not uf.connected(j1, j2):
            uf.merge(j1, j2)
        count += 1
        if count >= n:
            break
    return [len(s) for s in uf.subsets()]


def calculate_distance_between_junctions(junction1: str, junction2: str) -> float:
    x1, y1, z1 = map(float, junction1.split(","))
    x2, y2, z2 = map(float, junction2.split(","))

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def top_three_value_counts(set_sizes: list[int]) -> int:
    sizes = sorted(set_sizes, reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def compute_all_edges(junctions):
    edges = []
    for j1, j2 in combinations(junctions, 2):
        x1, y1, z1 = map(float, j1.split(","))
        x2, y2, z2 = map(float, j2.split(","))
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        edges.append((dist, j1, j2))
    edges.sort(key=lambda x: x[0])
    return edges
