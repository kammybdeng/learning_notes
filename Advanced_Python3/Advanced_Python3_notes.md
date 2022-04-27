## Logging


- Differences between sys.exit(0) and sys.exit(1)
    - [stackoverflow explaination](https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python)

- What is "__name__" in python
    - """__name__ is a built-in variable which evaluates to the name of the current module."""
    - [geek_for_geek explaination](https://www.geeksforgeeks.org/__name__-special-variable-python/)

- Logging level: to set the level log messages will be produced (Default logging.WARNING)
```
NOTSET          0
DEBUG          10
INFO           20
WARNING        30
ERROR          40
CRITICAL       50
```
- Formatting: to format log message (eg. timestamps, function names, and line numbers)
- Logging to file and/console:
- Configure with basicConfig

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

```
EXAMPLE 1:
------ Imperative ------

lst = []
for i in nums:
  if i % 3 == 0:
    lst.append(i)

for i in range(len(lst)):
  lst[i] = lst[i] * 3

----- Declarative ------

map(lambda x: x * 3, filter(lambda x: x % 3 == 0, nums))

EXAMPLE 2:
------ Imperative ------
lst = []
for i in nums:
  if i < 5:
    lst.append(i)

largest = 0
for i in lst:
  if i > largest:
    largest = i

----- Declarative ------
reduce(lambda x, y: x if x > y else y, filter(lambda x: x < 5, nums))


```

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


## Extra
[Cheat Sheet](https://www.codecademy.com/learn/paths/learn-advanced-python/tracks/learn-advanced-python/modules/logging/cheatsheet)
