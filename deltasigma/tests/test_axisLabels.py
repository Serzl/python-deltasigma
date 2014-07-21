import unittest
import numpy as np
import deltasigma as ds

class TestAxisLabels(unittest.TestCase):
    """Test function for axisLabels()"""
    def setUp(self):
        self.ran = np.arange(100)
    
    def test_axis_label_geneation_part1(self):
        ss = ds.axisLabels(self.ran, incr=10)
        r = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']
        self.assertTrue(r == ss)
        
    def test_axis_label_generation_part2(self):
        ss = ds.axisLabels(self.ran, incr=(15, 10))
        r = ['10', '25', '40', '55', '70', '85']
        self.assertTrue(r == ss)