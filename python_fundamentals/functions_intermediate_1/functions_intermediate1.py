import random, math
def randInt(lower=0, higher=100):
    if lower > higher:
        lower, higher = higher, lower
    return math.floor(random.random()*(higher-lower))+lower
    
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(higher=50)) 	    # should print a random integer between 0 to 50
# print(randInt(lower=50)) 	    # should print a random integer between 50 to 100
# print(randInt(lower=50, higher=500))    # should print a random integer between 50 and 500
# print(randInt(lower=100, higher=50)) # edge case1: min > max
# print(randInt(higher=-50)) 	#edge case2: max < 0