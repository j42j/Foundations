'''Pig Latin Translator
rules: if word begins with vowel, add "way" to the end of the word.
       if word begins with consenant, removes all consenants until
       reach first vowel, then add those consenants to the end of word,
       then add "ay."'''

while True:
    s = input('Enter word: ')
    if s.isalpha():
        break
    else:
        print("Please try again.")

vowels = ['a', 'i', 'e', 'o' ,'u', 'y']

sl = s.lower()
vowels_i = [sl.find(x) for x in vowels]
try:
    i = min([x for x in vowels_i if x >= 0])
except ValueError:
    print("This is not translatable.")
else:
    if i == 0:
        t = sl + 'way'
    else:
        t = sl[i:] + sl[:i] + 'ay'
print("Translation: {}".format(t))
