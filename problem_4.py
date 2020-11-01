#Justine Rosado
#10/31/20
#this program is supports to iterates the integers from 1 to 50 

def divisible_by_3(n):
        if n%3 == 0  or n%6 == 0:
            print("divisible by 3")
            if n%5 == 0 or n%20 == 0:
                print("divisible by 5")
            elif n%3 == 0 and n%5 == 0:
                 print("divisible by both")
        else:
            print("non are divisible")


divisible_by_3(3)
divisible_by_3(2)
divisible_by_3(5)


