#DATA TYPE CONVERSTIONS

# Integer conversions
int_val = 10
print(float(int_val))   # True: int → float
print(complex(int_val)) # True: int → complex
print(bool(int_val))    # True: int → bool
print(str(int_val))     # True: int → string
# print(list(int_val))  # False: int → list (Error)
# print(tuple(int_val)) # False: int → tuple (Error)

# Float conversions
float_val = 10.5
print(int(float_val))   # True: float → int
print(complex(float_val)) # True: float → complex
print(bool(float_val))  # True: float → bool
print(str(float_val))   # True: float → string
# print(list(float_val))  # False: float → list (Error)
# print(tuple(float_val)) # False: float → tuple (Error)

# Complex conversions
complex_val = 2 + 3j
# print(float(complex_val)) # False: complex → float (Error)
print(complex(complex_val)) # True: complex → complex
print(bool(complex_val))  # True: complex → bool
print(str(complex_val))   # True: complex → string
# print(list(complex_val))  # False: complex → list (Error)
# print(tuple(complex_val)) # False: complex → tuple (Error)

# Boolean conversions
bool_val = True
print(int(bool_val))    # True: bool → int
print(float(bool_val))  # True: bool → float
print(complex(bool_val)) # True: bool → complex
print(str(bool_val))    # True: bool → string
# print(list(bool_val))   # False: bool → list (Error)
# print(tuple(bool_val))  # False: bool → tuple (Error)

# String conversions
str_val = "123"
print(int(str_val))    # True: string → int
# print(complex(str_val)) # False: string → complex (unless it's a valid number)
print(bool(str_val))   # True: string → bool (Non-empty string is True)
print(str(str_val))    # True: string → string
print(list(str_val))   # True: string → list
print(tuple(str_val))  # True: string → tuple

# List conversions
list_val = [1, 2, 3]
# print(int(list_val))   # False: list → int (Error)
# print(float(list_val)) # False: list → float (Error)
print(bool(list_val))  # True: list → bool (Non-empty list is True)
print(str(list_val))   # True: list → string
print(list(list_val))  # True: list → list
print(tuple(list_val)) # True: list → tuple

# Tuple conversions
tuple_val = (4, 5, 6)
# print(int(tuple_val))   # False: tuple → int (Error)
# print(float(tuple_val)) # False: tuple → float (Error)
print(bool(tuple_val))  # True: tuple → bool (Non-empty tuple is True)
print(str(tuple_val))   # True: tuple → string
print(list(tuple_val))  # True: tuple → list
print(tuple(tuple_val)) # True: tuple → tuple



#output for all converstions

# Define the data for type conversions
data = {
    "": ["int", "float", "complex", "bool", "string", "list", "tuple"],
    "float": [True, True, False, True, True, False, False],
    "complex": [True, True, True, True, False, False, False],
    "bool": [True, True, True, True, True, True, True],
    "string": [True, True, True, True, True, True, True],
    "list": [False, False, False, False, True, True, True],
    "tuple": [False, False, False, False, True, True, True],
    "int": [True, True, True, True, True, False, False]
}


