# test_novapulse.py
"""
Tests for NovaPulse module.
"""

import unittest
from novapulse import NovaPulse

class TestNovaPulse(unittest.TestCase):
    """Test cases for NovaPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaPulse()
        self.assertIsInstance(instance, NovaPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
