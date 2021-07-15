# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 14:21:27 2021

@author: z.czaplinski

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


"""

#import libraries:
import random
import string 

#parameters of simulation:
final = "METHINKS IT IS LIKE A WEASEL"
letters= string.ascii_uppercase + " "
evolution_rate = 0.05
num_of_offspring = 100

#variables that change during the simulation
generation=0 
parent=""
score = None


#generate random string for start
def generate_parent():
    global parent
    for i in final:
        parent+=random.choice(letters)
    return  parent

#generate mutation in strings with chance = evolution_rate
def generate_mutation(parent): 
    mutated=""
    for i in parent:
        if random.random() <= evolution_rate:
            mutated += random.choice(letters)
        else:
            mutated += i
    return mutated

#generate mutated offsprings of parent string 
def generate_offsprings (parent):
    offsprings =[]
    for i in range(num_of_offspring):
       offsprings.append(generate_mutation(parent))
    return offsprings

#selecting one of  the most similar to final string offspring - and it start to be new parent 
def selection (offsprings):
    global parent, score
    scores={}
    for o in offsprings:
        scores [o]= sum(a==b for a,b in zip(final,o))
    max_similarity= max(scores, key=lambda key: scores[key])
    parent = max_similarity
    score = scores[max_similarity]

# implemaentation of Weasel program
def main():
    global generation, parent, score
    generate_parent()
    score_generation_0 = sum(a==b for a,b in zip(final,parent))
    print ("Generation: {} String: {} Score: {} Similarity: {}%".format(generation, parent, 
                                                         score_generation_0, 
                                                         int(score_generation_0/28*100)))
    while parent != final:
        generation += 1
        generate_mutation(parent)
        selection (generate_offsprings(parent))
        print ("Generation: {} String: {} Score: {} Similarity: {}%".format(generation, 
                                                             parent, score,
                                                             int(score/28*100)))
        
main()