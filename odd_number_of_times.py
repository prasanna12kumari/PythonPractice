

# I didn't get how it works

class NumberOccuringOddNumberOfTimes:
    
    def finding_number(self,a):
        
        result = a[0]
        values = []
        for i in range(1,len(a)):
            result = result ^ a[i]
        return result

a = [45,54,54,65,45,45,65] 

odd_no_obj1 = NumberOccuringOddNumberOfTimes()
number1 = odd_no_obj1.finding_number(a)
print(number1)

# Another way, this I got it

class OddNumberTimes:
    
    def finding_number(self,a):
        
        numbers_odd_times = []
        
        for i in range(len(a)):
            count = 1
            for j in range(len(a)):
                if a[i] == a[j] and i != j:
                    count = count + 1
            if count % 2 == 1:
                numbers_odd_times.append(a[i])
                
        return list(set(numbers_odd_times))
                
b = [12,10,10,12,10,34,54,54] 

odd_no_obj2 = OddNumberTimes()
number2 = odd_no_obj2.finding_number(b)

print(number2)