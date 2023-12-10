#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testRollsBetween0And10(self):
        ok = self.game.roll(3)
        assert ok == 0
    def testRollsNegative(self):
        ok = self.game.roll(-5)
        assert ok == -1
    def testRollsTooMany(self):
        ok = self.game.roll(12)
        assert ok == -1

    
    def testGutterGame(self):
        ok = self.game.roll(0)
        for i in range(0,0):
            self.game.roll(0)
            assert ok == 0
            
        
    
    
    def test_all_ones(self):
        ok =  self.game.roll(0)
        for i in range(1, 20):
         self.game.roll(20)  
         assert ok == 0
         
         
    def test_simple_spare(self):
        ok = self.game.roll(0) 
        for i in range(1, 20):
          self.game.roll(13) 
          assert ok == 0
        
        
       
   
          
    """def testOneSpare(self):
       
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        
    """
       

