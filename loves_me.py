
# todo Loves Me, Loves Me Not...
#  ? "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

#  ? Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

# * Examples
#  ? loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

#  ? loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

# ? loves_me(1) ➞ "LOVES ME"
# !Notes
# *  Remember to return a string.
#  * The first phrase is always "Loves me".





def loves_me(petals):
    phrases = []
    
    for i in range(1, petals + 1):
        if i % 2 == 1:
            phrases.append("Loves me")
        else:
            phrases.append("Loves me not")
    
    # Capitalize the last phrase
    phrases[-1] = phrases[-1].upper()
    
    # Join the phrases with a comma and space
    return ', '.join(phrases)

# Test cases
print(loves_me(3))  # ➞ "Loves me, Loves me not, LOVES ME"
print(loves_me(6))  # ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
print(loves_me(1))  # ➞ "LOVES ME"
