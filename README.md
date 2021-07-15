# Weasel_program
R. Dawkins' "Weasel program" implementation in Python 

This is implementation of R. Dawkins "Weasel program". Simulation show in very
simple way how evolution works: random variation combined with non-random 
cumulative selection. 


Algorithm of it run as follows (from wikipedia.com):
    
    1. Start with a random string of 28 characters.
    
    2.Make 100 copies of the string (reproduce).
    
    3.For each character in each of the 100 copies, with a probability of 5%, 
      replace (mutate) the character with a new random character.
      
    4.Compare each new string with the target string "METHINKS IT IS LIKE A WEASEL",
      and give each a score (the number of letters in the string that are correct 
      and in the correct position).
      
    5. If any of the new strings has a perfect score (28), halt. Otherwise, 
       take the highest scoring string, and go to step 2.
