from typing import List, Any

class factorial_cal:
    def factorial(self, num):
            fact_result = [ ]
            print("fatorial passed number"+str(num))
            while (1):
                if  num == 1:
                    break
                for i in range(2,num+1):
                    res = num % i
                    #print( "values are num {0}   i value {1}".format(num , i))
                    if res == 0:
                        fact_result.append(i)
                        num = int(num / i)
                        break
            return fact_result
    def merge_lcm(self,fact1,fact2):
        for i in fact1:
            try:
                fact2.remove(i)
            except ValueError:
                pass
        return fact1+fact2
    def lcm( self, num1, num2):
        x = factorial_cal()
        fact1 = x.factorial(num1)
        print(" factorial of"+str(num1))
        print(fact1)
        fact2 = x.factorial(num2)
        print(" fact orial of" + str(num2))
        print(fact2)
        final_lcm=x.merge_lcm(fact1,fact2)
        print("final lcm of &num1 and &num2")
        print(fact2+fact1)
