# WRITE A PROGRAM THAT WILL CALCULATE THE SUM, DIFFERENCE, PRODUCT, EXPONENTIATION ETC. OF TWO NUMBERS A AND B THAT THE PROGRAM READS FROM THE CONSOLE (DATA ENTERED BY THE USER) AND WILL OUTPUT APPROPRIATE RESULT:
# "A + B = "  ...
# "A - B = "   ...
# "A * B = "   ...
# "A / B = "   ...
# "A**B = "   ...
# "A//B = "   ...
# "A%B = "  ...

A = int(input("GIVE ME NUMBER "))
B = int(input("GIVE ME ANOTHER NUMBER "))
print(f"\n")
print(f"{A} + {B} =", A + B) 
print(f"{A} - {B} =", A - B) 
print(f"{A} * {B} =", A * B) 
print(f"{A} / {B} =", A / B) 
print(f"{A} ** {B} =", A ** B) 
print(f"{A} // {B} =", A // B) 
print(f"{A} % {B} =", A % B)