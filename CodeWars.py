"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    return int("".join([str(int(x)**2) for x in str(num)]))

################################
###############################
###############################

"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

def likes(names):
    if len(names) <= 0:
        return("no one likes this")
    elif len(names) == 1:
        return(f"{names[0]} likes this")
    elif len(names) == 2:
        return(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3 :
        return(f"{names[0]}, {names[1]} and {names[2]} like this")
    else : 
        return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")


################################
##################################
#################################



'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

def valid_parentheses(string):
    parentheses = ["(", ")"]
    s = [x for x in string if x in parentheses]
    if len(s) == 0 : return True
    else :
        count = 0
        i = 0
        while count >= 0:
            if s[i] == "(":
                count += 1  # each time open parenthese : count += 1
            else:
                count -= 1  # each time close parenthese : count += 1
            i += 1
            if i > len(s)-1 : break
        if count < 0 :  
                    return False
        elif count == 0 :  
                            return(True)
        else : 
                            return(False)


############################################
############################################
############################################

'''
# Get the Middle Character

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.

'''


def get_middle(s):
    s_list = list(s)
    Index = int(len(s_list)/2)
    if len(s_list)%2 == 0:
        return("".join([s_list[Index-1], s_list[Index]]))
    else:
        return(s_list[Index])




#################################
################################
################################


"""

    Who is the killer?
Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and also a list of the names of the dead people:

['Lucas', 'Bill']
return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'
    
    """

def killer(suspect_info, dead):
    for i in range(len(suspect_info)) :
        if set(dead).issubset(set(list(suspect_info.values())[i])) :
            suspect = list(suspect_info.keys())[i]
    return(suspect)


#################################
################################
################################
