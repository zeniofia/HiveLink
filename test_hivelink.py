# test_hivelink.py
"""
Tests for HiveLink module.
"""

import unittest
from hivelink import HiveLink

class TestHiveLink(unittest.TestCase):
    """Test cases for HiveLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HiveLink()
        self.assertIsInstance(instance, HiveLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HiveLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
