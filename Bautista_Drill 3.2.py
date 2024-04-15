row_count = 3
col_count = 5

for i in range(row_count):
  for j in range(col_count):
    if j % 2 == 0:
      print("*", end=" ")  
    else:
      print("-", end=" ") 
  print()  
