#pazgen is a mega high security tool! ypur pazgen will take time write properly.
#1. run pazgen.py 2.enter < 1 >ENTER 3. enter <9333>ENTER EXIT 4. OPEN PASSKEY.TXT in fave txt edditor 5. ALLOW NUMBERED BULLITS(IMPORTANT FOR LATER) 6. break passkey into sets of 4-7 characters depending on desired pass strenth(make sure each line is numbered) 7. save file somewhere safe 8. rinse and repeat make at least 2 passkey files 
# HOW TO USE: ENSURE PASSKEY FILES ARE SAFE. USING NUMBERS YOU CAN NOW GENERATE RANDOM PASSWORDS WITH HIGH STRENTH
#EX PASSKEY1 1.AF_>     2.ydye7% 
#PASSKEY2 1.JD7. 2.YDH8r 3.ks9 
#MY KEY = 1,3 / PK1,PK2
#MIX UP "chars" ADD SOME TOO FOR EXTRA PW STRENTH
import random
chars = 'cbadefghilkjmnoqprstuvwxyz1423657890ABCDEFGHIJKLMNOPQRVUTSWXYZ1234567890}(".^:;}<=+@¿?,# !<=+÷]~`$ />%-_^&*.'
number = input('Number of passwords - ')
number = int(number)

length = input('password length? - ')
length = int(length)

answer = input

for P in range(number):
    password = ''
for C in range(length):
    password += random.choice(chars)
    print(password)


passwd = open("passkey.txt", "a")
passwd.write(password)
passwd.close()

file = open('passlist', 'w')
file.write(password)
file.close()
