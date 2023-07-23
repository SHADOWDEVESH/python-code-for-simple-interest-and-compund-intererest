p=int(input("enter principle amount "))
r=int(input('enter rate of interest '))
t=int(input('enter number of years '))
si=(p*r*t)/100
ci= p*(1+r/100)**t -p
print('simple intrest is ',si)
print('compound intrest is ',ci)
