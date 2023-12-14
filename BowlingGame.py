class BowlingGame:
    def __init__(self):
        self.rolls=[]


    def roll(self,pins):
        '''Save points for a roll.'''
        if (pins < 0 or pins > 10):
            return -1
        else:
            self.rolls.append(pins)
            return 0

    def score(self):
        '''Calculate score for a game.'''
        result = 0
        rollIndex=0
        
        for frameIndex in range(10):
            # if frameIndex in range(10):
            if frameIndex in range(10):
                if self.isStrike(rollIndex):
                    result += self.strikeScore(rollIndex)
                    rollIndex += 1
                elif self.isSpare(rollIndex):
                    result += self.spareScore(rollIndex)
                    rollIndex += 2
                else:
                    result += self.frameScore(rollIndex)
                    rollIndex += 2
                
        return result

    def isStrike(self, rollIndex):
        '''Returns true if a roll is a strike.'''
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        '''Returns true if the score for a frame is a spare.'''
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self,rollIndex):
        '''Calculates score for a strike by inlcuding points from the next frame.'''
        score = 10 + self.rolls[rollIndex+1]
        if rollIndex < 9:
            score += self.rolls[rollIndex+2]
        else:
            score += self.rolls[10]
        return score

    def spareScore(self,rollIndex):
        '''Calculates score for a spare by including points from the next roll.'''
        return  10 + self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        '''Calculates the points for a frame.'''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
              