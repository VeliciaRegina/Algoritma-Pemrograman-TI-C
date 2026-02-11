def my_function(nama):
  print("Hello", nama)

my_function("cia")


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# lambda
x = lambda a : a + 10
print(x(5))


# recursion
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))