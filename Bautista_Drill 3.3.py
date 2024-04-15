def isprime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

n = int(input("Enter the number of prime numbers to print: "))
count = 0
num = 2 
while count < n:
  if isprime(num):
    print(num)
    count += 1
  num += 1
