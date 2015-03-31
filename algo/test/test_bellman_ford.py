# -*- coding: utf-8 -*-

import unittest

from src.bellman_ford import shortest_path
from src.graph import Graph


class BellmanFordTest(unittest.TestCase):

    def test_bellman_ford_for_positive_edge_lengths(self):
        """ Given the following graph:
           /--2-->(v)---2--->(w)--2--\v
        (s)        1\v               (t)
          \----4--->(x)------4------/^
        """
        g = Graph.build(edges=[
                ('s', 'v', 2), ('s', 'x', 4), ('v', 'w', 2),
                ('w', 't', 2), ('v', 'x', 1), ('x', 't', 4)
            ],
            directed=True)
        paths = shortest_path(g, 's')
        expected_paths = {'x': 3, 's': 0, 't': 6, 'w': 4, 'v': 2}
        self.assertEqual(paths, expected_paths,
            'should return the correct paths')

    def test_bellman_ford_with_non_negative_cycle(self):
        """ Given the following graph:
           /--2-->(v)---2--->(w)--2--\v
        (s)        \^      /        (t)
          \         \1  v/-5        /^
           \---4---->(x)------4---/
        """
        g = Graph.build(edges=[
                ('s', 'v', 2), ('v', 'w', 2), ('w', 't', 2),
                ('s', 'x', 4), ('x', 'v', 1), ('w', 'x', -5),
                ('x', 't', 4)
            ],
            directed=True)
        noNegativeCycles = shortest_path(g, 's')
        self.assertFalse(noNegativeCycles, 'should detect no negative cycles')
