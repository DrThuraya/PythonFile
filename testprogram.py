import unittest
import main
import numpy as np
from numpy import testing

"""this file includes unit tests for each functions defined in the main file (main.py) """
"""tests was done according to the input file (testfile.txt) """

class MyTestCase(unittest.TestCase):

    def test_extractParameters(self):
        resulted_list=[]
        expected_list=[3, 4, 3]
        x="testfile.txt"
        resulted_list= main.extract_parameters(x)
        self.assertEqual(resulted_list, expected_list)

    def test_initiate_matrix(self):
        x="testfile.txt"
        expected_GRID= [ [0, 0, 0 ], [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
        returned_GRID=main.initiate_matrix(x)
        self.assertTrue((expected_GRID == returned_GRID).all())
        list=main.extract_parameters(x)
        print("empty Matrix")
        main.display_matrix(returned_GRID, list[1], list[0])

    def test_tomatrix(self):
        x="testfile.txt"
        GRID=main.initiate_matrix(x)
        expected_GRID = [[1, 1, 1], [1, 1, 0], [0, 0, 0], [0, 1, 0]]
        returned_GRID = main.tomatrix(GRID, x)
        self.assertTrue((expected_GRID == returned_GRID).all())
        list = main.extract_parameters(x)

        print("updated  Matrix, according to alive cells indicated in the txt file")
        main.display_matrix(returned_GRID, list[1], list[0])

    def test_cpmputeNeighbors(self):
        x = "testfile.txt"
        GRID = main.initiate_matrix(x)
        upGRID = main.tomatrix(GRID, x)
        """test neighbors of cell (0, 0)"""
        expected_n=3
        resulted_n=main.cell_neighbors(upGRID, 0, 0)
        self.assertEqual(expected_n, resulted_n)
        """test neighbors of cell(1, 1)"""
        expected_n = 4
        resulted_n = main.cell_neighbors(upGRID, 1, 1)
        self.assertEqual(expected_n, resulted_n)

    def test_compute_next_gen(self):
        x = "testfile.txt"
        expected_GRID = [[1, 0, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0]]
        list=main.extract_parameters(x)
        GRID = main.initiate_matrix(x)
        upGRID = main.tomatrix(GRID, x)
        resulted_GRID = main.compute_next_gen(upGRID, list[1], list[0])
        self.assertTrue ((expected_GRID == resulted_GRID).all())

    def test_compute_gen_after_n_iterations(self):
        x = "testfile.txt"
        expected_GRID = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 0, 0]]
        list = main.extract_parameters(x)
        GRID = main.initiate_matrix(x)
        upGRID = main.tomatrix(GRID, x)
        mg=upGRID
        for i in range(list[2]):
            print("transformation number", i)
            newM=main.compute_next_gen(mg, list[1], list[0])
            main.display_matrix(newM, list[1], list[0])
            mg=newM
        self.assertTrue((expected_GRID == mg).all())


if __name__ == '__main__':
    unittest.main()
