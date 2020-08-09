import sys
import codecs,string
def detect_language(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return 'hindi'

with codecs.open(sys.argv[1], encoding='utf-8') as f:
    input = f.readlines()
    for i in input:
        isEng = detect_language(i)
        if isEng == "hindi":
            #Hindi Character
            #add this to another file
            with open("hindi.txt","a") as f:
                f.write(i+'\n')
