print('Welcome to the Love Calculator!')
name1 = input('What is your name? ')
name2 = input('What is the other name?')

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t = lower_name1.count('t') + lower_name2.count('t')
r = lower_name1.count('r') + lower_name2.count('r')
u = lower_name1.count('u') + lower_name2.count('u')
e = lower_name1.count('e') + lower_name2.count('e')
l = lower_name1.count('l') + lower_name2.count('l')
o = lower_name1.count('o') + lower_name2.count('o')
v = lower_name1.count('v') + lower_name2.count('v')
e = lower_name1.count('e') + lower_name2.count('e')

true = t + r + u + e
love = l + o + v + e
#print(true)
#print(love)
score = str(true) + str(love)
#print(score)

#score = int(t + r + u + e + l + o + v)
#avevo capito male e pensavo che lo score fosse la somma dei count, non str + str.

if int(score) <= 10 or int(score) >= 90:
    print(f'Your score is {score}, you go together like coke and menthos')
elif int(score) >=40 and score <= 50:
    print (f'Your score is {score}, you are alright together')
else:
    print (f'Your score is {score}')






