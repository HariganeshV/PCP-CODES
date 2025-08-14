def fibonacci(n):
  if n<=0:
    return "invalid input"
  elif n ==1:
    return[0]
  elif n == 2:
    return[0,1]
    
  sequence = [0,1]
  for i in range(2,n):
    nextterm = sequence[i-1] + sequence[i-2]
    sequence.append(nextterm)
  return sequence
  
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(10))
  