## Input and Output



## Serialization

**Serialization**: process of taking an object's **state** and transform it into a stream of bytes
- stream: a sequence of data
1. Fields and types -> bytes.
2. Bytes -> written to memory/file/database or sent over a network
3. Recreate object from byte (aka. deserialization)

**Deserialization**: process of converting bytes to object

1. Stream of bytes created by serialization only includes member variables and not its methods
2. Deserialization -> copy of object -> copy shares same state but is a new object in memory
