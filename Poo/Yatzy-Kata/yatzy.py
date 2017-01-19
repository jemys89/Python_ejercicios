class Yatzy:

    def __init__(self, *dice):
        self.dice = dice

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50
    
    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO
        
    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE

    
    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR
    

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE
    

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX
    
    @staticmethod
    def pair(*dice):
        
        TWO = 2
        for number in range(6,0,-1):
            if dice.count(number) >= TWO:
                return number * TWO
        return 0
    
    @staticmethod
    def two_pairs(*dice):
        PAIR = 2
        pairs = 0
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= PAIR:
                pairs += 1  
                score = score + number *PAIR
        if pairs == PAIR:
            return score
        return 0    
    
    
    

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for number in range(6,1,-1):
            if dice.count(number) >= THREE:
                return number * THREE
        return 0
    
    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for number in range(6,1,-1):
            if dice.count(number) >= FOUR:
                return number * FOUR
        return 0

    @staticmethod
    def small_straight(*dice):
        score = 15
        for numero in range(1, 6):
            if dice.count(numero) != 1:
                return 0
        return score
    

    @staticmethod
    def large_straight(*dice):
        score = 20
        for numero in range(2, 7):
            if dice.count(numero) != 1:
                return 0
        return score
    

    @staticmethod
    def full_house(*dice):
        score = 0
        for number in range(1, 7):
            if dice.count(number) > 4 or dice.count(number) == 1:
                return 0
            elif dice.count(number) == 3:
                score += number * 3
            elif dice.count(number) == 2:
                score += number * 2
        return score
