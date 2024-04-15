table_size = 10

for i in range(1, table_size + 1):
  print(i, end=" ")  

print()  

for i in range(1, table_size + 1):
  print(i, end=" ")
  for j in range(1, table_size + 1):
    product = i * j
    print(product, end="  ") 
  print() 