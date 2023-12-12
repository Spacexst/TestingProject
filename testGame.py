#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    # done
    def testRollsBetween0And10(self):
        ok = self.game.roll(3)
        assert ok == 0
       
    # done
    def testRollsNegative(self):
        ok = self.game.roll(-5)
        assert ok == -1
        
    # done
    def testRollsTooMany(self):
        ok = self.game.roll(12)
        assert ok == -1

    # done
    def testGutterFrame(self):
        zeroScore1 = self.game.roll(0)
        zeroScore2 = self.game.roll(0)
        assert zeroScore1 == 0
        assert zeroScore1 == zeroScore2
        
    # done
    def testGutterGame(self):
        for i in range(10):
            for j in range(2):
                self.game.roll(0)
        score = self.game.score()
        assert score == 0

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
          
    def test_one_strike(self):
        ok = self.game.roll(0) 
        for i in range(1, 20):
           self.game.roll(17) 
           assert ok == 0

    def test_perfect_game(self):
        ok = self.game.roll(0) 
        # Arrange
        for _ in range(12):
            self.game.roll(300)
            assert ok == 0
    
    def testOneSpare(self):
        ok = self.game.roll(0)
        for _ in range(5, 21):
            self.game.roll(150)
            assert ok == 0

    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
                
    
   
    
    
           
   
   
   
       

   
            
    
    
        
              
        
        
   

        
        
       
   
          
    
       

