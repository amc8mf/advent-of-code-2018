import csv

def isValid(phrase):
    for x in range(0, len(phrase) -1):
        if (phrase.count(phrase[x])) > 1:
            return 0
    return 1

def isAnagram(phrase):
    tempPhrase = list(phrase)
    for x in range(0, len(tempPhrase)):
        tempPhrase[x] = sorted(list(tempPhrase[x]))
    for i in range(0, len(tempPhrase) - 1):
        if tempPhrase.count(tempPhrase[i]) > 1:
            return True

    return False

def countValidPhrases(file):
    count = 0
    with open(file) as phraseList:
        for phrase in csv.reader(phraseList, dialect="excel-tab"):
            phrase = phrase[0].split(' ')
            if isAnagram(phrase) == False:
                count += isValid(phrase)
    return count


print(countValidPhrases('A4_input.txt'))