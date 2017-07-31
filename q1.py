# Ziru Fan
# ziru.z.fan@gmail.com
# The code is running on python2, if using python3, "raw_input" should be "input",
# "IOError" should be "FileNotFoundError"

import string
from collections import Counter
import operator
import sys

# Get full text from either STDIN or a file
option = raw_input('Please select input method: enter "1" for STDIN, enter "2" for a file on system: ')
if option == '1':
    full_text = raw_input('Please type your text: ')
elif option == '2':
    file_name = raw_input('Type in file path: ')
    try:
        with open(file_name,'r') as my_file:
            full_text = ''.join([l.strip() for l in my_file if l.strip() is not ''])
    except IOError:
        print 'File not found'
        sys.exit()
else:
    print '"1" and "2" are the only options you have! Try again.'
    sys.exit()
# Clean full_text by replacing "?" and "!" with "."
full_text = full_text.replace("?",".")
full_text = full_text.replace("!",".")

# Get all words
def getAllwords(text):
    words = [w.translate(None, string.punctuation).lower() for w in text.split(' ') if w is not '']
    return words

# Get all sentences
def getAllsentences(text):
    sentences = [s for s in text.split('.') if s is not '']
    return sentences

# 1. total word count
# Here the assumption is that numbers count as words
def totalWordcount(text):
    word_count = len(getAllwords(text))
    return word_count

# 2. count of unique words
def countUniqueword(text):
    words_unique = set(getAllwords(text))
    return len(words_unique)

# 3. sentence count
# Here period is the only indicators of a complete sententce
def countSentence(text):
    sentences_count = len(getAllsentences(text))
    return sentences_count

# 4. average sentence length
def avgSentencelen(text):
    s_length = []
    sentences = getAllsentences(text)
    for s in sentences:
        s_length.append(len([w for w in s.split(' ') if w is not '']))
    return sum(s_length)/len(s_length)

# 5. Phrases finder
def phraseFinder(text):
    phrases = []
    sentences = getAllsentences(text)
    # Go through each sentence
    for s in sentences:
        # Get all possible word counts for phrases starting from 3
        word_count = range(3,len(s.split(' '))+1)
        # Get all phrases with the same length each round and store them in "phrases"
        for w in word_count:
            for loc in range(0,len(s)):
                sentence = [i for i in s.lower().split(' ') if i is not '']
                if (loc+w)<=len(sentence):
                    phrase = ' '.join(sentence[loc:loc+w])
                    phrases.append(phrase)
    my_dict = Counter(phrases)
    result = [key for key in my_dict if my_dict[key] > 3]
    return result

# 6. list of word:frequency pair, desc
def wordFrequency(text):
    words = getAllwords(text)
    d = Counter(words)
    sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    return sorted_d

# required output
print '- Total word count: ',totalWordcount(full_text)
print '- Unique words: ',countUniqueword(full_text)
print '- Sentences: ',countSentence(full_text)
print '- Average sentence length: ',avgSentencelen(full_text)
print '- Often used phrases (a phrase of 3 or more words used over 3 times): '
if len(phraseFinder(full_text))==0:
    print "None!"
for p in phraseFinder(full_text):
    print '"',p,'"'
print '- List of words used -- descending frequency: '
for w in wordFrequency(full_text):
    print w

