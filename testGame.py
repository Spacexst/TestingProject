#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    
    def testRollsBetween0And10(self):
        '''check that a roll that knocks down a number of pins between 0 and 10 is allowed.'''
        ok = self.game.roll(3)
        assert ok == 0

    def testRollsNegative(self):
        '''check that a negative number of pins cannot be knocked down'''
        ok = self.game.roll(-5)
        assert ok == -1

    def testRollsTooMany(self):
        '''check that more than 10 pins cannot be knocked down'''
        ok = self.game.roll(12)
        assert ok == -1
    
    def testGutterFrame(self)
        '''check that a frame with two gutter balls has a score of zero'''
        zeroScore1 = self.game.roll(0)
        zeroScore2 = self.game.roll(0)
        assert zeroScore1 == 0
        assert zeroScore1 == zeroScore2
    
    def testGutterGame(self):
        '''check that a game consisting only of gutter balls has a score of zero'''
        for i in range(10):
            for j in range(2):
                self.game.roll(0)
        score = self.game.score()
        assert score == 0
    
    def testAllOnes(self):
        '''check that a game of scores other than gutter balls, spares and strikes produces the correct score'''
        for i in range(20):
            self.game.roll(1)  
        assert self.game.score() == 20
    
    def testSpare(self):
        '''check that a frame with a score of 10 is recognized as a spare'''
        self.game.roll(7)
        self.game.roll(3)
        assert self.game.isSpare(0) == True
     
    def testStrike(self):
        '''check that the first ball of a frame with a score of 10 is recognized as a strike'''   
        self.game.roll(10)
        assert self.game.isStrike(0) == True

    
    def testPerfectGame(self):
        '''check that a game of all strikes produces the correct score'''
        for i in range(11):
            self.game.roll(10)
        assert self.game.score() == 300
    
    def testManySpares(self):
        '''check that a game of all spares produces the correct score'''
        for rolls in range(21):
            self.game.roll(5)
        assert self.game.score() == 150
                
    
   
    
    
           
   
   
   
       

   
            
    
    
        
              
        
        
   

        
        
       
   
          
    
       

