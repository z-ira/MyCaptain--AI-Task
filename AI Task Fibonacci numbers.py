# Write a Python Program for Fibonacci numbers.

T = int(input("How many terms you want to print? : "))
n1, n2 = 0, 1
if T <= 0:
   print("Please enter a positive integer")

elif T == 1:
   print("Fibonacci sequence upto",T,":")
   print(n1)

else:  
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, T):
        n3 = n1 + n2
        #update values
        n1 = n2
        n2 = n3
        print(n3, end=" ")

