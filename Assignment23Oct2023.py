#✅ Count vowels and consonants in a String
Name=input("Please enter your name \n")
vowel=0
consonent=0

for i in Name:
    if i == 'a'or i =='e'or i =='i'or i =='o'or i =='u' or i =='A'or i =='E'or i =='I' or i == 'O'or i == 'U':
        vowel=vowel+1
    else:
        consonent=consonent+1

print("The vowel in a character passed is ",vowel)
print("The Consonent in character passed is ",consonent)