from random import randrange


def linkLetters(n1, n2, n3, n4, n5):
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1
    n1.prev = None


def linkWords(n1, n2, n3, n4, n5, n6):
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = None
    
    n6.prev = n5
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1
    n1.prev = None
    
    
def getWord():
    file = open("wordlist.txt", "r")
    wordNum = randrange(1, 501)
    word = ""
    
    c = 1
    for row in file:
        if (wordNum == c):
            word = row
            break
        c += 1

    file.close()
    return word.upper()

def ifValidWord(word, wordList, minIndex, maxIndex):
    word = word.upper()
    midIndex = (minIndex + maxIndex) // 2

    # if word is less than 5 letters
    if "0" in word:
        return False

    # if word is not in the list
    elif len(wordList[minIndex:maxIndex]) == 0 or (len(wordList[minIndex:maxIndex]) == 1 and wordList[minIndex:maxIndex] != [word]):
        return False

    # if word is in the middle
    elif wordList[midIndex] == word:
        return True

    # if the word is "less" than mid
    elif word < wordList[midIndex].upper():
        return ifValidWord(word, wordList, minIndex, midIndex)

    # if the word is "greater" than mid
    elif word > wordList[midIndex].upper():
        return ifValidWord(word, wordList, midIndex, maxIndex)

    # if word doesn't exist
    else:
        return False









    
    

