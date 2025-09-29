word=input("Введите слово: ")
if len(word)%2==1:
    lenth1=len(word)//2
    print(word[lenth1])
else:
    lenth1=len(word)//2
    lenth2=len(word)//2-1
    word1=str(word[lenth2])
    word2=str(word[lenth1])
    print(word1+word2)