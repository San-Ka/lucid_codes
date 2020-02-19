words = input( 'Enter a Number or Word: ')
if words[0] in ['a', 'e','i','o','u','A','E','I','O','U']:
    print("Vowel")
elif words[0] in ['b', 'c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
    print("consonant")
elif words[0] in [0,1,2,3,4,5,6,7,8,9]:
    print("Number")
else:
    print("Unkown")
