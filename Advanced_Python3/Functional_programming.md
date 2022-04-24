## Functional Programming

### OOP
- structure code based on **concepts of objects**
- objects have fields that store data and methods that manipulate data
- objects can be passed as an argument in the function of another object


### Functional
- structure code based on **using functions**
- functions are **"first-class citizens"**: can be used to store and manipulate data (with limitations)
- functions can be passed as an argument to another the function and be returned by other functions
- functions have to be **deterministic**: when provide with same input, must return same output
- use recursion instead of loops


### Declarative vs Imperative
- Imperative (急切): "how to solve a problem"
    - OOP
    - procedural
- Declarative (聲明性): "what problem to solve"
    - functional

### Immutable Data types
- thread-safe data manipulation
- preventing programmers from accidentally changing a value



#### Tuple vs Namedtuple
- **Tuple**: immuntable
- **Namedtuple**: light-weight, object-like variable. "You should use named tuples instead of tuples anywhere you think object notation will make your code more pythonic and more easily readable". [stackoverflow credit: what are namedtuple](https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python)
```
from collections import namedtuple

# create a class called student
student = namedtuple("student", ["name", "age", "grade"])

# Create tuples for the three students
scott = student("Scott", 28, 'A')
nicole = student("Nicole", 26, 'B')
john = student("John", 29, 'D')

# Access Scott’s information for example
print(scott.name) # Output: Scott
print(scott.age) # Output: 28
print(scott.grade) # Output: ‘A’
```

#### Namedtuple vs Python Dictionaries
- Dictionaries: hash table type
```
In dicts, only the keys have to be hashable, not the values. namedtuples don't have keys, so hashability isn't an issue.
```
- [stackoverflow credit: namedtuple vs dictionary](https://stackoverflow.com/questions/9872255/when-and-why-should-i-use-a-namedtuple-instead-of-a-dictionary)
- [python doc credit: hashable](https://docs.python.org/3/glossary.html#term-hashable)
