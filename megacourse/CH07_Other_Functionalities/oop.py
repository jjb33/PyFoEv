'''
Each object belongs to a class, and inherets the properties of that class, but is independent of other objects of the same class (it's an instace of the class). Methods are functions contained within a class.
'''

class pet:
    number_of_legs = 0
    
spot = pet()

spot.number_of_legs = 4

print ("Spot has %s legs." % spot.number_of_legs)