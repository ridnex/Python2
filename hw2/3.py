year = int(input())
dogYear = 0
for i in range(year):
    if i<2:
        dogYear+=10.5
    else:
        dogYear+=4
print('Input a dog\'s age in human years:', year)
print('The dog\'s age in dog\'s years is:', dogYear)