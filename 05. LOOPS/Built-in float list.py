#  Create a list that contains elements of integer type, then 
# use the loop to change the type of these elements to a floating 
# type. 
# (Hint: use the built-in float () function).

l1=[1, 2, 128, 1924]
print("Before:",l1)
for i in range(0,4):
  l1[i] = float(l1[i])
print("After:",l1)
