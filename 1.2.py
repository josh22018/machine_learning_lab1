#counting vowels and consonants in a string.
instr="hello everyone!"
def count(instr):
    instr=instr.lower()
    vowel=0
    consonants=0
    for i in range(len(instr)):
        if instr[i].isalpha():
            if instr[i] in ['a','i','e','o','u']:
                vowel+=1
            else:
                consonants+=1
    return (vowel,consonants)
value=count(instr)
print("The no of vowels are : ",value[0])
print("The no of consonants are : ",value[1])