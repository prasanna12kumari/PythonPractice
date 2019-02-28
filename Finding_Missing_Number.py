
class MissingNumber:
    
    def findmissing(self,a,b):
        
        result = sum(a) - sum(b)
        
        return result
        
class MissingNumberWithoutArithmetic:
    
    def findmissing(self,a,b):
        
        result = a[0]
       
        for i in range(1,len(a)):
            
            result = result ^ a[i]
           
        for i in range(len(b)):
            
            result = result ^ b[i]
              
        return result
		
a = [10,20,30,47,15,10]
b = [10,20,47,15,10]
c = [10,20,47,30,10]

miss_obj1 = MissingNumber()
miss_obj2 = MissingNumberWithoutArithmetic()
missing_number1 = miss_obj1.findmissing(a,b)
missing_number2 = miss_obj2.findmissing(a,c)

print(missing_number1)
print(missing_number2)