# aritmatic operator
"""
+	         Addition	            x + y	
-	         Subtraction       	x - y	
*	         Multiplication	      x * y	
/	         Division	            x / y	
%	         Modulus	            x % y	
**	         Exponentiation	      x ** y	
//	         Floor division	      x // y
"""      

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# comparison operator
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

# identity operator
"""
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# membership operator
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# bitwise operator
print(6 & 3)

# presedence operator
print((6 + 3) - (6 + 3))

