import unittest
import math
from app.days.day08 import (
    parse_input,
    calculate_distance_between_junctions,
    top_three_value_counts,
    compute_all_edges,
    find_n_shortest_connections,
)


class TestDay08(unittest.TestCase):

    def test_parse_input(self):
        input_str = "1,2,3\n4,5,6\n7,8,9"
        expected = ["1,2,3", "4,5,6", "7,8,9"]
        self.assertEqual(parse_input(input_str), expected)

    def test_calculate_distance_between_junctions(self):
        j1 = "0,0,0"
        j2 = "1,2,2"
        expected = 3.0  # sqrt(1+4+4)
        self.assertAlmostEqual(calculate_distance_between_junctions(j1, j2), expected)

    def test_top_three_value_counts(self):
        sizes = [5, 2, 8, 3]
        expected = 8 * 5 * 3
        self.assertEqual(top_three_value_counts(sizes), expected)

    def test_compute_all_edges(self):
        junctions = ["0,0,0", "1,0,0", "0,1,0"]
        edges = compute_all_edges(junctions)
        distances = [round(e[0], 5) for e in edges]
        expected_distances = [1.0, 1.0, math.sqrt(2)]
        for d in expected_distances:
            self.assertIn(round(d, 5), distances)

    def test_find_n_shortest_connections(self):
        junctions = ["0,0,0", "1,0,0", "0,1,0"]
        # Using n=2 should connect all points
        sizes = find_n_shortest_connections(2, junctions)
        # Only one connected component of size 3
        self.assertIn(3, sizes)
        self.assertEqual(sum(sizes), 3)
