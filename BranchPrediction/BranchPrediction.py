
from random import paretovariate
from random import random



def next_branch_outcome_loop():
    alpha = 2
    outcome = paretovariate(alpha)
    outcome = outcome > 2
    return outcome

def next_branch_outcome_random():
    outcome = random()
    outcome = outcome > 0.5
    return outcome

class Predictor:
    def __init__(self):
        self.state = 0
    def next_predict(self):

        pass
    
    def incorrect_predict(self):

        pass

    def correct_predict(self):

        pass

class OneBitPredictor(Predictor):

    def next_predict(self):

        prediction = False

        if self.state == 1:
           prediction = True

        return prediction

    def incorrect_predict(self):

        if self.state == 1:
            self.state = 0
        else:
            self.state = 1

    def correct_predict(self):
        pass


class TwoBitPredictor(Predictor):

    def next_predict(self):

        taken = 2
        s_taken = 3
        prediction = False

        if self.state == taken or self.state == s_taken:
           prediction = True

        return prediction

    def incorrect_predict(self):

        if self.state == 3:
            self.state = 2
        elif self.state == 2:
            self.state = 1
        elif self.state == 1:
            self.state = 0


    def correct_predict(self):

        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 3



def test1b_next_branch_outcome_random(num):
    
    oneBit = OneBitPredictor()
    total_correct = 0

    for i in range(num):

        before = oneBit.next_predict()
        actual = next_branch_outcome_random()

        if before == actual:
            oneBit.correct_predict()
            total_correct += 1
        else:
            oneBit.incorrect_predict()
      
    percent_correct = (total_correct / num) * 100
    return percent_correct



def test1b_next_branch_outcome_loop(num): 

    oneBit = OneBitPredictor()
    total_correct = 0

    for i in range(num):

        before = oneBit.next_predict()
        actual = next_branch_outcome_loop()

        if before == actual:
            oneBit.correct_predict()
            total_correct += 1
        else:
            oneBit.incorrect_predict()

    percent_correct = (total_correct / num) * 100
    return percent_correct



def test2b_next_branch_outcome_random(num):

    twoBit = TwoBitPredictor()
    total_correct = 0

    for i in range(num):
        before = twoBit.next_predict()
        actual = next_branch_outcome_random()

        if before == actual:
            total_correct += 1
         
        if actual == True:
            twoBit.correct_predict()
        else:
            twoBit.incorrect_predict()
            
    percent_correct = (total_correct / num) * 100
    return percent_correct



def test2b_next_branch_outcome_loop(num):

    twoBit = TwoBitPredictor()
    total_correct = 0

    for i in range(num):
        before = twoBit.next_predict()
        actual = next_branch_outcome_loop()

        if before == actual:
            total_correct += 1

        if actual == True:
            twoBit.correct_predict()
        else:
            twoBit.incorrect_predict()   
        
    percent_correct = (total_correct / num) * 100
    return percent_correct


        
percent_correct = test1b_next_branch_outcome_random(1000)
print("One Bit, Next Branch Outcome Random")
print("Percent Correct: %d" %percent_correct + "%")

percent_correct = test1b_next_branch_outcome_loop(1000)
print("One Bit, Next Branch Outcome Loop")
print("Percent Correct: %d" %percent_correct + "%")

percent_correct = test2b_next_branch_outcome_random(1000)
print("Two Bit, Next Branch Outcome Random")
print("Percent Correct: %d" %percent_correct + "%")

percent_correct = test2b_next_branch_outcome_loop(1000)
print("Two Bit, Next Branch Outcome Loop")
print("Percent Correct: %d" %percent_correct + "%")        














