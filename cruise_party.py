""" A party has been organised on cruise. The party is organised for a limited time(T). 
The number of guests entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array. 
The task is to find the maximum number of guests present on the cruise at any given instance within T hours. """

N_guest = int(input("Enter Number of guest"))

maxx = 0
summ = 0

guest_come = []

guest_exit = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

for i in range(N_guest):
    guest_come.append(int(input()))

for i in range(N_guest):
    guest_exit.append(int(input()))

for i in range(N_guest):
    summ  = summ+ (guest_come[i]-guest_exit[i])
    if(summ>maxx):
        maxx = summ
        
print(maxx)
