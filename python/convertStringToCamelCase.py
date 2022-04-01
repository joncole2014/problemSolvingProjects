# Complete the method/function so that it converts dash/underscore delimited 
# words into camel casing. The first word within the output should be 
# capitalized *only* if the original word was capitalized.
#
# ex: 'the-stealth-warrior' gets converted to 'theStealthWarrior'
#
# Link to problem: https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    
    out = ""   # empty string for output
    i = 0   # while loop counter
    
    while i < len(text):
        if text[i] == "-" or text[i] == "_":
            out += text[i+1].capitalize()   # capitalizes the next character and joins it to output string
            i +=2   # increment two to correct position
            continue
        out += text[i]   # joins correct characters to output string
        i += 1   # increment one to next letter
    return(out)
