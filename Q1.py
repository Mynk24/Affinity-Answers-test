import re

# Define the list of racial slurs to look for
racial_slurs = ["word1", "word2", "word3", ...]


def calculate_profanity(sentence):
    
    num_slurs = sum([1 for slur in racial_slurs if slur in sentence])
    
    # Calculate the degree of profanity as a percentage of the total number of words in the sentence
    degree_of_profanity = num_slurs / len(re.findall(r'\w+', sentence)) * 100
    
    return degree_of_profanity

with open("tweets.txt", "r") as f:

    for line in f:
        # Calculate the degree of profanity for the line
        profanity = calculate_profanity(line)
        
        # Print the line and its degree of profanity
        print(f"{line.strip()} - {profanity:.2f}% profanity")


 Assumptions:
# The racial slurs provided are in strings called 'racial_slurs'.
# The tweets are in a file tweets.txt, one tweet per line.
# The racial slurs should match exact words, so we're using the 'in' operator to check for matches in the sentence.
# We are assuming that the degree of profanity is the percentage of words in the sentence.
# We are using a regular expression to count the number of words. Here a "word" is any sequence of  characters separated by whitespace, which may not be true in all cases.
