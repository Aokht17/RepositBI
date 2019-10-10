i=int(input())
if i%3==0 and i%5!=0:
    print ('fizz')
elif i%5==0 and i%3!=0:
    print ('buzz')
elif i%15==0:
    print ('fizzbuzz')
else:
    print (i)