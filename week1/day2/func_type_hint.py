 # Write functions with parameters, return types, type hints

# qno1: Function with Parameters + Type Hints
def greet(name: str) -> None:
    print(f"Hello, {name}!")                # func return nothing
greet("Alice")


# qno2: Function with Return Type + Type Hints
def add(a: int, b: int) -> int:
    return a + b
result = add(5, 3)
print(f"Sum: {result}")


# qno3: Function with Multiple Parameters + Type Hints
def multiply(x: float, y: float) -> float:
    return x * y
product = multiply(2.5, 4.0)
print(f"Product: {product}") 


# qno4: Function with Optional Parameters + Type Hints
from typing import Optional
def power(base:int,exponent:Optional[int]=2) ->int:
        return base ** exponent
squared=power(3)
cubed=power(2,3)
print(f"squared:{squared},cubed:{cubed}")


# qno5: function with String Return Type + Type Hints
def make_message(name: str, age: int) -> str:
    return f"{name} is {age} years old."
message = make_message("Bob", 25)
print(message)

# qno6: Function with List Return Type + Type Hints
def get_even_numbers(n: int) -> list[int]:
    return [i for i in range(n) if i % 2 == 0]

evens = get_even_numbers(10)
print(f"Even numbers up to 10: {evens}")

def even(n:int) ->list[int]:
     return[i for i in range(n) if i%2==0]
print(even(15))
  
  



  



