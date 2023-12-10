#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testRollsBetween0And10(self):
        ok = self.game.rolls(3)
        assert ok == 0
    def testRollsNegative(self):
        ok = self.game.rolls(-5)
        assert ok == -1
    def testRollsTooMany(self):
        ok = self.game.rolls(12)
        assert ok == -1

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16

