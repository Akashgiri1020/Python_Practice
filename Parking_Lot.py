""" A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). 
The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) 
in the parking lot that has the most of the parking spaces full(1). """

r = int(input())
c = int(input())

summ = 0
maxx = 0
for i in range(r):
    for j in range(c):
        summ += int(input())
    if(summ>maxx):
        maxx = summ
        ide = i
print(ide)
