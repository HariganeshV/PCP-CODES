def decimal_to_binary(decimal_num):
   if decimal_num == 0:
     return "0"
     
   binary_digits = []
   num = decimal_num
   
   while num > 0:
     reminder = num % 2
     binary_digits.append(str(reminder))
     num = num // 2
     
    #The binary digits are stored in reverse order
   #binary_str = ''.join(reversed(binary_digits))
   return binary_digits
    
#Example usage:
print(decimal_to_binary(10)) #Output:"0101"
print(decimal_to_binary(0)) #Output:"0"
print(decimal_to_binary(4)) #Output:"001"

