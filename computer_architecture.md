# Computer Architecture

## How Computers Work
1. Input: Human phyical interaction with computer (eg. clicking, turning knobs, typing)
2. Processing:
    - CPU: [Central Processing Unit](#Central-Processing-Unit).
    - Responsibility of establishing communication between hardware and software. (eg. Decipher data input and sends instruction to hardwares as outputs.)
3. Memory:
    - RAM: Random Access Memory (* Primary Memory)
    - Hard Disk: (* Secondary Memory)
        - **Primary Memory (known as Main memory)**: where computer stores data and information for *fast access*. It is **volatile** memory, which means data is stored *temporarily* and requires power to maintain.
        - **Secondary Memory**: *external* storage / memory that stores data **permanently**
4. Output: Monitors, Speakers, Printers


### Binary System
- Computer only understand **2 states**. 1 and 0.
- **Bit**: smallest unit of data measturement. 1 or 0
- **Byte**: 8 bits
- **Word**: 16 bits

#### Binary to Decimal Conversion
```
8-bit number: 11001110
(2^7) | (2^6) | (2^5) | (2^4) | (2^3) | (2^2) | (2^1) | (2^0)
  1       1       0       0       1       1       1       0

 128  +   64  +               +   8   +   4   +   2

= 206

```


## Intruction Set Architecture (ISA)

**ISA**: set of rules that define the communication between hardware and software

```
1. Hardware (eg. CPU) - works with binary
2. Software (eg. Python, Java, etc) - works with human-readable code
```
###### ISA manage the translation of the above.

Two design practices:
1. Complex Instruction Set Computer (CISC):
    - focus on having the fewest lines of code to maximize performance
    - machine codes have same lengths
2. Reduced Instruction Set Computer (RISC):
    - focus on reducing complexity
    - machine codes have same lengths


#### Central-Processing-Unit
1. Control Unit (CU): monitoring input and output from hardware
2. Arithmetic and Logic Unit (ALU): consists of all processors
3. Registers (Immediate Access Store): limited space, high speed memory and CPU can quickly access

#### OPCODEs
```
First few bits is the OPICODE or OPeration CODE, which always tells the processorr what type of instruction it is receiving
```
###### 32-bit instruction
```
Example:
000001 01001 10111 0001101001010110
OPCODE
```


## Assembly

**Assembly**: low-level programming language used to translate instructions into computer's machine code.

#### Compilation Process
1. **Preprocessing**: removing comments, expanding included macros, and code maintainance
2. **Compiling**: translate into optimized Assembly language
3. **Assembling**: generate machine code with the assembly language
4. **Linking**: filing in function calls

###### Microprocessor without Interlocked Pipeline Stages(MIPS) Examples:
```
ADD $5, $5, $6
    -> add values in Register 5 to Register 5 and save result at Register 6

LW $4, ($5)
    -> Load value stored in memory address of Register 5 into Register 4
    -> "()" indirect, treats value in Register as the **memory address in another memory location** and retrieve that value from that memory location
    (eg.
    Register 5: 839
    Another memory with address 839: 1234
    $5 : 839
    ($5): 1234
    )
```

## Cache
**Processor-Memory Performance Gap**
- Processor performance > Memory performance
- Simple Memory Hierarchy
```
    ^                Processor         ^
    |                Cache             |
    |                Main Memory       |
Size decreases                 Performance increases
```
Cache
- Tag, Data
- Cache hit
