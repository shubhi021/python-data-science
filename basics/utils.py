def char_counter(sentence):
    data={} #blank dictionary
    for char in set(sentence): #set dunction gives unique characters
          print(char,sentence.count(char))
          data[char] = sentence.count(char)
    return data      

def word_counter(sentence):
    data={}
    words=sentence.split()
    for word in set(words):
        data[word]=word.count(word)
    return data

def remove_punc(sentence):
    '''remove punctuations(TBC)'''
    pass