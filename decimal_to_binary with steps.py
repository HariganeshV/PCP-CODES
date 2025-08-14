def decimal_to_binary(decimal_num):
   if decimal_num == 0:
     return "0"
     
   binary_digits = []
   num = decimal_num
   
   while num >= 1:
     remainder = num % 2
     binary_digits.append(str(remainder))
     num = num // 2
     print(num,"\n")
     
   binary_digits.reverse()
   return "".join(binary_digits)
    
#Example usage:
print(decimal_to_binary(10)) 

