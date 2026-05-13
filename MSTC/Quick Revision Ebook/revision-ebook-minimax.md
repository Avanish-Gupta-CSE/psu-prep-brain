
Computer Science &

Engineering / Information

Technology

CAPSULE

Quick Revision

Key Notes, Terms, Definitions and Formulae

Use Full for :

· UGC-NET/JRF / GATE / IES / PSU / UPPSC AE/Polytechnic Lecturer/LT Grade/

NIELIT/ISRO . UPPCL AE . UPRVUNAL AE . UJVNL AE . KVS NVS PGT . DSSSB

. PTCUL . ASSAM PSC . APPSC . BPSC . CGPSC . GUJRAT SC . HPPSC . UPSC

. MPPSC . Rajasthan Basic Computer Teacher · J&KPSC · Kerala PSC . Karnataka

PSC . KPCLAE . ISRO Scientist/Engineer · OPSC . RPSC . TNPSC . Punjab PSC

. Maharashtra PSC . BHEL ET . TANGEDCO AE . TELANGANA PSC . JUVNL

AEE . CIL MT . RRB SSC . SJVNL ET . TSGENCO AE . VIZAG STEEL MT

· TAMILNADU TRB Polytechnic Lecturer

CHIEF EDITOR

Anand Kumar Mahajan

COMPILED & WRITTEN BY

Computer Science & Information Technology Expert Group

EDITORIAL OFFICE

12, Church Lane Prayagraj-211002

L

Mob. : 9415650134

Email : yctap12@gmail.com

website : www.yctbooks.com

PUBLISHER DECLARATION

Edited and Published by A.K. Mahajan printed for YCT Publications Pvt. Ltd.

and Printed by Lakshmi Narayan Printing Press, Prayagraj.

In order to publish the book, full care has been taken by the Editor and the

Publisher, still your suggestions and queries are welcomed.

Rs. : 495/-

In case of any dispute, the Judicial area will be Prayagraj.

INDEX

Computer Organization and Architecture

3-10

Data Structures & Algorithm

11-27

Discrete Mathematics

28-35

Digital Logic

36-49

Database Management System.

50-65

Theory of Computation

66-78

Compiler Design

79-85

Operating Systems

86-103

Computer Networks

104-119

Programming in C & C++

120-141

Web Technology

142-156

Software Engineering

157-180

Cloud Computing

181-192

2

01.

Computer Organization and

Architecture

Von Neumann Architecture (Stored Memory

Program)

Main

Memory

Central Processing Unit

Registers

Control

Unit

Arithmetic

Logic

Unit

1

Input Output System

Various General Purpose Registers-

· Address Register

· Data Register

· Accumulator

· Program Counter

OP code Operand

· Instruction Register

· Temporary Register

· Input Register

· Output Register

Type of Bus- There are three type of Bus.

· Address Bus

· Data Bus

· Control Bus

Bus Architecture

8085

Microprocessor

Unit

Control

Unit

Address Bus

Unidirectional

Data Bus

Bidirectional

Control Bus

Unidirectional

Memory

Input

Output

· The address bus, which is a unidirectional path

way that allows information to travel in only one

direction, carries information about where data

will be stored in memory.

· The data bus is a bidirectional path way that

carries the actual data (information) to and from

the main memory.

. The control bus carries the control and timing

signals needed to coordinate the activities of the

entire computer. Think of this as a traffic cop.

Bus Arbitration-The overall control which decides

who will control the master bus line.

Memory

CPU

DMA

There are two approaches to bus arbitration.

· Centralization bus arbitration

· Distributed bus arbitration

Register-

1. Memory Address Register (MAR) hold on

address of the memory unit.

2. PC-Program Counter

3. IR-Instruction Register

4. R-Processor Register

Computer register are designated by capital letters.

Register Transfer- R2 <- R1

5. DR - Data Register

Bus and Memory Transfers-

Common Bus- It consists of a set of common lines

one for each bit of a register through which binary

information is transfered one at a time.

Control Signal-Determine which register is

selected by the bus during each particular register

transfer.

Bus System for four Register-

· In general bus system will multiplex K register

of n bits each to produce an n-line common bus.

· The number of multiplexers needed to construct

the bus is equal to n, the number of bits in each

register.

· The size of each multiplexer must be K×1 since it

multiplexer K data lines.

S

S

4 line

Common

Bus

4× 1

MUX 3

4 × 1

4 × 1

MUX 1

4 × 1

MUX 0

MUX 2

3

3210

3210

3210

3210

D2 C2 B2A2 DICIBIA,

Do Co Bo Ao

D2DID0

C2 C1 Co

B2B1B0

A2A1A0

3210

3210

3210

3210

Register D

Register C

Register B

Register A

Bus Transfer-

Bus <- R2, R1 <- BUS

=>R1 <- R2

Computer Organization and Architecture

3

YCT

Memory Transfer- Read : DR <- M[AR]

Write : M[AR] <- R1

Where,

DR -> Data Register

AR -> Address Register

Micro-operations- Micro-operations classified into

four categories Address Register «- Program

counter

1. Register Transfer Micro-operations

2. Arithmetic Micro-operation

3. Logic Micro-operation

4. Shift Micro-operation

Register Transfer Micro-operations- These type

of micro operations are used to transfer from one

register to another binary information.

Arithmetic Micro-operation

1. Addition - R3 <- R1 + R2

2. Subtraction - R3 <- R1 - R2

R3 <- R1 + R2 +1

3. 1's complement - R2 <- R2

4. 2's complement - R2 <- R2 +1

5. Increment - R1 <- R1 +1

6. Decrement - R1 <- R1 -1

Arithmetic shift - The increment and decrement

micro operations are implemented with a binary up-

down counter.

Logic micro operation-

1. OR - R1 <- R1VR3

2. AND - R1 <- R2 AR3

3. XOR - R1 <- R2 OR3

4. Compliment - R1 <R

5. X-NOR - R1 <- R2 OR3

Shift Micro operation-

· Logical shift

· Circular shift (Rotation)

· Arithmetic shift

Logical Shift- There are two types

· Left shift

Example-

1011 ->

×

10110-0110

· Right shift.

Example-

1011->

01011-0101

×

Circular shift- There are two types

· Left shift

1011

/11

0 1 1 1+=0111

· Right shift

1011

1101=1101

Arithmetic shift- Applied on signed number after

the shift sign of the number should remain same.

Left shift- It is same as logical left shift but it is

allowed only when sign is not going to change.

Example-

1 1 0 1 =>-Ve

1 0 1 1 =>-Ve

× 1 0 1 0=>-Ve

allowed

/ //

not allowed

× 0110=>+Ve

Error-arithmetic

left shift overflow

Right shift-

1001

+1100x

self

Instruction format-

· A group of bits which instructs computer to

perform some operation.

ISA (Instruction Set Architecture) Collection of

all instruction CPU supports.

Type of Instruction (Based on Operation)

· Data Transfer - MOV, LDI, LDA

· Arithmetic & Logic - ADD, SUB, AND, OR

· Machine Control - EI, DI, PUSH, POP

· Iterative - LOOP, LOOPE, LOOPZ

· Branch - JMP, CALL, RE T, JZ, JNZ

Type of Instruction (Based on Operand

Information)

· 4-Address Instruction

· 3-Address Instruction

· 2-Address Instruction

· 1-Address Instruction

· 0-Address Instruction

Operand

Opcode

Types of CPU Organization- The number of

address fields in the instruction format of a

computer depends on the internal organization of

the registers.

There are three types of organization.

1. Single Accumulator Organization

2. General Register Organization

3. Stack Organization (LIFO)

1. Single Accumulator Organization- The

instruction format in this type of computer user one

address field.

Example-

ADD x AC <- AC + M[X];

AC -> Accumulator Register

2. General Register Organization uses three and two

address instructions.

Computer Organization and Architecture

4

YCT

Example-

ADD R1, R2, R3 = R1 <- R2 + R3

ADD R1, R2= R1 <- R1 + R2

3. Stack Organization uses zero and one address

instruction.

Example-(i) PUSH (ii) ADD

In a general register CPU organization there are

eight general purpose register and ALU can perform

32-different operation.

The number of selection line of each multipliers for

selecting the operand = 3 (23 =8)

The number of bits in operation code= 5(25 = 32)

The length of the control word = 5 + 3 + 3 + 3 = 14

(for 3-address instruction)

Addressing Mode

The way of operand are choosen during program

execution is dependent on the addressing mode of

instruction.

The addressing mode may reduce the number of bits

in the addressing field of the instruction.

Instruction Cycle- CPU performs 6 phases to

execute an instruction.

Instruction

Fetch

Instruction

Decode

Effective

Address

Calculation

Operand

Fetch

Execution

Copy Back

Result

Fetch cycle - Instruction fetch

Execution cycle - from decode ...... to write back

Type of addressing mode-

· Implied Mode- Operand is specified Implied

in the definition of instruction.

Used for zero address and one address instruction.

. Immediate Mode- Operand is directly

provided as constant.

No computation required to calculate effective

address.

· Register Mode- Operand is present in the

register.

Example- LDR1=> AC <- R1

Register number is written in instruction.

· Register Indirect Mode- Register contains

address of operand rather than operand itself.

Example- LD (R1) => AC <- M[R]]

. Auto Increment or Auto Decrement

Addressing Mode- Special case of register

indirect addressing mode.

Example-

LD(R1)+=>AC <- M[R]], R1 <- R1 +1

. Direct Addressing Mode (Absolute

addressing mode)- Actual address is given in

instruction.

Use to access variables

Example- LD ADR => AC <- M[ADR]

· Indirect Addressing Mode-

Using to implement pointers and passing

parameters.

2 memory access required. Where the effective

address is stored in memory.

Example- LD@ADR => AC <- M[M[ADR]]

. Relative Address Mode- In this mode the

content of the program counter (PC) is added to

the address part of the instruction in order to

obtain the effective address.

Example- LD$ADR => AC <- M[PC + ADR]

# Relative addressing is often used with

branch-type instruction.

· Base Register Mode- Used in program

relocation of programs in memory.

Indexed Addressing Mode-

-> Use to access or implement array efficiently.

-> Multiple Registers required to implement.

-> Any element can be accessed without changing

instruction.

Example- LD AD R(x) => AC <- M [ADR + X]

Arithmetic Logic Unit (ALU)

Inside a computer, there is an (ALU) which is

capable of performing logical operations (e.g AND,

OR, Ex-OR, Invert etc.) in addition to arithmetic

operation (Addition, Subtraction etc.). The control

unit supplies the data required by the ALU from

memory or from input devices and directs the ALU

to perform a specific operation based on the

instruction fetched from memory.

Integer

Operand

T

Integer

Operand

A

B

Status

>Status

Opcode

Y

Integer

result

Arithmetic Logic Unit (ALU)

Memory Hierarchy

Bytes

Register

Cache

Memory

Internal

Memory

KB/MB

GB

Main Memory

(RAM)

Primary

Memory

GB

USB/Flash Memory

Secondary

Storage

TB

Magnetic Disk/Hard Disk

PB

Magnetic Tapes/Tape Drive

Tertiary

Storage

Cache Memory

Cache memory faster than main memory.

Cache hit- It required element present in cache that

called cache hit.

Hit latency- Time taken to find out whether

element present on the cache or not that is called hit

latency.

Cache miss- It required element not present in

cache, that is called 'Cache miss'.

Computer Organization and Architecture

5

YCT

Miss latency- Time taken to get something from

main memory and then place it into the cache and

then read that's called miss latency.

Page hit- It required element present in main

memory.

Page fault- It required element not present in main

memory.

Tag directory- Tag directory say that required

element present in tag on not.

Introduction to Direct mapping-

. Taking about disk and main memory we talking

about paging.

. Talking about Cache and main memory we talking

about blocks.

· Block size = lines size.

Cache

Main Memory

Lo

B0 B4 B& B12

Wo W1 W2 W3

Bo

L1

B, B, B, B13

W4 W5 W6 W7

BI

B2 B6 B10 B14

Wg W9 W10 W11

B2

L2

W12 W13 W14 W15

B3

L3

B3 B, B11 B15

16 words

W 124 W 125 W 126 W 127

B31

128 words

· Smallest addressable unit in the memory called

word.

Let's

1 w = 1B (means system is byte addressable)

Block size = 4 word

No. of black in main memory = 128/4 = 32 block

No. of Lines in Cache = 16/4 = 4 lines

Physical address contain = 128 = 27 = 7 bits

Processure generate address =

322

tag

line

Block

Offset

5

2

no.

001

01

00 20

Block

Block

001

01

01 21

number | off set

001

01

10 22

001 01

11.23

Example-

Main memory size = 128 KB

Cache size = 16 KB

Block size = 256 B

Tag bits = 3 bit

Tag directory size = ?

Solution -

Main memory size 128 KB

= 210 *128 B

= 210 *27 B

= 217 B

Block size = 256 B = 28 B

217

No. of Block = == 29 bit

28

Cache size = 16 KB = 214 b

Line number

1

₦

₭

17 b

3 bit

6 bit

8 bit

Tag

Block Offset

Block number

Cache size

Number of line =

Block size 28

=

214

: 2° bit

Tag directory size = (Tag size * No. of lines)

= (3*2º) bit

Fully Associative- The associative memory stores

both the address and content (data) of the memory

word. This permits any location in cache to store

any word from main memory.

Lo

Bo

W0 W1 W2 W3

Bo

L1

Bo

W4 W5 W6 W7

BI

L2

Wg W9 W10 W11

B2

Bo

L3

Bộ

16 words

W 124 W 125 W 126 W127

B31

128 words

7

5

2

Block

number

Block

Offset

Tag

Block no. = 32 = 25 = 5 bit

Block offset = 4 = 22 = 2 bit

Set-Associative Mapping- The set associative

mapping is an improvement over the direct mapping

in that each word of cache can store two or more

word of memory under the same index address.

Total number of set

=

No.of lines

K

K is number of way

Example-

4 way set associative cache lines = 128

Lines size = 64 word

Physical address = 20 bits

Tag, set and word field are?

Solution-

K

20 b

₦

9 5 6

Tag

Set Block word

Cache size

Number of lines =

Lines size

Computer Organization and Architecture

6

YCT

Cache size = 2° * 27 = 213 word

Sets = Lines == 2

not size -2 =2

27

Set

22

Tag = 9, Set =5, Word =6

Locality of Reference-

1. Spatial locality

2. Temporal locality

. If a word is accessed now then the word adjacent

to it (close proscimity) will be accessed next.

· Keeping more words in a block affects spatial

locality (block size).

. If a word is referenced now then the same word

will be referenced again in future.

· LRU is used in temporal locality.

Cache Replacement Algorithms-

· Replacement policy is required for associative

mapping and set associative mapping but not for

direct mapping.

· Replacement policies are aimed to minimize miss

Penalty for future references.

Replacement Policies

Random

FIFO

LRU

LFU

(No specific

Criteria to

(The block

(The block

which entered which is not

the replace first is references

the block) candidate

for longest

time which

is replace)

Replacement)

Example- Consider the cache has 8 blocks for the

memory reference (5, 12, 13, 17, 4, 12, 13, 17, 2,

13, 19, 13, 43, 61, 19). What is the hit ratio for the

following cache replacement algorithms.

(i) FIFO

(ii) LRU

(iii) Direct mapping

(iv) 2-way set associate

(i) FIFO

M

M

M

M

M

H

H

H

M H

5, 12, 13, 17, 4, 12, 13, 17, 2, 13,

MMMMH

19, 13, 43, 61, 19

So

8

A 43

SI

12

2 61

S2

13 19

S3

V1

13

Hit ratio

=x100 == 33-

100

1

5

15

3

3

Miss = = x100 == x100=66=

10

15

2

2

3

3

MMMMMHH H MH

(ii) LRU

5, 12, 13, 17, 4, 12, 13, 17, 2, 13,

MHMMH

19, 13, 43, 61, 19

($, 12, 15, 11, A, 12, 13, 11, 2, 15, 19, 13,

43, 61, 19)

Hit ratio

=

×100

15

= 40

Miss = x100 = 60

15

9

(iii)

Direct

mapping

M

M

M

MMMMMMMM

5, 12, 13, 17, 4, 12, 13, 17, 2, 13,

5,

M

MHMMM

19, 13, 43, 61, 19

So

12

1 122

SI

$

฿ X 3 61

Line number = B.No mode 4

Cache hit ratio = = x100 =6.66

1

15

Miss ratio =

== x100 =93.333

15

14

(iv) 2-way set associate

5 12 13 17 4 12 13 17 2 13

M, M, M, M, M, H, H, H, M, H,

1

19 13 43 61 19

M, H, M, M, M

1

So

V2 A

12 12

V V V V V V3 V3 61 19

SI

8 V3

Line no. = (i mod 2) i -> Block number

Hit ratio = = x100 =33.33

15

Miss ratio = = x100 =66.66

10

15

Computer Organization and Architecture

7

YCT

(The block

which fever

S2

references

is replaced)

S3

19

43 19

Control Processing Unit

CPU Control Design- There are two major types

of control organization.

(i) Hardwired Control

(ii) Micro programmed control

Hardwired Control Unit- Control logic is

implemented with gates, flip-flops, decoders and

other digital circuits.

Advantage- Can be optimized to produce a faster

mode of operation.

Disadvantage- Rearranging the wires among

various components is difficult.

Instruction Register

Decoder

Clock

Timing

Generator

Control Unit

Flags

Control signal-C. C ..... Cm

m

Micro-Programmed Control Unit- Control Logic

is implemented with micro programmed.

Advantage- Updating the control logic is easy.

Disadvantaged- Slower than hardwired control

unit.

Control Word Sequencing

External

I/P

Next-address

Generator

Sequence

Control

Address

Register

(CAR)

Control

Memory

(ROM)

Control

Data

Register

Control

Word

Next Address Information

Example- CPU has 64 distinct instructions each

instruction takes 8 micro operation micro-

instruction-

(i) Signals (128 bits)

(ii) Mux select [16 mux inputs]

(iii) Address

What is size of control memory?

Solution- Total micro operations = 64*8

= 26 * 23 = 29

Memory address = 9 bits

Signals

MUX

select

Address

128

4

9

Total micro Instruction = 128 + 4 + 9 = 141 bit

so size of control memory = 29 *141 bits

Difference between Horizontal Micro

Programming and Vertical Micro Programming

Horizontal Micro

Programming

Vertical Micro

Programming

1.

Control Word Large

Control word is

small

2.

Parallelism is high

No parallalism

3.

Faster

Slower

Difference between Hardwired Control Unit and

Micro Programming Unit

Hardwired

Control Unit

Micro Programming

Unit

1.

Fixed Instruction

Instruction can flexible

2.

High speed

Slower compared to

hardwired instruction

3.

Expensive

Relatively cheap

4.

Complex

Simple

Example- Intel

8085, Motorola

6802 Tilog 80 and

Instruction Set

any

Reduce

Computer (RISC)

Example- INTEL 8080,

Motorola 68000 and any

complex instruction set

computer.

Difference between RISC and CISC

RISC

CISC

Less number of

instruction

More

number of

instruction

Fixed length instruction

Variable

length

instruction

Simple Instruction

Complex Instruction

Limited addressing

More & complex

addressing modes

Easy to implement using

hardwired control unit

Difficult to implement

using hardwired

One cycle per instruction

Multiple cycle per

instruction

Register to register

arithmetic operation only

Register to memory &

memory to register

arithmetic operations

possible

More number of registers

Less number of registers

Example- Consider the following processor design

characteristics.

(i) Register to register arithmetic operation only

(ii) Fixed length instruction format

(iii) Hardwired control unit

Which of the characteristics above are used in the

design of a RISC processor?

(a) i and ii only

(b) ii and iii only

(c) i and iii only

(d) i, ii and iii

Computer Organization and Architecture

8

YCT

IO Organization

Peripheral Device- Devices connected to processor

externally are known as peripherals. There are three

type-

· Input Devices

· Output devices

· Storage devices

Input/Output Subsystem Of Computer- Provides

an efficient mode of communication between

control system & outside word.

Input/Output Interface- Provides a method for

transferring information between internal storage

(memory & registers) & external I/O devices.

CPU

I/O

Interface

I/O

Device

· Serial and Parallel Transmission

(i) Serial Transmission

Source

Destination

(ii) Parallel Transmission

Source

Destination

Difference between Serial and Parallel

Serial

Parallel

Need of shift register

No need of shift

register

Burst errors

Bit errors

Cheaper

Costless

Less reliable

More reliable

Used to more distance

Used

to

less

distance

Asynchronous Transmission- Data

is sent in

form of byte or character. This transmission is the

half-duplex type transmission. In this transmission

start bits and stop bits are added with data.

Example-

· Email

· Forums

· Letters

Synchronous Transmission- Data is sent in form

of blocks or frames. This transmission is the full-

duplex type. Between sender and receiver,

synchronization is compulsory.

Example-

· Chat rooms

· Telephonic conversations

Example-

How many 8 bit characters can be transmitted per

second over 9600 baud (bits/sec) serial

communication link using a parity synchronous

mode of transmission with 1 start bit, 8 data bits, 2

stop bits and 1 parity bit.

Solution-

For 1 char = 1 +8+2+ 1 = 12 bits

Characters transmitted

=

9600

800 char / sec

12

Mode of transfer- 3-way to perform I/O

· Programmed I/O

· Interrupt driven I/O

· DMA

Programmed I/O

{1. Read the status flag.

2. It data is not available (status = 0) then go to step

1.

3. Move the data}

· Waste time processor

. Mostly devices time to transfer 1 byte.

Interrupt Initiated IO-

· IO device has a provision (interrupt signal) to

inform to CPU about communication

When CPU receives interrupt-

· It completes execution of current instruction

· Saves the status (PC, PSW etc.) of current process

onto the stack

· Branches to service the interrupt

· Resumes the previous process by taking out the

values from stack.

DMA (Direct Memory Access)

· Enables data transfer between I/O and memory

without CPU intervention.

. Need a hardware : DMAC

Starting Address - Memory Address starting from

where data transfer should be perform.

Data Count- No of bytes or word to be transferred.

Starting

Address

Data

Count

Initially

After 1B

After 2B

After 3B

1000

1001

1002

1003

500

499

498

497

0

No data transfer

Modes of DMA Transfer

· Burst mode (all data transfer at the same time)

· Cycle stealing (it happen word by word)

· Interleaving DMA (Whenever CPU does not

require system buses (doing internal work) then

only control of the buses given to DMAC).

Computer Organization and Architecture

9

YCT

Flynn's Classification of computer

· SISD- Single Instruction Stream, Single Data

Stream

Example- Von-neamann

· SIMD- Single Instruction Stream, Multiple Data

Stream

Example- Pipeline processor

· MISD- Multiple Instruction Stream, Single Data

Stream only hypothetical

· MIMD - Multiple Instruction Stream, Multiple

Data Stream

Example- Multiple Pipelines (Super Scalar

Computer (ILP))

Pipelining

· Pipelining is useful, when same processing is

applied over multiple inputs.

· Technique to decompose a sequential process into

sub-operations.

· Sub-operations performed in all segments.

· Task: one operation performed in all segments.

General Consideration about pipeline

· Consider a K segment pipeline with clock cycle

time = tp to perform n tasks.

Time required to perform 1st task = K*tp

Time required to perform remaining (n -1) tasks =

(n-1)tp

Time required for all n tasks =(K+n-1)tp

(K + n-1) is total cycle.

· Consider a non-pipeline system that takes tn time

to perform a task

Time required for n task = n*tn

· Performance of a pipeline is given by speed up

ratio.

Speed up ratio

=

Non - pipeline time

Pipeline time

n*tn

S=

(K+n-1)tp

as the number of task increases, n>>K (Ignore K-1)

Sideal = 1

tn

tp

Latency- Time after machine takes next input.

. Latency in non-pipeline = tn

. Latency in pipeline = tp

Throughput- No of input processed per unit of

n

time =

(K+n-1)tp

Ideal case-

Throughput ="

1

tp

Example- Consider a 5 stage pipeline with cycle time

of 15 ns. Calculate processing time of pipeline

for 500 tasks.

n = 500, K = 5, tp = 15

processing time of pipeline = (K + n- 1)tp

=(5 + 500-1)15

= 504×15

= 7560 n sec

Instruction Pipeline

If pipeline processing is implemented on instruction

cycle.

IF : Instruction fetch

ID : Instruction decode & Address calculation

OF : Operand Fetch

EX : Execution

WB : Write Back

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

I1

IF

ID

OF

EX

WB

I2

IF

ID

OF

EX

WB

I3

IF

ID

OF

EX

WB

I4

IF

ID

OF

EX

WB

I5

IF

−

−

I6

I7

I8

IF

ID

OF

EX

WB

I9

IF

ID

OF

EX

WB

Assume in cycle number 5, I4 decoded as branch

instruction.

By standard => Branch decision is made in

'Execution' phase.

· After execution phase next instruction can be

fetched.

Actually only instruction executed (n = 6) K = 5 for

n input, no. of cycles = K+ n - 1

=5+6-1

=10

3 cycles are extra (stall cycles because of branch)

Total = 10 + 3 = 13 cycles

Total execution time = cycle * tp

Pipeline Hazards- Situations that prevent the next

instruction from being executing its designated

clock cycle.

· Hazard lead to have stall cycles

There are three type-

1. Structural Hazard/Resource Conflict

2. Data Hazard/Data Dependency

3. Control Hazard/Branch difficulty

Structural Hazard- When multiple instruction

need same resource.

Control Hazard- All Instruction who change the

program counter leads to control hazard because of

branch instruction.

Data Hazards Classification-

. RAW (Read After Write) [Flow/true data

dependency]

· WAR (Write After Read) [Anti Data dependency]

. WAW (Write After Write) [Output data

dependency]

Computer Organization and Architecture

10

YCT

02.

DATA STRUCTURE AND

ALGORITHM

DATA STRUCTURE

Data- Data is a collection of raw, unorganized facts and

details like text, observations figures, symbols, and

descriptions of things etc.

Data can be record and does not have any meaning

unless processed.

Information- Information is processed, organized, and

structured data.

Definition of data structure - A data structure is a

collection of data, generally organized so that items can

be stored and retrieved by some fixed techniques.

Classification

Primitive

Non-Primitive

Example

·Integer-1,2,3 ....

·Real

.Character-'A','B',

·Pointer

Linear

Non-linear

·Logical

Example

Example

·Linked list

·Graph

·Stack

·Tree

·Queue

Data structure operation

Insertion- Add a new data in the data structure.

Example-

10 20 30 40

50

10 20 30 40 50

new data

Insertion data structure

Deleting- Remove a data from the data structure.

Example-

10

20

30

40

50

Deleting

20

10

30

40

Sorting- Arrange data in increasing or decreasing order.

Example-

data- 20, 30, 10, 5, 6

5 6

10

20

30

Searching- Final the location of data in data structure.

Example-

5

6

10

20

30

a[0] a[1] a[2] a[3] a[4]

Search = 10 -> a[2]

Merging- Combining the data of two different sorted

files into a single sorted.

Example-

12 3

4 5 6

Merge

123456

Traversing- Accessing Each data Exactly one in the

data structure so that Each data item is traversed or

visited.

Example-

1 2 345

Arrays in Data structure

Array- Array is a fixed size sequenced collection of

data items of same type.

· Access a particular element = array name [index]

= Int a [ ]

· data items are stored in continuous locations.

How the data is to be accessed, how you can calculate

the address.

Int a [5] 0 1 2 3 4

62430

100 104 108 112 116

Base

a[0]=6, a[1]=2, a[2]=4, a[3]=3, a[4]=0

Formula-

Address of a[i] = Base +i * (size of data type)

i = 0, 1, 2 ........ (n - 1)

n = size of array

so if want to, i = 2;

Int size = 4 bit

= 100+2×4

=108

. Random Access taking Constant time.

1-D-array

Type

2-D-array

Multi-dimensional array

· Name [LB:UB] LB ≤ UB

LB = Lower Bound

UB = Upper Bound

Data Structure and Algorithm

11

YCT

Nonthor

array

Size of array = UB-LB+1

Consider an array A [6:18].

Total number of element in array

By formula

Size of array = UB - LB+1

=18-6+1

= 13

Searching Array-

· Searching an array means to find a particular element

in the array. The search can be used to return the

position of the element or check if it exists in the

array.

· Linear Search

Time complexity

Average

O (n)

Best

O (1)

Worst

O (n)

· Binary search

Time complexity

Average

O (log n)

Best

O (1)

Worth

O (n)

· Pointer is an address of another variable

Example-

int b = 10;

int* P;

b

P

10

200

P = & b;

200

204

2-D Array

The two-dimensional array can be defined as an array of

array.

2D array syntax-

data type array_name [row][columns];

Representation of 2-D Arrays in memory

Row major order-

a [i][j] = B+((i*n)+ j)*size.

IF start (0,0)

A [i][j]=[((i-1)*n+(j-1))*size + Base if start (1,1)

Colom major

A [i][j] =((i*m) + i)*size + Base

Linked List

A Linked list is a Linear data structure in which the

elements are not stored at contiguous memory location.

· A liked list is a dynamic data structure.

· Each element is called a node which has two part,

info part stores the information and pointer part

which point to the next element.

info

Pointer

Start

Node

NULL

info

Pointer

info

Pointer

info

Operation On Linked List-

1. Creation - This operation are used to created a linked

list in this node is created and linked to the Another

node.

2. Insertion- This operation is used to insert a new node

in the linked list.

3. Deletion- In this operation, elements can be deleted

at the starting of the list.

4. Traversing- It is a process of going through all the

nodes of linked list from one End to the other end.

Type of Linked List

· Singly Linked List- A singly linked list is a

unidirectional linked list. It is the simplest type of

linked list in which every node contains some data and a

pointer to the next node of the same data type.

Start

10

20

30

Sequential manner

•

Doubly Linked List- A doubly linked list is a

bidirectional linked list that contains a pointer to the

next as well as the previous node in sequence.

Start

Prev Data succ

Prev Data

Last

Prev Data succ

10

20

30

· Circular Linked List- A circular linked list is that in

which the last node contains the pointer to the first node

of the list.

Start

10

20

30

. Circular Doubly Linked List- A circular doubly

linked list is a mixture of a doubly linked list and a

circular linked list.

last

Start

10

20

30

added 100

Data Structure and Algorithm

12

YCT

Representation of Linked List-

· A data item

· An address of another node

We wrap both the data item and the next reference in a

struct as.

Syntax-

Struct node

{ Int data;

Struct node*next;

};

Linked list Applications

. Dynamic memory allocation.

· Implemented in stack and queue.

. In undo functionality of software.

· Hash tables, graphs.

STACKS

Stack is a non-primitive linear data structure.

It is an ordered list in which addition of new data item

and deletion of already existing data item is done from

only one End know as Top of Stack (TOS).

POP

PUSH

4

3

2

1

0

. It follows the LIFO pattern, which means the last

added element will be the first to be Removed from the

stack.

Stack has two operation- 1. PUSH Operation

2. POP Operation

PUSH Operation- Every PUSH operation TOP is

incremented by one.

TOP = TOP + 1

In case the Array is full no new Element is added. This

condition is called stack full or stack over flow

condition.

. The process of adding a new element of the TOP of

stack is called PUSH operation.

POP Operation- The process of Deleting an element

from the top of stack is called POP.

After Every POP operation the stack TOP is

decremented by one.

TOP = TOP-1

(This is called operation stack underflow).

POP operation

2

30

TOP=2

30 deleted

TOP = TOP-1

1

20

20

=2-1

0

10

10

=1

Stack Notation- There are three stack notation.

. Infix Notation- Where the operator is written in

between the operands.

Example-

A + B

+ operator

A, B operands

. Prefix Notation- In this operator is written before

the operands. It is also know as polish Notation.

Example- +AB

· Post fix Notation- In this operator is written After

the operands. It is also know as suffix Notation.

Example- AB+

. Convert the following Infix to prefix and postfix

for (A + B)* C/D+E ^ F/G

Prefix -

(A+B)* C/D + E^F/G

+ AB* C/D + E^ F/G

Let + AB = R1R1

* C/D + E^F/G

R1 * C/D+^ EF/G

Let ^ EF = R2

R1 * C/D+R2/G

R1 */CD + R2/G

Let /CD = R3

R1*R3 + R2/G

R1*R3 + /R2G

Let /R2G = R4

R1 *R3 + R4

*R1R3 + R4

Let *R1R3 = R5

R5 + R4

+R5R4

Now enter the value of R5, R4, R3, R2, R1

+*R1R3/R2G

+*+AB/CD/AEFG

Post fix-

(A+B)*C/D+E^F/G

AB+*C/D+E^F/G

Let AB+=R1

R1*C/D+EF^/G

Let EF ^ =R2

R1*C/D+R2/G

R1*CD/+R2/G

Let CD/ = R3

R1*R3+R2/G

R1*R3+R2G/

Let R2G/=R4

R1*R3+R4

R1R3*+R4

R5+R4+

Let R1R3*=R5

Data Structure and Algorithm

13

YCT

Now Enter the value of R5, R4,R3 R2,R1

R5R4+

R1R3*R4+

AB+CD*R2G/+

AB+CD* EF ^ G/+

QUEUE

· Queue is a Non primitive Linear data structure.

. The first added Element will be the first to be remove

from the queue that is the reason queue is called

(FIFO) type list.

· In queue Every insert operation Rear is incremented

by one. (R = R + 1) and every delete operation front

is increment by one.

F =- 1 & F=F+1

11

11012 3

Empty Queue

F=0

R= 0

F=0

R= 1

insert 10

insert 20

10

10

20

0

1

2

3

0

1

2

3

1

1

1

1

FR

F

R

BASIC OPERATION OF QUEUE

. Enqueue: Add an element to the end of the queue.

. Dequeue: Remove an element from the front of the

queue.

· Is Empty: Check if the queue is Empty.

· Is full: Check if the queue is full.

. Peek: Get the value of the front of the queue without

removing it.

Application of Queue-

· CPU scheduling, Disk scheduling

· Handling of interrupts in real time system

· Call center phone system use Queues to hold people

calling them in order.

. Unlike stack, Queue is also considered as the ordered

list of the data the ordered list of the data that has a

similar data type.

Priority Queue- Priority Queue is an Extension of

queue with following properties. An element with high

priority is dequeued before an element with low

priority.

Operations-

· Insert (item, priority): Inserts an item with given

priority time (O(logn)).

· Get highest priority ( ): Returns the highest priority

item. operation implemented by linear searching the

highest priority item in array. O(1).

· Delete highest priority (): Removes the highest

priority operation can be implemented by first

linearly searching an item, the removing the item by

moving all subsequent items one position back. (time

O(logn)).

. Heap is generally preferred for priority queue

implementation because heaps provide better

performance compared array or linked list.

Circular Queue- A circular queue is one in which the

insertion of a new element is done at very first location

of queue is full.

Q[4]

Q[0]

Q[3]

Q[1] F=R =- 1

Q[2]

· A circular queue overcome the problem of utilized

space in linear queues implemented as arrays.

BINARY TREE

· Binary tree is a finite set of data item which is either empty

of consists of a single item called root and two disjoint

binary tree called the left sub tree and right sub tree.

· In Binary tree, every node can have maximum of two

children which are known as left child and right child.

Left

A

- root

subtrees

B

C

Right

subtrees

D

E

F

Types of Binary Tree

Full Binary Tree- A Binary tree is full if every node

has 0 or 2 child.

A

B

C

D

E

Data Structure and Algorithm

14

YCT

Complete Binary Tree- A Binary tree is complete

Binary tree if all level are completely filled.

A

Level 0 2°=1

B

C

Level 1 21=2

D

E

F

G

Level 2 22=4

H

I

J

K

Level 3 23=8

Perfect Binary Tree- A Tree in which all internal

nodes has two children and all leaves are at the same

level in which all level has 2" children.

A

B

C

D

E

F

G

Traversal of Binary Tree

1. Preorder traversal (NLR) Node left Right

2. In order traversal (LNT) Left Node Right

3. Post order traversal (LRN) Left Right Node

Example-

A

B

O

Pre order - ABC

In order - BAC

Post order - BCA

B-Tree

B-Tree is a self-balancing tree. in most of the other self-

balancing searching ( like AVL and Red-Black tree). It

assumed that everything is in the main memory.

Time complexity of B-Tree

Algorithm

Time complexity

Search

O (logn)

Insert

O (logn)

Delete

O (logn)

Properties of B-Tree

. All nodes of the leaf must be on the same level.

. At least two root nodes are required.

· Each B-Tree node a maximum of m children.

· Each node in a B- tree includes at least m/2 children,

except the root and the leaf node.

· Maintains sorted data.

· Minimum children:

leaf = 0

root =2

Internal nodes =

m

2

· Every node has max. (m-1) keys

· Min key :- root node -> 1

m

all other =

1

−

2

GRAPH

Graph in data structure are non linear data structure

made up of a finite number of vertices and the edges

that connect them. Graph in data structure are used to

address real problem in which it represents the real

problem in which it represents the problem area as a

network like telephone networks, circuit network and

social network.

1

Edges

2

3

Nodes

4

5

This graph has a set of vertices

V = { 1, 2, 3, 4, 5} and a set of edges

E= {(1,2), (1,3), (2,3), (2,4), (2,5), (3,5), (4,5)}

Operation Of Graph In Data Structure

· Creating graphs

· Insert vertex

· Delete vertex

· Insert edge

· Delete edge

Graph Traversal Algorithm-

Graph traversal is a subset of tree traversal. There are

two techniques to implement a graph traversal

Algorithm.

1. Breadth - first Search or BFS

2. Depth - first - search or DFS

BFS- Two data structure for traversing the graph.

· Visited array (size of the graph)

· Queue data structure

· Using the FIFO concept.

· Until the queue is not empty and no vertex is left to

be visited.

1

2

3

4

5

6

BFS

123 4 56

Data Structure and Algorithm

15

YCT

DFS- The (DFS) algorithm traverses or explores data

structure such as trees and graphs. The DFS algorithm

begins at the root nodes and examines each branch as

for feasible before backtracking.

· Examine any two data structures for traversing the graph.

· Visited array (size of the graph)

· Stack data structure

· Using the FIFO principle.

· Stack data structure is not empty.

1

2

3

4

5

6

DFS

1 2 4 5 3 6

Application of graph

· The friend suggestion system on facebook is based

on graph theory.

· Graph transformation system manipulate graph in memory

using rules. Graph databases store and query graph-

structure data in a transaction-safe permanent manner.

Difference between stack and Queue

Stack

Queue

The collection of element

in last in first out (LIFO).

The collection of Element

in first in first out (FIFO)

Objects are inserted and

removed at the same end

called TOP of sack.

Objects are inserted and

removed from different ends

called Front and Rear end.

Insert operation is called

PUSH operation.

Insert operation is called

Enqueue operation.

Delete operation is called

POP operation.

Delete operation is called

Dequeue operation.

In stack There is no

wastage of memory space.

In Queue there is a wastage

of memory space.

Plate counter at marriage

Reception is an Example

of stack.

Students standing in a line

at fees counter is an

Example of Queue.

Non-Linear Data

structure

Linear Data structure

The non- linear data

structure are

comparatively difficult

The linear data structure are

comparatively

easier

to

implement

implement and

understand as compared

to linear data structure.

The data element

connect to each other

hierarchically.

The data element connect to

each other sequentially.

It is not easy to traverse

in multiple runs

You can traverse in a single

run.

It is memory friendly.

It is not very memory friendly.

Map, Graph, Tree

List, Array, Stack, Queue

Array

Linked list

Array is a collection

of Homogeneous

(same) data type.

Linked-list is a collection

of node (data & address)

Size of an Array is

fixed

Size of list is not fixed.

Memory is allocated

from stack.

Memory is allocated from

heap.

Work with static data

structure

Work with dynamic data

structure.

Array Element are

independent to each

other.

Linked list Element are

depend to each other.

Array take more time

(Insertion & Deletion)

Linked- list take less time

(Insertion & Deletion)

Tree

Graph

There is a unique node

called root in tree.

There is no unique node.

Tree is a collection of

node and edges.

Ex- T {node, Edges}

Graph is a collection of

vertices/nodes and edges.

Ex G = {V,E}

There will not be any

cycle/loops.

There can be loops/cycle.

In this Pre-order, In-

order and post order

Traversal.

In this BFS and DFS

traversal.

HEAP DATA STRUCTURE

A Heap is a special Tree-based structure in which the

tree is complete binary tree.

A

B

C

D

F

F

G

ABCDEFG

1 2 3 4 5 6 7

Data Structure and Algorithm

16

YCT

Formula-

if a Node is at index i

its left child is at = 2*i

its right child is at = 2*i+1

it parent is at =

[]

(This is true when your heap is starting from index 1.)

If you represent a binary tree in an array then they

should not be any empty locations or gaps in between

the elements bins from first element to last element in

between anywhere.

· Height of a complete binary tree will be minimum

only that is log n.

HEAP

Max Heap

Min Heap

50

10

30

20

30

20

15

10

8

16

35

40

32

25

Max Heap- A max heap is a complete binary tree in

which the value in each internal node is greater than or

equal to the values in the children of the node. Max

heap data structure is useful for sorting data using heap

sort.

50>30,20 30>15,10 20>8,16

Min Heap- A min heap is a heap where every single

parent node including the root, is less than or equal to

the value of its children nodes. The most important

property of a min heap is that the node with the

smallest, or minimum value, will always be the root

node.

10<30,20 30<35,40 20<32,25

Operations of Heap

. Heapify- a process of creating a heap from an array.

· Insertion- time complexity O (log N)

· Deletion - time complexity O (log N)

· Peek-To check or find the most prior element in the

heap.

HASHING

Hashing is a technique or process of mapping keys and

values into the hash table by using a hush function. It is

done for faster access to elements.

· Hashing storing and Retrieving data in O (1) time.

· Search key (24, 52, 91, 67, 48, 8 3)

· Hash Table

· Hash Function (K mod 10, K mod n, Mid, Square )

folding method.

K mod n = (n-1)

0

↓

91

1

24 mod 10 =4

52

2

52 mid 10= 2

83

3

91 mod 10=1

24

4

67 mod 10=7

5

48 mod 10=8

6

83 mod 10=3

67

7

48

8

9

Collision in Hashing

or

Collision Resolution Techniques

Chaining

(Open Hashing)

Open Addressing

(Closed Hashing)

Linear Quadratic Double Hashing

B-Tree & B+Tree

Data is stored in leaf

as well as internal

nodes

Data is stored only in leaf

nodes.

Leaf nodes not linked

together

Linked together like

Linked list.

Searching is slower

deletion complex

Searching is faster,

deletion easy (directly

from leaf node)

BPKey Dp Bp Key Dp Bp

...

BP

null

BP means Block pointer

DP means Data pointer

BPKey Bp Key Bp key BP

BP

Key Dp Key Dp ... Bp>

ALGORITHM

Analysis of Algorithms

· A well defined procedure to solve a specific problem

is called Algorithm.

· Data structure + Algorithm = Programming

· Algorithms Criteria

Input

Output

Finiteness

Definiteness

Effectiveness

Data Structure and Algorithm

17

YCT

Asymptotic Notations

Asymptotic notations are abstract notation for describe

the behavior of Algorithm and determine the rate of

growth of a function.

Exponentiol

O(2") quadratic O(n2)

Space requirement

Linear O(n)

Logarithmic O(log(n))

Constant O(1)

n

>

1. Big O Notation

· The Big O Notation defines an upper bound of an

algorithm. Therefore, it gives the worst-case

complexity of an algorithm.

· O (g(n)) = {f(n): there exist positive constants C

and n0 such that

O ≤ f (n) ≤ Cg(n) for all n > n0

Cg(n)

f(n)

f(n) = O(g(n))

no

n

2. Omega (22) Notation:

Omega notation represents the lower bound of the

running time of an algorithm. thus, it provides the best

case complexity of an algorithm.

f(n)

Cg(n)

Cg(n)≤f(n),≥no

C>0, no≥1

f(n) =£2(g(n))

no

3. Theta (0) Notation:

Theta notation encloses the function from above and

below. It is used for analyzing the average case

complexity of an algorithm.

Cjg(n)≤f(n)≤C2g(n)

C,C2 ≥0,n ≥ no, no ≥1

C2g(n)

f(n)

C1g(n)

no

n

f(n) =0(g(n))

Worst Case Analysis-

The case that causes a

maximum number of operation to be executed.

Best Case Analysis- The case that causes a minimum

number of operations to be executed .

Average Case Analysis- We take all possible inputs

and calculate the computing time for all of the inputs,

sum all calculate values and divide the sum by the total

number of inputs.

Sorting

Comparison based

·Bubble sort

Counting based

·Selection sort

·Bucket

or

·Insertion sort

·Quick sort

·Redix sort

·Marge sort

·Heap sort

BUBBLE SORT

Algorithm-

1. Start with an array of unsorted numbers

2. Defines a function called 'bubblesort" that takes in

the array and the length of the array as parameters.

3. In the function, create a variable called "sorted" that

is set to false.

4. Create a for loop that iterates through the array

starting at index 0 and ending at the length of the

array -1

5. Within the for loop, compare the current element

with the next element in the array.

6. If the current element is greater than the next elements,

swap their positions and set "sorted" to true.

7. After the for loop, check if "sorted" is true.

8. If "sorted" is true, call the "bubblesort" function

again with the same array and length as parameters.

9. If "sorted" is false, the array is now sorted and the

function will return the sorted array.

10. Call the "bubbleSort" function with the initial

unsorted array and its length as parameters to befin

the sorting process.

· It is stable sorting techniques.

· Recursive relation in Bubble sort.

T(n) =T (n-1)+n

Data Structure and Algorithm

18

YCT

· It is In place sorting

· Time complexity = 0 (n2)

Space complexity = 1 + n

= 0 (n)

Best case = 0 (n)

Worst case = 0 (n2)

Average case = 0 (n2)

SELECTION SORT

Algorithm-

1. Initialize minimum value(min_idx) to location 0.

2. Traverse the array to find the minimum element in

the array.

3. While traversing if any element smaller than min_idx

is found then swap both the values.

4. Then, increment min_idx to point to the next

element.

5. Repeat until the array is sorted.

· Recursive relation

T(n) = T (n-1)+(n-1)

· Max swap = (n-1) Complexity 0(n)

· Min swap = 0

Time complexity 0(n2)

L

Space complexity0(1)

·Iterative

Best case

Worst case

7

0(n2)

Average case

· It is unstable sorting

INSERTION SORT

Algorithm- To sort an array of size N in ascending

order:

1. Iterate from arr[1] to arr[N] over the array.

2. Compare the current element (key) to its predecessor.

3. If the key element is smaller than its predecessor,

compare it to the elements before. Move the greater

elements before. Move the greater elements one

position up to make space for the swapped element.

· Number of comparison- max =

n(n-1)

2

min = n-1

· Best case = 0(n)

Worst case & Average case = 0(n2)

· Insertion sort = Position +Shifting

. It is highly affected due to order of input.

· Recursive time T (n) = T (n-1)+n

= 0 (n2)

space =0(n)

· Stable sorting

QUICK SORT

. It is Divide and conquer technique.

· It is unstable sorting

· Best case = 0 (n logn) = Average case

Worst case = 0 (n2)

· Recursive

T(n) =2T(n/2)+n

Using master theorem

0 (n logn)

n(n-1)

· Number of comparison =

2

Merge Sort

Algorithm-

MergeSort(arr[],l,r)

Ifr>1

1. Find the middle point to divide the array into two

halves.

middle m=1+ (r-1)/2

2. Call mergeSort for first half:

Call mergeSort(arr, l, m)

3. Call mergeSort for second half:

Call mergeSort(arr, m + 1, r)

Call merge(arr, l, m, r)

4. Merge the two halves sorted in steps 2 and 3:

· It is stable sorting.

· It is pure divide & conquer.

· Recursive-

T(n)=2T(n/2)+n

· Complexity-

Best case = Average case = Worst case =0(n logn)

RADIX SORT

. It is counting Based sorting.

. It is outplace sorting

· Q (n k)

· If n>>K=Q(n)

· If n=K=Q(n2)

1

Time complexity

· Q (n*R) space complexity.

RECURSION

A recurrence is an equation or inequality that describes a

function in terms of its values on smaller inputs. To solve a

Recurrence Relation means to obtain a function defined on

the natural numbers that satisfy the recurrence.

. There are four methods for solving Recurrence

(i) Substitution method (iii) Iteration method

(ii) Recursion tree

(vi) Master method

Data Structure and Algorithm

19

YCT

(i) Substitution method-

T(n) =

1

n = 0

T(n-1)+1 n>of

T(n)=T(n-1)+1

:T(n)=T(n-1)+1 ...... (i)

1

.: T(n-1)= T(n-2)+1 ....... (ii)]

Substitution T(n-1)

T(n)=[T(n-2)+1]+1 {Fromequ*(ii)}

T(n) =T(n-2)+2

T(n) =T(n-3)+3

⋮

:Continue for k time

⋮

T(n)=T(n-k)+k

Assume n-k = 0

.. n = k

T(n)=T(n-n)+n

T(n) = T(0)+n

T(n)=1+n

.. 0(n)

(ii) Recursion Tree -

T(n)=

1

T(n-1)+n

n = 0)

n> 0]

T(n)->n

n

T(n-1)->n-1

n-1

T(n-2)->n-2

n-2

T(n-3)->n-3

T(2)->2

2

T(1)->1

T(0)->0

0+1+2

n-1+n=

1

n(n+1)

2

T(n) =

n(n+1)

2

0(n2)

(iii) Iteration Method-

T(n)=

1

n = 0

T(n-1)+n n>0)

of

T(n)=T(n-1)+n

{ .: T(n)=T(n-1)+2

T(n)=[T(n-1)+n-1]+n ..... (i) {T(n-1)=T(n-2)+n-1

T(n)=T(n-2)+n-1]+n ...... (ii)

T(n)=T(n-3)+(n-2)+(n-1)+n ...... (iii)

:

: Continue of k time

:

T(n)=T(n-k)+(n-(k-1))+(n-(k-2)+ ...... +(n-1)+n

Assume n-k=0

.. n=k

T(n)=T(0)+1+2+3+ ..... n-1+n

n(n+1)

=1+

2

2

n(n+1)

=

θ

2

(iv) Master theorem for Decreasing function

· T(n) =2T(n-1)+1

By solving recursion tree

1+2+23+ ..... +2K = 2k+1 (This is GP series)

= 0(21)

T(n)= aT(n-b)+f(n)

a>0, b>0 and f(n)=O(nk) where K≥0

Case

· If a<1

· If a=1

· If a>n

O(nk)

O(nK+1)

O(nKan/b)

O(f(n))

O(n*f(n))

O(f(n)a™/b)

. Master Theorem for Dividing function

(i) logia T(n)=a T(n/b)+f(n)

a≥1

(ii) b> f(n)=0(nklog'n)

Case1: if log,ª>k them 0(nlog;ª)

Case2: if log,a=k

If P>-1 0(nklogP+In)

If P =- 1 0(nklog log n)

If P <- 1 0(nk)

Case3: If loga<K_IfP≥00(nklogPn)

If P <0 O(nk)

T(n) =2T(n/2)+1

a =2, b=2, f(n)=O(1)=0(nºlogºn)

log22=1>K=0

Case1: 0(n1)

Recurrence Relation

T(n)=T(n-1)+1 O(n)

T(n)=T(n-1)+1

O(n2)

T(n)=T(n-1)+logn O(n logn)

T(n)=T(n-1)+n2 O(n3)

T(n)=T(n-2)+1

=O(n)

2

T(n)=T(n-100)+n O(n2)

Data Structure and Algorithm

20

YCT

HUFFMAN CODING

· Huffman Coding is a famous greedy Algorithm.

. It is used for the lossless compression of data.

· It used variable length in encoding.

. It assigns variable length code to all the Characters.

Prefix rule-

· Huffman coding implements a rule know as a prefix

coding

· This is to prevent the ambiguities while decoding

. It ensures that the code assigned to any character is

not a prefix of the code assigned to any other

character.

· There are two major steps in Huffman Coding.

1. Building a Huffman tree from the input characters

2. Assigning code to the characters by traversing the

Human tree.

Huffman Tree-

Step.1 Create a leaf node for each Character of the test.

. Leaf node of a character contains the Occurring

frequency of the character.

Step.2 Arrange all the nodes in increasing order of their

frequency value.

· Considering the first two nodes having considering

the first two nodes having minimum frequency.

· The frequency of this new node is the sum of

frequency of those two nodes.

Step.3 Make the first node as a left child and the other

node as right child of the newly created node.

Step.4 Keep repeating step 2 and step 3 until all the

nodes from a single tree.

Time complexity-

· Extract Min() is called 2*(n-1) times if there are n nodes.

· As extract Min() cells min Heapify, it take O (logn) time.

Thus, Overall time complexity of Huffman coding

become O(n logn).

Example- ABBCDBCCDAABBEEEBEAB

0

20

1

8

12

0

1

0

1

4

4

5

7

E

A

0

1

B

2

3

D

C

Char

frequency

count

A

4

01

B

7

11

C

3

101

D

3

101

E

4

00

KNAPSACK PROBLEM

· A Knapsack (kind of shoulder bag) with limited

weight capacity.

· Few items each having some weight and value.

· There are two knapsack problem.

1. Fractional knapsack problem.

2. 0/1 Knapsack problem.

Fraction knapsack problem

· As the name suggest, items are divisible here.

· For each item, compute its value/ weight.

· Arrange all the items in decreasing order of their

value/weight ratio.

Put as many items as you can into the knapsack.

Time Complexity-

· If the items are already arranged in the required order

then while loop takes O (n) time.

· Average time complexity of Quick sort is O (n logn)

Example-

Object : O 1 2 3 4 5 6 7

Profits : P 10 5 15 7 6 18 3

Weights: W 2 3 5 7 1 4 1

P

51331645 3

W

x (1 2/3 1 0 1 1 1)

X1 X2 X3 X4 X5 X6 X7

n = 7, M=15

2

3

Ex; Wi=1×2+=x3+1×5+0×7+1x4+1x1

=2+2+5+0+1+4+1=15

2

3

Ex;Pi=1×10+=x5+1×15+1x6+1x18+1x3

=54.6

Constraint

Ex;W,sm

Objective

max Ex; P.

OPTIMAL MERGE PATTERN

Given n number of sorted files, the task is to find the

minimum computations done to reach the optimal

merge pattern, when two or more sorted files are to be

merged altogether to form a single file, the minimum

computation are done to reach this file are known as

Optimal merge pattern.

Data Structure and Algorithm

21

YCT

Example- List- X1, X2, X3, X4, X5

Size- 20 30 10 5 30

95

1

1

35

60

2

2

2

2

15

20

30

30

3

3

5

10

Total cost of merging =Ed; * Xi

di = distance of each node

The size of each node = Xi

So,

Total number of merging

=3×5+3×10+2×20+2×30+2×30=205

DYNAMIC PROGRAMMING

· It is used to solve optimization solution .

· Breaks down the complex problem into simpler sub-

problems.

· Find optimal solution to these sub-problems.

· Store the results of sub-problems. (memorization)

· Reuse then so that same sub-problem is not

calculated more than once.

. Finally calculate the result of complex problem.

· Overlapping sub problems & Optimal Substructure.

Type of Dynamic Programming-

· Multistage Graph

· Floyd Warshall

· Bellman Ford Algorithm

· 0/1 Knapsack

· Optimal Binary Tree

· Reliability Design

· Longest common subsequence (LCS)

· Matrix chain Multiplication

MULTISTAGE GRAPH

Multistage graph is a data structure that is used to

represent a graph in which the vertices are divided into

a number of levels. The edges of the graph are also

divided into a number of levers. The multistage graph is

also called a Hierarchical graph.

4

2

5

Stage

1

20

S

9

8

2

5

15

N

1

3

6

8

D = Destination

7

17

2

Sı

4

>

7

2

S4

S2

S3

KVS

1+1

Fun (Si, Vi)= min

fun(S[+],K)+C(Vj,K)}

C(Vi,D)ifS; = Sf -1

1

Where, S=stage, V = Vertex, F= final stage

F (1,1)

24

21

11

fun (2,2)+1

24

min(24, 23)

23

fun (2,3)+2+19

29

min(29, 20, 19)

20

fun (2,4)+7

4

19

f (3,5)+4

f (3,6)+8

f(3,5)+9

f(3,6)+5

f(3,7)+17

£(3,7)+2

V

V

20

V

V

V

15

20

15

V

2

2

Minimum cost = 11

Path

1

4

7

8

7

2

2

Time Complexity = O (V + E)

(E is edge)

FLOYD-WARSHALL

The strategy adopted by the Floyd-Warshall algorithm

is Dynamic programming. The running time of the

Floyd-Warshall algorithm is determined by the triply

nested for loops of lines 3-6. Each execution of line 6

takes O(1) time. The algorithm thus runs in time 0 (n3).

1

8

2

1

3

4

1

3

€

2

9

3

0

00

2

A

A

1

0 8 00 1

4

1

2 Dº

2

3

00

1

0

00

V

4

Example-

1

1

0

8

0

2

00

1

0

9

4

1

{1,2}D2 =2

1

3

4

0

12

9

1

00

5

3

4

10

{1,2,3}D3 =2 5 0 1 6D4 = 2 5 0 1 6

3 4 12

47 2

0

7

2

9

5

0

AK-1[i, j]

E

Ak-][i, k]+ AK-1[k, j]

5

0

Ak[i, j] = min

0

3

1

Time Complexity = O(n3)

Space Complexity = O(n3)

00

4

4 00 2 9 0

1

2

3

8

0

4

{1}D1 =2

00

4

12

00

5

00

0

1 2 3 4

9

8

1

2

00

4

3

4 00 2 3 0

1

2

3

1

3

4

0

4

7

1

0

4

1

Data Structure and Algorithm

22

YCT

Bellman Ford Algorithm

&

1

de

$ 0

0

-1

6

B

E

0

-2

3

A

C

3

4

3

5

-2

D

F

de

5

-1

3

$

go on relaxing all the edges(n-1) times

n = number of verites

if([u]+c(u, v) < d[v])

d[v]=d[u]+c(u,v)

Edges-

(A, B), (A, C), (A, D), (B, E), (C, E), (D, C), (D,F), (E,

F), (C, B)

We are done algorithm 5 time.

A-0, B-1, C-3, D-5, E-0, F-3

Single Source Shortest Path

Time Complexity = O(E(|v|-1)

= O(E.V)

= O(n2)

0/1 Knapsack Problem

. Consider- Knapsack weight capacity = w

Number of items each having some weight

and value = n

· Problem solving steps-

(i) Draw a table say 'T' with (n+1) number or row and

(w+1) number of column.

(ii) Fill all the boxes of 0th row and 0th column with

zeroes as

(iii) Start filling the table row wise top to bottom from

left to right.

Using formula

V[i, w]=max {v(i-1, w), v[i-1, w-w[i]+P[i]}

Here V [i, w]= maximum value of the selected items

if we can take items 1 to i and weight restrictions of w.

. This step leads to completely filling the table.

. Then value of the last box represents the maximum

possible value that can be put into the knapsack.

· The knapsack to obtain that maximum profit.

. Consider the last column of the table.

· Start scanning the entries from bottom to top.

· On encountering an entry whose value is not same as

the value stored in the entry immediately about it,

mark the row label of that entry.

. After all the entries are scanned the marked labels

represent the items that must be put into the

knapsack.

Example-

Value of V

O/1 Knapsack problem

m =8 P= {1,2,5,6}

n =4 w = {2,3,4,5}

V[4, 5] = max[V[3, 5], {V[3, 5-5]+6]}

= max[5,0]=5

V[4, 6] = max[V[3, 6], {V[3,6-5]+6]}

= max[6, 6] =6

V[4, 7] = max[V[3, 7], {V[3,2]+6]}

= max[7, 7] =7

V[4, 8] = max[V[3, 8], {V[3, 3]+6]}

= max[7,8]=8

012 3 4 5 6 7 8

000000000

W.

0

i

1

21001111 1 1 1

2

2001223333

5

3

4

3

0

0

1

2

5

5

6

7

7

6

54001256678

Solution

JX1 X2 X3 X4\_

10 1 0 1} {2,6}

Optimal Binary Search Tree

A set of integers are given in the sorted order and

another array to frequency count. Our task is to create a

binary search tree with those data to find the maximum

cost for all searches.

Example-

1

2

3

4

Key

10

20

30

40

frequency

4

2

6

3

Formula-

[i, j]= min{C[i, k-1]+C[k, j]}+w(i, j) i<k≤j

j

i

0

1

2

3

4

0

0

4

8

203

263

1

0

2

103

163

2

0

6

123

3

0

3

4

0

Data Structure and Algorithm

23

YCT

C[0,1] = 4

1=j-i=0

C[1,2]=2

1=j-i=1

C[2,3]=6

C[3,4]=3

So,

1=j-i=2

C[0,2]=8, C[1,3]=103,C[2,4]=123

Using formula

w(0,4)=>f(i)

i=1

4

1=j-i=3

1=j-i=4

C[0, 4] = 263

Matrix Chain Multiplication

C[0, 3] = 203, C[1, 4] = 163

A1

A2

A3

A2×5

B5×10

C10×3

P0×P1

P1XP2

P2×P3

ABC

A(BC)

(AB)C

Left side

(BC)5x3=B5×10 C10x3=5×10×3=150

M [2, 3] = M [2, 2] + M [3,3]+5×10×3=150

(ABC)2×3=A2x5(BC)=2×5×3=30

M [1, 3] = M [1, 1] + M [2, 3] + P0×P1×P3

= 0+150+30 =180

Right side

(AB)2×10= A2x5 .B5x10=2×5x10=100

M [1, 2] = M [1, 1] + M [2,2]+2×5x10=100

(ABC)2×3=(AB)2×10C=2×10×3=60

M [1, 2] = M [1, 2] + M [3, 3] + P0×P1×P3 = 160

Formula using

M (i, j) = min {M [i, k] + M [k + 1, j] + Pi-1 Pk Pj

i≤k<j

1

Example- A2x1 B1x3 C3x4 D4x5

M [1, 2] = M [1, 1] + M [2, 2]+2×1×3=6

M [2, 3] =M [2, 2] + M [3, 3] + 1×3×4 = 12

M [3, 4]=M [3,3]+M [4,4]+3×4×5=60

So by formula

1

2

3

4

123 4

1

0

6

20

42

1

1

1

1

2

0

12

32

2

2

3

3

0

60

3

3

4

0

4

A (B(CD))

Time Complexity

= O (n)

= O (n3 )

DIVIDE AND CONQUER

· Divide: In this step, we will break the problem into

sub-parts by recursion.

. Conquer: We will solve the smaller subparts

recursively. It the sub problem is small, then we can

solve it instantly.

· Application of divide and conquer Algorithm

(i) Binary search

(ii) Merge sort

(iii) Quick sort

(iv) Strassen's Matrix Multiplication.

(v) Karatsuba Algorithm

(vi) Stassen's Algorithm.

GREEDY ALGORITHM

· A greedy algorithm is a problem solving approach

like subtract and conquer and dynamic programming,

which is used for solving optimality problem(one

solution), out of all feasible solution.

· Minimum spanning tree

· Single source shortest path

· Huffman coding

· Optimal merge pattern

KRUSKAL'S ALGORITHM

· Kruskal's Algorithm is a famous greedy Algorithm.

. It is used for finding the Minimum spanning tree

(MST) of a given graph.

· The given graph must be weighted, connected and

undirected.

· Simple draw all the vertices on the paper.

· Connect these vertices using edges with minimum

weights such that no cycle gets formed.

Example-

A

2

4

D

7

A

4

D

C

5

E

1

2

C

5

E

6

B

3

6

F

8

B

F

Given graph

Minimum

Spanning true

Weight of the MST

= Sum of all edge weights

= 1+2+4+5+6=18 units

Worst case time complexity

= O(E logV) or O(E logE)

SINGLE SOURCE SHORTEST PATH

· Dijkstra Algorithm is a very famous greedy

Algorithm.

. It is used for solving the single source shortest path

problem.

Data Structure and Algorithm

24

YCT

· Dijkstra algorithm work only for connected graphs.

· Dijkstra algorithm work only for those graphs that do

not contain any negative weight edge.

· The actual Dijkstra algorithm does not output the

shortest paths

· Dijkstra algorithm works for directed as well as

undirected graphs.

Dijkstra Algorithm Steps-

Step-01 In the first step. two set are defined .

· One set contains all those vertices which have been

included in the shortest path tree.

· In the beginning, this set is empty.

· In the beginning, this set contains all the vertices of

the given graph.

Step-02 Two variables are defined as

· IT[v] which denotes the predecessor of vertex 'v)

· d [v] which denotes the shortest path estimate of

vertex 'V' from the source vertex.

Initially, the value of these variables in set as-

· The value of variable 'II ' for each vertex is set to

NIL. i.e. IT[v] = NIL.

· The value of variable 'd ' for source vertex is set to 0

i.e. d[s] = 0

The value of variable 'd 'for remaining vertices is set

to oo i.e. d[v]oo

Step-03

· Among unprocessed vertices, a vertex with minimum

value of variable d is chosen.

. Its outgoing edges are relaxed.

. After relaxing the edges for that vertex, the sets

Created in step-01 are updated.

Edge relaxation-

edge(a, b)-

a

d[a]

S

W

b

d[b]

Here, d[a] and d[b] denotes the shortest path estimate

for vertices a and b respectively from the source vertex

'S'

Now

If d[a]+w<d[b]

then d[b]= d[a]+w and IT[b]=a

this is called as edge relaxation.

Advantages-

· It is used in google map

. It is employed to identify the shortest path.

. It is very popular in the Geographical Maps.

· The telephone network makes use of it.

Application-

· To determine the quickest route.

· In application for social networking

· Within a phone network.

Time complexity is O(E log V)

Space complexity is O(V)

BACK TRACKING

Back tracking uses brute force approach to solve

problem. Brute force approach say that for any given

problem generate all possible solution and pich up

decided solution . Back tracking uses Depth- first-

search to generate state space tree.

Brute force Approach-

Example-

Let B1 B2 G1 {B=Boy

Seating arrangement

{G=Girl

State space tree - n=3

B1

G,

B2

B2

B1

G1

B2

B,

G,

Bounding

function

G1

B2

B1

N-Queens Problem

The N Queen is the problem of placing N chess queens

on an N×N Chessboard so that no two queens attack

each other.

Formula-

Maximum number of nodes

i

=1+

i=0

n

n

(N- j)

j=0

· Time complexity: O(N!) which represent the

maximum number of queens placed.

· Space complexity: O(N2) for the board.

Graph Coloring

1

2

m =3

{Red, Green, Blue}

4

3

. How many number of nodes = C"+1

Data Structure and Algorithm

25

YCT

· Coloring of graph constitutes coloring vertices edges

of the graph.

· Coloring all the vertices of a graph is the property

that no two adjacent vertices have same color.

[Always try to color with minimum colors]

HAMILTONIAN CYCLE

The Hamiltonian cycle is the cycle. graph which visits

all the vertices in graph exactly once and terminates at

the staring node. It may not include all the edges.

Step

· In any path, vertex i and (i+1) must be adjacent.

· 1st and (n-1)th vertex must be adjacent.

· Vertex i must not appear in the first (i-1) vertices of

any path.

· With the adjacency matrix representation of the

graph, the adjacency of two vertices can be verified

in constant time.

· Maximum number of nodes

=

(n-1)!

2

· Complexity

T(n) = O(n2)

Traveling Salesman Problem using Dynamic

Programming

1

2

4

1

10

3

15

9

10

0

12

9

20

0

10+25=35

15+25=40

1

20+23=43

9+20=29

8+15=23

10+15=25

9+18=27

12+13=25

2

3

4

8+5=13

9+6=15

3

4

2

4

2

3

12+8

10+8

9+6

13+5

=20

=18

=15

=18

4

3

4

2

3

2

6

8

5

6

5

[4,1] [3,2] [4,1] [2,1] [3,1][2,1]

Minimum Cost = 35

Using formula

g(i, S)=min{Cik +g(k,S-{k}}

k <- S

So

g(1{2,3,4})= min {C|g(k{2,3,4)}-{k}}

k <- {2,3,4}

g=Cost

g(2, ¢)=5, g(3, $)=6

[¢ is null value]

g(4, ¢)=8, g(2,{3})=15

g=(2, {4})=8, g(3,{3})=5

g(3, {4})=5, g(4, {2})=5

g=(4,{3})=6, g(4, {2})=25

g=(4,{2,3})=23

Last values

g =(1,{2,3,4} = min{C12+g(2,{3,4}, C13 +g(3, {2,4} }

C14 + g(4, {2,3})}

= min{10+25,15+25,20+ 23}

= min {35, 40, 43}

g(1, {2,3,4})=35

BRANCH AND BOUND

· An algorithm design technique, primarily for solving

hard optimization problem.

· Guarantees that the optimal solution will be found

. Does not necessarily guarantee worst case

polynomial time complexity.

· But tries to ensure faster time on most instances

Basic Idea.

· Model the entire solution space as a tree.

Search for a solution in the tree systematically,

eliminating parts of the tree from the search intelligently.

· Important technique for solving many problems for

which efficient algorithms (worst case polynomial

time) are not know.

Optimization problems-

· Set of input variables I

· Set of output variables O

· Values of the output variables define the solution space.

· Set of constrains cover the variables.

Data Structure and Algorithm

26

YCT

2

3

4

5

6

8

0

0

13

8

13+18

1

2

4

€

3

8

· Set of feasible solutions.

· Set of solutions that satisfy all the constraints.

· Objective function F:S ->R (also called cast function)

· Gives a value F(s) for each solution SE S.

Optimal solution-

· A Solution SE S for which F(S) is maximum among

all SES(for a maximization problem) or

minimum(for a minimization problem).

Job searching-

Using problem solving

1. FIFO - Queue

2. LIFO - Stack

3. Least - Cost

· Job sequencing with deadline

Upper = sum of all penalties except that included

solution

Cost= sum of penalties till that last job considered

job 1 2 3 4

Penalty

5 10 6 3

deadline

1 32 1

time

1 2 1 1

U = Pi

ies

C= > Pi

Upper = 19 1,4 g

iESK

U=8

u=10+6+3+19

1

J2

J4

U=5+6+3

2

=14

3

4

C=0

5

C=5+10+6=21

C=5+10=15

J2

J3

J4

U=9

J3

J4

6

7

8

C=0

9

10

C=5+6=11

J3

J4

C=10 C=16

C=5

U=5+3=8

Solution-

Ĉ=5

u=8

J2, J3=16

J1J4=8

LOWER BOUND THEORY

L(n) to be the running time of an algorithm A, then g(n)

is the lower bound of the algorithm A. It there are two

constants C and N such that

L(n)>=C*g(n), for n>n

Techniques-

· Comparisons tree

. Oracle and adversary argument

· State space method

Non -Deterministic Algorithm-

Outcome of Non deterministic Algorithm will be

restricted to specific set of possibilities.

(1) Choice (S): Arbitrarily choose one element from set S.

(2) Failure (): Signal an unsuccessful solution.

(3) Success (): Signal an successful solution.

Example- Searching x on A [1:n], n≥1 on success

returns of it A[j]=x or returns 0 otherwise.

(1) j=Choice (1,n);

(2) If (A [j] == x) then {write (j); success}

(3) Write (0); Failure();

NP-Hard and NP-Complete

Polynomial time

Exponential time

linear search-n

0/1 Knapsack- 2"

Binary search-logn

Traveling SP-2"

Insertion sort-n2

Sum of subsets-2"

Marge sort-n logn

Graph coloring cycle-2"

Matrix mullipliction-n3

Hamiltonian cycle-2"

NP-Hard- If every problem in NP can be polynomial

time reducible to a problem 'A' is called NP Hard. If'A'

Could be solved in polynomial time then every problem

in NP is 'P'.

NP- complete: A problem, if it is in NP and NP-Hard,

then it is said to be.

NP-Complete problem.

NP

NP

Hard

NP-Complete

Note-If NP-Hard or NP-Complete is solved in

polynomial time, then NP=P

· If NP-Hard or NP- Complete problem is proven to be

not solvable in polynomial time, then P != NP

But, till date it is not possible to find out whether

NP= P or not.

· Status of NP is still unknown.

Data Structure and Algorithm

27

YCT

03.

DISCRETE MATHEMATICS

LOGIC

Propositional Logic- A declarative sentence to

why we can assign one and only one truth value.

i,e. True or False

Example-

. London is a city. True

· 2×3 = 5 .. False

Propositional

· x+2 = 5

}

Not

·15th August is independence day | Propositional

Logical Connective or Operators

The following symbols are used to represent the

logical connectives.

AND

^ (Conjunction)

Primary

OR

v (Disjunction)

NOT

- (NOT)

EX-OR

⊕

Secondary

NAND

↑

NOR

↓

If ..... then

-> (Implication)

If and only if

«> (Biconditional)

Truth Table of primary operator AND (A) OR (v) -

(not)

A

B

AAB

AvB

-A

-B

F

F

F

F

T

T

F

T

F

T

T

F

T

F

F

T

F

T

T

T

T

T

F

F

Properties

Commutative Law

pvq=qvp

paq=qAp

Associative Law

pv(qvr)=(pvq)vr

pa(qar)=(paq)Ar

Distributive Law

pv(qar)=(pvq)^(pvr)

p^(qvr)=(paq)v(par)

Identity Law

PvF =P

PAT=P

Compliment

pvP'=T

PAP'=F

Example-

(i) P + Q+P'=P+P'+Q=1+Q=1

(ii) P v (P' v Q) = (Pv P') v Q

= 1 + Q=1 Tautology

Derived Operators & Properties

(1, 4, 4, ->, <>)

Truth Table

P Q PIQ PVQ

POQ

P-> Q

P<>Q

F

F

T

T

F

T

T

F

T

T

F

T

T

F

T

F

T

F

T

F

F

T

T

F

F

F

T

T

Example-P->Q = Q'-> P+Q=Q+P this is true.

Tautology- An atomic proposition cannot be

tautology. So a compound proposition which is

always true is called as 'tautology.'

Example- Pv (_P)

Contradiction- A compound proposition which is

always false is called a contradiction.

Example- PA(_P) =F

Contigency- A compound position which is neither

a tautology nor a contradiction is called contigency.

Example- P -> q, Pvq, PAq, P+>q

Satisfiable function of satisfiability-

. A compound proposition which is not a

contradiction is called satisfiable function.

· A satisfiable function can be a tautology also.

Arguments

The argument is a set of statements or propositions

which contains premises and conclusion. The end of

last statement is called a conclusion and the rest

statements are called premises.

An argument is denoted by the following expression

as follows.

P1, P2 ........ Pn $ Q

Where P1, P2 ........ Pn is the premises and Q is the

conclusion.

Example-

. Every mother is a woman.

· All women is caring

. Therefore, every mother is caring.

Rules of Inferences

In logical reasoning (an argument or proof), a

certain number of propositions are assumed to be

true and based on that assumption some other

propositions are derived. There are some important

reasoning or rules of inferences.

Discrete Mathematics

28

YCT

Sr.

No.

Rules

of

Inference

Implicant form

1.

Addition

P

P -> (PvQ)

:. PvQ

2.

Conjunction P

PAQ->PAQ

Q

:. PAQ

3.

Simplification

PAQ

(PAQ)->Q

.. Q

4.

Modus ponens

P

(PA (P->Q))->Q

P->Q

.. Q

5.

Modus tollens

-Q

(-QA(P->Q))->-P

P->Q

.. - P

6.

Disjunctive

syllogism - P

PvQ

.. Q

(- PA (PVQ))->Q

7.

Hypothetical

syllogism P ->

Q

((P->Q)^(Q->R))->(P->R

)

Q->R

:. P=>R

8.

Constructive

Dilemma

(P->Q)^(R->S

)

(P->Q)^(R->S)A(PVR)->(

QvS)

PVR

:. QvS

9.

Destructive

Dilemma

(P->Q)^(R->S

)

-QV-S

:. - PV-R

(P->Q)^(R->S)A(-QV-S

)-> (- Pv-R)

Example- If you study hard you will pass the exam. I

studied hard. Therefore I will pass the exam, can

be translated as

P : I study hard

Q : I will pass the exam (P -> Q, P) - Q

This argument is valid if the well-formed

formulas (P -> Q) A (P) -> Q is a tautology. It

can be verified that, it is indeed a tautology &

therefore the given argument is valid.

Rules of inference for quantified

propositions

1. (US) Universal instantiation -> (specification)

VxP(x)

valid for any element

.. P(a)

'a' in the universe of discourse.

2. (ES) Existential specification (Instantiation)

→

3xP(x)

.. P(c)

valid for some elements 'c' in the

universe of discourse.

3. (UG) Universal Generalization -> If P(a) is

true for all elements in the universe of discourse

P(a)

.. VxP(x)

4. (ES) Existential Generalization -> If P(c) is

valid true for some element in universe of

discourse.

P(c)

.. 3xP(x)

Equivalences ->

(1) Vx{P(x)^Q(x)}{x(P(x))}{VxQ(x)}

If we replace Vx with Ex, the above statement

does not hold good.

i.x 3x{P(x) \Q(x)} }xP(x)=xP(x)

It is a tautological implication

Ex {P(x)\Q(x)} => {xP(x)}{xQ(x)}

Properties of quantifiers-

(1) VxP(x)->=xP(x)

(2) VxVy P(x, y) <> Vy VxP(x, y)

(3) 3 x 3 yP(x, y) <> By 3x P(x, y)

(4) 3 xVy P(x, y) -> Vy Ex P(x, y)

KAXA

VyVx

ExVy

EyVx

Vy3x

Vx3y

ŻyƷx

3x3y

Graphical Representation of Relation between

Sentences Involving two quantifiers.

TRANSLATIONS

V=> "For all", "Every", "Any", "All", (->) =>

"Their exist", "Same", "a", "an" (^)

Example-

Birds can fly

Assumption

B(x) : x is bird

F(x) : x can fly

Domain : Univers

Discrete Mathematics

29

YCT

Solution:

Vx(B(x)->F(x))

Example-

Some birds can fly

Assumption

B(x) : x is Birds

F(x) : x can fly

Domain : Universe

Solution:

Ex(b(x) AF(x))

Combinatorics

Fundamental Principle of counting

· Sum Rule- Let an event occur thru process-1 in

'm'-way and thru process-2 in 'n'-ways 'non-over

lapping' then total number of ways of occurrences

of event will be 'm + n'.

. Product Rule -> If event &1 can occur thru m-

ways and another independent event E2 can occur

thru n-way then total number of ways of occurrence

of E1 and E2 will be 'm.n'.

Note- It between two processes order is possible then it

will be considered by itself in multiplication.

· Bijection Rule- Number of favorable way of

occurrence of an event

= total number of ways unfavorable - number of ways

Permutations

> An arrangement of (or) ordered selection of

objects is called a permutation.

The formula of counting this is

" P =

n!

(n-r)!

=n×(n-1)×(n-1)×(n-2) ..... (n-r+1)

Combinations- Let n, r integers. If n ≥ r for the

set of n elements a sub set of r element is called a

"combination".

Formula-

"C =

r!(n-r)!

n!

Nine categories of problem

(i) Permutation without repetition

np = n!

(n-r)!

(ii) Permutation limited repetition

n!

nl !* n2 !*

(iii) Permutation unlimited repetition

n'

(iv) combination without repetition

"CI =

n!

r!(n-r)!

(v) Combination limited repetition

Generating function

(vi) Combination unlimited repetition

n-1+'C

(vii) Distribution

(viii) Principle of Inclusion Exclusion

(ix) Pigeon Hole Principle

Recurrence Relations- Let a0,a1,a2 ... an be a

sequence of real number.

an = f(an-1, an-2, ..... )

Arithmetic sequence

{a, a + d, a + 2d, ..... }

the recurrence relation is an = an-1 + d (n≥1)

where a0 = a

Geometric sequence

{a, ar, ar2, ar3 ...... }

The recurrence relation

an = an-1.r (n≥1) ao = a

There are two type of recurrence relation

· Linear · Non-linear

Generating Function-

Let {a0, a1, a2......an} be a sequence of real

number, then a function f(x) defined by

f(x) = a0, a1x, a2x2 + ..... + an.x12 + ... is called

generating function of the sequence.

It the sequence contains infinitely many terms

then

f(x)=>(an.x")

n=0

00

Set Theory

Set-> A set can be defined as a well-defined

unordered collection of distinct element.

Example- A = {1, 2, 3, 4, ...... , 00}

S = {x/(x is a positive integer)} and 1≤x≤10

S = {1,2, 3, ..... , 10}

Null set (empty set)- A set with no elements is

called a "Null/empty set" denoted as 'o'., {}.

Example- A = {x/x is a prime number and 8≤x≤10}

Subset- If every element of A is also an element

of B then A is subset of B.

Example- A = {a, b, c} so A @ B

B = {a, b, c}

Discrete Mathematics

30

YCT

Proper Subset- Any subset of A which is not a

trivial subset of A is called proper subset of A. It

is denoted by 'C'.

Power set of a Set- If A is a finite set then set

of all subsets of it is denoted by P(A).

Example- If A = {a, b, c}, then P(A) = {0}, {a}, {b},

{c}, {a,b}, {b,c}, {c,a}, {a, b, c} }

Note- If |A| = n the |P(A) | = 2".

Universal Set- Set of all objects under

discussion. It is denoted by 'U'.

Example :- Let A={1,2,3,}, B={4,5,6}

AUB ={1,2,3,4,5,6,}

A

A

C

Complement of a set- If A is any set then

complement of A, denoted by À or Ac defined

as

AC = {x/x¢A and x € U}

Set Difference- If A and B are two set, then A -

B = {x/x € A and X¢ B}

U

A - B

Example :-

A= {1,2, 3}, B = {2, 4, 6}

then A - B = {1, 3}

Set Union- If A and B are two sets then,

AUB = {x/xE A or x E Bor x € AnB}

Set Intersection -> If A and B are two set then,

AnB = {x/xe A and x € B}

Note- If AnB is empty set, then A and B are called

disjoint sets.

Symmetric Difference/Boolean sum-

ΑΔΒ/ΑΦΒ = {x/x € A or x € B but x € An B}

Note- The symmetric difference of A and B

(a)

A+B=(A-B)U(B-A)

=(AUB)-(BnA)

(b) (i) (A-B) =(ABC)

(ii) (AnB)

(iii) (B -A) = (BnAc)

(iv) (A U B)C=(ABC)

(c) For any 3 set -> A, B, C the following

properties hold good.

(1) If A & B, then AU B = B and An B = A

(2) (AC) = A

(3) Commutative laws

(i) (AUB) = (BUA)

(ii) (AnB) = (BnA)

(iii) (A + B) = (BỘ A)

(4) Associative laws

(i) (AUB) UC=AU (BUC)

(ii) (AnB) nC=An(BnC)

(iii) (A+ B) + C = A + (B + C)

(5) Distributive law

(i) AU(BnC)=(AUB)(AUC)

(ii) An (BUC) =(AnB) U(AnC)

(6) Demorgans laws

(i) (AUB)C =(AB9)

(ii) (AB)C=(ACUB9)

(iii) A -(BUC)=(A-B)^(A-C)

(iv) A -(Bn C) =(A-B) U (A-C)

(7) Idempotent property

(i) AUA = A

(ii) BOB =B

(8) Absorption laws

(i) AU (AnB) = A

(ii) An (AUB)= A

(9) Modular laws

(i) (A UB) C= AU (Bn C) iff Ag C

(ii) (AB) UC=An (BUC) iffCCA

(10) AUDA , AND =¢

AUU=U, And =¢

A U AC = U, AnAC = ¢

Relation- Let A & B be two sets and some

elements of A be in certain correspondence with

some elements of B then that correspondence

defines a relation between those element of the

two set.

Domain and Range of Relation- Let R be a

relation from A to B then the elements of A

which are in relation are said to be domain and

the element of B which occur in R constitute in

range of R.

Discrete Mathematics

31

YCT

Example- If R = {(1, p), (1, q), (2, q)} be a relation

then

Domain = {1, 2}, Range = {p, q}

Properties of Relation-

(1) Reflexive relation- A relation R is reflexive

if for all xe A, (x, x) € R

Example- Let A = {1,2}& B = {1,2, 3}

R = {(1, 2), (2, 2), (1, 3)}

Note- A relation R is not reflexive then it is called

irreflexive.

(2) Symmetric Relation- A relation R is

symmetric if (a, b) E R then (b, a) € R

Example-

A = {1,2} & B = {1, 2, 3}

R= {(1,2), (2,1), (2, 2)}

(3) Transitivity of a relation- A relation R is

transitive if (x, y)ER & (y, z)ER then (x,

z)ER

Example- The relation "less then or equal to (≤) i.e. 1 <

2& 3 <4 then 1 <4.

Equivalence Relation- A relation R is called

equivalence relation in A, if

(1) R is reflexive

(2) R is symmetric

(3) R is transitive

Partial Order Relation- A relation R, defined

on a set A is called a partial order relation if it is

(i) Reflexive

(ii) Anti symmetric

(iii) Transitive

Anti symmetric- If a ≤ b & b ≤ a are true iff a =

b so relation is anti-symmetric. The set A with

the partial order relation R is called POSET.

So (R, ≤) is POSET.

Total Order Relation- A partial order relation

R in a set A is called total order relation if for

every element a, b, E A either a R b or b R a or a

= b.

To Set- A set with total order relation is called

To Set.

HASSE DIAGRAM

A graphical representation of a partial order relation

in which all arrowhead are understood to be

pointing upward is known as the Hasse Diagram.

Example- Let A = {1, 2, 3, 4, 6, 8} be ordered by the

relation "a divides b".

8

4

6

2

3

1

LATTICE

Maximal element- In a poset, if an element is not

related to any other element.

Minimal element- In a poset, if no element is

related to an element.

Example- Let (P, R) be a poset and P = {1, 2, 3, 4,

5} and R is relation of division.

We know that 3, 4 & 5 are not related to any

element. So, 3, 4 & 5 are maximal element but no

element is related to 1. So, 1 is minimal element.

LOWER BOUND AND UPPER BOUND

Upper Bound- Let (P, R) be a poset and B be a

subset of P element xeA is a upper bound of B if B

if y is related to x for every yeB.

Lower Bound- An element xEA is a lower bound

of B if x is related to y for every yeB.

Function- Let X and Y are two set. a rule in which

every element of X assigned to unique element of Y,

then this rule is called Function.

It is written as f:X->Y.

Domain And Range of the function- If f is a

function from A to B then A is called domain and B

is co-domain.

Range of Function- The set of all those elements of

B which are related with elements of A is called the

range of f. Evidently Range fc B.

Kind of Function

(i) One-one Function- Let f:A->B be a function it

is called one-one if x # y => f(x) # f(y) for x, y € A

or if f(x) = f(y) => x = y.

Example- Let f : R->R s.t f(x)=ax+b, a0

f(x) = f(y)

=> f(ax + b) = ay + b

=> ax = ay

=>x=y

Note- If f is not one-one then it is called many one.

Discrete Mathematics

32

YCT

Onto Function- A function f : A -> B is called onto

if Range f = B.

Bijective- Let f: A -> B be a function and it is

called bijective if f is one-one and onto.

INVERS AND COMPOSITION OF FUNCTION

Inverse function- If f : X -> Y is a bijection then

there always exist pre image f (a) of each element a

of y and this will be a unique element of y.

Composition function- If f : A -> B and g : B -> C

be two function then the function gof : A ->C;

where gof(x) = g[f(x)] for all x € A is the

composition function of f and g.

Groups

Algebraic structure- A non-empty set S is called

an algebraic structure with respect to the binary

operation '*'.

then (S, *) is an algebraic structure (N, +) (Z ,+), (Z-

1), (R, +, x) are all examples of algebraic structures.

Semi-Groups- An Algebraic structure (S, *) is

called a semi group.

(a*b)*c = a*(b*c) V a, b, c E S

* is associative on S.

Monoid- An Semigroup (S, *) is called a monoid.

(i) '*' is closed on G.

(ii) '*' is associative &

(iii) e e G such that V aEM, e*a = a = a*e

such an element 'e' is unique and is called the

identity element for the monoid.

Note- Every monoid is a semigroup the converse is not

true.

Group- An algebraic structure (G, *) is called a

group. If the binary operation satisfies the following

postulates.

1. Closure property: a * b E G V a, b E G

2. Associativity : (a*b)*c = a*(b*c)Va, b, c E G

3. Existence of identity: There exists an element

eEG such that e*a = a = a*e V a E G. the element e

is called identity for '*' is G.

4. Existence of inverse:

Thus a-1 is an element of G, such that a*A-1 = a-1 *a = e

Abelian Group or Commutative group- A group

G is said to be abellan.

Commutative: a * b = b * a V a, b E G.

Subgroup- Let (G*) be a group. A subset H of G is

called a sub group of G if (H, *) is a group.

Cyclic Groups- A group (G, *) is said to be cyclic

if there exists an element a E G such that every

element of G can be written as 'a"' for some integer

"n"; then a is called generating element.

Example- G = {1, -1} is a cyclic group of order 2

with respect to multiplication.

The generator of G =- 1.

GRAPH THEORY

Graph- A Graph G is mathematical structure

consisting of two sets V and E share V is a non-

empty set of vertices and E is a non-empty set of

edges.

V1

O

e1

V2

O

Basic Termenology-

(1) Trivial Graph- A graph consisting only one vertex

and no edge.

Example- 0

(2) Null Graph- A graph consisting n vertices and no

edge.

Example- 0000

(3) Directed Graph- A graph consist the direction of

edges then is called directed graph.

V

1

e1

V.

2

℮5

7

℮2

℮3

V

4

℮4

3

(4) Undirected graph- A graph which is not directed

then it is called undirected graph.

(5) Self loop in a graph- If edge having the same.

Vertex as both its end vertexes is called self loop.

Example-

e

V

(6) Proper edge- An edge which is not self loop is

called proper edge.

(7) Multi edge-A collection of two or more edge

having identically end point.

Example-

el

V

e2

V

2

e3

e1, e2, e3 are multi edge

Discrete Mathematics

33

YCT

(8) Simple graph- A graph does not contain any self

loop and multi edge.

(9) Multi graph- A graph does not contain any self

loop but contain multi edge is called multi graph.

V.

1

e1

e2

℮4

V

O

V

2

℮3

V

3

es

4

(10) Pseudo graph- A graph contain both self loop and

multi edge is called pseudo graph.

V

1

e1

V

C

2

e2

e,

V

O

6

V

3

e

e3

es

V

4

℮4

V

5

(11) Incidence and Adjacency- Let ek be an edge

joining two vertices V1 & V2 then ek is said to be

incident of V1 & V2.

Two vertices are said to be adjacent if there exist

and edge joining this vertices.

Example-

V,

e2

e1

V

2

e3

V

3

Here e1 is incident of V1 & V2 and V1 & V2 are

adjacent but V3 & V4 are not adjacent.

(12) Degree of Vertex- The degree of vertex V in a

graph G written as d(V) is equal to number of edges

which are incident on V with self loop counted

twice.

Example-

V,

V

2

V

OV.

8

4

V,

V

6

V.

3

V

5

Here d(V1) = 2, d(V2) ,= 4, d(V3) = 2, d(V4) = 3,

d(V5)=2, d(V6)=2,d(V7)=1,d(Vg)=0

(13) Isolated Vertex & Pendant Vertex- A Vertex

having 0 is called isolated vertex and a vertex

having degree 1 is called pendant vertex.

(14) Finite and Infinite Graph- A graph with a finite

number of vertices as well as edge is called finite

graph otherwise is infinite graph.

Some Important Graph-

(i) A simple connected graph is said to be complete

if each vertex is connected to every other vertex.

Example- OO

(ii) Regular Graph- A graph G is said to be regular

if every vertex has the same degree. If degree of

each vertex of graph G is K, then it is called K-

regular graph.

O

2-Regular

(iii)

Bipartite- If the vertex set V of a graph G can

be partilioned into two non-empty disjoint subset X and

Y in such a way that edge of G has one end in X and

one end in Y. Then G is called bipartite.

Note- If a graph is connected then it will not bipartite.

(4) Sub graph- Let G(V, E) be a graph. Let V be a

subset of V and let E be a subset of E whose end

point belong to V: The G(V, E) is a graph and called

a sub graph of G(V, E).

Decomposition of Graph- A graph is said to be

decomposition into two sub graph G1 and G2 if G1 U

G2 & GING2 = null graph.

HAND SHAKING THEOREM

The sum of the degree of the vertices of a graph G is

equal to twice the number of edges in G.

n

=>

∑

i=1

deg (V1) = 2x Number of edges

MATRIX REPRESENTATION OF GRAPH

(1) Adjacency Matrix- Let al denote the number of

edges (Vi, Vi) then A = [aj]mxn is called adjacency

matrix of G if

aj =10

1 if (Vi, Vi)is an edges

other wise

if (V1, V;) is an edges otherwise

(2) Incidence Matrix- Let G be a graph with m

vertices V1, V2, ..... Vm and n edges e1, e2,e3 ..... en

Let a matrix M = [Mij]mxn defined by

Discrete Mathematics

34

YCT

1 If the vertex V;is incident on the ij

mij = { 0 If V;isnot incident on ij

2 If Vi is an end of the loop ij

Path Matrix- Suppose G is a simple directed graph with

m vertices then path matrix P and Bm have same non zero

entries where Bm = A1 + A2 + A3 ...... Am.

Where A is adjacency matrix

ISOMORPHISM OF GRAPH

Definition- Two graphs G1 & G2 are isomorphic if

(i) Number of vertices are same.

(ii) Number of edges are same.

(iii) An equal number of vertices with given degree

(iv) Vertex correspondence & edge correspondence valid.

Homeomorphic Graph

Two graph G and G' are said to be homeomorphic if they

can be obtained from the same graph.

Note-If G & G' are homeomorhpic they need not be

insomorphic.

WALK, TRAIL and PATH

(1) Walk- A walk is a finite alternating sequence v1

e1 V2 e2 V3 e3 ... Vn en of vertices and edges beginning

and ending with same or different vertices.

(i) Length of the walk- The number of edge is called

length of the walk.

(ii) Closed & open walk- A walk is said to be closed if

its origin & terminus vertex (V0 = Vn) is equal

otherwise it is called open walk.

Trail: Any walk having different edges called trail.

Cycle- A closed trail is called circuit.

Path: A walk is called path if all vertices are not

repeated.

Cycle- A closed path is called cycle.

EULERIAN PATH- A path in a graph is said to be

an Eulerian path if it traverses each edge in the

graph once and only once.

EULERIAN GRAPH- A connected graph which

contain a Eulerian circuit is called Eulerian graph.

HAMILTONIAN PATH- A path which contain

every vertex of a graph G exactly once is called

Hamiltonian graph.

HAMILTONIAN CIRCUIT- A circuit that passes

through each of the vertices in a graph G exactly one

except the starting vertex & end vertex is called

Hamiltonian circuit.

HAMILTONIAN GRAPH- A connected graph

which contain Hamiltonial circuit is called

Hamiltonian Graph.

WEIGHTED GRAPH- A graph is called weighted

graph if a non-negative integer W(e) associate to each

edge and this W(e) is a weight of corresponding edge.

GRAPH COLORING- Painting all the vertices of a

graph with colours such that no two adjacent vertices

have the same color is called coloring of graph.

CHROMATIC NUMBER- The least number of

colors required for coloring of a graph G is called its

chromatic number.

Note-1. The chromatic number of graph G is denoted by

X(G).

2. If X(G) = K, then the graph is called K-chromatic.

3. Chromatic number of null graph is 1.

4. Chromatic number of complete graph Kn of n

vertices is n.

5. If a graph is circuit with n vertices then.

(i) It is 2-chromatic if n is even

(ii) If is 3-chromatic if n is odd.

TREE AND ITS PROPER TIES

TREE- A tree is a connected graph without any

loop or circuits.

Rooted Tree- A rooted tree is a tree in which one

vertex is root.

SPANNING TREE-If G is any connected graph a

spanning tree in G is a subgroup T of G, which is a tree.

Minimal Spanning Tree- Let G be a weighted

graph. A minimal spanning with minimum weight.

Algorithms For Minimal Spanning Tree

KRUSHKAL's Algorithm

Working Rule

(i) Choose an edge of minimal weight

(ii) Al each step, choose the edge whose inclusion

will not create a circuit.

(iii) If G has n vertices stop after (n-1) edges.

Example-

a

O

3

bo

1

c

2

Od

1

Weight = 3+1+2+1=7

e

(2) PRIM'S ALGORITHM

Working Rule-

(i) Select any vertex & choose the edge and smallest

weight from G

(ii) At each stage, choose the edge of smallest weight joining

a vertex already included to vertex not yet included.

(iii) Continue until all vertices are included.

Discrete Mathematics

35

YCT

04.

DIGITAL LOGIC

Number System

Decimal System-

It is a positional number system that uses 10 as a base to represent different values. Therefore, this number system is

also known as base 10 number system. In this system, 10 symbols are available for representing the value. These

symbols include the digits from 0 to 9.

Example, the value 237 which comes before the decimal point, is called integer value and the value 25, which

comes after the decimal point, is called fraction value.

Positive powers of 10

(Integer part)

Negative powers of 10

(Fractional part)

Decimal point

+

3

y

7

1

2

2×102

200

+ 7×10°

+ 7

+

2×101

.2

2

5

+ 3×101

+

+ 5×10ª

.05 = 237.25

30

Binary System- The binary system uses base 2 to represent different value. Therefore, the binary system is also

known as base-2 system. As this system used base2, only two symbols. are available for representing the different

values in this system. These symbols are 0 and 1, Which are also known as bits in computer terminology. Using

binary system, the computer systems can store and process each type of data in terms of 0s and 1s only.

Example, the binary number 11001.101 represents the decimal value 25.625.

Integer Part

Binary Point

V

1×2-1

+

0×2-2

Fraction Part

T 1 0 0 1 * TO

1

1×2

1×24 + 1×23 + 0×22 + 0×21 + 1×2º

+

16 + 8 + 0 + 0 + 1 + 0.5 + 0 + 0.125 =25.625

Technical terms

Used in Binary System.

Bit

+ It is the smallest unit of information used in a computer system.

+ It can either have the value 0 or 1.

+ Derived from the words 'Binary digit'.

Nibble

It is a combination of 4 bits.

Byte

+ It is combination of 8 bits.

+ Derived from words 'by eight'.

Word

It is a combination of 16 bits.

Double word.

It is a combination of 32 bits.

Kilobyte (KB)

It is used to represent the 1024 bytes of information.

Megabyte (MB)

1024 KBs

Gigabyte (GB)

1024 MBs

Terrabyte (TB)

1024 GBs

Petabyte (PB)

1024 TBS

Exabyte (EB)

1024 PBS

Zettabyte (ZB)

1024 EBs

Yottabyte (YB)

1024 ZBs

Digital Logic

36

YCT

Octal system- The octal system is the positional number system that used base 8 to represent different values.

Therefore, this number system is also known as base-8 system. As this system uses base 8, eight symbols are a

available for representing the value in this system. These symbols are the digits 0 to 7.

Example, The octal number 215.43 represents the decimal value 141.5469.

Integer Part

Octal point

Fraction Part

2

1

5

V

4

3

2×82 + 1×8' + 5×80

1×8-1 + 3×8-2

128

+

8

+

5

+

0.5 + 0.0469 = 141.5469

Hexadecimal system- The hexadecimal system is a positional number system that uses base 16 to represent

different values. Therefore, this number system is known as base-16 system. As this system uses base 16, 16

symbols are available for representing the value in this system. These symbols are the digits 0-9 and the letters A, B,

C, D, E and F. The digits 0-9 are used to represent the decimal value 0 through 9 and The letters A, B, C, D, E and F

are used to represent the decimal value 10 through 15.

Example, the hexadecimal number 4A9.2B represents the decimal value 1193.1679.

Integer Part

Hexadecimal point Fraction Part

L

¥

4

A

9

2

B

4×162 + 10×161 + 9×160

2×16-1 + 11×16-2

1024 + 160

+

9

+

0.125

+

0.0429 = 1193.1679

Decimal to non-decimal conversions

The decimal to non-decimal (binary, octal or hexadecimal), conversions use the step given below.

Step 1: Divide the given number by the base value of the number system in which It is to be converted.

Step 2 : Note the remainder.

Step 3: Keep on dividing the quotient by the base value and note the remainder till the quotient is Zero.

Step 4 : Write the noted remainders in the reverse order (from bottom to top).

(i) Decimal to Binary conversion-

Let us now convert a decimal value to its binary representation and verify that the binary equivalent of (65)10 is

(1000001)2.

Step 1 : Divide the decimal number by 2

1

2

65

Remainders

4

Step 2 : Write :Is ramainder

2

32

1

4

Step 3: Keep or dividing the quotient by

the base value 2 and not the remainder

fill the quetient is zero.

2

16

0

2

8

0

2

4

0

2

2

0

2

1

0

0

1

A

-

Step 4 : Collect the remainders from

bottom to top to get the binary equivalent

(65))) = (1000001),

Digital Logic

37

YCT

(ii).Decimal to Octal conversion-

The following example illustrate the method of converting decimal number 98 into its equivalent octal number.

Step 1 : Divide the decimal number by 8

Remainders

Step2 : Write its ramainder

8

98

8

12

2

8

1

4

Step 3: Keep or dividing the quotient by

the base value 8 and not the remainder

fill the quotient is zero.

0

1

Step 4 : Collect the remainders from

bottom to top to get the binary equivalent

(98)10 = (142);

(iii).Decimal to Hexadecimal conversion- The following example illustrate the method of converting decimal

number to its hexadecimal equivalent.

Step 1 : Divide the decimal number by16

Remainders

16

1567

Step2 : Write its ramainder

F (Hexadecimal symbol F

1

equivalent to decimal

number 15)

6

Step 3: Keep or dividing the quotient by

the base value 16 and not the remainder

fill the quotient is zero.

16

97

16

6

0

Step 4 : Collect the remainders from

bottom to top to get the hexadecimal equivalent

7

(1567)10 =(61F)16

Non-decimal to Decimal Conversions

The non-decimal to decimal conversions can be implemented by taking the concept of place values not

consideration we can use the following steps to convert the given number with base value to its decimal

equivalent, where base value can be 2, 8 and 16 for binary, octal and hexadecimal number system, respectively.

Step 1 : Write the position number for each alphanumeric symbol in the given number.

Step 2 : Get positional value for each symbol by raising its position number to the base value symbol in the given

number.

Step 3 : Multiply each digit with the respective positional value to get a decimal value.

Step 4 : Add all these decimal values to get the equivalent decimal number.

(i). Binary Number to Decimal Number conversion- The following example illustrate the method of

converting binary number (1101)2 to decimal number.

Digit->

Positional value->

nal value> 23 2 21 20

Decimal Number-> 1x 23 + 1×22 + 0x21 + 1x 2º

8 + 4 + 0 + 1

Therefore,

(1101)2 = (13)10

2

1 1 0 1

=(13)10

(ii). Octal number to Decimal number conversion- The following example shows how to compute the decimal

equivalent of an octal number (257)g.

Digit->

Positional value->

83

82

7

81

5

Decimal Number> 2x 82 +5×81 + 7×80

128 + 40 + 7 = (175)10

Therefore,

(257)8 =(175)10

Digital Logic

38

YCT

(iii). Hexadecimal Number to Decimal number conversion- The following example Shows how to compute the

decimal equivalent of an Hexadecimal (3A5)16-

Digit->

Positional value->

162

3

A

5

161

16°

Decimal Number-> 3x 162 + 10x16 + 5x16º

768

Therefore, (3A5)16 = (933)10

+

160 +

5

=(933)10

Conversion from Binary number to Octal number and Vice-versa

(i) Binary number to Octal Number- Given a binary number, an equivalent octal number representation by 3

bits is computed by grouping 3 bits from right to left and replacing each 3-bit group by the corresponding octal

digit. In case number of bits in a binary number is not multiple of 3, then add required, number of Os on most

significant position of the binary number

Example - Convert (10101100)2 to octal number.

Make group of 3-bits of the

given binary number (Right to left)

010

101

100

Write octal number for each 3- bit group.

2

5

4

Therefore, (10101100)2 = (254)8

(ii) Octal number to Binary number- Each octal digit is an encoding for a 3-digit binary number. Octal number

is converted to binary by replacing each octal digit by a group of three binary digits.

Example- Convert (705)8 to binary number.

0

5

Octal digit ->

7

Write 3-bits binary

value for each digit ->

111

000

101

Therefore,

(705)g=(111000101)2

Conversion from Binary number to Hexadecimal number and vice-versa

(i) Binary Number to Hexadecimal Number- Given a binary number, its equivalent hexadecimal number is

computed by making a group of 4 binary digits from right to left and substituting each 4-bit group by its

corresponding computed by making a group of 4 binary digits from right to left and substituting each 4-bit group

by its corresponding hexadecimal alphanumeric symbol. If required, add 0 bit on to have number of bit in a binary

number as multiple of 4.

Example- Convert (0110101100)2 to hexadecimal number.

Make group of 4-bits of

the given binary number (Right to left)

0001

1010

1100

C

Writ hexadecimal symbol for each group->1

Therefore, (0110101100)2 = (1AC)16

A

(ii). Hexadecimal number to Binary number- Each hexadecimal symbol is an encoding for a 4-digit binary

number. Hence, the binary equivalent of a hexadecimal number is obtained by substituting 4-bit binary equivalent

of each hexadecimal digit and combining them together.

Example. Convert (23D)16 to binary number.

Hexadecimal digits->

Write 4-bit binary for each digit-> 0010

2

3

0011

D

1101

Therefore, (23D)16 = (001000111101)2

Conversion from octal number to hexadecimal number

The given octal number can be converted' into its equivalent hexadecimal number in two different steps. Firstly,

We need to convert the given octal number into its binary equivalent. After obtaining the binary equivalent, we

need to making a group of 4 binary digits from Right to left and substituting each 4-bit group by its corresponding

hexadecimal alphanumeric symbol. In this type of conversion, we need to represent each digit in the octal number

to its equivalent 3-bit binary number.

Example- Convert the octal number (365); into its hexadecimal number.

Octal digits->

3

Write 3-bits binary value

6

5

for each digit->

011 110 101

Regrouping into 4-bits of

the binary number (Right to left)-> 0000 1111

0101

Write hexadecimal symbol

for each group->

0

F 5

(365)g=(F5)16

Therefore,

Digital Logic

39

YCT

Conversion of a Number with Fractional Part.

(i) Fractional part of Decimal number to Binary number.

Example. Convert decimal number (0.25)10 to binary.

Integer part

0.25×2 = 0.50

0.50×2=1.00

1

Į

0

Since the fractional part is 0, the multiplication is stopped. Write the integer part from top to bottom to get binary

number for the fractional part.

Therefore, (0.25)10 = (0.01)2

Example- Convert (0.675)10 to binary.

0.675×2=1.350

0.350×2 =0.700

0.700×2 = 1.400

1

0.400×2 =0.800

0.800×2 =1.600

1

0.600×2 = 1.200

0.200×2 = 0.400

0

0

1

1

0

Since the fractional part (.400) is the repeating value in the calculation, the multiplication is stopped, write the

integer part from top to bottom to get binary number for the fractional part.

Therefore, (0.675)= = (0.1010110)2

(ii) Fractional part of Decimal number to Octal Number.

Example- Convert (0.625)10 to Octal Number.

0.625 × 8=5.000

0.000 × 8 =0.000

Integer part

0

5

0

Since the fractional part is 0, the multiplication is stopped, write the integer part from top to bottom to get octal

number for the fractional part .

Therefore, (0.625)10 = (0.50)8

(iii) Fractional part of Decimal number to hexadecimal number.

Example- Convert (0.675)10 to hexadecimal.

Integer Part

0.675×16=10.800

A

(Hexademal symbol for 10)

0.800×16=12.800

Ī

C

(Hexadecimal symbol for 12)

Since the fractional part (.800) is repeating, the multiplication is stopped, Write the integer part from top to bottom

to get hexadecimal equivalent for the fractional part.

Therefore, (0.675)10 = (0.AC)16

Non-decimal Number with Fractional part to Decimal Number System

(i) Fractional part of Binary number to Decimal number.

Convert (0.111)2 into decimal number.

Digit-> 0. 11

1

Fractional

al value-> 2-1 2-2 2-3

Decimal value->

1×2- + 1x2-2 + 1×2-3

0.5 + 0.25 + 0.125 = 0.875

Therefore,

(0.111)2 = (0.875)10

Digital Logic

40

YCT

(ii) Fractional part of octal number to Decimal number.

=> Convert (0.12); into decimal number.

Digit->

0.

1

2

8-2

Fractional value->

8-1

Decimal value->

1×8-1 + 2×8-2

0.125

+

0.03125 = 0.15625

Therefore

(0.120)g =(0.15625)10

(iii) Fractional part of Hexadecimal number to Decimal number

=> Convert (0.58)16 into decimal number.

Digit->

0.

5

8

16-2

Fractional value->

16-1

Decimal value->

5×16-1

+ 8×16-2

0.3125

+ 0.03125 = 0.34375

Therefore,

(0.58)16=(0.34375)10

Fractional Binary Number to Octal or Hexadecimal Number

Example- Convert (10101100.01011)2 to octal number.

Make perfect group of 3-bits->

010

101

100

010

110

Write octal symbol for each group > 2 5 4 2 6

Therefore,

(10101100.01011)2 = (254.26)8

Note- Make 3-bit groups from right to left for the integer part and left to right for the fractional part.

Example- Convert (10101100.010111)2 to hexadecimal number.

make perfect group of 4-bits->

1010

1100 . 0101

1100

Write hexadecimal symbol for each group-> A C . 5 C

Therefore,

(10101100.010111)2 = (AC.5C)16

Binary coded Decimal (BCD) systems

Weighted 4-bit BCD

Code

BCD System

Excess-3 (XS-3) BCD

Code

Weighted 4-bit BCD code-

Example- Represent the decimal number 5327 in

weighted BCD code.

=> The given decimal number is 5327

The corresponding 4-bit 8421 BCD representation of

decimal digit.

8421

5 ->0101

3 -> 0011

2 -> 0010

7 ->0111

Therefore, The 8421 BCD representation of decimal

number (5327)10 is (0101001100100111)2

Example- Convert the decimal number (87.34)10 to

weighted BCD code.

=> The given decimal number is 87.34

The corresponding 4-bit 8421 BCD representation of

decimal digit

8421

8 ->1000

7 ->0111

3 -> 0011

4 -> 0100

Therefore, The 8421 BCD representation of decimal

number (87.34)10 is (1000 0111.0011 0100)2.

Excess-3 BCD Code-

Example- Convert the decimal number 85 to XS-3 BCD

code.

=> The given decimal number is 85. now, add 3 to each

digit of the given decimal number as-

8+3 = 11

5+3=8

The corresponding 4-bit 8421 BCD representation of the

decimal digit-

8 4 2 1

11->1011

8 ->1000

Therefore, the XS-3 BCD representation of the decimal

number 85 is 1011 1000.

Digital Logic

41

YCT

Gray Code

The Gray code or reflected binary code is an ordering

of the binary number system such that two successive

values differ in only one bit. Gray cods are very useful

in the normal sequence of binary number generated by

the hardware that may cause an error or ambiguity

during the transition from one number to the next. The

Gary code is not weighted that means it does not

depends on positional value of digit. This cyclic

variable code that means every transition from one

value to the next value involves only one bit change.

Binary to Gray code conversion- We can convert a

number represented in the binary form to the Gray we

need to remember the following two rules :-

(i) The most significant Bit (MSB) of the Gray code is

always equal to the MSB of the given binary code.

(ii) Other Bits of the output gray code can be obtained

by XORing binary code but at that index and

previous index.

Example- Convert the Binary number 1011 to its

equivalent Gray coded number.

Binary

1

0

1

1

+

+

0

1

0

1

Gray Code

1

1

1

0

Hence, the Gray coded equivalent of the binary number

1011 is 1110.

Gray to binary conversion- We can convert the gray

coded number to its binary equivalent by remembering

the following two major rules.

(i) The most significant bit (MSB) of the binary code is

always equal to the MSB of the given gray code.

(ii) Other bits of the output binary code can be obtained

by checking gray code bit at that index. If current gray

code bit is 0, then copy previous binary code bit, else

copy invert of previous binary code bit.

Example- Convert the Gray coded number 11010011

to its binary equivalent.

Gray code digit

Binary digit

1

1

invert of previous binary code bit

1

0

copy previous binary code bit

0

invert of previous binary code bit

1

0

1

0

copy previous binary code bit

1

copy previous binary code bit

0

1

invert of previous binary code bit

0

invert of previous binary code bit

1

1

1

Hence, the binary equivalent of gray coded number

11010011 is 10011101.

One's complement system

1's complement of a binary number is another binary

number obtained by toggling all bits in it, i.e.

transforming the 0 bit to 1 and the 1 bit to 0.

Example- 1's complement of'1100' is '0011'

Two's complement system

2's complement of a binary number is 1, added to the 1's

complement of the binary number.

Exmaple- 2's complement of 1100 is ?

1's complement of 1100 is 0011 added 1, to the is

complement.

0011

+1

0100

2's complement of '1100' is '0100'

Boolean Algebra

Commutative

Law

· A+B = B+A

· A.B = B.A

Associative Law

· A+(B+C) =(A+B)+C

· A.(B.C) = (A.B)C = ABC

Distributive

Law

· A(B+C) = AB + AC

· A+(B.C) = (A+B).(A+C)

· (A+B)(C+D)=AC+AD+BC+BD

· A+(A.B)= A +B

Absorption law

· A + AB = A · A(A+B) =A

· A+AB= A + B

· A+ AB = A + B

Idempotence

Law

· ORing-A+A+A + ........ = A

· ANDing- A.A.A

= A

AND

Operation

Theorem

· A.0 = 0

· A.1 = A

· A.A = A

· A.A = 0

OR Operation

Theorem

· A+A = A

· A+0 = A

· A+1 = 1

· A+A =1

Transposition

Theorem

· (A+B).(A+C) = A + BC

Consensus or

Redundancy

Theorem

· AB+AC+BC= AB+ AC

Demorgan's

Theorem

. A.B = A +B · A + B = A.B

Duality

Theorem

·(·) < >(+)·(0) < > (1)

AND <> OR

· Taking all literals as it is.

Complementary

Theorem

.(.)<>(+).(0)<>(1)

· Complement literals individually

Involution

Theorem

· A = A

Note :-

› Maximum possible minterm or maxterm = 2"

> Maximum possible logical expression = 22"

Digital Logic

42

YCT

Maximum possible self dual expression = 22

n

−

> AND, OR, NAND, NOR, XOR and X-NOR- Gate

follow commutative law

1

AND, OR, XOR, and X-NOR- Gate follow

associative law

NAND and NOR-Gate does not follow associative

law

Logic Gates

> Logic Gate is a electronics switch which performs the arithmetic and logic function.

Basic Gates

Gate

Symbol

Diode circuit

Transistor

Truth table

Switch table

NOT

A

A

A

o

A

+V

CC

A

Y=A

0

+V

cc

T,

Y= Ā

A

₹ G=0

Input

Output

A

T1/D1

Y

A

Ā

Low

OFF

High

ON

High

Low

0

1

1

0

AND

A

Y= AB

B

+V

cc

D

A

Y=AB

D

2

B

+V

CC

Rc

A

1

T,

B

T2

Y= AB

RE

Input

Output

A

B

T,/D,

T2/D,

Y

A

B

Y = AB

Low

Low

ON

ON

Low

0

0

0

Low

High

High

ON

OFF

Low

0

1

0

High

Low

High

OFF

OFF

ON

OFF

Low

High

1

0

0

1

1

1

OR

A

Y=A+B

B

+V

cc

A

DI

Y= A+B

B

D2

2

+V

CC

T

T2

A

A

K

w+ B

RE

Y= A+B

Input

Output

A

B

T,/D,

T2/D2

Y

A

0

B

0

Y = A+B

0

Low

Low

Low

High

OFF

OFF

OFF

ON

Low

High

0

1

1

High

Low

ON

OFF

High

1

0

1

High

High

ON

ON

High

1

1

1

Universal Gate

NAND

Gate

A

Y=AB

B

0

+Vcc

Y= AB

T,

Input

Output

ABTTY

Low

Low

OFF

OFF

High

A

B

Y = AB

Low

High

OFF

ON

High

0

0

1

High

Low

ON

OFF

High

0

1

1

High

High

ON

ON

Low

1

0

1

Be-ww

T2

1

1

0

NOR

Gate

A

Y= A+B

B

+V

CC

Rc

Y=A+B

T

A

B

T2

-

N

N

Input

Output

A

B

T,

T2

Y

High

Low

Low

OFF

OFF

A

B

Y = A+B

Low

High

High

Low

OFF

ON

ON

OFF

Low

Low

0

0

1

High

High

ON

ON

Low

0

1

0

1

0

0

1

1

0

Digital Logic

43

YCT

FET as a Switch

Gate

Diagram

Truth Table

JFET

as

NOT Gate

V

DD

Rp

V

Y=Ā

out

A, V-

A

T1

Y

Low

OFF

High

High

ON

Low

MOSFET as

NOT Gate

T2

V., Y

A, V_

T,

7

A

T1

T2

Y

Low

ON

OFF

High

High

ON

ON

Low

Special Purpose Gates

Gate

Symbol

Truth Table

EX-

OR

A

Y=A+ B = ĀB+ AB

B

> In EXOR operation

Input

Output

· For BUFFER

A

B

Y - AOB

0

0

0

CIRCUIT => Logic '0'

0

1

1

· For INVERSION

1

0

1

1

1

0

CIRCUIT => Logic '1'

EX-

NOR

A

Y = AOB = AB+ ĀB

Input

Output

B

A

B

Y = AOB

> In EXNOR operation

· For BUFFER

0

0

1

0

1

1

0

0

0

1

1

1

CIRCUIT => Logic '1'

· For INVERSION

CIRCUIT => Logic '0'

Logic gates

No. of NAND

Gate required

No. of NOR

Gate required

NOT

1

1

AND

2

3

OR

3

2

EX-OR

4

5

EX-NOR

5

4

NAND

1

4

NOR

4

1

+ Remember point

-> Indeterminant output

-> Work as Bistable multivibrator

Work as Astable multivibrator,

> square wave generator,

clock generator

AND Gate is also called all or nothing gate

AND Gate works as a series switch

OR Gate is also called any or all Gate

OR Gate works as a parallel switch

> EX-OR gate acts as odd number of "1's detector".

> EX-OR gate is used for even parity generator and

detector.

> EX-OR gate is known as stair case switch.

> EX-NOR gate acts as even number of "1's detector".

> EX-NOR gate is used for odd parity generator.

> XOR-Gate is also called anti-incidental logic gate.

A@0 = A -> work as buffer

A+1=A -> work as inverter

> X-NOR-Gate is also called equivalence gate or

equality detector or co-incident logic gate.

> AO0=A -> work as inverter

> AO1=A -> work as Buffer

> NOR and NAND are special logic gates

AOBOC=AOBOC

> ΑΦΑΘΑΘ

n times

= 0, (if n =even)

= A, (if n = odd)

> AOAOAO

n times

= 1, (if n =even)

= A, (if n = odd)

> AOB=AOB=AOB > AOB=AOB

> AOB=AOB=AOB

Positive logic

Negative logic

Bubbled logic

AND- Gate

OR- Gate

NOR- Gate

OR- Gate

AND- Gate

NAND- Gate

NAND- Gate

NOR- Gate

OR- Gate

NOR- Gate

NAND- Gate

AND- Gate

Positive logic and Negative logic system

· Positive logic

> Logic '1' voltage level is higher than logic '0'

voltage level

Digital Logic

44

YCT

> Logic '0' voltage level is lower than logic '1'

voltage level

· Negative logic

> Logic '0' voltage level is higher than logic '1'

voltage level

> Logic '1' voltage level is lower than logic '0'

voltage level

Representation of Boolean functions

Representation of Boolean function

Cononical form

Minimal form

Ex:

F(X,Y,Z)=XYZ+XYZ+XYZ F(X,Y,Z)=X+YZ+XYZ

Ex:

> Maximum no. of Boolean expression or function = 22"

· Sum of Product (SOP) : Each product term is

known as minterm. SOP form (Em) is used when

output is logic 1. Ex .- (ABC)+(ABC)+(ABC)

· Product of Sum (POS) : Each product term is

known as maxterm. POS form (IIM) is used when

output is logic '0'.

Ex .- (A+B+C).(A+B+C).(A+B+C)

Remember point

> Maximum possible minterm or maxterm = 2"

> Maximum possible self dual function = 22"-

> AND-OR logic = NAND-NAND logic (Used in

SOP).

> OR-AND Logic = NOR-NOR logic (Used in POS).

Karnaugh Map (K - Map]

> A systematic & simple way of minimization of

Boolean algebra.

> Minimization using K-map, the solution is not unique.

> "Gray Code" is used in K-map.

> Number of cells = 2", n = Number of variables.

· Don't Care - Considered when this is helping in

minimization of Boolean algebra.

> Implicants = Number of minterms/maxterms

> Prime implicants = Number of pairs

> Essential Prime Implicants= Number of prime

implicants without redundant terms

Digital Logic Circuits

Combinational Circuit

Sequential Circuit

Present output depends only

on present input.

Present output

depends on both

present input as well

as past output.

No memory present.

Memory is present.

Faster.

Slower.

Easy to design.

Harder to Design.

No feedback present.

Feedback present.

No clock pulse required.

Clock pulse required.

Arithmetic operation and

Boolean operation.

Data storing system.

Ex .- Adder, Substractor,

Decoder, Encoder, Comparator

MUX, D-MUX, parallel adder,

ROM, RAM etc.

Ex .- Flip-flop, Latch,

Counter, Register,

serial adder etc.

Combinational Circuits

Circuit Diagram

Formula

Implement by

Half Adder

A

S

B

C

S=AB+AB=AOB

C = A.B

· 5- NAND gates

· 5- NOR gates

· 3- (2 × 1) MUX

· 2- (4×1) MUX

Full Adder

A

B

S

C

C,

S=AOBỌC

= ABC + ABC + ABC+ ABC

Co =(A@B).C+ AB

= AB + BC + CA

· 2- H.A+ 1 OR

gate

· 9- NAND gate

· 9- NOR gate

· 7-(2 × 1) MUX

Half

subtractor

A

B

D

Bo

D=ĀB+ AB= A + B

B = ĀB

· 5- NAND gates

· 5- NOR gates

· 3- (2 × 1) MUX

· 2- (4×1) MUX

Full

subtractor

A

B

D

Cir

in

Bo

D=AOBOC

= ABC + ABC + ABC + ABC

Bo=(AOB).C+AB

= ĀB+ ĀC+ BC

· 2- H.S + 1 OR

gates

· 9- NAND gates

· 9- NOR gates

· 7- (2 × 1) MUX

Digital Logic

45

YCT

· In parallel adder for two n-bits numbers requires-

> n Full Adder

> (n-1) F.A + 1 H.A

> (2n-1) H·A + (n-1) OR Gate

Circuit Diagram

Specification

MUX

2ª Input

lines

2"×1

Output

(01- Output line)

n-Select lines

> Named as-

· Data Selector circuit

. Many to One circuit

· Universal logic circuit

· Parallel to serial converter

· Wave form generator

· Data Routing

· m=2" = no. of input lines, no. of output line = 1

n = number of select lines

D-MUX

Input

(Single)

1 × 2ª

2ª o/p lines

n-Number of select lines

> Named as -

· Data Distributor circuit

. One to many circuit

· Serial to Parallel Converter

· Single Input to multiple output

· No. of input line =1, no. of output lines = 2"

No. of select lines = n

Decoder

n-I/p

Lines

n × 2"

2" o/p lines

E (Enable Signal)

> It is a combinational logic circuit that converts

binary information from n bit input lines to a

maximum 2" o/p lines

> Decoders are used to convert a particular code-

· Binary to octal (3×8 lines decoders)

· Binary to Hexadecimal (4×16 line decoders)

· BCD to decimal (4×10 line decoders)

· BCD to 7-Segment display.

· The total number of output line m ≤ 2"

· Decoders are widely used memory system of computer.

Encoder

2" Input

Lines

n- Output

Lines

E (Enable Signal)

> Inversion of Decoder circuit is known as Encoder.

> Encoder is used to convert other codes to binary

such as -

· Octal to Binary encoder (8×3 lines)

· Decimal to BCD encoder (10×4 lines)

· Hexadecimal to Binary encoder (16×4 lines)

Sequential Circuits

Latch

Flip-flop

Latches use level

triggering

Flip-flops use edge

triggering.

No clock pulse

Clock pulse

Build from gates

Build from latch

The output changes as per

the input till enable is

high.

The output changes as

per the input only at

triggering point.

Buffer

· 1 bit memory element.

· 2 Stable states

· Bi-stable Multi-vibrator

Output cannot predict

Output can predict (0/1)

Triggering

Triggering is used to initiate the

operation of latches or flip-flops.

· Level trigger

OR

> Edge trigger

OR

7

Clock In Flip-Flop

· Setup Time : The time period required to hold the

incoming data before the arrival of clock pulse.

> This is of the order of 50ns.

· Hold Time : The time period required to hold the

incoming signal information after the arrival of

clock pulse.

> This is in order of 10-20 ns.

> Setup Time > Hold Time.

Digital Logic

46

YCT

Flip-

Flop

Logic Diagram

Graphical Diagram

Characteristics

Equation

Truth Table

SR

R

Qn

Clk

Q.

S

S

Clk

R

Qn

Qn

Qn+1 = S+RQn

Clock

S

R

Qn+1

State

1

0

0

Q.

Hold state

1

0

1

0

Reset state

1

1

0

1

Set state

1

1

1

Invalid

Forbidden state

JK

J

Q.

CLK

K

Qa

J

Q.

Clk

K

Qn

Qn+1 = JQn + KQn

Clock

J

K

Qn+1

State

1

0

0

Q.

Hold state

1

0

1

0

Reset state

1

1

0

1

Set state

1

1

1

Qn

Toggle state

D Flip-

flop

D

S

Qn

Clk

Q

R

D

J

Clk·

K

Qn

Q.

Qn+1 = D

Clock

D

Qn+1

0

X

Q.

1

0

0

1

1

1

T flip-

flop

T

Qn

CLK

Q.

T

J

Clk·

K

Qn

Q.

Qn+1 = TQn + TQn

=TOQn

Clock

T

Qn+1

State

0

X

Qn

Previous state

1

0

Qn

Hold state

1

1

Q.

Toggle state

Conversion of Flip-flop

Desired flip-flop

Given Flip-flop Flip-flop Flip-flop Flip-flop Flip-flop

SR

D

JK

T

SR Flip-flop

S=D

R = Ď

S = JŌ.

R = KQ.

S = TŌ.

R = TQ.

D Flip-flop

D = S+RQ.

D = JŪ.+KQ.

D =TĐQ.

JK Flip-flop

J= S

K= R

J= D

K =D

J=T

K=T

T Flip-flop

D= SÕn+RQn

T = DĐQn

J = JŪ.+KQ,

Excitation table

Qn

Qn+1

S

R

J

K

D

T

0

0

0

x

0

x

0

0

0

1

1

0

1

x

1

1

1

0

0 1

x

1

0

1

1

1

X 0

x

0

1

0

· Applications of Flip-flops

Serial and Parallel data storage, Data Transfer,

Serial to Parallel Converter, Parallel to serial converter

Latch, Counter, Frequency division, memory

Remember point

> Race-around condition occurs in JK-FF to store 1-

bit of Information. [J = K = 1], tpd (FF) << tpw-

> Race-around Condition always arises in

"Asynchronous circuits."

. To Avoid Race Around -

> tpw < tpd (FF) < T > Edge triggering

> Master-Slave FF

O Registers

> Register is a memory device, which is used for data

storage & shifting.

> Register is a group of flip-flops & gates.

> For n-bit data, the n-flip-flops are required.

Shift Register

> Data can be shifted by single bit.

· Four types of shift Registers

Register

Presentation

Clock pulse

Input

Output

SISO

IN

LSB

FF

FF

FF

FF

Out

n

(n-1)

SIPO

LSB

IN

FF

FF

FF

FF

Out

n

0

PISO

IN

FF

FF

FF

FF

Out

1

(n-1)

PIPO

IN

1

1

1

1

FF

FF

FF

FF

Out

1

0

Digital Logic

47

YCT

> Time delay for SISO shift register-

At = N×T = Nx

1

f

c

N = Number of FFs.

fc = Clock frequency

T = Time period of Clock pulse

> All shift Registers made of JK-FFs.

> In storage registers mostly D flip-flops are used.

O Counters

> Counter is formed by the cascading of FFs.

. Counter are basically used for -

> Counting of the number of clock pulses.

> Frequency division > Timers > In RADAR

> Frequency Measurement > Wave form generation

> In each count the binary data is known as "State of

counter."

> Number of states counted by a counter is known as

'modules of counter'.

If M = Modules = Mod = Total Number of states

n = Number of bits or flip-flop then M ≤ 2"

> M=2" => Binary Counter or ripple counter

> M <2" => Non-Binary Counter or BCD counter

. Counters are classified in two categories.

i. Asynchronous Counter [Ripple Counter/Series

Counter]

ii. Synchronous Counter [Parallel Counter]

Synchronous counter

Asynchronous counter

Same clock pulse is

applied to individual flip-

flop.

Clock Signal is applied

only the first flip-flop.

Any sequence can be

generate.

Fixed sequence [Upper or

Down]

Faster

Slower

No Decoding Error

Due to propagation delay

decoding error exist.

Design is complex, as

number of bits increases.

Design easy, even more

number of bits.

Types:

i. Ring Counter / End

Carry Counter

ii. Twisted Ring

Counter / Johnson

Counter

iii. Synchronous-series

carry counter

iv. Synchronous-parallel

carry counter

Types:

i. Ripple Up Counter

ii. Ripple Down

Counter

iii. BCD Counter (Non-

Binary)

iv. Up counter

v. Down counter

· Modulus of counter

> Known as MOD or MOD number

MOD ≤ 2"

Where n = Number of flip-flop

f=f.

in

MOD-N

counter

f

out

f

f.

N

=

in

out

· Binary Counter

If the sequence of the states is either ascending or

descending order than the counter is called binary

counter. It is also called as (2":1) scalar counter

· Variable modulus counter

> It is counter in which the maximum number of state

can be changed.

Note: The final state of the counter sequence is called

the terminal counter.

· Application of counter

> It is used as frequency divider circuit

> It create time delay

> It generate a required sequence bit

> Output Frequency of two Cascaded Counters

Overall Mod of Counters = M.N

Overall Output frequency = f

f;

M.N

> For n-bits counter if delay for each Flip-flop is tpd

then total clock period -

T

≥ n.t

f

≤

n.t

1

f.

=

max

n.t

pd(ff)

pd(ff)

· Synchronous counter

Synchronous Counter

Shift register

counters

Synchronous

serial counter

Synchronous parallel

counter

(series-carry count) (Parallel-carry counter )

Ring counter

(End carry counter)

Twisted ring counter

(Johnson counter)

· Ring Counter

Q2

Q

Q0

Q

Serial

Input

D.

D

Qo

D

Q2

Qo

CLK

Digital Logic

48

YCT

1

CLK

pd(ff)

,

CLK

> Ring counter works as SISO

> It is also called n:1 counter

. Johnson Counter

Q2

Q

Q0

2

D

Q

D

D

Q

Qo

CLK

> Maximum count value = (2"-1)

> Synchronous-series carry counter,

fCLK ≤

tpd(FF) +(n-2)t

1

pd(ANDGate)

> Synchronous-parallel carry counter,

fCLK ≤

t

"pd(FF) +"pd(ANDGate)

+ t

1

It is the 'fastest counter".

Counter

Number

of states,

M

Unused

state

Output

frequency

f.

BCD/Mod-10

counter

10

6,

(2" - M)

fo = f

10

Ring counter

n

2" - n

f .= £

n

Johnson/Ring

Twisted counter

2n

2ª - 2n

f = f.

2n

Asynchronous counter

· 3-bit binary ripple up counter

T

(LSB) Q0

T

Q

1

Q,(MSB)

Q

2

Q

CLK-

Q

· 3-bit binary ripple down counter

T

(LSB) Q0

T

Q

,(MSB)

T

CLK

Trick to Identify Counter (Ripple counter)

Clock (Triggering)

Output

Counter

Positive edge

Q

Down-counter

Q

Up-counter

Negative edge

Q

Up-counter

Q

Down-counter

3-bit up-down ripple counter

M

1

1

CLK

T

1

T

T2

Q

Q

2

O

Q

Q.

o

If M = 1 => up counter,

If M = 0> down counter

Remember point

> The Ring counter and Johnson counter are not use

for counting purpose.

› Johnson Counter also known as-

> Twisted Ring counter

> Mobies Counter

> Switch tail Ring Counter

> Creeping counter

> Walking counter

> In ring counter all flip-flops output frequency

remain same but phase shift is different and equal to

360º/n, (where, n= number of state)

> "Lock out" problem occurs in non-binary counter.

> JK, SR, D and T are called synchronous Input.

> Reset and Set are called Asynchronous Input.

> "Preset" always make the output to '1'.

> "Clear" always make the output to '0'.

> "Glitch" is an unwanted spike in the signal.

> MOD-16 counter could also be called a "divide-by-

16 counter".

Digital Logic

49

YCT

05.

DATABASE MANAGEMENT

SYSTEMS

Introduction to DBMS

DBMS

Data Base Management System

Data Base System

Data base

DBMS

Structured Unstructured

SQL

IRCTC

Web pages

My SQL

University

Oracle

Database management system is the combination of

two words.

Database + Management System = DBMS

Data base

It is a collection of related data.

Data base management system is a collection of

programs that enables users to create and maintain

the database.

Structured Database

Structured data is highly specific and is stored in

predefined format.

Structured data store in relation form

Example- IRCTC, University

Unstructured- Unstructured data is information

that either does not have a predefined data model or

is not organised in a pre-defined manner. Example-

Web pages.

Database

Application

DBMS

OS

DBMS can also be define as a interface between the

application program and the operating system to

access and manipulate that database.

Database management system is a software which is

used to manage the database for example-

MYSQL, ORACLE etc. are a very popular

commercial database which is used in different

applications.

Characteristics of DBMS

Less

data

Data

Backup

Multiuser

7 support

ACID

properties

DBMS

Data

Integrity

Query language

support

Data

Security

Data

Consistency

It user a digital repository established on a server to

store and manage the information.

It can provide a clear and logical view of the

process that manipulates data.

DBMS contain automatic backup and recovery

procedures.

It contain ACID properties which maintain data in a

healthy state in case of failure.

It is used to provide security of data.

Application of DBMS

1. Banking- for maintaining customer information,

loans and banking transactions.

2. Universities- for maintaining, student records,

registration etc.

3. Railway Reservation- for checking the availability

of reservation in different trains, tickets etc.

4. Sales-for customer, product and purchase

information.

5. Hospital system- the hospital system which deals

with in patients as well as out-patients.

Room

Physician

Patients

Items

Charges

In patient

treatments

Out-patient

Advantages of DBMS

. Control database redundancy- It can control

data redundancy because it stores all the data in

one single database file and that recorded data is

placed in the database.

Database Management Systems

50

YCT

· Data sharing- In DBMS, the organization users

of an organization can share the data among

multiple users.

. Easily maintenance- It can be easily

maintenance due to the centralized nature of the

database system.

· Multiple user Interface- It provides different

types of user interface like graphical user

interface, application program interfaces.

Disadvantages of DBMS

· Cost of Hardware and Software- It requires a

high speed of data processor and large memory

size to run DBMS software.

Size- It occupies a large space of disks and large

memory to run them efficiently.

· Complexity- Database system creates additional

complexity and requirements.

File System Vs DBMS

File based system were an early attempt to

computerize the manual system.

Example-

Users

Users

Users

Student file

Subject file

Result file

Roll_no,

St_Name

Course

Phone_no.

Address,

Room

Sub, Name

Marks etc.

Sub_Id

Sub_Name

Course

Room etc.

Roll_no.

St_Name

Course

Sub_Name

Mark etc.

Consider an example of students file system.

The student file will contain information regarding

the student (rollno., studentName etc.).

We have subject file that contain information about

the subject and result regarding the result. File

which contains the information regarding the result.

DBMS

A data base is a well-organized collection of data

that are related in a meaningful.

Different users but stored only one in a system.

The various operation performed by the DBMS

system are Insertion, Deletion, Selection etc.

STUDENT FILE

SUBJECT FILE

RESULT FILE

Roll_no,

St_Name

Course

Phone_no.

Address,

Room

Sub, Name

Marks etc.

Sub_Id

Sub_Name

Room etc.

Roll_no.

St_Name

Course

Sub_Name

Mark etc.

DBMS

Users

Users

Users

Figure, duplication of data is reduced due to

centralization of data.

Basic

DBMS

File System

Sharing of

Data sharing is

So, it is not easy

Data

easy

to share data

Security and

protection

DBMS provides

The file system

does not have a

good protection

mechanism

crash

mechanism

Cost

The database

The file system

approach

is

cheaper

to

system

is

expensive

to

design

design

Data

Due to the

There exists a

Redundancy

Centralization

lot of

and

the database, the

duplication

of

Inconsistency

problems of

data which may

data redundancy

lead to

and

inconsistency

inconsistency

are controlled

Structure

The

database

The file system

approach has a

simple structure

structure

is

complex

to

design

2 tier layer

Client 2

Machine

Client 1

Client 3

Machine

Interface

Process

Data base

2 tier architecture also called client server

architecture.

direct communicates

example- Indian Railway

The application on client side interact directly with

the data base present at the server side.

Database Management Systems

51

YCT

3 tier architecture

Interface

User

Client 2

Client

application

Client 1

Client 3

Client

layer

Application

server

Business

layer

Data layer

Data source

All the web application are kind of 3 tier

architecture.

There is no direct communication between client

and server.

Application Server- This called business layer. It

act as a middle layer between the client and the

database server and exchange partially processed

data.

Data base layer- The data or information is stored.

Client layer- The main purpose is to communicate

with the application layer.

Schema- Schema is actually a logical

representation of the database.

There can be multiple tables in a schema.

DATA MODELS

Data model is the modeling of the data description,

data semantics and consistency constraints of the

data.

Four Types of DBMS System are-

· Hierarchical data base

· Network data base

· Relational data base

· ER model data base

Hierarchical DBMS - In a Hierarchical database,

model data is organized in a tree-like structure. Data

is stored Hierarchically (top down or bottom up)

format.

College

Department

Infrastructure

Course

Teachers

Students

Theory

Labs

Network Model- The network database model

allows each child to have multiple parents.

College

CSE

department

Library

Student

Relational Model- Relational DBMS is the most

widely used DBMS model because it is one of the

easiest.

ER Model- ER model is based on the notion of

real-world entities and relationship among them.

ER Model creates entity set, relationship set;

general attributes and constraints.

DBMS LANGUAGES

Data base languages are used to read update and

store data in a database.

DBMS Language

DDL

DCL

DML

TCL

· DDL - Data Definition Language. (CREATE,

DROP, ALTER, TRUNCATE, COMMENT,

RENAME)

· DML - Data Manipulation Language. (INSERT,

UPDATE, DELETE, SELECT)

· DCL-Data Control Language (GRANT, REVOKE)

· TCL - Transaction Control Language (COMMIT,

ROLLBACK)

DDL (Data Definition Language)

DDL actually consists of the SQL commands that can

be used to define the database schema.

CREATE- It is used to create the database or its

objects (Like table, Index, function views store

procedure and triggers).

There are two CREATE statements available in SQL.

1. CREATE DATABASE

2. CREATE TABLE

CREATE DATABASE- The CREATE DATABASE

statement is used to create a new data base in SQL.

Syntax-

CREATE DATABASE database_name;

Example-

SQL>CREATE DATABASE Employee;

In order to get the list of all the database, you can

use SHOW databases statement.

SQL > SHOW DATABASE;

CREATE TABLE- The CREATE TABLE

statement is used to create table in SQL we know

that a table comprises of rows and columns.

Database Management Systems

52

YCT

Syntax-

CREATE TABLE table_name

(

Column1 data_type(size),

Column2 data_type(size),

Column3 data_type(size),

);

Example Query- This query will create a table

students with three columns, RoLL_No, NAME and

SUBJECT.

CREATE TABLE students

(

RoLL_No int(3)

NAME Varchar (20),

SUBJECT Varchar (20),

);

DROP-

· DROP is used to delete a whole database or just a

table.

· A DROP statement in SQL removes a component

from a relational database management system

(RDBMS).

Syntax-

DROP object object_name;

Example-

DROP TABLE table_name;

table_name: Name of the table to be deleted.

DROP DATABASE database_name;

database_name: Name of the data base to be

deleted.

TRUNCATE- It is used to remove all records from

a table, including all spaces the TRUNCATE

TABLE my table statement is logically equivalent

to the DELETE FROM my table (without a

WHERE clause).

Syntax-

TRUNCATE TABLE table_name;

DROP Vs TRUNCATE-

· Truncate is normally ultra fast and its ideal for

deleting data from a temporary table.

· Table or database deletion using DROP statement

cannot be rollback so it must used wisely.

To delete the whole database

DROP DATABASE student_data;

After running the above query whole database will

be deleted.

To truncate student_details table from student_data

database.

TRUNCATE TABLE student_details;

· ALTER (ADD, DROP, MODIFY)

ALTER TABLE is used to add, delete/drop or

modify columns in the existing table. It is also used

to add and drop various constraints on the existing

table.

ALTER TABLE_ADD-

· ADD is used to add columns into the existing table.

Syntax-

ALTER TABLE table_name;

ADD(Columnname1 datatype,

Columnname2 datatype,

columnnamen datatype);

ALTER TABLE_DROP-

· DROP COLUMN is used to drop column in a table.

Syntax-

ALTER TABLE table_name;

DROP COLUMN column_name;

ALTER TABLE_MODIFY- It is used to modify

the existing columns in a table.

syntax-

ALTER TABLE table_name;

MODIFY Column_name column_type;

QUERY:

TO ADD 2columns AGE and COURSE to table

student.

ALTER TABLE student ADD (AGE number (3),

COURSE Varchar(40));

DML

The SQL commands that deals with the manipulation of

data present in the database belong to DML and this

includes most of the SQL statements.

SELECT statement- select statement is used to fetch

data from relational database. SQL select statement or

SQL select query is used to fetch data from one or more

than one tables.

Syntax- One Column:

Here column_name is the name of the column for

which we need to fetch data and table_name is the

name of the table in the database.

Select column_name FROM table_name;

To fetch the entire table or all the fields in the table.

SELECT * FROM table_name;

SELECT EMP_NAME FROM EMPLOYEES;

To fetch the entire EMPLOYEES table;

SELECT * FROM EMPLOYEES;

Database Management Systems

53

YCT

INSERT INTO statement-

INSERT INTO student of SQL is used to insert a

new row in a table.

INSERT INTO table_name VALUES (value1,

value2, value3 ....... );

Example-

method1 (Inserting only values):

INSERT INTO student values ('5' 'HARSH' WEST

BENGAL; 19;)

Method2 (Inserting values in only specified

columns);

INSERT INTO student(Roll_NO, Name, Age)

VALUES ('5' PRATIK, '19');

UPDATE statement-

The UPDATE statement in SQL is used to update

the data of an existing table in database.

Basic syntax-

UPDATE Table Name

SET Column_name] = value, column_names2 =

value

WHERE condition;

Example-

SQL > update EMPLOYEES

SET EMP_SALARY = 10000

WHERE EMP_AGE > 25;

Example-

SQL > UPDATE EMPLOYEES

SET EMP_SALARY = 120000

WHERE EMP_NAME = 'APOORV';

DELETE statement- The DELETE statement in

SQL is used to delete existing records from a table.

Syntax-

DELETE FROM table_name WHERE

some_condition;

DCL (Data Control Language)

GRANT- Give users access privileges to database.

REVOKE- Withdraw users access privileges given by

using the GRANT command.

TCL (Transaction Control Language)

COMMIT - Commit a Transaction

ROLLBACK- rollback a transaction in case of any

error occurs.

SAVE POINT- Set a save point with in a transaction.

ACID Properties

ACID properties are used for maintaining the

integrity of database during transaction processing.

ACID in DBMS stands for atomicity, consistency,

Isolation and Durability.

Atomicity- A transaction is a single unit of

operation. You either execute it entirely or do not

execute it at all. There cannot be partial execution.

Consistency- Once the transaction is executed, it

should move from one consistent state to another.

Durability- After successful completion of a

transaction, the changes in the database should

persist. Even in the case of system failures.

Relational Model Concepts

1. Attribute- Each column in a table. Attributes are

the properties which define a relation e.g.

students_Rollno, Name, etc.

2. Tables- In the Relational model the relations are

saved in the table format.

Tuple- It is nothing but a single row of a table,

which contains a single record.

Relation schema- A relation schema represents the

name of the relation with its attributes.

Degree- The total number of attributes which in the

relation is called the degree of the relation.

Cardinality - Total number of rows present in the

Table.

Relation key - Every row has one, two or multiple

attributes, which is called relation key.

ER Model

ER Model stands for an entity-Relationship model.

It is a high-level data model.

Example- Suppose we design a school database.

Name

Address

Student

id

age

ER Diagram

ER Model

Entity

Attribute

Relation

>Weak entity

> Key attribute +> One to one

>Composite

> One to many

> Multivalued

> Many to one

>Derived

> Many to many

1. Entity- An entity many be any object, class, person

or place.

Ex- Manager, product, employee etc.

Employee

Work

for

Department

Database Management Systems

54

YCT

(a) Weak entity- An entity that depends on another

entity called a weak entity.

Loan

Installment

2. Attribute- The attribute is used to describe the

property of an entity.

For example- Id, age, contact number, name etc.

id

phone_no

student

name

age

(a) Key attribute- The key attribute is used to

represent the main characteristics of an entity

represent a primary key.

id

phone_no

student

name

age

(b) Composite attribute- An attribute that

composed of many other attributes is known as a

composite.

The composite attribute is represented by an ellipse.

name

first_name

last_name

middle_name

(c) Multivalued Attribute- An attribute can have

more than one value.

A student can have more than one phone number.

phone_no.

(d) Derived attribute- It can be represented by a

dashed ellipse. An attribute that can be derived from

other attribute.

name

Birth Date

Student

Roll no,

age

3. Relationship- Diamond or rhombus is used to

represent the relationship. A relationship is used to

describe the relation between entities.

Teacher

Teaches

Department

(a) One-to-one relationship- When only one

instance of an entity is associated with the

relationship.

Example- A female can marry to one male and a

male can marry to one female.

Female

1

married to

1

Male

(b) One-to-many relationship

Example- Scientist can invent many inventions,

but the invention is done by the only specific

scientist.

Scientist

1

invents

M

Invention

(c) Many-to-one relationship

Example- Student enrolls for only one course, but a

course can have many students.

Student

M

enroll

1

Course

(d) Many-to-many relationship

Example- Employee can assign by many projects

and project can have many employees.

Employee

M

is assigned

M

Project

Notation of ER Diagram

Company

one to one

one to many

many

Employee

one or more

O

zero or one

0

zero or many

Projects

Integrity Constraint

Integrity Constraint

Domain

Constraint

Key

Constraint

Entity

Integrity

Constraint

Referential

Integrity

Database Management Systems

55

YCT

1. Domain Constraints- Defined of a valid set of

values of an attribute.

Example-

ID

NAME

SEMENSTER

AGE

1000

Tom

1st

17

1001

Johnson

2nd

24

1002

Morgan

8th

A

Not allowed, because, AGE is an integer, attribute.

2. Entity Integrity- The entity integrity state that

primary key value can't be null.

Example-

EMPLOYEE

Emp_ ID

Emp_NAME

SALARY

123

Jak

30000

164

John

20000

Jackson

27000

Not allowed as primary key can't contain

a NuLL value.

3. Referential Integrity- Referential integrity in

DBMS is based on primary and foreign key. the rule

defines that a foreign key have a matching primary

key.

Example-

<Employee>

EMP_ID

EMP_NAME

DEPT_ID

<Department>

DEPT_ID

DEPT_NAME

DEPT_ZONE

The rule states that the DEPT_ID in the employee

table has a matching valid DEPT_ID in the

Department table.

To allow join Primary Key and

Foreign Key have same data types.

EMP_ID

EMP_NAME

DEPT_ID

01

Rahul

D01

02

Kumar

D02

03

Raj

D03

Foreign Key

Primary Key

DEPT_ID

DEPT_NAME

DEPT_ZONE

D01

Computer

East

D02

Science

West

D03

Art

South

4. Key constraints- Its entity set uniquely.

ID

NAME

SEMESTER

AGE

1000

Tom

1 st

17

1001

Johnson

2nd

24

1002

Kate

3rd

21

1001

Morgan

8th

22

Not allowed because all row must be unique.

KEY IN DBMS

Key is dbms is an attribute or set of attributes which

helps you to identify a row (tuple) in a relation

(table).

Key help you to identify any row of data in a table.

In a real world application, a table could contain

thousands of records.

There are mainly seven different types of key.

Super Key- A super key is a group of single or

multiple keys which identifies row in a table.

Primary Key- Primary key is a column or group of

columns in a table that uniquely identify every row

in that table.

Candidate Key- Candidate key is a set of attributes

that uniquely identify tuples in a table Candidate

key is a super key with no repeated attributes.

Alternate Key- Alternate key is a column or group

of columns in a table that uniquely identify every

row in that table.

Foreign Key- Foreign key is a column that creates

a relationship between two tables the purpose of

foreign key is to maintain data integrity and allow

navigation between two different instances of an

entity.

Compound Key- Compound key has two or more

attributes that allow you to uniquely recognize a

specific record.

Surrogate Key- An artificial key which aims to

uniquely identify each record is called surrogate

key.

Primary Key Example-

CREATE TABLE PERSONS (

ID int Not NULL

LastName varchar(255),

first Name varchar(255),

Age int,

PRIMARY Key (ID)

);

Create Primary Key (ALTER TABLE statement)

Database Management Systems

56

YCT

Syntax-

the syntax to create a primary key using the ALTER

TABLE statement in SQL is;

ALTER TABLE table_name;

ADD CONSTRAINT constraint_name,

PRIMARY Key (column1, column2,

column_n);

FOREIGN KEY ON CREATE TABLE

the following SQL creates a FOREIGN KEY on

the "personID" column when the "orders" table is

created.

CREATE TABLE ORDERS (

order ID int NOT NULL,

orderNumber int NOT NULL,

personID int,

PRIMARY KEY (orderID),

Foreign KEY (person ID) REFERENCES

persons (person ID)

);

Relational Algebra

Relational Algebra is procedural query language,

which take relation as input and generates relation

as output.

Relational Algebra works on the whole table at

once, so we do not have to use loops etc to iterate

over all the rows of data one by one.

ID

Name

Age

1

Akon

17

2

Bkon

19

3

Ckon

15

4

Dkon

13

Select Name

student with

age less than

17

1

Output

Name

Ckon

Dkon

We can use Relational

algebra to fetch data

from this table (relation)

The output for query

is also in form of a

table, with results in

different columns.

Basic/Fundamental Operations-

1. Select (o)

2. Project (T)

3. Union (U)

4. Set difference (-)

5. Cartesian product (x)

6. Rename (P)

1. Select operation (o)- This is used to fetch rows

(tuples) from table (relation) which satisfies a given

condition.

Syntax: op(r).

· o is the predicate.

· r stands for relation which is the name of the table.

· p is prepositional logic.

Example: o age>17(student)

This will fetch the tuples (rows) from table student,,

for which age will be greater than 17.

oage>17 and gender = 'Male' (student)

This will return tuples (rows) from table student

with information of male students, of age more than

17.

BRANCH_NAME

LOAN_NO

AMOUNT

Down town

L-17

1000

Redwood

L-23

2000

Perryride

L-15

1500

Downtown

L-14

1500

Mianus

L-13

500

Roundhill

L-11

900

Perryride

L-16

1300

Input:

«BRANCH_NAME="Perryride"(LOAN)

Output:

BRANCH_NAME

LOAN_NO

AMOUNT

Perryride

L-15

1500

Perryride

L-16

1300

2. Project Operation (7)

· Project operation is used to project only a certain

only a certain set of attributes of a relation.

· In simple words, if you want to see only the names

all of the students in the student table, then you can

use project operation.

Syntax of project Operator (T)-

Tt column_name1, column_name2,

column_nameN(table_name)

Example-

TName,Age(student)

Above statement will show as only the Name and Age

columns for all the rows of data in student table.

3. Union Operation (U): This operation is used to

fetch data from two relation (tables) or temporary

relation (result of another operation).

Syntax: AUB

Tt student (Regular class) U Tstudent (extraclass)

4. Set difference (-): This operation is used to find

data present in one relation and not present in the

second relation.

Database Management Systems

57

YCT

Syntax-

A-B where A and B are relations.

Example- If we want to find name of student who

attend the regular class but not the extra class, then

we can use the below operation.

Tstudent (Regular class) - Tstudent (Extra class)

5. Cartesian product (x)- This is used to combine

data from different relation (tables) into one and

fetch data from the combined relation.

Syntax- (A×B)

6. Rename operation (P)-

. This operation is used to rename the output

relation for any query operation which returns result

like select, project etc.

Syntax- P(Relation New, Relation old)

the rename operation is used to rename the output

relation. It is denoted by rho (p).

JOIN in DBMS

· A JOIN clause is used to combine rows from two or

more tables, based on a related column between them.

· Join in DBMS is a binary operation which allows

you to combine Join product and selection in one

single statement.

Types of SQL JOIN

1. INNER JOIN

2. LEFT JOIN

3. RIGHT JOIN

4. FULL JOIN

Example- EMPLOYEE

EMP _ID

EMP _Name

CITY

SALARY

AGE

1

Angelina

Chicago

200000

30

2

Robert

Austin

300000

26

3

Christain

Denver

100000

42

4

Kristen

Wash int on

500000

29

5

Russell

Losangels

200000

36

PROJECT-

PROJECT_NO

EMP _ID

DEPARTMENT

101

1

Testing

102

2

Development

103

3

Designing

104

4

Development

1. INNER JOIN- In SQL INNER JOIN selects

records that have matching values in both tables as

long as the condition is satisfied.

table 1

table2

Syntax-

SELECT tables1.column1, table1.column2

FROM table1 INNER JOIN table2

ON

table1.matching_column=table2.matching_columns

Query-

SELECT EMPLOYEE.EMP_NAME,

PROJECT.DEPARTMENT

FROM EMPLOYEE INNER JOIN PROJECT

ON PROJECT.EMP_ID = EMPLOYEE_ID

Output-

EMP_NAME

DEPARTMENT

Angelina

Testing

Robert

Development

Christian

Designing

Kristen

Development

2. LEFT JOIN- The SQL Left JOIN returns all the

values from left table and the matching values from

the right table.

· If there is no matching join value, it will return

NULL.

table A

table B

Syntax-

SELECT table1.column1, table1.column2 FROM

table1 LEFT JOIN table2

ON

table1.matching_column=table2.matching_column:

QUERY-

SELECT

EMPLOYEE.EMP_NAME,

PROJECT.DEPARTEMENT

FROM EMPLOYTEE LEFT JOIN PROJECT

ON PROJECT.EMP_ID=EMPLOYEE.EMP_ID;

Output-

EMP_NAME

DEPARTMENT

Angelina

Testing

Robert

Development

Christian

Designing

Kristen

Development

Russell

NULL

Marry

NULL

3. RIGHT JOIN- IN SQL, RIGHT JOIN returns all

the values from the values from the rows of right

and the matched values from the left table. If there

is no matching in both tables, it will return NULL.

O

table A

table B

Database Management Systems

58

YCT

Syntax-

SELECT table1. column1, table1.column2

FROM table1 RIGHT JOIN table2

No

table1.matching_column

=

table2.matching_column_,

4. FULL JOIN- In SQL, FULL JOIN is the result

of a combination of both left and right outer join.

Join table have all the records from both tables. It

puts NULL on the place of matches not found.

table A

table B

Syntax-

SELECT table1.column1, table1.column2

FROM table1 FULL JOIN table2

ON

table1.matching_column=table2.matching_column;

SQL Basic Structure

1. Basic structure of an SQL expression consists of

select, from and where clauses.

· From clause corresponds to cartesian product lists

relation to be used.

· Where clause corresponds to seclection predicate

in relational algebra.

To fetch the entire table or all the fields in the

table.

· SELECTFROM table_name;

WHERE SQL Clause

WHERE clause s used to specify/apply any

condition while retrieving, updating or deleting data

from a table. This clause is used mostly with

SELECT, UPDATE and DELETE query.

The basic syntax of the SELECT statement with the

WHERE clause is as shown below-

SELECT column1, column2, columnN FROM

table_name;

ID

NAME

AGE

ADDRESS

SALARY

1

Ramesh

32

Ahmadabad

2000.00

2

Khilan

25

Delhi

500.00

3

Kaushik

23

Kota

2000.00

4

Chaitali

25

Mumbai

6500.00

5

Hardik

21

Bhopal

8500.00

6

Komal

22

MP

4500.00

7

Mufty

24

Indore

1000.00

SQL > SELECT ID, NAME, SALARY

FROM CUSTOMERS

WHERE SALARY > 2000;

Example-

Consider the CUSTOMERS table having the following

records-

The following code is an example which would fetch

the ID, Name and salary fields from the CUSTOMERS

table, where the salary is greater than 2000-

This would produce the following result.

ID

NAME

SALARY

4

Chaitali

6500.00

5

Hardik

8500.00

6

Komal

4500.00

7

Mufty

1000.00

· From Clause

· From clause can be used to specify a sub query

expression in SQL.

· Sub queries in the from clause are supported by

most of the SQL implementation.

Syntax-

SELECT column1, column2 FROM

(SELECT column_x as C1, column_y FROM table

WHERE PREDICATE_x) as table2 WHERE

PREDICATE;

SET

Operations

1.

UNION

2.

UNION ALL

3.

INTERECT

4.

MINUS

Functional Dependency

Functional dependency (FD) is a set of constraints

between two attributes in a relation functional

dependency says that if two tuples have same values

for attributes A1, A2, ..... An then those two tuples

must have to have same values for attributes B1,

B2, ....... Bn.

Functional dependency is represented by an arrow

sign (->) that is,

X -> Y

Trivial-If a functional dependency (FD) X->Y

holds where Y is a subset of X, then it is called a

trivial FD. Trivial FDs always hold.

Non-Trivial- If an FD X -> Y holds, where Y is

not a subset of x, then it is called a non-trivial FD.

Completely non-trivial- If an FD X->Y holds,

where X intersect Y = ¢, it is said to be a

completely non-trivial FD.

Armstrong's Axioms- If F is a set of functional

dependencies then the closure of F, denoted as F+, is

the set of all functional dependencies logically

implied by F.

Database Management Systems

59

YCT

. Armstrong rules-

1. Reflexive Rule

2. Augmentation Rule

3. Transitivity Rule

Aggregate function in SQL

SQL aggregation function is used to perform the

calculations on multiple rows of a single column of

a table.

· Aggregate functions

1. count()

2. sum()

3. avg()

4. min()

5. max()

Trigger- A trigger is a stored procedure in database

which automatically invokes whenever a special

event in the database occurs.

Syntax- Create trigger [Trigger_name] [before/after)

{insert|update|delete} on [table_name]

[for each row]

[trigger_body]

Normalization- Non loss decomposition and functional

dependencies, first, second and third normal forms

dependency preservation, Boyce/codd normal form.

Decomposition- The process of breading up or

dividing a single relation into two or more sub

relations is called as decomposition of a relation.

Decomposition

Lossless

Decomposition

Dependency

preserving

Dependency preserving

are the desirable

properties of

decomposition

Update anomalies- If data items are scattered and

are not linked to each other properly, then it could

lead to strange situations.

Deletion anomalies- We tried to delete a record,

but parts of it was left undeleted because of

unawareness, the data is also saved somewhere else.

Insert anomalies- We tried to insert data in a

record that does not exist at all.

Normalization is a method to remove all these

anomalies and bring the database to a consistent

state.

First Normal Form

First Normal form is defined in the definition of

relations (table) itself.

Course

Content

Programming

Java, C++

Web

HTML, PHP

We rearrange the relation (table) as below to

convert it to first normal form.

Course

Content

Programming

Java

Programming

C++

Web

HTML

Web

PHP

Each attribute must contain only a single value from

its pre-defined domain.

Second Normal Form

Second normal form, we need to understand the

following-

Prime attribute- An attribute which is a part of the

candidate key, is known as a prime attribute.

Non-prime attribute- An attribute which is not a

part of the prime-key, is said to be a non-prime

attribute.

· If we follow second normal form, then every non-

prime attribute should be fully functionally

dependent on prime key attribute.

· That is, if X-> A holds, then there should not be

any proper subject Y of X, for which Y-A also

holds true.

Student_project

Stu_ID

Proj_ID

Stu_Name

Proj_Name

Student-

Stu_ID

Stu_Name

Proj_ID

Project-

Proj_ID

Proj_Name

Third Normal Form

For a relation to be in third normal form, it must be

in second normal form and the following must

satisfy.

No non-prime attribute is transitively dependent on

prime key attribute.

Student_Detail-

Stu_ID

Stu_Name

City

Zip

Database Management Systems

60

YCT

Student_Detail-

Stu_ID

Stu_Name

Zip

Zip codes-

City

Zip

Boyce-Codd Normal form

· BCNF is an extension of third normal form on

strict terms.

. For any non-trivial functional dependency, X -> A

X, must be a super key.

· In above image Stu_ID is the super key in the

relation student_Detail and zip is the super key in

the relation zip codes.

Stu_ID -> Stu_Name, Zip

and zip -> city (which conforms that both the

relation are in BCNF).

Fourth normal form (4NF)

A relation will be 4NF if it is Boyce/codd normal

and has no multi valued dependency.

for a dependency A -> B, if for single value of

multiple value of B exists, then the relation will be a

multi-valued dependency.

Fifth normal form (5NF)

A relation in 5NF if it is in 4NF and not contains

any join dependency and joining should be lossless.

5NF is also known as project-join normal form

(PJ/NF).

Transaction Management In DBMS-

· A transaction is set of logically related operation.

· Now that we understand what is transaction we

should understand what are the problems

associated with it.

· To solve this problem, we have the following two

operations.

· Commit- If all the operations in a transaction are

completed successfully then commit those

changes to the database permanently.

. Rollback- If any the operations fails then

rollback all the changes does by pervious

operations.

States of transaction- Transaction can be implemented

using SQL queries and sever.

Partially

Committed

Active

end

Failed

Aborted

Active state-

. The active state is the first state of every

transaction. In this state, the transaction is being

executed.

For Example- Insertion or deletion or updating a

record is done here. But all the records are still not

saved to the database.

Partially committed- In the partially committed

state, a transaction executes its final operation but

the data is still not saved to the database.

Committed- A transaction is said to be in a

committed state if it executes all its operations

successfully.

Failed state- If any of the checks made by the

database recovery system fails, then the transaction

is said to be in the failed state.

Aborted- If the transaction fails in the middle of

the transaction then before executing the

transaction, all the executed transaction are rolled

back to its consistent state.

Two operation-

1. Re-start the transaction

2. Kill the transaction

Transaction property

The transaction has the four properties. These are

used to maintain consistency in a database, before

and after the transaction.

Property of transaction

1. Atomicity

2. Consistency

3. Isolation

4. Durability

1. Atomicity- It states that all operation of the

transaction take place at once if not the transaction

is aborted.

2. Consistency- A transaction must after the database

from one steady state to another steady state. This is

the responsibility of both the DBMS and the

application developers to make certain consistency.

3. Isolation- Transactions that are executing

independently of one another is the primary concept

followed by isolation.

4. Durability- The durability property is used to

indicate the performance of the database consistent

state.

Implementation of Atomicity and durability-

The recovery management component of a database

system can support atomicity and durability by a

variety of schemes.

Database Management Systems

61

YCT

Shadow copy-

In the shadow copy scheme, a transaction that wants

to update the database first creates a complete copy

of the database.

Figure below depicts the scheme, showing the

database state before and after the update.

Db-pointer

Db-pointer

Old copy

of

data base

Old copy

of

data base

New copy

of

data base

before update

after update

Shadow-copy technique for atomicity and durability

Schedule- A series of operation from one

transaction to another transaction is known as

schedule.

Schedule

Serial

Schedule

Non-serial

Schedule

Serializable

Schedule

Serializability in DBMS

Some non-serial schedules may lead to

inconsistency of the database. Serializability is

mainly of two types-

Types

of

Serializability

Conflict

Serializability

View

Serializability

Conflict serializability- If a given non-serial

schedule can be converted into a serial schedule by

swapping its non-conflicting operations, then it is

called as a conflict serializable schedule.

Conflict operations- Two operations are called as

conflicting operations if all the following conditions

hold true for them.

. Both the operation belong to different transaction.

. At least one of the two operations is a write

operations.

Example- Consider the following schedule

Transaction T1

Transaction T2

R1(A)

R2(A)

W1(A)

R1(B)

In this schedule,

· W1(A) and R2(A) are called as conflicting

operations.

. This is because all the above conditions hold ture

for them.

VIEW Serializability- View serializability is a

process to find out that a given schedule is view

serializable is not.

Two schedules S1 and S2 are said to be view

equivalent if they satisfy the following conditions.

1. Initial Read- An Initial read of both schedules

must be the same suppose two schedule S1 and S2.

IN schedule S1, if a transaction T1 is reading the

data item A, then in S2, transaction T1 should also

read A.

T1

T2

T1

T2

Read (A)

Write (A)

Read(A)

Write (A)

Schedule S1

Schedule S2

2. Update Read-

T1

T2

T3

T1

T2

T3

Write(A)

Write(A)

Read (A)

Write(A)

Write (A)

Read (A)

Schedule S1

ScheduleS2

3. Final write-

T1

T2

T3

T1

T2

T3

Write (A)

Read(A)

Write (A)

Write (A)

Read(A)

Write(A)

Transaction Isolation Levels in DBMS

The SQL standard defines four isolation levels.

1. Read uncommitted

2. Read committed

3. Repeatable Read

4. Serializable

Failure Classification-

1. Transaction Failure

2. System Crash

3. Disk Failure

1. Transaction failure- Transaction failure occurs

when it fails to execute or when it reaches a point

from where it can't go any further.

1. Logical error

2. Syntax error

2. System Crash- System failure can occur due to

power failure or other Hardware or Software failure.

Example- Operating system error

Database Management Systems

62

YCT

3. Disk Failure- It occurs where hand-disk drives or

storage drives used to fail frequently.

Problems with Concurrent Execution- In a database

transaction, the two main operation are READ and

WRITE operations.

(i) Lost Update Problem (W-W Conflict)

(ii) Dirty Read Problems (W-R Conflict)

(iii) Unrepeatable Read Problem (W-R Conflict)

Lost Update Problem (Write-Write Conflict)- Let's

take the value of A is 100

Time

Transaction T1

Transaction T2

t1

Read (A)

t2

A= A-50

t3

Read(A)

t4

A= A+50

t5

Write (A)

t6

Write (A)

· At ti times, T1 Transaction reads the value of A i.e.

100.

. At t2 Time, T1 Transaction deducts the value of A

by 50.

Dirty Read Problem (W-R Conflict)- This type of

problem occurs when one transaction T1 update a data

item of the database, and then that transaction falls due

to some reason but its updates are accessed by some

other transaction.

Example- Lets value A is 100.

Time

Transaction T1

Transaction T2

t1

Read (A)

t2

A=A+20

t3

Write(A)

t4

Read(A)

t5

A=A+30

t6

Write(A)

t7

Write (B)

Unrepeatable Read Problem (R-W Conflict)-

Example- Let take value A is 100

Time

Transaction T1

Transaction T2

t1

Read (A)

t2

Read(A)

t3

A=A+ T30

t4

Write (A)

t5

Read (A)

CONCURRENCY CONTROL- Concurrency

control is the working concept that is required for

controlling and managing the concurrent execution

of database and thus avoiding the in consistencies in

the database.

Two-PHASE LOCKING (2PL)- The Two-Phase

locking protocol divides the execution phase of the

transaction into three parts.

Lock is

attained

Lock is

released

T-Begin

T-end

Time

There are two phases of 2PL-

1. Growing phase

2. Shrinking phase

Example-

T1

T2

0

LOCK -S(A)

1

LOCK -S(A)

2

LOCK -X(B)

3

−

−

4

UNLOCK (A)

5

LOCK -X(C)

6

UNLOCK (B)

7

UNLOCK (A)

8

UNLOCK (C)

9

−

−

The following way shows how unlocking and

locking work with 2-PL.

Transaction T1

· Growing phase from step 1-3

· Shrinking phase from step 5-7

. Lock point at = 3

Transaction T2

· Growing phase from step 2-6

· Shrinking phase from step 8-9

. Lock point at 6

Strict two-phase locking (strict-2PL)

The first phase of strict-2PL is similar to 2PL.

Strict-2PL protocol does not have shrinking phase

of lock release.

Lock is

attained

Release

at commit

1

T-Begin

T-end

Time

Database Management Systems

63

YCT

Basic Time stamp ordering protocol works as

follows-

1.Check the following condition whenever a

transaction Ti issues a Read (X) operation.

· If W_Ts (X) > Ts(T;) then the operation is

rejected.

· If W_T$(X) <= Ts(Ti) then the operation is

executed.

2. Check the following condition whenever a

transaction Ti issues a write (X) operation.

· If Ts (Ti) < R_Ts (X) then the operation is

rejected.

· If Ts(Ti) < W_Ts(X) the operation is rejected and

Ti is rolled back other waise the operation is

executed.

Where,

Ts(Ti) denotes the time tap of the transaction Ti-

R_Ts(X) denotes the Read time_stamp of

data_itemX.

W_Ts(X) denotes the write time_stamp of

data_itemX.

Validation Based Protocol- Validation phase is also

known as optimistic concurrency control technique the

transaction is executed in the following three phase.

1. Read phase

2. Validation phase

3. Write phase

THOMAS WRITE RULE- Thomas write rule provides

the guarantee of serializability order for protocol.

The Basic Thomas Write rules as follows.

· If Ts(T)<R+Ts(X) then transaction T is aborted and

rolled back and operation is rejected.

· If Ts(T)<W_Ts(X) then don't execute the

W_item(X) operation of the transaction and

continue processing.

. If neither condition 1 nor condition 2 occurs, then

allowed to execute write operation by transaction Ti

and set W_Ts(X) to Ts(T).

MULTIPLE GRANULARITY

Granularity- It is the size of data item allowed to

lock.

Multiple Granularity- It can be defined as

liearachically breaking up the database into blocks

which can be locked.

Hence, the levels of the tree starting from the top

level are as follow.

1. Database 2. Area 3. File 4. Record

DB

A1

A2

Fa

Fb

F.

Fa

(R21)

(Ran) (Rbi)

(Rbn)

(Ren)

Multi Granulanity tree Hierarchy

Recovery and Atomicity

· When a system crashes, it may have several

transaction being executed and various file opened

for them to modify the data items.

. But according to ACID properties of DBMS

atomicity of transaction as a whole must be

maintained, that is, either all the operations are

executed or none.

Log-Based Recovery- The log is a sequence

of records. Log of each transaction is maintained in

some stable so that if any failure occurs, then it can be

recovered from there.

There we two approach to modify the database

1. Deferred database modification

2. Immediate database modification

Recovery with concurrent transactions

Concurrency control means that multiple

transactions can be executed at the same time and then

the inter leaved logs occur.

Recovery with concurrent transactions can be

done in the following four ways.

1. Interaction with concurrency control

2. Transaction rollback

3. Check point

4. Restart recovery

BUFFER Management- The buffer manager is the

software layer that is responsible for bringing pages

from physical disk to main memory as needed. The

buffer manages the available main memory by dividing

the main memory into a collection of pages, which we

called as buffer pool the main memory pages in the

buffer pool are called frames.

ARIES Algorithm- Algorithm for recovery and

isolation exploiting semantics (ARIES) is based on the

write Ahead Log (WAL) protocol. Every update

operation writes a log record which is one of the

following-

Database Management Systems

64

YCT

1. Undo-only log record- Only the before image is

logged.

2. Redo-only log record-Only the after image is logged.

3. Undo-redo log record- Both before image and

after images are logged.

The recovery process actually consists of 3 phases.

1. Analysis

2. Redo 3. Undo

Remote Backup

Remote backup provides a sense in case the primary

location where the database is located gets

destroyed. Remote backup can be offline or real-

time or online.

Network

Remote

data backup

Local data backup

File- A file is named collection of related

information that is recorded on secondary storage

such as magnetic disks, magnetic tables and optical

disks.

S.

No.

SQL

No SQL

1.

RELATIONAL

DATABASE

MANAGEMENT

SYSTEM

(RDBMS)

No-relational

or

distributed

database

system.

2.

These databases

have fixed or static

or predefined

schema.

They have dynamic

schema.

3.

These data bases

are not suited for

hierarchical data

storage.

These database are

best

suited

for

hierarchical

data

storage.

4.

Follows ACID

property

Example- MySQL,

Oracle, MS-SQL

Server etc.

Follows

CAP

(Consistency,

availability, partition

tolerance)

Example- MongoDB,

GraphQL, HBase, ect.

NoSQL Database

We know that MongoDB is a NoSQL database, so it

is very necessary to know about NoSQL database to

understand MongoDB throughly.

NoSQL database is used to refer a non-SQL or non

relational database.

Advantages of NoSQL-

1. It supports query language

2. It provides fast performance

3. It provides horizontal scalability

MongoDB advantages over RDBMS- MongoDB is a

new and popularly used database it is a document

based, non relational database provider.

MongoDB Advantages

· MongoDB is schema less.

· There may be difference between number of fields,

content and size of the document from one to other.

· Structure of a single object is clear in MongoDB.

· There are no complex joins in MongoDB.

· Distinctive features of MongoDB.

Easy to use

Light weight

Extremely faster than RDBMS

Where MongoDB should be used-

· Big and complex data

· Mobile and social infrastructure

. Content management and delivery

· User data management

· Data hub

MongoDB Datatypes

Following is a list of usable data types in MongoDB.

Data type

Description

String

String is the most commonly used

data type. It is used to store data.

Integer

Integer is used to store the numeric

value. It can be 32 bit or 64 bit

depending on the server you are using.

Boolean

This data type is used to store Boolean

values. It just shows yes/no values.

Double

Double data type stores floating point

values

Arrays

This data type is used to store a list or

multiple values into a single key.

Object

Object data type is used for embedded

documents.

Null

It is used to store null values.

Database Management Systems

65

YCT

06.

THEORY OF COMPUTATION

Theory of Computation(TOC)-

It is the mathematical study of computing machine

and their capabilities.

OR

It is the study of automata theory and formal

languages.

Ambiguity problem-(undecidable).

· The general problems are two types known as-

1. Decidable problem

2. Undecidable problem

. To estimate the Nature of problem some

mathematical tools are used which is known as

Automata.

· Automata is mathematical model in which are

study practical situation of computer science.

Alphabet 'E'- Finite non-empty set of symbols.

Example- {0,1}, {a,b,c,d}

String- Finite sequence of symbols over the given alphabet 'Z'.

Example- {0, 1} repetition allowed. | |"

{0, 1,0,1}

{0, 1,0,1,0,1}

Length ->

4

6

Epsilon (€) - Length will be zero.

Language - Any set of strings over the given alphabet.

L1: set of all string of length

{0,1}

L = {0,1,10,01 ........ }

· The set can finite, infinite, empty.

· Finite language : (strings are finite)

· Infinite Language : (strings are Infinite)

. Empty Language : L = {E}, finite length

L= {E}-> Valid String

L = {€, 0, 1, 00, 11, 01, 10

}

↓

Complete Language = >

Substring- Consecutive sequence of symbols over

the given string known as substring.

Ex. Mode -> 4 length

Hence,

Total Number of Substring =

N(N+1)

+1

2

Power of Σ : Σ= {a, b }

1

Set of all string of length 1, = {a, b}

2

{aa, ab, ba, bb}

3| 8

0

Set of all string of length zero = {E } or |E|

*

0

1

2

= {E} U {a, b} U {aa, ab, ba, bb}

= Infinite

= Complete language

Finite Automata

Finite automata is the mathematical model which

contains finite number of state and transition defined

between the states.

Finite Automata

DFA

Mealy m/c

Moore m/c

NFA

Finite Automata

without output

Finite Automata

with output

Deterministic Finite Automata (DFA)

Finite Automata can be represented by following

two methods.

· Transition diagram

· Transition table

DFA: It is finite Automata in which from each and

every state on every input symbol exactly one

transition exist.

DFA is formally define as five tuple :

Q = Finite Number of state

Input alphabet

q0 = Initial state

F = Final state

8 = Transition function

DFA (Q, , q0, F,8)

Transition Function ->

Qx

Q

a

a

b

q0

q1

b

DFA

a,b

a,b

90

q1

{qo-q1} x (a, b)

{q0.a}

{q0.b}

{qi.a}

{q1.b}

Acceptance of DFA: By reading string from left to

right end of the string the DFA enter into secure

final state than the given string accepted otherwise

rejected.

Theory of Computation

66

YCT

The set of string accepted by given DFA is known as

Language of the DFA, Hence Every DFA represents

exactly one language.

a/b

a/b

a/b

b

q0

'b

>

40

<

'b

a,b

a/b

a/b

90

'b

Ib

Valid DFA's

Empty Language accepted:

In any DFA, if no final state exist, or final state are

not reachable from initial state than the language

accepted by DFA is Empty Language.

In any DFA if initial state is also final state then 'e'

is also accepted by DFA.

Dead State: If any non-final state having self loop

on input symbol than that state is known as dead

state.

By reading any input, if automata in DFA and if we

don't reach to final state then that input is rejected.

C-programming language = set of all valid program.

Program void main ()

{

int a, b;

{

L (Language)

String S -> F

Yes (Accept)

No (Reject)

Finite Representation

A Finite Automata is said to accept a language if all

the strings in the language are accepted and all the

string are rejected which are not presented in the

language.

DFA (Minimal)-

@= {a, b}, |c| ≤2

L = {€, a, b, aa, ab, ba, bb}

a,b

a,b

a,b

qo

q1

q2

D

•

||=2

|0|≥2

a,b

a,b

a,b

a,b

a,b

D

||=n

|o|≥n

(n + 1) state

(n + 2) state,

•

|0|≤2

a,b

a,b

a,b

D

|o|≤n

(n + 2) state

Minimal DFA:

@ E {a, b}

|| mod 2 = 0

L = {€, aa, ab, ba, bb} aaaa,

3

Even

Odd

a,b

|@| mod 2 = 1

a,b

a,b

|c| mod 3 = 0

a,b

a,b

a,b

=|@ |=1mod3

|c| mod n = 0

'n' length string

3->3

4->4

.

.

n ->n

· Minimal DFA- @ € {a, b) *

na(@) =2 (exactly two a's)

L = {aa, aba, baa, aab,

3

b

b

a,b

D

a

a

a

· na(@) ≥ 2 (at least two a's)

b

b

a,b

a

a

· na (@) ≤ 2 (at most two a's)

b

b

b

a,b

D

a

a

a

· @ E {a, b) *

na(@) mod 2= 0

na(@) = 0 mod 2

b

a

b

a

Theory of Computation

67

YCT

b

ee

eo

b

a

a

a

a

b

oe

00

b

· WE {a, b) *

na(@) = o mod 2

and

nb(@) = o mod 2

E, aa, bb, aabb

abab

L=

baba

1

bbbb

na(@)

nb(@)

even

even

€, aa, bb

even

odd

aab

odd

odd

ab

odd

even

abb

Compliment of DFA- By interchanging final state

into non-final state and non-final state, then we can

get the compliment of DFA.

b

a

a

A

B

b

. If language accepted by DFA is '1' then

compliment of DFA accept "E* - 1".

· Compliment is applicable only for DFA.

Note- We cannot get the compliment of NFA and e-

NFA.

Chomskey Hirarchy-

· Finite automata having one stack memory element

know as push down automata.

· The comparison element remember the stack to

perform validation of string in push down

automata.

. Hence language L2 is accepted by push down

automata but not finite automata.

· To accept language L3 finite automata phase and

push down automata phase hence turning machine

is constructed.

· The language for which FA is possible know as

Regular language.

· The language for which PDA is possible know as

CFL.

· The Language for which LBA is possible know as

CSL.

· The language for which TM is possible know as

REL.

Note- FA -> Finite Automata

PDA -> Push Down Automata

CFL -> Context-Free Language

CSL -> Context Sensitive Language

TM -> Turing Machine

REL -> Recursively Enumerable Language

LBA -> Linear Bounded Automata

Type 3+

REL

TM

Type 2+

CSL

LBA

CFL

Type 1

PDA

Regular

DFA

Type 0

Language

FA

-

Regular

NFA

Power Sequence = [TM > LBA > PDA > FA]

Expressive Power-

· Number of language accepted by particular

automata know as expressive power of that

Automata.

. It is important to note that DFA and NFA are of

same power because every NFA can be converted

into DFA and every DFA can be converted into

NFA.

· The turning machine i.e. TM is more powerful

than any other machine.

Minimization of DFA

Equivalent state- Two state q1 and q2 are equivalent

+XE Z* both 8(q1,x) and 8(q2, x) result either

final state or non-final state otherwise they are not

equivalent.

State Equivalence Algorithm- To detect equivalent

state for two algorithm exist know as-

· State equivalence algorithm

· Marking algorithm

There minimization algorithm application for only

for DFA (Non-applicable for NFA and E-NFA)

After apply minimization algorithm for any DFA

then the language accepted by DFA remains same.

Before apply minimization algorithm all not

reachable state one eliminated first.

Minimum Number of State of following-

a

b

a

91

93

a

Dead state

a

qo

a

b

95

a

b

92

94

b

b

Theory of Computation

68

YCT

a

b

{q0, 91, 92,93}{q4}

->qo

q1

q2

{q, q1, q2} {q3} {q4}

q1

q1

q3

{q0, 92} {q1} {q3} {94}

q2

q1

q2

{q0, 921 1913193)1943

q3

q1

q4

*

q4

q1

q2

Total = 4 state

Construct the Minimal DFA-

L = {a" b"/n, m ≥ 1}

L = {ab, aabb, aaab, abb

3

a

b

b

A

B

C

a

a

D

. Construct the minimal DFA for the language.

L = {1, 2, 4 ...... 2"}

all these number are in unary.

L= {1,11, 1111 ........ }

L= {12n/n>0}

not possible

•

r mod n

n is odd

n is even

n state

n state

2

m

(n is not power of 2)

m + 1

n/2 odd

n/2

n/2 + 1

n/2/2/2 add of +2

· Construct a minimal DFA that accept all the

strings of 0's and 1's which contains.

(i) 0 1 as substring

L = {01, 010, 011, 101, 001

}

1

0

0

1

0,1

90

91

92

Non-Deterministric Finite Automata (NFA)

In NFA from the given state and the given input

signal there may be '0' transition or '1' transition or

more than '1' transition exist.

· NFA is formally different (Q, E 8, q0, F)

Q-> Finite no. of state

Σ -> Input alphabet

qo -> Initial state

F -> Set of final state

8 -> Transition function

· Minimization algorithm not applicable for NFA.

. Complementation is not applicable for the NFA.

· In NFA for valid string also Non-final paths or

transition may exist.

Construction of NFA

1. Construct NFA that accept all string of a'b and b's

where each string ending with abab.

a,b

90

91

92

93

94

a

b

a

b

2.

With aba or abb

b

a,

b

q

q2

a

a

qo

qf

b

a

93

94

b

NFA to DFA conversion-

Subset construction algorithm (Equivalence

algorithm)

· Construct DFA equivalent to solving NFA.

0

1

VO

90

91

1

1

NFA:

0

1

0

90

q1

0, 1

> qo

q0 91

qoq1

*

q1

91 190, 913

0,1

[9% q1]

19% qi][90

E-closer- E-closer state of which starting by

reading only E-reachable state. The initial state of

DFA is E-closer initial state of NFA.

Properties of FA-

1. Emptyness problem

2. finiteness problem

3. Equivalence problem

4. Membership problem

1. Emptyness problem- It means, checking whether

language accepted by the given FA is empty or not.

Step-1 -> Eliminate all non-reachable state form

DFA.

(ii) To resultant automata at least one. Final item

exist and we accept non-empty language other

empty language.

a

b

b

b

A

B

O

a

a,b

b

X

Y

a

2. Finiteness problem- It means checking whether

language accepted by given automata is finite or not.

Theory of Computation

69

YCT

a

b

0

1

A

B

C

>

A

B

b

a,b

0

D

3. Equivalence problem- Checking whether given

two automata accept same language.

4. Membership problem- It means checking whether

the Exist 'x' in the given automata or not.

x, y, z. E = {a, b}

I/P alphabet (> = {a, b})

b

V

a

a

X

y

b

Regular Expression

· The simplest way of represent regular languages

know as regular expression.

· Regular expression can be constructed by using

following '3' operand and input symbols as operands.

* - > Kleene closer

+ -> Union operator

. - Concatenation operation

1.L={ } ¢

2. L = {E} €

3. L = {a} a

4. L = {a, b} ab

5. L = (a, b) a + b

6. L = {€, a, aa, aaa ...... } a*

7. L = {a, aa, aaa ...... } a+

· For one regular language, there, may be possibility

of having many regular expression by but one

regular expression represent only one regular

language only.

Identities of Regular Expression

1. R + $ = ¢ + R = R

2. R.p = ¢.R = ¢

3. R.E = E.R = R

4. R* = (R*)* = (R+)* = (R*)+

5. RR* = R+ = R*R

6. R+ + € = R*

7. a(ba)* = (ab)*a

8. a + b = b+a

9. ab # ba

10. (a+b)* * (ab)*

11. (a+b)* * (a*b*)

12. (a + b)* * a* + b*

13. (a + b)* = (a* + b*)* = (a* + b)* = (a +b*)* =

(a*b*)*

14. € *= €; €+ = €

15. 0* = €, ¢* = ¢

Regular Expression

Converstion

> Finite Automata

(RE => E-NFA) Thomson construction

Regular

Expression

E-NFA

1. ¢

90

qf

Basic R.E.

2. €

qo

qf

Basic R.E.

3. a

a

qo

qf

Basic R.E.

4. 11.12

€

q0

ľ1

ľ2

5. 11 + 12

€

rı

€

€

€

ľ2

6. 11*

E

€

€

ľ1

€

7. 11+

E

€

€

r1

8. ¢+

€

€

€

Construct NFA for RE-

(a + b)* (aa + bb) (a +b)*

(a+b)*(aa+bb)(a+b)*

a, b

a

aa+bb

b

a

a

b

a

a

2

b

b

b

F.A as output generator or FA with O/P

Mealy M/C

Moore M/C

· Mealy- Mealy is mathematical model in which

output is associated with transition.

a/1

b/0

b/0

qo

q1

a/1

Theory of Computation

70

YCT

. Moore- Moore is mathematical model in which

output is associated with state.

a

2

b

b

90. 1

'b

0

a

Definition- (Q, Σ, 90, Δ, δ, λ)

Q-> Infinite Number of states

Σ -> Input alphabet

qo -> Initial state

4 -> Output state

8 -> Transition function

2 -> Output function

Mealy Machine => Q×2->4

Moore Machine => Q->4

· Mealy and Moore Machine are deterministic in

nature hence from each and every state input symbol

exactly one transition exist.

. There is no final state in Mealy and Moore Machine

because they are not acceptors, they are output

generators.

· Mealy and Moore Machine are practical use in Ckt

design.

· Mealy and Moore Machine can be represented

transition table or transition diagram.

Mealy Machine

· Construct Mealy Machine that represents behaviour

of 1's complement of binary number ckt.

0/1

1/0

qo

· Construct the Mealy Machine that represents 2's

complement of binary number Ckt behaviour.

(Assume that we are reading the string from LSB to

MSB and carry is discarded)

While reading the string from LSB initially any

number of zero replace them by zero until we get

first '1' replace as it is and then complement

remaining things.

0/0

0/1

1/1

Lo

'b

11/0

· Construct Mealy Machine that contain all the string

of a's and b's and produces one as output if last two

symbol input are same otherwise produce.

qo

a/0

q1

a/1

q2

b/0

b/1

a/1

a/0

q0

a/0

b/0

b/0

Tb/1

· Construct the Moore Machine that takes all strings

of 0's and 1's as input and produces A's output if

input is ending with 10 or produces B's output if

input is ending with 11 otherwise C as output.

0

0

1

q0, C

1

91,

C

0

92

4

1

0

q3, B

1

· Construct the Moore Machine that takes all binary

number if input and produces residue modulo '3' as

output.

0

1

q0, 0

1

q1,

1

0

q2;

2

1

1

0

· Construct the Moore Machine that takes all base '3'

as input and produces residue modulo 4 as output.

0

1

2

[q0,1]

q2

[q1,2]

q3 90

q1

[q2,3]

92 93

q0

[q3,4]

q1 92

q3

Moore to Mealy Machine Conversion

· Construct the Equivalent Mealy Machine to

following Moore Machine

b

a

b

q0, 1

91, 2

92, 3

a

b

Theory of Computation

71

YCT

· Mealy Machine-

b/3

a/2

b/3

q0

q1

q2

a/1

a/2

b/1

Mealy Machine to Moore Machine Conversion-

a/1

a/0

q0

b/0

a/0

b/0

b/1

Moore Machine-

91, 0

a

a

q0

a

b

91, 1

a

a

b

b

q2, 0

b

q2, 1

b

. While converting from Mealy Machine to Moore

Machine number of state of Moore M/C may

increases because there may be possibility of having

more than one output at one state hence splitting of

states happens.

· While converting from Mealy M/C to Moore M/C

Maximum number of state possible in Moore M/C

from the given 'n' state m-output symbol Mealy M/C

is n*m.

Regular Language Detection

(i) Finite language is always regular, but all regular

language need not be finite.

(ii) Finite Automata having finite memory, hence

the language which requires finite comparison

can be recognized by FA.

(iii) Finite Automata fails to accept language, which

requires infinite memory.

(iv) Any infinite language having comparison

between symbol is non-regular.

(v) Palindrome language has one symbol regular

and over more them one symbol are non-

regular.

Pumping Lemma

· Pumping Lemma is the theorem using to prove non-

regular language as non-regular.

· Pumping Lemma uses prove by contradiction

strategies.

•

non-regular-

Pumping Lemma -non-regular

Contradiction

Method steps- L = {a" b"/n ≥ 1} non regular

1. Assume L is regular

2. L = FA = n state

3. |z|≥n

4. |z|

↑

u|v|w

5. Loop string

6. uv, we Vi>0

u, v W ¢ L, non regular.

Steps-

To prove language 'L' is non-regular

(i) Assume L is regular

(ii) If 'L' is regular than their exist finite Automata

for 'L' assume 'n' states on their.

(iii) Select some |z| string |z| from length whose

length is greater than or equal to n.

· Divide |z| string in three parts (u, v, w) such length

of v is |v| ≥1.

. If L is regular for all Vi ≥ 1,

u v, WE L

at least i value u v w ø L then L is non-regular.

Closure properties of Regular Language

1. Union Operation-

L1 = Regular Language = FA1

L2 = Regular Language = FA2

F

€

E

LIUL2-

Regular

Thomson

algorithm

€

€

F

2

Hence regular language are closed under union.

Theory of Computation

72

YCT

2. Sub-set Operation- The subset of regular language

may or may not regular, hence regular language are

not closed under subset operation.

a" b" ca* b* c (a +b)*

Non-regular Regular

3. Concatenation-

L1 = Regular Language = a" = FA1

L2 = Regular Language = b" = FA2

FA1

€

FA2

L1

L2

Regular language are closed under concatenation.

Note- Let 'LI' and 'L2' are two Regular Language F1 and

F2 are finite Automata for L1 and L2 is always

regular. Hence Regular Language are closed under

concatenation.

4. Kleene Closure-

L -> Regular Language

the FA exist

€

L *= >

FA1

€

€

5. Positive Kleene closure-

€

LE>

€

€

FA

(i) Let 'L' be a Regular Language and 'F' be the finite

Automata for 'L' then the Kleene closure of it,

always regular because FA exists as follows.

(ii) Let 'L' is Regular Language F be the FA for 'L'

then the positive closure of it always regular because

FA as follow.

6. Complementation-

L - Regular Language

>* - L => Regular

Compliment of Regular Language is always regular

because can construct complemented DFA by

interchanging final state as non-final and non-final

state as final.

7. Intersection-

L1 -> Regular

L2 -> Regular

LIL = LIUL2)

Intersection is closed under Regular Language.

. Whenever union and complement one closed then

intersection is also closed. Hence finally Regular

Language are closed under intersection.

8. Reversal Operation-

L = {a" b"} => LR = {b" a"}

a

b

a

b

a

b

90

91

92

90

91

92

b

· Reversal of Regular Language is always Regular

because Regular Language are closed under reversal.

· Reversal operation on regular expression applied

as follows-

1-(E+F)R=ER+FR(001+110)R=>100011

9. Init Operation-

Init (L)- Init of language 'L' is set of all prefix of all

string of the language.

10. Substitution operation-

L= {a" b"/n, m ≥ 1}

S(L) = {0"1"/n, m ≥ 1}

Substitution (s) is a mapping from £ -> A where

each symbol of _ is replaced by a Regular

Language over the 4.

S(0) = ¢

S(E) = €

S(a) = a

11. Homomorphism Operation- Homomorphism is a

special case of substitution where each symbol of _

can be replaced by A single string for the 4.

1. H(+)=¢

2. H(E) = €

3. H(a) = a

4. H(a+b) = H(a) +H(b)

Two DFA

a

a

b

b

Finite

control

2DFA -> (Q, E, δ, q0, F)

8 : Qx E->Qx{L,R}

· 2-DFA is a DFA which is capable to move Left as

well as right side direction.

. 2-DFA is formally defined as follows.

Theory of Computation

73

YCT

Acceptance method- By reading the string starting

from left if the 2DFA enter into. Final state

whenever M/C is halted. Then the string is accepted

otherwise string is rejected.

Equivalence classes-

· Equivalence class of state 'q' is set of string by

which we can reach state 'q' from the initial state.

· The number of equivalence for given Regular

Language is number of states of minimal DFA

exist for that language.

GRAMMARS

· Set of rules used for describe rules for the language.

· Grammar is following determines as:

N = Set of non-terminals [S, A, B]

T = Set of terminals [a, b]

P = Number of production S -> ab/ba/c/€

S = Starting symbol

Example- S -> AB

A ->a

B-> b

Every grammar is formed a -> B

where ß is replacement of 'a'

Derivation- The process of generating string from

the given grammar know as derivation.

· The derivation can be either left most derivation

(LMD) or completely right most derivation (RMD).

S

Derivation

S

AD

LMD

RMD

AB

aB

Ab

ab

ab

LMD- It is process of derivation in which left most

non-terminal is replaced by its right hand side part.

RMD- It is process of derivation in which right

most non-terminal is replaced by its RHS part at

every set.

Parse Tree or Derivation Tree-Tree representation

of the derivation know as parse tree all heaf node of

parse tree know as yield of the parse tree.

S

A

B

a

b

Yield of the Parse Tree

Sentential Form-

· Every step in the derivation is one sentential form

sentential form may be collection of terminals and

non-terminals.

· The derivation is LMD then sentential form is left

sentential form.

· Every grammar represent one language.

. For CFL their exist grammar context free

grammar.

· For CSL their exist grammar context sensitive

grammar.

Types of Grammars

Types 3 Grammars

or

Regular Grammar

Types 2 Grammars

or

Context Free

Grammar

Right

Linear

Grammar

Left

Linear

Grammar

A->a

a € (V + T)*

S -> asb/ab

A->x A/x

A->Ax/x

A, B E V

x E V*

Type 1 grammar

or

Context sensitive

grammar

Type 0 grammar

or

Unrestricted

grammar

α - β

|a| ≤|B|

a, ß E (V + T)*

α - β

a € (V + T)*

ß E (VUT)*

. All grammar is of the form of a, B, a should

contain at least order.

Linear Grammar- In any grammar their exist

exactly one non-terminal on LHS and almost one

non terminal (A) on RHS.

· The linear grammar can be left linear or Right

grammar or middle linear.

· Regular grammars are not one class of linear

grammar hence all regular grammar are linear

grammar but all linear grammar need not be

regular.

Regular Grammar- Grammar is called a type 3 or

regular grammar if all its production are type 3

production. A production S -> A is allowed in type

3 grammar, but in this case S does not appear on the

right-hand side of any production.

S -> bs/aA

A -> bA/aS/€

Theory of Computation

74

YCT

Context Free Grammar

Context-free languages are applied in parser design.

They are also useful for describing block structures

in programming languages. It is easy to visualize

derivations in context-free languages as we can

represent derivations using tree structures.

The language generate by context-free grammar are

known as CFL.

S ->AB

S -> asb/ab

A ->a

Regular

Non- Regular

B ->b

· Checking whether the given CFG is Regular or

not, is undecidable.

Ambiguity Problem

A terminal string @ E L (G) is ambiguous if there

exist two or more derivation tree for @ (or these

exist two or more left most derivation of @).

S -> S*S/S+S/ num

S

S

S

*

S

S

+

S

S

+

S

num

num

S

*

S

4

2

num

num

3

num

3

num

4

2

=>5×4=20

2+(3×4) =14

Unambiguous Grammar

The grammar is said to be unambiguous for all string

if the grammar exist only one parse tree or only one

LMD or one RMD or if one LMD and one RMD

ever exist but both produces the same parse tree.

1. a=b+c *d;

S -> id/E

E -> E +E/ E*E |id;

E ->E+E

> E+E*E

-> id + E * E

->id + id*E

-> id + id * E

Inherently Ambiguous Grammar

· In ambiguous grammar from which elimination of

ambiguity is not possible.

Example-The following language is inherently

ambiguous CFL Means, all of its grammar are

ambiguous and elimination of ambiguity is not

possible for each grammar.

S->S1/S2

S1 -> AB

A -> aAb/ab

B -> CB/C

SL -> PQ

P -> aP/Q

Q -> bQC/bc

Simplification of context free grammar-

(i) Useless Variable

(ii) Unit Production

(iii) Null Production

. Elimination of useless variable- It means

elimination of variable from the grammar which are

not deriving any string and also eliminate variable

which are not required for derivation.

· Variable not reachable from S (Starting Symbol).

(ii) Unit Production- Any production of the form

"A->B" known as unit production.

(iii) Null Production (A->€)- Any production like

"A->€" known as Null production.

Normal Form of CFG

Chomsky Normal

form

(CNF)

Greibach Normal

form

(GNF)

A -> BC

A -> av*

A ->a

a € T

A, B, C E V

a € T

(i) Normal form of CFG means applying condition

on RHS of the production.

(ii) To normalize the grammar, it should be

simplified.

(iii) There are mainly two normal forms known as

Chomsky and Greibach normal form.

GNF Normal Form- A ->av*

(a) Convert into GNF?

S-> AB

A -> aA|bB|b

B -> b

· The grammar is left recursive grammar, then

eliminate the left recursion to convert into GNF.

Decision Properties of CFG-

(i) Emptyness

(ii) Finiteness

Decidable

(iii) Membership

(i) Emptyness- Checking whether CFG generate

empty language or not.

Theory of Computation

75

YCT

Algorithm-

(a) Eliminate useless variable from the given

grammar.

(b) Starting symbol is also useless then that grammar

generates empty language otherwise non-empty.

(ii) Finiteness problem- It means checking whether

given CFG generates finite language or not.

Algorithm-

(a) Convert the given grammar into CNF grammar.

(b) Construct CNF graph.

(iii) Membership Problem or Parsing Algorithm-

(a) Checking whether string 'x' is generated from

given CFG or not.

(b) Checking whether given string is member of

given grammar or not, know as parsing.

(c) The algorithm which performs parsing, know as

parsing algorithm or membership algorithm.

Push Down Automata (PDA)

Input Tape

aabb

Î

Infinite

Finite Control

q0, 91 ..... In

1

Zo

FA + stack = PDA

PDA(Q, E, qo, F, δ, Zo, Γ)

Q-> Finite number of state

E -> Input alphabet

qo -> Initial state

F -> Set of final states

Zo -> Initial stack element

> Stack element

8 -> Transition function

Qx EU {e} x[ >Qx[*

Notations

Transition diagram

Transitions

PDA

DPDA

NDPDA

· PDA is only one type only, but recognize or are

two types, DPDA, NDPDA.

Definition-

(i) There is only one type of PDA, that is language

recognizer (No output generator).

(ii) Expressive power of NPDA is more than

DPDA.

(iii) By default PDA means N-PDA.

(iv) There are two type of acceptance methods to

accept a string in PDA, they are-

· Empty Stack Method

· Final State Method

Example- L = {b"a" /n≥1}

(a) Empty Stack Method- By reading the string

from left to right, end of the string. If the stack is

empty then the given string is accepted and irrelative

about number of final state.

(b) Final State Method- By reading the starting

from left to right, end of the string, the PDA enters

into final state, then given string is accepted and

irrelative about stack symbol.

Parsing and Push Down Automata

(i) Top-Down Parsing- We present certain

techniques for top-down parsing which can be

applied to a certain subclass of context free

languages. We discuss LL(1) parsing, LL(K)

parsing, Left factoring and the technique to remove

left reversion.

(ii) Bottom up Parsing- In bottom-up parsing we

have to reverse the productions to gets finally. This

suggests the following moves for a PDA acting as

bottom up parser.

(a) 8(P, A, a") = {(P, A)| there exists a production

A ->a}

(b) δ(Ρ,σ,^) = (Ρ,σ)} forall oin Σ.

Using (i) we replace a™ on the basis by A when

A->a is a production the input symbol o is moved

on to the stack using (ii) for acceptability we require

some moves when the PDS has S or z0 on the top.

Theory of Computation

76

YCT

Turing Machine Model

Turing's Aim-

Design a model that is-

(i) simple (ii) Intuitive (iii) Generic

Aabaa

Read/write head

(moves in both

directions)

Tape divided

into cells and of

infinite length ..

n

q0

q1

Finite control

q3

q2

. The Turing Machine can be thought of as finite

control connected to a R/W (read/write) head. It

has one tape which is divided into a number of

cells.

. A Turing machine M is a 7-tuple, namely (Q, E, F,

8, qo, b, F)

1. Q is finite nonempty set of states.

2. [ is a finite nonempty set of tape symbols.

3. be [ is the blank

4. E is a non-empty set of input symbols and is a

subset of | and b € E,

5. 8 is transition function mapping (q, x) on to (q, y,

D) where D denotes the direction of movement of

R/W head; D=L or R according as the movement is

to the left or right.

6. q0 € Q is the initial state.

7. F _ Q is the set of final states.

Representation of Turing Machines

(i) instantaneous descriptions using move-relations.

(ii) transition table

(iii) transition diagram

Nondeterministic Turing Machines

· A non-deterministic Turing machine is a 7-tuple

(Q, Σ, Γ, δ, q, b, F)

(i) Q is a finite nonempty set of states

(ii) [ is a finite nonempty set of tape symbols

(iii) be [ is called the blank symbol.

(iv) E is a nonempty subset of [, called the set of

input symbols.

(v) q0 is the initial state.

(vi) Fc Q is the set of final states.

(vii) 8 is a partial function from Q x [ into the power

set of Q x | x {L, R}.

Recursive Enumerable (RE) or Type-0

Language- RE language or type-0 language are

generated by type-0 grammars. It means TM can

loop for ever for the string which are not a part of

the language. RE languages are also called as Turing

recognizable languages.

Recursive Language (REC)- REC language are

also called as Turing decidable languages the

relationship between RE and REC language can be

shown in figure.

RE

REC

Closure Properties of Recursive Languages

· Union- If L1 and if L2 are two recursive languages,

their union L1 O L2 will also be recursive because if

TM halts for L1 and halts for L2, it will also halt for

LI UL2.

· Concatenation- If L1 and if L2 are two recursive

languages, their concatenation L1, L2 will also be

recursive.

· Kleene Closure- If L1 is recursive, its Kleene

closure L1* will also be recursive.

· Intersection and complement- If L1 and if L2 are

two recursive languages, their intersection L1 2 L2

will also be recursive.

Linear Bounded Automata

· A linear bounded Automata is a multi-track non-

deterministic Turing machine with a tape of some

bounded finite length.

Length = function

(length of the initial input string, constant C)

A linear bounded automata can be defined as an 8-

tuple (Q, X, E, q, Mi, MR, d, F)

(i) Q is a finite set of states

(ii) X is the tape alphabet

(iii) E is the input alphabet

(iv) q0 is the initial state

(v) ML is the left end marker

(vi) MR is the right end marker were MR # ML

(vii) 8 is a transition function which maps each pair

(state, tape symbol) to (state, tape symbol,

constant 'C') where C can be o or +1 or -1

Theory of Computation

77

YCT

(viii) F is the set of final state

End

End

1

1

Left End

Marker

Right End

Marker

A deterministic linear bounded automaton is always

context sensitive and the linear bounded automaton

with empty language is undecidable.

Context Sensitive Language

· A context sensitive grammar is an unrestricted

grammar in which all the productions are of form.

α - β

Where a, B E (VUT)* and |a| ≤ |B|

where a and B are strings of non-terminals and

terminals.

· Context-sensitive grammars are more powerful

than context free grammars because there are

some languages that can be described by CSG but

not by context free grammars and CSL are less

powerful than unrestricted grammar.

Unrestricted

Grammar

(REL and RL)

Context

Sensitive

Grammar

Context

Free

Grammar

· Context sensitive grammar has 4-tuples.

G = {Ν, E, P,S}

N = Set of non-terminal symbols

E = Set of terminal symbols

S = Start symbol of the production

P = Finite set of production

All rules in p are of the form a, a2 -> a1 Ba2

· The language that can be defined by context

sensitive grammar is called CSL.

Properties of CSL are-

· Union, intersection and concatenation of two

context sensitive languages is context sensitive.

· Complement of a context-sensitive language is

context-sensitive.

DECIDABILITY

· A decision problem is a function that associates

with each input instance of the problem a truth

value true or false.

· A decision problem is decidable if there exists a

decision algorithm for it otherwise it is

undecidable.

Decidability properties of regular languages-

(i) DFA membership-

Instance : ADFAM = {Q,E, 8,q0, F} and string @ €

Σ *.

(ii) DFA emptiness-

ADFA m = {Q, E, δ, q0, F}

Undecidable problems-

We will now discuss the notion of undecidability.

N

W

m

yes

yes

Input

W

W

m'

yes

no

A decider for the Language L

· All computations of a decider TM must halt.

Decidable language are often called also recursive

language.

· A language is Turing recognizable if it is

recognized by a TM.

Theorem- LTM accept is undecidable the proof (to

be gone through in class) show that in fact the more

restricted language.

Lsel accept = {{ M, < M >> M is a TM} is

undecidable the crucial idea is diagonalization.

Complexity-

The classes P and NP- We introduce the classes P

and NP of languages.

. A Turing Machine M is said to be of time

complexity T(n) if the following holds. Input w of

length n, M halts after making at most T(n)

moves.

. A language L is in class P if there Exists come

polynomial T(n) such that L = T(m) for some

deterministic Tm m of time complexity T(n).

Theory of Computation

78

YCT

07.

COMPILER DESIGN

Overview of Language Processing System

Source Program with Macros

Preprocessor

Modified Source Program

Compiler

Target Assembly Program

Assembler

Relocatable Machine Code

Loader/linker

Library files,

Relocatable object files

Absolute Machine Code

Compiler- Compiler is a translator program that

translates a program written in (High Level

Language) the source program and translate it into

equivalent in (Machine Level Language) the target

program. As an important part of a compiler is error

showing to the programmer.

Source

Program

Compiler

Target

Program

Error

Message

Assembler- Programmers found it difficult to write

or read programs in machine language. They begin

to use a mnemonic (symbols) for each machine

instruction, which they would subsequently

translate into machine language. Such a mnemonic

machine language is now called an assembly

language. Programs known as assembler were

written to automate the translation of assembly

language in to machine language.

Interpreter- An interpreter converts high level

language into low level machine language, just like

a compiler. But they are different in the way they

read the input. The compiler in one go reads the

inputs, does the processing, and executes the source

code whereas the interpreter does the same line by

line. A compiler scans the entire program and

translates it as a whole into machine code whereas

an interpreter translates the program one statement

at a time. Interpreted programs are usually slower

with respect to compiled ones.

Loader/Linker- It converts the re-locatable code

into absolute code and tries to run the program

resulting in a running program or an error message.

Linker loads a variety of object files into a single

file to make it executable. Then loader loads it in

memory and executes it.

Structure of the compiler Design

Input Source Program

Lexical Analyzer

Front End

(analysis Phase)

Syntax Analyzer

Symbol Table

Manager

Semantic Analyzer

Intermediate Code

Generator

Error

Handler

Code Optimizer

Code Generator

Back End

(Synthesis Phase)

Out Target Program

LEXICAL ANALYSIS

Lexical analysis is the first phase of the compiler

also known as a scanner. It converts the high level

input program into a sequence of Tokens.

· Lexical analysis can be implemented with the

Deterministic Finite Automata (DFA).

· The output is a sequence of tokens that is sent to the

parser for syntax analysis.

Tokens

Source

Program

Lexical

Analyzer

Parser

Get Next Token

Symbol

Table

· Token- Token is a sequence of characters that can

be treated as a single logical entity. Typical token

are, (1) Identifiers (2) Keywords (3) Operators (4)

Special symbols (5) Constants.

· Pattern- A set of strings in the input for which the

same token is produced as output. This set of strings

is described by a rule called a pattern associated

with the token.

· Lexeme- A lexeme is a sequence of characters in

the source program that is matched by the pattern

for a token. e.g- "float", "=", "273".

FLEX (Fast Lexical Analyzer Generator)- FLEX

is a computer program for generating lexical

analyzers written by Vern Paxson in C around 1987.

It is used together with Berkeley Yacc Parser

Compiler Design

79

YCT

generator or GNU Bison parser generator. FLEX

and Bison both are more flexible than Lex and Yacc

and produces faster code. Bison produces parser

from the input file provided by the users. The

function yylex() is automatically generated by the

flex when it is provided with a .I file and this

yylex() function is expected by parser to call to

retrieve tokens from this token stream.

Note- The function yylex() is the main flex

function that runs the Rule section and extension (.1)

is the extension used to save the programs.

Lex.yy.c

Lex.1 file

or

Lex

Compiler

file

C

compiler

a.out file

Sequence

of tokens

lex source

Input

stream

program

Program Structure- In the input file, there are 3

sections.

(i) Definition Section- The definition section contains

the declaration of variables, regular definitions,

manifest constants. In the definition section, text is

enclosed in "%{%}" brackets. Anything written in

this brackets is copied directly to the file lex.yy.c.

(ii) Rules Section- The rules section contains a series

of rules in the form; pattern action and pattern must

be unintended and action begin on the same line in

{} brackets. The rule section is enclosed in

"%%%%".

(iii) User Code Section- This section contains C

statements and additional functions. We can also

compile these functions separately and load with the

lexical analyzer.

Parsing

A program that performs syntax analysis is called a

parser. A syntax analyzer takes tokens as input and

output error message if the program syntax is wrong.

Parser obtains a string of tokens from the lexical

analyzer and verifies that it can be generated by the

language for the source program. The parser should

report any syntax errors in an intelligible fashion.

Types of Parsing

Parsers

Topdown parsers

(predictive parser)

Bottom up parsers

Recursive Non-recursive precedence

descent

descent

parsing

parsing

parsing

Operator

(LR parsers)

SLR CLR LALR

Constructing a parsing table- To construct a

parsing table, we have to learn about two functions:

1. FIRST() 2. FOLLOW()

1. FIRST(X)- To compute FIRST(X) for all grammar

symbols X, apply the following rules until no more

terminals or & can be added to any FIRST set.

1. If X is a terminal, then FIRST(X) is {X}.

2. If X -> & is a production, then add & to FIRST(X).

3. If X is non-terminal and X-> Y Y2 .... YK is a

production, then place 'a' in FIRST(X) if for some i,

a is an FIRST(Y;) and & is in all of FIRST(Y;).

,

FIRST(Yi-1); that is, Y1, .... , Yi-1 => *8.

If & is in FIRST(Y;) for all j = 1,2, ..... , k then add &

to FIRST(X). For example, everything in

FIRST(Y1) is surely in FIRST(X). If Y1 does not

derive &, then add nothing more to FIRST(X), but if

Y1 =>*8, then add FIRST(Y2) and so on.

2. FOLLOW(A)- To compute FOLLOW(A) for all

non-terminals A, apply the following rules until

nothing can be added to any FOLLOW set.

1. Place $ in FOLLOW(S), where S is the start

symbol and $ is input right end marker.

2. If there is a production A => a B B, then

everything in FIRST(B) except & is placed in

FOLLOW(B).

3. If there is a production A -> aB or a production

A->aBB, where FIRST(B) contains &, then

everything in FOLLOW(A) is in FOLLOW(B).

LR Parsers

· In LR(K), L stands for Left to right scanning, R

stands for Right most derivation, K stands for

number of look ahead symbols.

· LR parsers are table-driven, much like the non-

recursive LL parsers. A grammar which is used in

construction of LR parser is LR grammar. For a

grammar to be LR it is sufficient that a left-to-right

shift-reduce parser be able to recognize handles of

right-sentential forms when they appear on the top

of the stack.

· The time complexity for such parsers is O(n3).

· LR parsers are faster than LL(1) parser.

· LR parsing is attractive because-

-> The most general non-backtracking shift reduce

parser.

-> The class of grammars that can be passed using

LR methods is a proper super set of predictive

parsers, LL(1) grammars CLR(1) grammars.

-> LR parser can detect a syntactic error in the left

to right scan of the input.

The LR parsing algorithm-

· It consists of an input, an output, a stack, a driver

program and a parsing table that has two parts

(action and go to).

· The driver/parser program is same for all these LR

parsers, only the parsing table changes from parser

to another.

a1

a2

....

a¡

....

an

$

Input

Stack

S,

Predictive parsing

Program

X,

m

Output

SI

States

Terminals

Non-terminals

X1

So

0

1

2

Action

part

Go to

part

Compiler Design

80

YCT

Stack- To store the string of the form.

S0 X1 S1 ..... XmSm where

Sm : state

Xm: grammar symbol

Each state symbol summarizes the information

contained in the stack below it.

Parsing Table- Parsing table consists of two parts-

(i) ACTION Part-

Let,

Sm -> top of the stack

aj -> current symbol

Then action [Sm, a;] which can have one of four

values.

1. Shift S, where S is a state.

2. Reduce by a grammar production A->B

3. Accept

4. Error

(ii) GO TO Part- If goto (S, A) = X where

S->state, A -> non-terminal, then GOTO maps

state S and non-terminal A to state X.

Configuration-

(SoxIS, X2S2 ... SmSm, ajaj +1 .. an $)

The next move of the parser is based on action [Sm, a;].

The configurations are as follows-

1. If action [Sm, aj] = Shift S

(SoXIS1, X2S2 ... XmSm, ajaj +1 ... an $)

2. If action [Sm, aj] = reduce A -> B then

(Sox1S1 X2S2 ... Xm-rSm-r, As ajaj +1 ... an $)

where S = goto [Sm-r, A]

3. If action [Sm, aj] = accept, parsing is complete.

4. If action [Sm, aj] = error, it calls an error recovery

routine.

SLR parsing table construction

1. Construct the canonical collection of sets LR(0) items

for G'. Where G' the augmented grammar for G.

2. Create the parsing action table as follows:

(a) If a is a terminal and [A-> a aß] is in Ij, go to

(Ii, a) = Ij then action (i, a) to shift j. Here 'a' must be

a terminal.

(b) If [A ->a] is in I¡, then set action [i, a] to

'reduce A -> a' for all a in FOLLOW(A);

(c) If [S'->S] is in I¡ then set action [i, $] to

'accept'.

3. Create the parsing go to table for all non-

terminals A, if go to (Ii, A) = I; then go to [i, A] = j.

4. All entries not defined by steps 2 and 3 are made

errors.

5. Initial state of the parser contains S' -> S.

The parsing table constructed using the above

algorithm is known as SLR(1) table for G.

Note-Every SLR(1) grammar is unambiguous, but every

unambiguous grammar is not a SLR grammar.

Canonical LR Parsing (CLR)

· To avoid some of invalid reductions, the states

need to carry more information.

· Extra information input into a state by including a

terminal symbol as a second component of an item.

· The general form of an item.

[A -> aß, a]

Where A -> aß is a production.

a is terminal/right end marker ($). We will call it as

LR(1) item.

'LR(1) item is a combination of LR(0) items along

with look ahead of the item. Here 1 refers to look

ahead of the item.'

Construction of the sets of LR(1) items

Function closure(I):

Begin

Repeat

For each item [A-> a.B.B, a] in I,

Each production B -> y in G',

And each terminal b in FIRST(Ba)

Such that [B->y, b] is not in I do

Add [B -> y, b] to I;

End;

Until no more items can be added to I;

L. ALR Parsing Table

· The tables obtained by it are considerably smaller

than the canonical LR table.

· LALR stands for look ahead LR.

· The number of states in SLR and LALR parsing

tables for a grammar G are equal.

· But LALR parsers recognize more grammars than

SLR.

. YACC creates a LALR parser for the given

grammar.

· YACC stands for 'Yet another compiler compiler'.

· An easy, but space-consuming LALR table

construction is explained below:

1. Construct C = {I0, I1, .... , In}, the collection of sets

of LR(1) items.

2. Find all sets having the common core; replace these

sets by their union.

3. Let C' = {J0, J1, .... Jm} be the resulting sets of LR(1)

items. If there is a parsing action conflict then the

grammar is not a LALR(1).

4. Let K be the union of all sets of items having the

same core. Then goto (J, X) = K.

. If there are no parsing action conflicts then the

grammar is said to LALR(1) grammar.

. The collection of items constructed is called

LALR(1) collection.

Comparison of parsing methods-

CLR(1)

LALR(1)

SLR(1)

LR(0)

LL(1)

Every LR(0) in SLR (1) but vice versa is not true.

Compiler Design

81

YCT

Syntax Directed Translation- To translate a

programming language construct, a compiler may

need to know the type of construct, the location of

the first instruction, and the number of instructions

generated etc so, we have to use the term 'attributes'

associated with constructs.

An attribute may represent type,

number of arguments, memory location,

compatibility of variables used in a statement which

cannot be represented by CFG alone.

So, we need to have one more phase to

do this, i.e., 'semantic analysis' phase.

Syntax

tree

Semantic Analysis

Semantically

checked

syntax tree

In this phase, for each production CFG, we will

given some semantic rule.

Syntax Directed Definition (SDD)

It is high level specification for translation. They

hide the implementation details, i.e., the order in

which translation takes place.

Attributes + CFG + Semantic rules = SSD

A SDD is a generalization of a CFG in which each

grammar symbol is associated with a set of

attributes. There are two types of set of attributes

for a grammar symbol.

1. Synthesized attributes

2. Inherited attributes

Each production rule is associated with a set of

semantic rules. Semantic rules setup dependencies

between attributes which can be represented by a

dependency graph. The dependency graph

determines the evaluation order of these semantic

rules. Evaluation of a semantic rule defines the

value of an attribute. But a semantic rule may also

have some side effects such as printing a value.

Attribute grammar- An attribute grammar is a

syntax directed definition in which the functions in

semantic rules 'cannot have side effects'.

Annotated parse tree- A parse tree showing the

values of attributes at each node is called an

annotated parse tree. The process of computing the

attribute values at the nodes is called annotating (or

decorating) of the parse tree.

In a SDD, each production A -> o is

associated with a set of semantic rules of the form:

b = f(C1, C2, ...... Cn) where

f : A function

b can be one of the following:

b is a 'synthesized attribute' of A and C1, C2,

Cn are attributes of the grammar symbols in

A> 00

The value of a 'synthesized attribute' at a node is

computed from the value of attributes at the

children of that node in the parse tree.

Synthesized Attribute- The value of a synthesized

attribute at a node is computed from the value of

attributes at the children of that node in a parse tree.

Consider the following grammar:

L ->En

E->E1+T

E ->T

T->T1*F

T->F

F ->(E)

F -> digit

Let us consider synthesized attribute value with

each of the non-terminals E, T and F Token digit

has a synthesized attribute lexical supplied by

lexical analyzer.

Production

Semantic Rule

L -> En

print (E.val)

E -> E1+ T

E.val: = E1.val + T.val

E ->T

E.val: = T1.val

T->T1*F

T.val: = T1.val*F.val

T ->F

T.val: = F.val

F -> (E)

F.val: = E.val

F -> digit

F.val: = digit.lexval

Inherited Attributes- An attribute of a non-

terminal on the right-hand side of a production is

called an inherited attribute. The attribute can take

value either from its parent or form its siblings

(variables in the LHS or RHS of the production).

For example, let's say A -> BC is a production of a

grammar and B's attribute is dependent on A's

attributes or C's attributes then it will be inherited

attribute.

Types of SDD's- Syntax Directed Definitions

(SDD) are used to specify syntax directed

translations. There are two types of SDD.

1. S-attributed definitions

2. L-attributed definitions

S-attributed definitions-

· Only synthesize attributes used in syntax direct

definition.

· S-attributed grammars interact well LR(K) parsers

since the evaluation of attributes is bottom-up. They

do not permit dependency graphs with cycles.

L-attributed definitions-

· Both inherited and synthesized attribute are used.

· L-attributed grammar support the evaluation of

attributes associated with a production body,

dependency-graph edges can go from left to right

only.

· Each s-attributed grammar is also a L-attributed

grammar.

· L-attributed grammars can be incorporated

conveniently in top down parsing.

· These grammars interact will with LL(K) parsers

(both table driven and recursive descent).

A syntax directed definition is L-attributed if each

inherited attribute of Xj, 1 ≤j ≤n, on the right side

of A->X1, X2 ..... Xn, depends only on-

1. The attributes of symbols X1, X2, .... Xj-1 to the left

of Xj in the production.

Compiler Design

82

YCT

2. The inherited attributes of A.

Every S-attributed definition is L-attributed,

because the above two rules apply only to the

inherited attributes.

Intermediate Code Generation

In the analysis-synthesis model, the front end translates

a source program into an intermediate representation

(IR). From IR the back end generates target code.

Source

code

Front

end

Intermediate

representation

Back

end

Target

representation

+

.

Target

independent,

Mostly target

dependent,

Target

dependent

source dependent source independent source independed

There are different types of intermediate

representations-

· High level IR, i.e. AST (Abstract Syntax Tree).

· Medium level IR, i.e. Three address code.

· Low level IR, i.e. DAG (Directed Acyclic Graph)

· Postfix Notation (Reverse Polish Notation, RPN).

Benefits of Intermediate Code Generation (ICG)-

1. We can obtain an optimized code.

2. Compilers can be created for the different machines

by attaching different backend to existing front end

of each machine.

3. Compilers can be created for the different source

languages.

Directed Acyclic Graphs (DAG) for expression-

· A DAG for an expression identifies the common

sub expressions in the given expression.

. A node N in a DAG has more than one parent if

N represents a common sub expression.

. DAG gives the compiler, important clues

regarding the generation of efficient code to

evaluate the expressions.

Three-Address Code- In three address codes, each

statement usually contains 3 addresses, 2 for

operands and 1 for the result.

Example- x = y OP z

· x, y, z are names constants or compiler generated

temporaries.

· OP stands for any operator. any arithmetic

operator or logical operator.

Types of three address statement-

Assignment-

· Binary assignment : x = y OP z store the result of

y OP z to x.

. Unary assignment x = OP y store the result of

unary operation on y to x.

Copy-

. Simple copy x = y store y to x.

. Indexed copy x = y [i] store the contents of y[i] to

X.

· x[i] = y store y to (x + i)th address.

Address and pointer manipulation-

x = & y

store address of y to x

x = * y

store address of y to x

*x = y

store y to location pointed by x

Jump-

· Unconditional jump- goto L, jumps to L.

· Conditional:

if (x relop y)

goto L1;

else

{

goto L2;

}

where relop is <, <= , >, >=, = or ¢

Procedure call-

Param x1;

Param x2;

.

.

.

Param Xn;

Call p, n, x;

call procedure p with n parameters

and store the result in x.

return x

Use x as result from procedure.

Implementation of three Address Statements-

Three address statements can be implemented as

records with fields for the operator and the

operands. There are 3 types of representations-

1. Quadruples

2. Triples

3. Indirect triples

1. Quadruples- A quadruple has four fields: op, arg1,

arg2, and result.

· Unary operators do not use arg2.

· Param use neither arg2 nor result.

· Jumps put the target label in result.

· The contents of the fields are pointers to the

symbol table entries for the names represented by

these fields.

· Easier to optimize and move code around.

. For the expression x = y * - z + y* - z, the

quadruple representation is-

OP

Arg1

Arg2

Result

(0)

Uminus

z

t1

(1)

*

y

tı

t2

(2)

Uminus

z

t3

(3)

*

y

t3

t4

(4)

+

t2

t4

t5

(5)

=

t5

x

2. Triples- Triples have three fields: OP, arg1, arg2.

· Temporaries are not used and instead references

to instructions are made.

· Triples are also known as two address code.

· Triples takes less space when compared with

quadruples.

· Optimization by moving code around is difficult.

. The DAG and triple representations of

expressions are equivalent.

· For the expression a = y* - z + y* - z the triple

representation is-

Compiler Design

83

YCT

OP

Arg1

Arg2

(0)

Uminus

z

(1)

*

y

(0)

(2)

Uminus

z

(3)

*

y

(2)

(4)

+

(1)

(3)

(5)

=

a

(4)

3. Indirect Triples-

. In direct triples, pointers to triples will be there

instead of triples.

· Optimization by moving code around is easy.

· Indirect triples takes less space when compared

with quadruples.

· Both indirect triples and quadruples are almost

equally efficient.

· Indirect triple representation of 3-address code.

Statement

(0)

(14)

(1)

(15)

(2)

(16)

(3)

(17)

(4)

(18)

(5)

(19)

OP

Arg1

Arg2

(14)

Uminus

z

(15)

*

y

(14)

(16)

Uminus

z

(17)

*

y

(16)

(18)

+

(15)

(17)

(19)

=

x

(18)

Code Generation

Code generation is the final phase of the compiler

model.

Input

or

Source

program

Front

end

Intermediate

Code

optimization

code

Intermediate

code

1

Target

Program

Code

generation

The requirement imposed on a code generator are-

· Output code must be correct.

· Output code must be of high quality.

· Code generator should run efficiently.

Issues in the design of a code generator-

1. Input to the code generator- Intermediate

representation with symbol table will be the input

for the code generator.

· High Level Intermediate representation. Example-

Abstract Syntax Tree (AST)

· Medium-level intermediate representation.

Example-Control flow graph of complex operations.

· Low-Level Intermediate representation. Example-

Quadruples, DAGs.

· Code for abstract stack machine, i.e. postfix code.

2. Target Programs- The output of the code

generator is the target program. The output may

take on a variety of forms-

(i) Absolute machine language

(ii) Relocatable machine language

(iii) Assembly language

3. Memory Management- Mapping names in the

source program to addresses of data objects in

runtime memory is done by the front end and the

code generator.

· A name in a three address statement refers to a

symbol entry for the name.

· Stack, heap, garbage collection is done here.

4. Instruction selection- Instruction selection

depends on the factors like-

· Uniformity

· Completeness of the instruction

· Instruction speed

· Machine idioms

· Choose set of instructions equivalent to intermediate

representation code.

· Minimize execution time used registers and code

size.

5. Register allocation-

· Instructions with register operands are faster. So,

keep frequently used values in registers.

· Some registers are reserved.

Example- SP, PC etc. minimize number of loads

and stores.

6. Evaluation order-

. The order of evaluation can affect the efficiency

of the target code.

· Some orders require fever registers to hold

intermediate results.

Runtime storage management- To run a compiled

program, compiler will demand the operating

system for the block of memory. This block of

memory is called runtime storage. This runtime

storage is subdivided into the generated target code,

Data objects and information which keeps track of

procedure activations.

The runtime storage contains stack and the heap.

Stack contains activation records and program

counter, data object within this activation record are

also stored in this stack with relevant information.

Activation Record- Information needed during an

execution of a procedure is kept in a block of

storage called an activation record.

· Storage for names local to the procedure appears

in the activation record.

· Each execution of a procedure is refereed as

activation of the procedure.

Compiler Design

84

YCT

· If the procedure is recursive, several of its

activation might be alive at a given time.

· Runtime storage is subdivided into

1. Generated target code area

2. Data objects area

3. Stack

4. Heap

Code

Static data

Stack

1

1

Heap

· Sizes of stack and heap can change during

program execution.

For code generation there are two standard storage

allocations:

1. Static allocation- The position of an activation

record in memory is fixed at compile time.

2. Stack allocation- A new activation record is

pushed on to the stack for each execution of the

procedure.

Basic Blocks- Basic blocks are sequence of

consecutive statements in which flow of control

enters at the beginning and leaves at the end without

a halt or branching.

1. First determine the set of leaders.

· First statement is leader

· Any target of goto is a leader.

· Any statement that follows a goto is a leader.

2. For each leader its basic block consists of the

leader and all statements up to next leader.

Initial node: Block with first statement is leader.

Once the basic blocks have been defined, a number

of transformations can be applied to them to

improve the quality of code.

1. Global : Data flow analysis.

2. Local : Structure preserving transformations,

Algebraic transformations

Basic Blocks compute a set of expressions. These

expressions are the values of the names live on exit

from the block.

Two basic blocks are equivalent it they compute the

same set of expressions.

DAG Representation of Basic Blocks-

· DAGs are useful data structures for implementing

transformations on basic blocks.

· Tells, how value computed by a statement is used

in subsequent statements.

. It is a good way of determining common sub

expressions.

· A DAG for a basic block has following labels on

the nodes:

> Leaves are labeled by unique identifiers, either

variable names or constants.

> Interior nodes are labeled by an operator

symbol.

> Nodes are also optionally given as a sequence

of identifiers for labels.

Peephole Optimization

· Target code often contains redundant instructions

and suboptimal constructs.

· Improving the performance of the target program by

examining a short sequence of target instructions

(peephole) and replacing these instructions by a

shorter or faster sequence is peephole optimization.

· The peephole is a small, moving window on the

target program. Some well known peephole

optimizations are-

(i) Elimination of Redundant Loads and Stores-

Example-

(i) MOV R0, a

(ii) MOV a, R0

We can delete instruction (ii), because the value of a

is already in R0.

(ii) Eliminating Unreachable Code- An unlabeled

instruction immediately following and

unconditional jump maybe removed.

· May be produced due to debugging code introduced

during development.

· May be due to updates in programs without

considering the whole program segment.

(iii) Flow of control optimizations- The

unnecessary jumps can be eliminated.

Jumps like:

Jumps to jumps,

Jumps to conditional jumps,

Conditional jumps to jumps:

Example- We can replace the jump sequence

goto L1

L1 : got L2

By the sequence

Got L2

L1: got L2

....

It there are no jumps to L1 then it may be possible to

eliminate the statement L1 : goto L2.

(iv) Reduction in strength-

· x- is cheaper to implement as x*x than as a call to

exponentiation routine.

· Replacement of multiplication by left shift.

Example- x*23=>x << 3

· Replace division by right shift.

Example-x >> 2 (is x/22)

(v) Use of machine Idioms-

· Auto increment and auto decrement addressing

modes can be used whenever possible.

Example- replace add # 1, R by INCR.

Compiler Design

85

YCT

08.

OPERATING SYSTEM

Introduction

Operating system acts as an interface between computer

hardware and user. It manages and controls all the

hardware and flow of data, instructions and information

to within the system. The operating system takes

instructions from the user and directs it to CPU, which

further passes the instructions to the hardware.

User 1

User 2

User 3

User n

Compiler Assembler

Text editor

Data base

System and Application Programs

Operating System

Computer Hardware

. Abstract view of the components of a computer system.

Operating system is one of the core software programs

that run on hardware and makes it usable. The user can

interact with hardware so that they can send commands

and receive output. An operating system provides an

interface between user and machine. This interface can

be Graphical User Interface (GUI) in which users. Click

on screen elements to interact with operating system or

a Command Line Interface (CLI) to tell the operating

system to do things, it also manages the computers

resource such as CPU, memory, disk drives and

printers. It provides services for application software.

Types of Operating System

Network

Operating

Systems

Batch

Processing

Operating

Systems

Multi-

tasking

Operating

Systems

Multi-

processor

Operating

Systems

Types of

Operating

System

Real-time

Operating

Systems

Embedded

Operating

systems

Distributed

Operating

system

Mobile

Operating

systems

Function of an Operating System-

Memory

Management

Secondary

Storage

Management

Process

Management

Job

Accounting

File

Management

Functions

of

Operating

System

Security

Device

Management

Communication

Management

Networking

Command

Interpretation

Operating system Services-

User and Other System Programs

GUI

Batch

Command Line

User Interfaces

System Calls

Program

Execution

I/O

Operations

File

Systems

Commun-

ication

Resource

Allocation

Accounting

Error

detection

Protection

and

Security

Services

Operating System

Hardware

Process concept

> Text Section- A process is more than the program

code, which is sometimes known as the text section.

It also includes the current activity, as represented

by the value of the program counter.

> Stack- The stack contains temporary data, such as

function parameters, returns addresses, and local

variables.

> Data Section- Contains the global variable.

> Heap- Dynamically allocated memory to process

during its run time.

'Process in Memory'

Max

Stack

V

1

Heap

Data

Text

0

Process state

Admitted

interrupt

Terminated

New

Exit

Ready

Running

I/O or event

completion

Scheduler dispatch

Waiting

I/O or event

wait

· New- The process is being created.

. Running- Instructions are being executed.

· Waiting- The process is waiting for some event

to occur.

· Ready- The process is waiting to be assigned to a

processor.

· Terminated- The process has finished execution.

YCT

Operating System

86

Process Control Block (PCB)- Process in an

operating system is represented by a data structure

called Process Control Block (PCB) also called a

task control block.

Pointer

Process state

Process number

Program counter

Registers

Memory limits

List of open files

.........

· Pointer- It is a stack pointer which is required to be

saved when the process is switched from one state

to another to retain the current position of the

process.

· Process State- The state may be new, ready,

running, waiting, halted and so on.

· Process Number- Every process is assigned with

unique ID known as process ID or PID which stores

the process identifier.

. Program Counter- The counter indicates the

address of the next instruction to be executed for

this process.

· Registers- These are the CPU registers which

includes: accumulator, base, registers and general

purpose registers.

. Memory Limits- This field contains the

information about memory management system

used by operating system. This may include the

page tables, segment tables etc.

· Open Files List- This information includes the list

of files opened for a process.

Threads

Thread is a single sequence stream within a process.

Threads have same properties as of the process so

they are called as light weight processes. Threads

are executed one after another but gives the illusion

as if they are executing in parallel. Each thread has

different states.

A Program Counter (PC)

Thread Consists

A Register Set

A Stack Space

Sr.

No.

Similarity between

Threads

and

Processes

Difference between

Threads

and

Processes

1.

Only one thread or

process is active at a

time.

Threads are not

independent of one

another but processes

are independent.

2.

Within a processes,

both

execute

sequentially.

Unlike processes, all

threads can access

every address in the

task.

3.

Both can create

children.

Threads are designed

to assist each other,

processes may or may

not do it.

4.

If one thread or

process is blocked,

another thread or

process can run.

Types of Threads

Parameters

1. User Level

Thread

(ULT)

2. Kernel

Level

Thread

(KLT)

Implemented

by

User threads

are

implemented

by users.

Kernel threads

are

implemented

by operating

system.

Recognize

Operating

system doesn't

recognize user

level threads.

Kernel threads

are recognize

by operating

system.

Context

switch time

Context switch

time is less.

Context switch

time is more.

Hardware

support

Context switch

requires no

hardware

support.

Hardware

support

is

needed.

Blocking

operation

If one user

level thread

performs

blocking

operation then

entire process

will be

blocked.

If one Kernel

thread perform

blocking

operation then

another thread

can continue

execution.

Operating System

87

YCT

Creation and

Management

User level

threads can be

created and

managed move

quickly.

Kernel level

threads take

more time to

create and

manage.

Operating

system

Any operating

system can

support user-

level threads.

Kernel level

threads are

operating

system-

specific.

Thread

management

The thread

library contains

the code for

thread creation

message

passing, thread

scheduling data

transfer and

thread

destroying.

The application

code does not

contain thread

management

code. It is

merely an API

to the Kernel

mode. The

windows

operating

system makes

use of this

feature.

Example

Example- Java

thread, POSIX

threads.

Example-

Window

Solaris.

Advantages

· User level

threads are

simple and

quick to

create.

· Scheduling of

multiple

threads that

belong to

same process

· Can run on

any

operating

system.

· In user level

threads,

switching

between

threads does

not need

Kernel mode

privileges.

on different

processors is

possible in

Kernel level

threads.

· Multi

threading can

be there for

Kernel

routines.

· When a

thread at the

Kernel level

is halted, the

Kernel can

schedule

another

thread for the

same process.

Disadvantages

· Multi thread

applications

on user-level

threads

cannot

benefit from

multi

processing.

· Transferring

control

within a

process from

one thread to

another

necessitates a

mode switch

to Kernel

mode.

· If a single

user-level

thread

performs a

blocking

operation,

the entire

process is

halted.

· Kernel level

threads takes

more time to

create and

manage than

user level

threads.

O

Multi-threading Models-

Many-to-One

Model

One-to-One

Model

Many-to-Many

Model

In this model,

In this model,

In this model,

we have

multiple user

threads

one to one

relationship

we have

multiple user

threads

between

mapped to one

Kernel and

multiplex to

Kernel thread.

user thread.

same or lesser

When a user

Multiple thread

number of

thread makes a

can run on

Kernel level

blocking

multiple

threads.

system call

processor.

Number of

entire process

Problem with

Kernel level

blocks. As we

this model is

threads are

have only one

that creating a

specific to the

Kernel thread

user thread

machine,

and only one

user thread can

requires the

corresponding

advantage of

this model is if

a user thread is

access Kernel

Kernel thread.

at a time, so

As each user

blocked we can

schedule others

multiple

thread is

threads are not

able access

multiprocessor

at the same

connected to

different.

Kernel, if any

user thread

user thread to

other Kernel

thread. Thus,

system does not

time.

makes a

block if a

User thread

blocking

particular thread

system call, the

other user

threads would

not be blocked.

User thread

is blocked. It is

the best multi-

threading

model.

K

Kernel thread

User thread

Kernel thread

Kernel thread

K

K

K

K

K

K

Operating System

88

YCT

fork() in C

Fork() system call is used for creating a new

process, which is called child process, which is

called process, which runs con-currently with the

process that makes the fork() call (parent

process). After a new child process is created,

both processes will execute the next instruction

following the fork() system call. A child process

uses the same program counter, same CPU

registers, same open files which use in the parent

process.

Forkotakes no parameters

and returns an integer

value. Below are

different values returned

by fork()

Negative Value:

Creation of a child

process was

unsuccessful

Zero:

Returned to the

newly created

child process

Positive value :

Returned to parent

or caller. The value

contains process ID

of newly created

child process

Note-

1. fork() is threading based function, to get the correct

output run the program on a local system.

2. Total number of processes = 2", where n is number of

fork() system calls.

Process Scheduling

The process scheduling is the activity of the

process manager that handles the removal of the

running process from the CPU and the selection

of another process on the basis of a particular

strategy. It is an essential part of a

multiprogramming operating systems. Such

operating systems allow more than one process

to be loaded into the executable memory at a

time and the loaded process shares the CPU

using time multiplexing.

Types of Process Scheduler

Long term

scheduler

short

term

scheduler

Medium term

scheduler

It is a job

scheduler.

It is a CPU

scheduler.

It is a process

swapping

scheduler.

Speed is

lesser than

short term

scheduler.

Speed is fastest

among other two.

Speed is in

between both

short and long

term

scheduler.

It controls the

degree of

multi-

programming.

It provides lesser

control over

degree of

multiprogramming

It reduces the

degree of

multi-

programming.

It is almost

absent or

minimal in

time sharing

system.

It is also minimal

in time sharing

system.

It is a part of

Time sharing

systems.

It selects

processes

from pool

and loads

them into

memory for

execution.

It selects those

processes which

are ready to

execute.

It can re-

introduce the

process into

memory and

execution can

be continued.

Categories of scheduling

Preemptive scheduling

Non-Preemptive

scheduling

A processor can be

preempted to execute

the different processes

in the middle of any

current process

execution.

Once the processor

starts its execution, it

must finish it before

executing the other. It

can't be paused in the

Middle.

CPU utilization is more

efficient compared to

non-preemptive

scheduling.

CPU utilization is less

efficient compared to

preemptive scheduling.

Preemptive scheduling

is prioritized. The

highest priority process

is a process that is

currently utilized.

When any process enters

the state of running, the

state of that process is

never deleted from the

scheduler until it

finishes its job.

Starvation may be

caused, due to the

insertion of priority

process in the queue.

Starvation can occur

when a process with

large burst time

occupies the system.

It is quite flexible

because the critical

processes are allowed to

access CPU as they

arrive in to the ready

queue, no matter what

process is executing

currently.

It is rigid as even if a

critical process enters

the ready queue the

process running CPU is

not disturbed.

Examples of preemptive

scheduling are Round

Robin and Shortest

Remaining Time First.

Examples of non-

preemptive scheduling

are First Come First

Serve and Shortest Job

First.

Operating System

89

YCT

Scheduling Algorithms

First-Come, First-Served (FCFS) Scheduling-

· In this scheduling algorithm, jobs are executed

on a first come, first serve basis.

. It is both preemptive and non-preemptive

scheduling algorithm.

· Easy to understand and implement.

· Its implementation is based on FIFO queue.

· Poor in performance as average wait time is

high.

Process

Arrival Time

Execute Time

Service Time

P 0

0

5

5

P1

1

3

8

P2

2

8

16

P3

3

9

25

Gantt Chart-

Po P1 P 2 P3

0 5 8

16

25

Waiting Time = Service Time - Arrival Time

Process

Waiting Time

P 0

5-0=5

P1

8-1=7

P2

16-2=14

P3

25-3 =22

Average Waiting Time = (5+7+14+22)/4 = 12

0

Shortest-Job-First (SJF) Scheduling-

· This algorithm scheduling depends on the

length of next CPU burst of process, rather than

its total length. Process with the minimum burst

time at an instance executes first.

. It is very efficient in minimizing the waiting

time and is easy to implement in Batch system.

. It cannot be implemented if the required CPU

time is not known in advance.

Process

Arrival Time

Execute Time

Service Time

P 0

0

5

5

P1

1

3

8

P2

2

8

14

P3

3

6

22

Po P1|P2 P3

0 5 8

14

22

Waiting Time = Service Time - Arrival Time

Process

Waiting Time

P 0

5-0=5

P1

8-1=7

P2

14-2=12

P3

22-3=19

Average Waiting Time =(5+7+12+19)/4

=10.75

O

Round-Robin Scheduling-

. Round Robin is the preemptive process

scheduling algorithm.

· Each process is provided a fix time to execute,

it is called a time quantum.

· Once a process is executed for a given time

period, it is preempted and other process

executes for a given time period.

· Context switching is used to save states of

preempted processes.

Example : Time Quantum = 3

Process

Number

Arrival

time

Execute

time

Service

time

Waiting

time

P0

0

4

12

12

P1

1

5

17

16

P2

2

3

9

7

P3

3

2

11

8

P4

5

6

20

15

Ready Queue

P0 ; P1 ; P2 ; P3 ; P4 ; P1; P5

Gantt chart

Po P1 P2 P3 PO P4 P1 P4

0

3

6

9

11

12

15

17

20

Average Waiting Time =(12+16+7+8+15)/5 =11.6

Synchronization

Some processes perform read and some

processes perform write on the file

simultaneously. This lead to data inconsistency

as data is being read as well as modified by many

processes at the same time. To prevent such data

inconsistency process synchronization is

required. All process that want to perform read

operation can do the reading simultaneously but

process that needs to perform write operation

should do it one at a time. The process that exist

at the same time are called concurrent processes.

Operating System

90

YCT

· Processes are categorized as one of the

following two types-

1. Independent process- The execution of one

process does not affect the execution of other

processes.

2. Cooperative process- A process that can

affect or be affected by other processes

executing in the system.

Process synchronization problem arises in the

case of cooperative process also because

resources are shared in cooperative process.

O

Race Conditions- Process that are working

together share some common storage (main

memory, file etc.) that each process can read and

write. When two or more processes are reading

or writing some shared data and the final result

depends on who runs precisely when, are called

race conditions. Several processes access and

process the manipulations over the same data

concurrently then the outcome depends on the

particular order in which the access takes place.

A race condition is a situation that may occur

inside a critical section.

The Critical-Section Problem- Considera

system consisting of n processes {Po, P1, ...... , Pn-

1}. Each process has a segment of code, called a

critical section, in which the process may be

changing common variables, updating a table,

writing a file, and so on. The critical section

problem is to design a protocol that the processes

can use to cooperate. Each process must request

permission to enter its critical section.

The section of code implementing this request is

the entry section. The critical section may be

followed by an exit section. The remaining code

is the remainder section. The entry section and

exit section are enclosed in boxes to highlight

these important segments of code. The general

structure of a typical process Pi is shown

following-

do {

entry section

critical section

exit section

remainder section

} while (true);

A solution to the critical-section problem must

satisfy the following three requirements:

1. Mutual exclusion- If process Pi is executing

in its critical section, then no other processes

can be executing in their critical sections.

2. Process- If no process is executing in its

critical section and some processes wish to

enter their critical sections, then only those

processes that are not executing in their

remainder sections can participate in

deciding which will enter its critical section

next, and this selection cannot be postponed

indefinitely.

3. Bounded waiting- There exists a bound, or

limit, on the number of times that other

processes are allowed to enter their critical

sections after a process has made a request to

enter its critical section and before that

request is granted.

O

Mutex locks- The hardware solutions presented

are after difficult for ordinary programmers to

access, particularly on multi-processor machines,

and particularly because they are often platform,

dependent. Therefore most systems after a

software API equivalent called mutex locks (the

term mutex is short for mutual exclusion).

We use the mutex lock to protect critical regions

and thus prevent race conditions. That is, a

process must acquire the lock before entering a

critical section, it releases the lock and the

release() function releases the lock.

do {

acquire lock

critical section

release lock

remainder section

} while (true);

A mutex lock has a Boolean variable available

whose value indicates if the lock is available or

not. It the lock is available, a call to acquire()

succeeds, and the lock is then considered

unavailable. A process that attempts to acquire

an unavailable lock is blocked until the lock is

released. Calls to either acquire() or release()

must be performed atomically. Thus, mutex

locks are often implemented using one of the

hardware mechanisms described.

Operating System

91

YCT

Acquire:

Release:

release() {

available = true;

}

acquire() {

while(!available)

; /*busy wait*/

available = false ;;

}

-

Semaphores- A semaphore is simply an integer

variable that is shared between threads. This

variable is used to solve the critical section

problem and to achieve process synchronization

in the multiprocessing environment.

A semaphore S is an integer variable that, apart

from initialization, is accessed only through two

standard atomic operations: wait() and signal().

The wait() operation was originally termed P;

signal() was originally called V. All

modifications to the integer value of the

semaphore in the wait() and signal() operations

must be executed indivisibly.

Wait:

Signal:

wait(S){

signal(S) {

while (S <= 0)

S++;

; //busy wait

}

S --;

}

O

The Bounded-Buffer Problem- This is a

generalization of the producer-consumer problem

wherein access is controlled to a shared group of

buffers of a limited size. In this problem,, the

producer and consumer processes share the

following data structures:

int n;

semaphore mutex = 1;

semaphore empty = n;

semaphore full = 0;

We assume that the pool consists of n buffers,

each capable of holding one item. The mutex

semaphore provides mutual exclusion for

accesses to the buffer pool and is initialized to

the value1. The empty and full semaphores count

the number of empty and full buffers. The

semaphore empty is initialized to the value n; the

semaphore full is initialized to the value 0.

Producer:

do {

/*produce an item in next-produced*/

wait(empty);

wait(mutex);

......

/*add next-produced to the buffer*/

signal(mutex);

signal(full);

} while(true);

Consumer:

do {

wait(full);

wait(mutex);

......

/*remove an item buffer to next-consumed*/

signal(mutex);

signal(empty);

......

/*consume the item in next-consumed*/

} while(true);

We can interpret this code as the producers

producing full buffers for the consumer or as the

consumer producing empty buffers for the

producer.

Deadlocks

Deadlock is a situation where a set of processes

are blocked because each process is holding a

resource and waiting for another resource

acquired by some other process.

Necessary Conditions of Deadlock-

1. Mutual exclusion- At least one resource must

be held in a non-sharable mode, that is, only

one process at a time can use the resource. If

another process requests that resource, the

requesting process must be delayed until the

resource has been released.

2. Hold and Wait- A process must be holding at

least one resource and waiting to acquire

additional resources that are currently being

held by other processes.

Operating System

92

YCT

3. No preemption- Resources cannot be

preempted; that is, a resource can be released

only voluntarily by the process holding it, after

that process has completed its task.

4. Circular wait- A set {P0, P1, ... Pn} of waiting

processes must exist such that P0 is waiting for

a resource held by P1. P1 is waiting for a

resource held by P2, ... Pn-1 is waiting for a

resource held by Pn and Pn is waiting for a

resource held by Po-

Resource-Allocation Graph (RAG)- Deadlocks

can be described more precisely in terms of a

directed graph called a system resource-allocation

graph. This graph consists of a set of vertices V

and a set of edges E. The set of vertices V is

partitioned into two different types of nodes: P =

{P1, P2, .... Pn}, the set consisting of all the active

processes in the system and R = { R1, R2 ...... Rm

}, the set consisting of all resource types in the

system.

RI

R3

P

P2

P3

R2

R4

Request Edges- A set of directed edge from Pi to

Rj, indicating that process Pi has requested R;(Pi

->Rj) and is currently waiting for that resource to

become available.

Assignment Edges- A set of directed edge from

Rj to Pi indicating that resources Rj has been

allocated to process Pi(Rj ->Pi) and that Pi is

currently holding resource Rj.

When process Pi requests an instance of resource

type Rj, a request edge is inserted in the resource-

allocation graph. When this request can be fulfilled,

the request edge is instantaneously transformed to

an assignment edge. When the process no longer

needs access to the resource, it releases the resource.

As a result, the assignment edge is deleted.

Resource-allocation graph with a

deadlock.

Resource-allocation graph with a

cycle but no deadlock.

RI

R3

RI

P2

P

P2

P3

P

P3

R2

R2

P4

R4

Banker's Algorithm- The resource-allocation-

graph algorithm is not application to a resource-

allocation system with multiple instances of each

resource type. The deadlock-avoidance algorithm

that we describe next is applicable to such a system

but is less efficient than the resource-allocation

graph scheme. This algorithm is commonly known

as the banker's algorithm.

We need the following data structures, where n is

the number of processes in the system and m is the

number of resource types:

· Available- A vector of length m indicates the

number of available resources of each type. If

available[j] equals k, then k instances of resource

type Rj are available.

· Max- An n x m matrix defines the maximum

demand of each process. If Max[i][j] equals k, then

process Pi may request at most k instances of

resource type Rj.

· Allocation- An nxm matrix defines the number of

resources of each type currently allocated to each

process. If allocation [i][j] equals k, then process Pi is

currently allocated k instances of resource type Rj-

· Need- An nxm matrix indicates the remaining

resource need of each process. If need [i][j] equals

k, then process Pi may need k more instances of

resource type R; to complete its task.

Need[i][j] = Max [i][j] - Allocation [i][j]

We can treat each row in the matrices Allocation

and Need as vectors and refer to them as Allocation;

and Needj. The vector Allocation; specifics the

resources currently allocated to process Pi; the

vector Need¡ specifies the additional resources that

process Pi may still request to complete its task.

Operating System

93

YCT

Banker's algorithm consists of safety algorithm and

resource request algorithm.

Safety Algorithm- The algorithm for finding out

whether or not a system is in a safe state. This

algorithm can be described as follows:

1. Let work and finish be vectors of length m and n,

respectively. Initialize work = Available and

Finish [i] = false for i = 0,1, .... , n - 1.

2. Find an index i such that both

a. Finish [i] = = false

b. Need¡ ≤ work

If no such i exists, go to step 4.

3. Work = Work + Allocation;

Finish [i] = true

Go to step 2.

4. If Finish [i] = = true for all i, then the system is in

a safe state.

This algorithm may require an order of mxn2

2

operations to determine whether a state is safe.

Resource-Request Algorithm- We describe the

algorithm for determining whether requests can be

safely granted.

Let request; be the request vector for process Pi. If

Request; [j] = = k, then process Pi wants k instances

of resource type Rj. When a request for resources is

made by process Pi,

1. If Request; ≤ Need¡, go to step 2, otherwise,

raise an error condition, since the process has

exceeded its maximum claim.

2. If Request; ≤ Available, go to step 3.

Otherwise, Pi must wait, since the resources are

not available.

3. Have the system pretend to have allocated the

requested resources to process Pi by modifying

the state as follows:

Available = Available - Requesti ;

Allocation; = Allocation; + Requesti ;

Need¡ = Need; - Requesti ;

If the resulting resource-allocation state is safe, the

transaction is completed, and process Pi is allocated

its resources. However, if the new state is unsafe,

then Pi must wait for Request; and the old resource-

allocated state is restored.

Recovery from Deadlock- When a detection

algorithm determines that a deadlock exists, several

alternatives are available. One possibility is to

inform the operator that a deadlock has occurred

and to let the operator deal with the deadlock

manually. Another possibility is to let the system

recover from the deadlock automatically. There are

two options for breaking a deadlock. One is simply

to abort one or more processes to break the circular

wait. The other is to preempt some resources from

one or more of the deadlocked processes.

(i) Process Termination- To eliminate deadlocks

by aborting a process, we use one of two methods.

In both methods, the system reclaims all resources

allocated to the terminated processes.

· Abort all deadlocked processes.

· Abort one process at a time until the deadlock

cycle is eliminated.

(ii) Resource Preemption- To eliminate deadlock

using resources preemption, we successively

preempt some resources from processes and give

these resources to other processes until the deadlock

cycle is broken.

If preemption is required to deal with deadlocks,

then three issues need to be addressed:

1. Selecting a victim

2. Rollback

3. Starvation

Memory-Management Strategies

> Swapping- Swapping is a process of removing the

currently running program from memory (called

swap out) and bringing in another program in to the

memory (called swap in). Swapping makes it

possible for the total physical address space of all

processes to exceed the real physical memory of the

system, thus increasing the degree of

multiprogramming in a system.

A program can be swapped out under following

conditions-

(i) If its time quantum has expired.

(ii) If higher priority process has arrived.

(iii) If using preemptive SJF scheduling algorithm

(iv) If a program has completed its execution.

Note-A process with pending I/O should never be

swapped out.

Swapping requires backing store which could be

fast disk. It should be large enough to accomodate

copies of all memory images for all users. The

context-switch time in such a swapping system is

fairly high.

Operating System

94

YCT

Memory Allocation- One of the simplest methods

for allocating contiguous memory is to divide all

available memory into equal sized partitions, and to

assign each process to their own partition. This

restricts both the number of simultaneous processes

and the maximum size of each process and is no

longer used. An alternate approach is to keep a list

of unused (free) memory blocks (holes) and to find

a hole of a suitable size whenever a process needs to

be loaded into memory. There are many different

strategies for finding the 'best' allocation of memory

to processes, including the three most commonly

discussed:

1. First fit: Allocate the first hole that is big

enough. Searching can start either at the

beginning of the set of holes or at the location

where the previous first-fit search ended. We

can stop searching as soon as we find a free

holes that is large enough.

2.

.. Best fit- Allocate the smallest hole that is big

enough. We must search the entire list, unless

the list is ordered by size. This strategy

produces the smallest leftover hole.

3. Worst fit- Allocate the largest hole. Again, we

must search the entire list, unless it is sorted by

size. This strategy produces the largest leftover

hole, which may be more useful than the

smaller leftover hole from a best-fit approach.

Simulations have shown that both first fit and best

fit are better than worst fit in terms of decreasing

time and storage utilization. Neither first fit nor best

fit is clearly better than the other in terms of storage

utilization, but first fit is generally faster.

Fragmentation- Fragmentation is an unwanted

problem in the operating system in which the

processes are loaded and unloaded from memory

and free memory space is fragmented. Processes

can't be assigned to memory blocks due to their

small size, and the memory blocks stay unused. It is

also necessary to understand that as programs are

loaded and deleted from memory, they generate free

space or a hole in the memory. These small blocks

cannot be allotted to new arriving processes,

resulting in inefficient memory use.

Segmentation- A process is divided in to segments.

The chunks that a program is divided into which are

not necessarily all of the same sized are called

segments. Segmentation gives the user's view of the

process which paging does not give. Here the user's

view is mapped to physical memory.

S

limit

base

CPU

Segment table

S

d

Yes

<

+

No

trap: addressing error

Physical memory

Important Points-

· In the segmentation, Logical Address space

will be divided in to various segments.

· To achieve user's view of memory allocation,

the segmentation will be implemented.

· The paging does not follow user's view of

memory allocation.

· Segments of Logical Address space will vary in

the size.

s = Number of bits required to represent segments

of logical address space.

OR

segment number

d = Number of bits required to represent segment

size.

OR

segment offset

· Number of entries in the segment table is same as

number of segments in the logical address space.

· The variable size segments are brought from

logical address space to physical address space so it

is similarly behaving like variable partition scheme.

Hence, the segmentation still suffers from 'External

fragmentation'.

Paging- The basic method for implementing paging

involves breaking physical memory into fixed sized

blocks called frames and breaking logical memory

into blocks of the same size called pages. When a

process is to be executed, its pages are loaded into

any available memory frames from their source (file

system or the backing store). The backing store is

divided into fixed-sized blocks that are the same

size as the memory frames or clusters of multiple

frames.

Operating System

95

YCT

Logical address

Physical address

f000 ... 000

f

CPU

p

d

f

d

p

f1111 ... 111

f

Page table

Physical memory

To avoid, the overhead of bringing large size

segment into memory, the segmented paging will be

implemented.

In the segment paging, paging will be applied on the

segment.

Instead of bringing, the entire segments into the

memory, pages of segment will be brought into

memory.

Number of entries in page table of segment =

Number of pages on segment.

Page size of segment is same as frame size of PAS

(Physical address space).

Virtual-Memory Management- Virtual memory

gives an illusion to the programmers that the

programs of larger size than actual physical memory

can be executed.

Virtual memory is implemented by using

Demand paging.

Demand Paging- The process of loading the page

into memory on demand (Whenever page fault

occurs) is known as demand paging.

O.S.

3

P.A.S

13 bits

2

P.A.

0

CPU

L.A

P7

0

P

.

3

10

2 10

-1

P5 P2

1

p

d

+ d

2

P3

2

0

--

3

P4

3

1

1

12

4

2

--

5

3

10

6

4

00

7

5

4

8

6

4

L.A.S.

7

01

Page table

Virtual memory concept is implement in order to

increase the degree of multiprogramming.

Step 1. The CPU is trying to refer some page in the

memory but the page is currently not available in

the main memory (that is called page fault).

Step 2. The program execution will be stopped, so

the signal will sent to the operating system

regarding the page fault.

Step 3. Operating system will search for the

required page in the logical address space.

Step 4. The required page is brought from logical

address space (LAS) to physical address space

(PAS). But the problem in the PAS, all the frames

are occupied by some other pages, so we need to

replace the page, so for that reason we need page

replacement algorithm.

Step 5. So after replacement, the page table will be

updated accordingly.

Step 6. The signal will be sent to the CPU to

continue the program execution and it will place the

process back into the ready state.

The CPU will access the required page in the main

memory and continue the program execution.

The page fault service time include the time to

perform all the above six steps.

Page fault service time = s

main memory access time = m

page fault rate = p

then the formula for EMAT(Effective Memory

Access Time)

EMAT = p(s) + m

EMAT= p*(s) +(1 -p)*m

"s>>m"

Page Replacement Algorithms

(i) FIFO Page Replacement- In this algorithm, the

operating system keeps track of all pages in the

memory in a queue, the oldest page is in the front of

the queue, when a page needs to be replaced page in

the front of the queue is selected for removal.

Reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1,

2, 0, 1, 7,0,1

(Reference means page number referred by the

process in the logical address)

The number of frames allocated to the process will

be decided by instruction set architecture.

Assume, Number of Frame = 4

INDIE W L

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

Allocated

frame

77

2 Therefore, total number of page fault = 10

10

07

A7 7 Page fault rate = __ x100 = 50%

20

17

0

Page hit rate = 100 - 50 = 50%

2

1

P.A.S.

Operating System

96

YCT

Belady's Anomaly- By increasing number of

frames to the process, the number of page faults

should decrease but instead they are increasing

case of FIFO, this problem is called as Belady's

anomaly.

(ii) Optimal Page Replacement- In the event of

page fault, the page is replaced which is not used

for longest duration of time in future. Use of this

page replacement algorithm guarantees the lowest

possible page fault rate for a fixed number of

frames.

Reference string:

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

with 4 frame

7

81

0

Number of page fault = 8

X

4

7

Note- If we confused about which one used (if they

are not given in future reference string), then follow

the FIFO order.

Reference string:

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

with 3 frame

7

07

X

3 1

877

A7 0

Total number of page fault = 9

(iii) LRU Page Replacement- In the event of page

fault, replace the page which is least recently used.

This approach is the Least Recently Used (LRU)

algorithm.

Reference string:

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

With 3 frame

77

07

2 ×1 071

3 0

Number of page fault = 12

7

8 27 7

Reference string:

7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

with 4 frame

7

877

07

Number of page fault = 8

X

47 1

Thrashing- Thrashing is a condition or a situation

when the system is spending a major portion of its

time serving the page faults, but the actual

processing done is very negligible.

CPU Utilization

'λ΄

Thrashing

Degree of Multiprogramming

If we further increase the degree of

multiprogramming, then the CPU utilization will

drastically fall down and the system will spend

more time only in the page replacement and the

time taken to complete the execution of the process

will increased. This situation in the system is called

as Thrashing.

Cause of Thrashing-

1. High degree of multiprogramming

2. Lack of frames

Recovery of Thrashing-

1. Do not allow the system to go into thrashing and

instruct long term scheduler, not to bring the

process in to the main memory after the point of '2'.

2. If the system is already present in the thrashing

then instruct the Midterm scheduler to suspend

some of the processes so that we can recover the

system from Thrashing.

Operating System

97

YCT

File System

A file is a named collection of related information

that is recorded on secondary storage. A file is the

smallest allotment of logical secondary storage; that

is, data cannot be written to secondary storage

unless they are within a file. Commonly, files

represent programs and data. Data files may be

numeric, alphabetic, alphanumeric, or binary. Files

may be free form, such as text files, or maybe

formatted rigidly.

File Attributes- A files attributes vary from one

operating system to another but typically consist of

these:

· Name

· Identifier

· Type

· Location

· Size

· Protection

· Time, date and user identification

All the attributes of the file is called as file context.

File context will be saved in the FCB (File Control

Block).

File Operations- A file is an abstract data type. In

the file is having various operations:

· Creating a file

· Writing a file

· Reading a file

· Opening a file

· Truncating a file

· Modify

· Repositioning within a file

· Deleting a file

· Appeding a file

· Save

· Rename

· Redo

· Print

· Copy

· Paste

· Cut

· Send

· Undo

File Types-

File type

Usual

Extension

Function

Executable

exe, com,

bin

ready-to-run

machine language

program

Object

obj, O

complied, machine

language, not

linked

Source code

C, CC, java,

perl, asm

ource code in

various language

batch

bat, sh

commands to the

command

interpreter

Markup

xml, html,

tex

textual

data,

documents

Word

processor

xml, rtf,

docx

various word-

processor formats

Library

lib, a, so,

dill

libraries of

routines for for

programmers

Print or view

gif, pdf, jpg

ASCII or binary

file in a format for

printing or viewing

Archive

rar, zip, tar

related files

grouped into one

file, sometimes

compressed, for

archiving or

storage

Multimedia

mpeg, mov,

mp3, mp4,

avi

binary file

containing audio or

A/v information

Access Methods-

· Sequential Access (Record by Record)

· Direct Access (Jump to particular Record)

Directory Structure- The directory can be viewed

as a symbol table that translates file names into their

directory entries. If we take such a view, we see that

the directory itself can be organized in many ways.

The organization must allows us to insert entries, to

delete entries, to search for a named entry and to list

all the entries in the directory.

1. Single Level Directory- The simplest directory

structure is the single level directory. All files are

contained in the same directory, which is easy to

support and understand. The two files cannot have

the same name.

Directory

cat bo |a test

data

mail

cont

hex

Files

2. Two Level Directory- In the two level directory

structure, each user has his own User File Directory

(UFD). The UFDs have similar structures, but each

lists only the files of a single user. When a user job

starts or a user logs in, the system's Master File

Directory (MFD) is searched. The MFD is indexed

by user name or a count number and each each

entry points to the UFD for that user.

Operating System

98

YCT

Master file

directory

User 1

User 2

User 3

User file

directory

cat

bo

a

test

a

data

a

test

Files

3. Tree structured Directories- The natural

generalization is to extend the directory structure to

a tree of arbitrary height. This generalization allows

users to create their own subdirectories and to

organize their files accordingly. A tree is the most

common directory structure. The tree has a root

directory and every file in the system has a unique

path name.

root

spell

bin

programs

stat

mail

dist

find

count

hex

p

e

mail

prog

copy

recorder

list

find

hex

count

4. Acyclic Graph Directories- An acyclic graph a

graph with no cycles, allows directories to share

subdirectories and files. The same file or

subdirectory may be in two different directories.

The acyclic graph is a natural generalization of the

tree-structured directory scheme.

root

dict

spell

list

all

W

count

count

words

list

list

rade

w7

0

Disk Space Allocation Methods-

1. Contiguous Allocation-

Directory

File

Starting Disk Block

Address (DBA)

Size

abc.doc

2

4

xyz.doc

9

5

abc.doc

0

1

2

3

Disk

Block

4

5

6

7

xyz.doc

8

9

10

11

12

13

14

15

DISK

· In the contiguous allocation, whenever the file

is created then disk block will be allocated in

the contiguous manner.

· Every file will be associated with starting DBA

and size of file with respect to Disk Block.

· If we want to increase file 'xyz.doc' then block

14 (Next Block) is should be free, but it is not

true always, so that increasing the file size is

not possible always.

· Even Though, it is suffering from external

fragmentation.

· Last block of file may not be full always, so,

that the internal fragmentation may exist in the

last disk block of the file.

· It supports both sequential and random access

of the file.

Random Access : Random Access Possible by

'Random Access = Starting DBA + Offset'

2. Linked Allocation (Non-Contiguous

Allocation)- Linked allocation solves all problems

of contiguous with linked allocation, each file is a

linked list of disk blocks, the disk blocks may be

scattered anywhere on the disk. The directory

contains a pointer to the first and last blocks of the

file. Each block contains a pointer to the next block.

File

Starting

(DBA)

Ending (DBA)

abc.doc

2

1

xyz.doc

9

10

Directory

Operating System

99

YCT

DISK

Disk

block

0

1

2

3

DBA of next disk

block of file (or)

pointer to next disk

block of the file)

4

5

6

7

8

9

10

11

12

13

14

15

· In the linked allocation, whenever the file is

created, the disk space will be allocated in a non-

contiguous manner.

· Increasing the file size is always possible if the

free disk block is available.

· There is no external fragmentation.

. In the last block, it may be full or may not be. The

internal fragmentation may exist in the last disk

block of the file.

· There is a overhead of maintaining the pointers in

every block.

. If the pointer of any disk lost, the file will be

truncate.

· It supports only sequential access of the file.

· So to avoid overhead of maintaining the

pointer, we go for indexed allocation.

3. Indexed Allocation-

Directory

File

Index node

abc.do

c

4

0

1

2

3

Disk

Block

9

12

4

5

6

7

2

DBA'S

of the file

-.

8

8

9

10

11

13

14

15

End of file

12

DISK

· In index allocation, every file is associated with a

its own index node.

. The index node contains all the disk block

address of the file.

. If the file is very-very large then one disk block

may not be sufficient to store all the disk block

addresses of the file, so it is pointing to another

block so it is behaving like indexed allocation.

· If the file is very-very small, it is waste of using

entire one disk block just to store the disk block

addresses.

· To avoid these problem, we go for unix-i node.

4. UNIX I-Node Implementation- An extension of

indexed allocation

Number of Hard

links presently

pointing to I-Node

Disk Block Size

Location

Data blocks

Owner

DB

Reference Count

DB

Date and Time Stamps

DB

Direct DBA's

DB

DB

DBA

DBA

+

Single Indirect

DB

DB

Double Indirect

DBA

Triple Indirect

DB

Address

DBA

DB

No. of single

DB Indirect address

No. of double

DB Indirect address

Total size of the

file system

No. of direct

DBA's

DBSize

DBA

DBSize

DBA

+

2

DBSize

DBA

3

=

+

+

+ ....

x DB Size

· UNIX follows I-Node way of allocation in order

to allocate the disk space to the file.

· Every file is associated with its own I-Node.

· All are disk block only, some contain disk block

and some contain addresses of disk block.

· Single indirect means one level contain address

and next level contains data block.

· Double indirect means two level address and then

next level data block.

· Whenever the file is created, then depending on

the size of the file, it will be stored in only one

place either direct DBA or single indirect or

double indirect and so on.

· Depending on the size of the file, file will be

stored only in one particular place, may be in the

direct DBA's or may be in the single indirect or

double indirect and so on.

· Reference count = Reference count contains the

total number of link to DB'S.

DB size

= Number of Disk Block Address's

DBA

one disk block can contain

Disk Free-Space Management-

1. Bit Vector- The free-space list is implemented as

a bit map or bit vector. Each block is represented by

1 bit. If the block is free, the bit is 1; if the block is

allocated, the bit is 0.

Operating System

100

YCT

The main advantage of this approach is its relative

simplicity and its efficiency in finding the first free

block or n consecutive free blocks on the disk. One

technique for finding the first free block on a system

that uses a bit-vector to allocate disk space is to

sequentially check each word in the bit map to see

whether that value is not 0, since a 0-valued word

contains only 0 bits and represents a set of allocated

blocks. The first non-0 word is scanned for the first

1 bit, which is the location of the first free block.

The calculation of the block number is-

number of bits

per word

× (number of 0 - value words) + off set of first 1 bit.

2. Linked List- In this approach, the free disk

blocks are linked together i.e. a free block contains

a pointer to the next free block. The block number

of the very first disk block is stored at a separate

location on disk and is also Cached in memory.

free-space

list head

0

1

2

3

4

5

6

7

8

In above figure, the free space list head points to

Block 4 which points to Block 5, the next free block

and so on. The last free block would contain a null

pointer indicating the end of free list. A drawback

of this method is the I/O required for free space list

traversal.

3. Grouping- This approach stores the address of

the free blocks in the first free block. The first free

block stores the address of some, say n free blocks.

Out of these n blocks, the first n-1 blocks are

actually free and the last block contains the address

of next free n blocks.

4. Counting- This approach stores the address of

the first free disk block and a number n of free

contiguous disk blocks that follow the first block.

Every entry in the list would contain-

(i) Address of first disk block

(ii) A number n

DISK Structure

Modern magnetic disk drives are addressed as large

one-dimensional arrays of logical blocks, where the

logical block is the smallest unit of transfer. The

size of a logical block is usually 512 bytes, although

some disks can be low-level formatted to have a

different logical blocks size, such as 1024 bytes.

The one-dimensional array of logical blocks is

mapped on to the sectors of the disk sequentially.

Sector 0(zero) is the first of the first track on the

outermost cylinder. The mapping proceeds in order

through that tracks, then through the rest of the

tracks in that cylinder and then through the rest of

the cylinders from outer most to inner most.

Track Sector

Track

Disk sector

· Seek Time- Seek time is the time taken to locate

the disk arm to a specified track where the data is to

be read or write.

· Rotational Latency- Rotational latency is the

time taken by the desired sector of disk to rotate

into a position so that it can access the read/write

heads.

. Transfer Time- Transfer time is the time to

transfer the data. It depends on the rotating speed of

the disk and number of bytes to be transferred.

. Disk Access Time-

Disk Access Time = Seek Time + Rotational

Latency + Transfer Time.

DISK Scheduling Algorithms

The goal of disk scheduling algorithms is to

minimize the average seek time of the disk.

1. FCFS Scheduling- A disk queue with requests

for I/O to blocks on cylinders

98, 183, 37, 122, 14, 124, 65, 67

head starts

0

14 37

53

65

67

98

122 124

183

199

Total track movement made by read/write header

(seek time) = (98 - 53) + (183 - 98) + (183 - 37) +

(122 - 37) + (122 - 14) + (124 - 14) + (124 - 65) +

(67- 65)

=45+85+146+85+108+110+59+2

= 640

Operating System

101

YCT

2. SSTF (Shortest Seek Time First) Scheduling-

The SSTF algorithm selects the request with the

least (minimum) seek time from the current head

position.

queue = 98, 183, 37, 122, 14, 124, 65, 67

head starts

0

14 37

53

65

67

98

122 124

183

199

H

Seek time = (65 - 53) + (67 - 65) + (67 - 37) + (37

- 14) + (98 - 14) + (122 - 98) + (124 - 122) + (183

- 124)

=12+2+30+23+84+24+2+59

= 236

3. SCAN Scheduling- In the scan algorithm, the

disk arm starts at one end of the disk and moves

toward the other end, servicing requests as it

reaches each cylinder, until it gets to the other end

of the disk. At the other end, the direction of head

movement is reversed and servicing continues. The

head continuously scans back and forth across the

disk. The SCAN algorithm is sometimes called the

elevator algorithm.

queue = 98, 183, 37, 122, 14, 124, 65, 67

head starts

0

14

+ 37

53

65

67

98

122

124

183

199

Right- It will first satisfy all the right-side request

and go till the end and come back to satisfy the

remaining left.

Left- First satisfy all left side and go till the 'O' and

satisfy the remaining.

Seek time = (65 - 53) + (67 - 65) + (98 - 67) +

(122 - 98) + (124 - 122) + (183 - 124) + (199 -

183) + (199 - 37) + (37 - 14)

= 12+2+31+24+2+59+16+162+23

=331

4. C-SCAN (Circular SCAN) Scheduling- C-

SCAN moves the head from one end of the disk to

the other, servicing requests along the way. When

the head reaches the other end, however, it

immediately returns to the beginning of the disk

without servicing any requests on the return trip.

The C-SCAN scheduling algorithm essentially

treats the cylinders as a circular list that wraps

around from the final cylinder to the first one.

queue = 98, 183, 37, 122, 14, 124, 65, 67

head starts

0 14 37 53 65 67 98 122 124 183 199

Seek time = (65 - 53) + (67 - 65) + (98 - 67) +

(122 - 98) + (124 - 122) + (183 - 124) + (199 -

183) + (199 - 0) + (14 - 0) + (37- 14)

= 12+2+31+24+2+59+16+199+14+23

= 382

5. LOOK Scheduling- In this algorithm, it will go

till only the last request (not 199) and come back to

satisfy the remaining request.

queue = 98, 183, 37, 122, 14, 124, 65, 67

head starts

0

14 37 53 65 67

98

122

124

183

199

Seek time = (65 - 53) + (67 - 65) + (98 - 67) +

(122 - 98) + (124 - 122) + (183 - 124) + (183 - 37)

+ (37- 14)

= 12+2+31+24+2+59+146+23

= 299

6. C-LOOK (Circular LOOK) Scheduling- In C-

LOOK, it will go in the right direction and go till

the last request and directly jump to first request

(14) left most and request and then satisfy the

remaining request.

queue = 98, 183, 37, 122, 14, 124, 65, 67

Operating System

102

YCT

0

14 37 53

65

67

98

122

124

183

199

Seek time = (65 - 53) + (67 - 65) + (98 - 67) +

(122 - 98) + (124 - 122) + (183 - 124) + (183 -

14) + (37- 14)

= 12+2+31+24+2+59+169+23

=332

O

RAID Structure- RAID (Redundant Arrays of

Independent Disks) is a technique which makes

use of a combination of multiple disks instead of

using a single disk for increased performance,

data redundancy or both.

Reliability- How many disk faults

can the system tolerate?

Availability- What fraction of the

total session time is a system in

uptime mode, i.e. how available is

the system for actual use?

Performance- How

good is the response

time? How high is the

throughput.

Evaluation

points

for a RAID

system

Capacity- Given a set of n

disks each with B blocks,

how much useful capacity is

available to the user?

RAID Levels- RAID combines several independent

and relatively small disks into single storage of a

large size. The disks included in the array are called

array members. The disks can combine into the

array in different ways, which are known as RAID

levels. We describe the various levels here-

RAID-0 (Stripping)- This configuration has

striping but no redundancy of data. It offers the best

performances but is does not provide fault

tolerance.

RAID-1 (Mirroring)- Also known as disk

mirroring, this configuration consists of at least two

drives that duplicate the storage of data. There is no

striping. Read performance is improved, since either

disk can be read at the same time. Write

performance is the same as for single disk storage.

C

C

RAID-2 - This configuration uses striping across

disks, with some disks storing error checking and

correcting (ECC) information. RAID 2 also uses a

dedicated Hamming code parity, a linear form of

ECC. RAID 2 has no advantage over RAID3 and is

no longer used.

P

P

RAID-3 - This technique uses striping and

dedicates one drive to storing parity information.

The embedded ECC information is used to detect

errors. Data recovery is accomplished by calculating

the exclusive information recorded on the other

drives. Because an I/O operation addresses all the

drives at the same time. RAID 3 cannot overlap I/O.

For this reason, RAID 3 is best for single user

systems with long record applications.

P

RAID-4 - This level uses large stripes, which

means a user can read records from any signle

drive. Overlapped I/O can then be used for read

operations. Because all write operations are required

to update the parity drive, no I/O overlapping is

possible.

P

RAID-5 - This level is based on parity block level

striping. The parity information is striped across

each drive, enabling the array to function, even if

one drive were to fail. The array's architecture

enables read and write operations to span multiple

drives. This results in performance better than that

of a single drive, but not as high as a RAID-0 array.

RAID-5 requires at least three disks, but it is often

recommended to use at least five disks for

performance reasons.

P

P

P

P

RAID-6- This technique is similar to RAID-5, but

it includes a second parity scheme distributed across

the drives in the array. The use of additional parity

enables the array to continue functioning even if

two disks fail simultaneously. However, this extra

protection comes at a cost. RAID 6 arrays often

have slower write performance than RAID 5 arrays.

P

P

P

P

P

P

P

Operating System

103

YCT

09.

COMPUTER NETWORK

Data Communication

Data communication is the exchange of data

between device or human by local or remote

using transmission medium.

Components- There are five mainly components

of a data communication system.

Rule 1:

Rule 1:

Rule 2:

Rule 2:

.......

Rule n;

Rule n:

Set of rule (Protocol)

Set of rule (Protocol)

Message

Sender

Receiver

1. Message

2. Sender

3. Receiver

4. Transmission Medium

5. Set of rules (protocol)

Message

It is the information or data to be

communicated. Message can be in

the form of text, number, picture,

audio, video and multimedia etc.

Sender

It is the device which capable of

sending data over network. It can

be a computer, telephone, laptop,

Mobile video camera and so on.

Receiver

It is the device (destination) where

finally message send by source

and received by receiver. It can be

computer workstation, telephone,

television etc.

Transmission

medium

It is physical path by which data

travels from sender to receiver. It

is act as bridge between sender

and receiver.

Example- Twisted pair cable,

coaxial cable fiber optic cable and

radio waves.

Protocol

It is a set of rules that govern data,

data communications. It represents

an agreement between the devices

without protocol you can connect

but not communicate.

Data Flow

Data flow is the communication between two

devices. It can be simplex half duplex and full

duplex.

Transmission Mode

Simplex Mode

Half Duplex Mode

Full Duplex Mode

Simplex- It is an unidirectional communication

or one way start. Key boards traditional monitor

and radios are example of simplex devices.

Simplex One Direction

Half-duplex- It is two or bidirectional

communication. In half-duplex each station can

both transmit and receive but not at same time.

Walkie-Takies is the example of half duplex

system.

Half Duplex

Full duplex- It is two or bidirectional

communication in full duplex both stations can

transmit and receive simultaneously. This

sharing contain two physically separate

transmission path to avoid collision telephone

line is the example of full duplex.

0

Q

Full Duplex

Networks

A computer network is a group of computers

connected to each other that enables one

computer to communicate with other computers

and share their resources, applications and data.

Networking

Device

E4.

Computer Network

Computer Network

104

YCT

Network Criteria

Performance

It can be measured in many ways,

including transit time and

response time . Transit time is the

amount of time required for a

message to travel from one device

to another.

Response time is the elapsed

between an inquiry and a

response.

The nature of a network depends

on a number of factors, including

the type transmission medium, the

number of user the capabilities of

the connected hardware and the

efficiency of the software.

Reliability

Network reliability is measured

by the frequency of failure. The

time is takes a link to recover

from a failure.

Security

Network security issues include

protecting data from unauthorized

access, protecting data loss and

implementing policies and

procedures for recovery from dot

losses.

Physical Structure

Types of connection- There are two possible

types of connection.

(a) Point-to-point connection- This connection

provides a dedicated link between two devices.

For example Television and remote control,

computer connected by telephone line.

Transmit Receive

Receive

Transmit

Point-to-Point Network

(b) Multipoint- In this connection more than

two specific devices share a single link.

Link

Mainframe

Multipoint

Two types of multipoint connection-

(i) Spatial sharing- In this sharing several

computer can share the link simultaneously.

(ii) Time sharing- In this, user must take turn.

Physical Topology

In physical topology, a network is formed by

physically connecting two or more devices with

two or more links.

Communication using OSI Model

Sending

computer

Receiving

computer

Encapsulation & De-encapsulation

in OSI Model

Application

Application

Presentation

Presentation

Encapsu lation

Data

Session

Session

De-encapsu lation

Transport

Segment

header

Data

Transport

Network

Packet

header

Segment

header

Data

Network

Data Link

>

Frame

header

Packet

header

Segment

header

Data

Frame

trailer

Data Link

Physical

>

010110011010101010110001 Bits

Physical

OSI (Open Source Interconnection) Model

Layer

Application

Functions

Protocols

Central Devices

Application

Layer

(Layer 7)

These application

produce the data which

has to be transferred

over the network. This

layer also serves as a

window for the

application services to

access the network and

for displaying the

received information to

the user.

Example- browsers,

Skype, Messenger etc.

· Networks

virtual

terminal

· Mail services

· Directory services

SMTP, HTTP, FTP,

POP3, SNMP,

Telnet.

–

Computer Network

105

YCT

Presentation

Layer

(Layer 6)

It is also called the

Translation Layer. the

data from the

application layer is

extracted here and

manipulated as per the

required format to

transmit over the

network.

· Translation ASCII to

EBCDIC

MPEG, XDR, SSL,

TLS, MIME

–

· Encryption/

Decryption

· Compression

Session layer

(Layer 5)

This layer is responsible

for the establishment of

connection maintenance

of sessions,

authentication and also

ensures security.

· Session

establishment,

maintenance

and

termination

· Synchronization

· Dialog controller

Net BIOS, SAP

PPTP,

ADSP,

RTCP, PAP,RPCP

Gateway

phone,

Servers

Transport

The data in the

· Segmentation

and

TCP,

Firewall, Gateway

Layer

(Layer 4)

transport layer is

reassembly

UDP,

referred to as

segments. It is

responsible for the end

to end delivery of the

complete message. The

transport layer also

provides the

acknowledgement of

the successful data

transmission and re-

transmits the data if an

error is found.

· Services point

SPX

addressing

· Message

acknowledgement

Network Layer

(Layer 3)

It works for the

transmission of data

from one host to the

other located in

different networks. It

also takes care of

packet routing. the

sender and receiver's

IP addresses are placed

in the header by the

network layer

· Routing

· Logical Addressing

· Subnet

traffic

control.

IPV4, IPV6, ICMP,

IPSEC, MPLS

Router

Brouters

Data Link

Layer (Layer

2)

It is responsible for the

node-to-node delivery

of the message. The

main function of this

layer is to make sure

data transfer is error

free from one node to

another, over the

physical layer, it

collects the packets to

from frames, which are

then transmitted over

the network.

· Framing

· Physical addressing

· Error control

. Flow control

. Access control

PPP, ARP Frame,

Relay, ATM, Fiber

Cable etc.

Switch

Bridge

Access point

Computer Network

106

YCT

Physical Layer

(Layer 1)

It is responsible for

transmitting individual

bits from one node to

the next. When

receiving data, this

layer will get the signal

received and convert it

into 0s and 1s and send

them to the data link

layer. Which will put

the frame back

together

· Bit synchronization

· Bit rate control

· Physical topologies

· Transmission mode

RJ-45 100 Base Tx,

ISDN.

Hub, NIC, Cable,

Modem, wireless

Repeaters

Network

Topology

Bus

Topology

Star

Topology

Ring

Topology

Tree

Topology

Mesh

Topology

Hybrid

Topology

Basis

Bus

Star

Ring

Tree

Mesh

Hybrid

Topology

2

In this

networking

topology,

each

communicat

ing device

is connected

with every

other device

in the

network. In

order to

connect

n

nodes.

Mesh

topology

require

n(n-1)/2

communicat

ion links

Architecture

A

network

topology in

which there

is a single

line (the bus)

to which all

nodes are

connected

and the node

connect only

to this bus.

A network

topology

in

which

peripheral

node are

connected to

central node

(such as a

hub, switch

or router)

In

ring

topology each

node is

connected to

two other

devices, one

each on either

side, the

nodes

connected

with each

other thus

forms a ring

the link in a

ring topology

is

unidirectional.

Tree topology

is the variation

of star

topology. This

topology has a

hierarchical

flow of data.

In tree

topology all

the computers

are connected

like the

branches

of

tree.

The hybrid

topology is the

combination of

multiple

topologies, used

for constructing a

single large

topology.

Computer Network

107

YCT

Advantages

· Usually

requires

less

cabling

· Allows

easy error

detection

and

· Each node

has an equal

access to

other nodes

in the

· Supported

by most

hardware

and

software

· Date is

· Message

delivery

is more

reliable.

. It is more

effective as it

uses multiple

topologies

. It is contains the

· The failure

correction

· Network

of one

· Star

network

congestio

best and

computer

topology is

· Addition of

receive a by

n is

efficient feature

does not

easy to

new node

all the

minimum

of the

effect the

install.

does not

degrade the

performanc

e of the

network

nodes

efficiently

because of

point-to-

point link.

due to

combined

topology form

which it is

constructed.

other

computers

in the

network

large

number

of links.

Disadvantage

s

· The failure

of the

· The hub

failure

· It

is

relatively

expensive to

construct

· When the

root node

fails, the

whole

· It is very

expensive

· It is relatively

more complex

than the other

backbone

leads to

to

cable

the overall

implemen

topology

results in

network

the ring

network

t.

· It is difficult to

the

crash.

topology.

crashes.

· It is very

install and

breakdown

of entire

network

· Requires

more

amount of

· The failure

of one node

in the ring

· It is difficult

to

configure.

difficult

to

configure

configure.

. It is

difficult to

reconstruct

in case of

faults

cable for

connecting

the nodes.

topology

affects the

other nodes

in the ring.

and

install.

Delay/

Slow

Good

Data has to

Slowly

Manages

Worst

response

Response

time

response

response

make a lot of

stops

because of

more traffic.

high

time.

time because

of one

computer

transmit at a

time

time,

depends on

lot of stops

amounts of

traffic

because

multiple

devices can

transmit

data

simultaneou

sly

Common

Cable

Coaxial

· Coaxial

Twisted pair

requires more

cables than

other

topologies

Overall length

of each

segment is

limited by the

of cabling

used (Coaxial.

Twisted pair-

Fiber)

All king of

Cabling depends

on the types of

networks, twisted

pair, coaxial fiber.

cable, twisted

pair, fiber

cable

twisted

pair fiber

· No more

than 100

meters

from the

computer

to the

connection

device

cable that

can be used

with LAN

and WAN.

Computer Network

108

YCT

Congestion

control

One

computer at a

Compared

bus topology

Information

goes in one

A

transmission

A few of

congestion

Often used across

long distances,

time sends

it gives for

direction

from any

direct from

information on

information.

much better

around the

station

source to

transfer can

Information

performance

ring and

propagates

destination

happen in

goes along

signals don't

passes

along

throughout the

except the

different ways,

the cable and

necessarily

the ring until it

medium and

station with

depending on the

the computer

get

reaches the

can be

less

other topologies.

accesses the

information

off the cable

transmitted

to all the

work stations

correct

computer, no

buffering

at

repeater.

received by all

other stations.

connection

Reliability

If

the

common

cable fails,

then

the

whole system

will crash

In hub fails

then the

whole system

will crash

down.

If the cable

fails or any

computer

shuts down,

then the whole

system will

In case of any

node failure,

other

hierarchical

network are

not affected

A failure of

one device

does not

cause a break

in the

network or

transmission

Extremely rare

reliability

down.

crash down.

of data.

Complexity

Easy

to

connect

or

remove

nodes in a

network

without

affecting any

other node.

Average

complexity

each device

connects to

central

device with

only one link

only.

Complexity

because of

simple to data

to devices.

Move

complex

because of

tree is

combination a

star

network

topology and a

bus topology.

Installation

is complex

in mesh

topology, as

each node is

connected

to more

than one

node.

the

most

complicated one

Security

Any

Security

data travels

The data pass

The

data

The

worst

computer

depends

on

from one

over more

pass

over

security

that is

central

device to the

than one node

more

than

connected to

bus topology

device

security.

next until they

reach their

one node

network will

be able to see

all the data

transmissions

on all the

other

computers

destination.

Computer Network

109

YCT

TCP/IP Model

TCP/IP stands for Transmission control

Protocol/Internet Protocol and is suite

communication Protocols used to interconnect

network devices on the internet. TCP/IP is also

used as a communication Protocol in a private

computer network. The TCP/IP model is a

concise version of the OSI model.

Logical connections between layers of

the TCP/IP Protocol.

Source

host

Destination

host

Application

Logical Connection

Application

>

Transport

>

Transport

Network

>

Network

Data link

--

>

>

Data link

Physical

--

>

Physical

Switch Router Switch

LAN

Router

LAN

Source

host

Link 1

Link 2

Destination

host

TCP/IP

Application

Transport

Network/

Internet

Data link Physical

1. Physical Layer- This

layer is

responsible for generating the data and

requesting connections. It acts on behalf of the

sender and the Network access layer on the

behalf of the receiver.

2. Transport Layer- This layer monitors end to

end path selection of the packets. It also provides

service to two application layer. Transmission

control Protocol (TCP) and User datagram

Protocol (UDP) are transport layer protocol at

this level.

1. TCP 2. UDP

3. Internet Layer- This layer is responsible

for sending packets different networks.

The main protocols residing at this layer

are as follows.

IP

ICMP

ARP

IPV4

IPV6

Reverse Proxy Gratuitous Intverse

4. Data link Layer- It is the closest to the network

hardware. It provides service to Internet layer.

5. Application Layer- This layer is analogous to

the transport layer at the OSI model. It is

responsible for end to end communication and

error free delivery of data.

TCP/IP model Vs OSI Model

OSI

TCP/IP

OSI represent open

system Interconnection

TCP/ IP model represents

the Transmission Control

Protocol/ Internet

Protocol.

OSI is a generic

independent Protocol in

standard. It is acting as

an interaction gateway

the network and the

final user.

TCP/IP model depends on

standard protocols about

which the computer

network has created. It is

a connection protocol that

assigns the network of

hosts over the internet.

The OSI model

represents defines

administration, interface

and connections. It

describes clearly which

layer provides services.

It does not mention the

services, interfaces, and

protocols.

The protocols of the

OSI model are better

unseen and can be

appropriate protocol

quickly.

.The TCP/IP model

protocols are not hidden,

and we can't fit a new

protocol stack in it.

It provides both

connection and

connectionless oriented

transmission in the

network layer however

only connection

oriented transmission in

the transport layer.

It provides connectionless

transmission in the

network layer and

supports connecting and

connectionless oriented

transmission in the

transport layer

The smallest size of the

OSI header is 5 bytes.

The smallest size of the

TCP/IP header is 20

bytes.

Network Types

Local Area Network- LAN is usually privately

owned and connects a few hosts within a single

building , office or campus.

Each host in a LAN has a identifier, an address,

that uniquely defines the host in the LAN.

Packets sent by one host to another host contain

the addresses of both the source host and the

destination host.

Computer Network

110

YCT

Most LANs use a smart connecting switches

which is able to recognize the destination address

of the packet to all other hosts.

Host-1

Host-2

Host-3 Host-4 Host-5

LAN (Common cable)

Host-1 Host-2

Switch

Host-3 Host-4

LAN with a switch

Metropolitan Area Network

It is larger than LAN but smaller than WAN.

This is the type of computer network that

connects computers over a geographical

distance through a shared communication path

over a city, town or metropolitan area.

College

Government

building

MAN

Office

Residential

Area

Wide Area Network

WAN has a wide geographical extension, it

means spreading in different geographical

location. WAN inter connects connecting devices

such as switches, routers or modem. WAN is

normally built and operated by communications

companies and leased by the organization using

it.

Example of WAN-

Point-to-Point WAN- This network connects

two communicating device through a

transmission media.

Switch WAN- It is a combination of several

point-to-point WANs that are connected by

switches.

To another

Network

To another

Network

To another

Network

To another

Network

LAN with a switch

The Internet

Internet is two or more networks that can

transmit data with each other.

Back

bones

Backbones are large networks owned

by some communication companies

Verizon, AT & T, sprint etc.

Customer

Network

Customer

Network

Customer

Network

Customer

Network

Network

Provider

Network

Provider

Peering

Point

Peering

Point

Back bones

Network

Provider

Network

Provider

Network

Provider

Customer

Network

Customer

Network

Customer

Network

Customer

Network

Customer

Network

Customer

Network

Peering

Point

Network

Provider

Peering points are complex switching

system that connects backbones.

It is a smaller networks that use the

services of the backbones for a free. It

connected to backbones and sometime

to other provider networks.

Customer

Network

The customer networks are networks at

the edge of the internet that is use the

services provided by the internet.

Customer network pay a fee to the

provider network to receive the

services.

ISP

Internet service providers is a

combination of backbones and provider

networks.

The backbones are after referred to as

international ISPs.

Provider networks are often referred to

as national or regional ISPs.

Computer Network

111

YCT

Accessing the Internet

Accessing Internet

1. Using Telephone Networks

2. Using Cable Networks

3. Using Wireless Networks

1.

Using Telephone Networks-

i. Dial up service

ii. DSL service

i. Dial-up Service- In this connection the

services connect to the internet through a phone

line connection. Dial-up service established

between two or more communication devices in

which it uses Public Switched Telephone

Network (PSTN) for connect to the internet. Its

data transfer rate is up to 56 kbps.

Digital

Analog

High speed digital

Dial-up connection

Modem

Converter

Telephone

network

S

X

Internet

P

Uploading 33.6 kbps

Downloading 56 kbps

ii. Digital Subscriber Line (DSL)- DSL

technology is the most promising for supporting

high-speed digital communication over the

existing telephone. This technology is a set of

technologies, each differing in the first letter

(ADSV, VDSL, HDSL and SDSL). The set is

often referred to as xDSL, where x can be

replaced by A, V, H, S. ADSL, provides a wider

frequency range for downstream transfers, which

offers several time faster downstream speeds. An

ADSL connection may offer 20 Mbps

downstream and 1.5 Mbps upstream.

Telephone

PC

Point-to-point WAN

PC

000

DSL

Core

DSLAM

2.

Cable Networks- Cable TV network ware

originally created to provide access to TV

programs, but later cable networks became

popular among people who just wanted a better

signal. In addition, cable networks enabled

access to remote broadcast stations via

microwave connections.

Now cable TV found a good market in internet

access provision.

Types of cable TV Networks are as follows-

1. Traditionally Cable Networks

2. Hybrid Fiber-Coaxial Network

1. Traditionally Cable Networks was called

Community Antenna Television (CATV) in

1940s.

2.

Hybrid Fiber-Coaxial Network (HFC) This

network user a combination of fiber and

coaxial cable.

Optic

Drop

cable

Coaxial cable

Head

end

Splitter

Amplifier

Traditional Cable Network

Tap

Optic

High bandwidth

fiber

Swtich

Distribution

Hub

Fiber

Node

Bidirectional

amplifier

Fiber

Node

Fiber

Coaxial

cable

SONET

· Synchronous Optical Network is a

communication protocol. It is used to transmit a

large amount of data using optical fiber.

· By SONET, multiple digital data streams

transferred at the same time over the optical

fiber.

SONET Network Elements

STS

Multiplexer

· Its converts electrical signal

to optical signal.

· STS performs multiplexing

of signals.

STS

De-

multiplexer

· It performs signal de-

multiplexing.

· It converts optical signal to

electrical signal.

Regenerator

It is a repeater that takes an

optical signal and strengthens it.

Multiplexer

This device allows to remove a

signal or add signals coming

from different sources into

given path.

Terminals

STS

Mux/

Memux

Regenerator

Regenerator

Add/Drop

Mux

Computer Network

112

YCT

O

SONET Layers- SONET includes

four

functional layers

Data Link

Path Layer

Line Layer

Section Layer

Physical

Photonic Layer

Path

Layer

· Path layer functionalities are provided

by STS Mux/Demux.

. Path layer is responsible for the

movements of signals from its optical

destination.

Line

Layer

· The line layer is in charge of signal

movement across a physical line.

· STS Mux/Demux and Add/Drop mux

provides its functions.

Section

Layer

. It layer responsible for the movement

of signal across a physical section.

· It layer functions are provided by each

network device.

Photonic

Layer

. It layer relates to the OSI models

physical layer.

· This includes physical specifications

for the optical fiber channel.

Wireless Transmission Radio

Wireless transmission is a format of unguided

media. Wireless communication involves no

physical link established between two or more

devices communicating wirelessly. A little part

of electromagnetic spectrum can be used for

wireless transmission.

O

Radio Transmission- Wireless communication

is the transmission of voice and data without

cable or wire. Radio waves can have wavelength

from 1mm to 100,000 km and have frequency

range from 3Hz (Extremely low frequency) to

300 GHz (extremely high frequency).

O

Infrared- Infrared is used for short-range

communication like TV remotes, Mobile phones,

Personal computers etc. The frequency range of

infrared rays 300 GHz to 400 THz.

Radio waves- Radio waves can travel large

distances as well as penetrate any wall (uni-

directional). The requirement of radio waves are

antennas, sending antennas when are transmit

message other is receiving range 3 KHz-1 GHz.

0

Microwaves- Microwaves are ratio waves that

provide a high-speed signal transmission.

Microwaves are a line of sight transmission.

Microwaves have a frequency range between

1GHz-300 GHz. Microwave unidirectional

antennas send out signal in one direction.

O

Millimeter wave- Millimeter wave is a band of

electromagnetic spectrum that can be used proud

range of product and services. It is high-speed

point to point wireless local area networks

(WLANs) and broadband access range 30 GHz

to 300 GHz.

Lightwave Transmission

Light wave transmission is used for wireless

lasers communication. It is a relatively low cost

way to connect two building LAN. Laser light

also diffuses easily in poor atmospheric

condition likes rain, fog and so on.

O

Telephone Local Loop- Local loop is the

portion of the telephone system that connects

home or office. Local loop wiring is used

Unshielded Twisted Pair (UTP) cabling to the

transmission method distance from the telco is co

to subscriber's customer premises 5 kilometers.

Local loop

Telco

Customer

Premises

Copper

twisted

pair cabling

Fiber-optic

cabling

Switching

Network

Maximum

5 kilometers

Local loop

O

Trunks- Trunks are used to form networks and

to interconnect LANs (Local Area Networks) to

form WAN (Wide Area Network) or VLAN

(Virtual LAN). Trunk network is built up locally

or through the internet. It is a point to point

connection between two points on a different

networks.

Multiplexing

Multiplexing is a set of technique used to

combine and send the multiple data over a single

medium. Multiplexing is a many to one combine

a single stream. There are a three multiplexing

technique such as-

Frequency Division Multiplexing (FDM), Wave

length Division Multiplexing (WDM), Time

Division Multiplexing (TDM).

Computer Network

113

YCT

FDM- FDM is an analog multiplexing technique

that combines analog signals.

WDM-WDM is an analog multiplexing

technique to combine optical signals. WDM is

used the high data rate capability of a fiber optic

cable.

TDM- TDM is a digital process that allow a

several connection to share high bandwidth of a

link.

Narrowband ISDN- Narrowband ISDN

integrated services digital network is called the

N-ISDN. Narrowband integrated services digital

network an attempt to digitize the analog voice

information. N-ISDN is users 64 kbps circuit

switching.

Broadband ISDN- Broadband integrated

services digital network digital networking

services and provides digital transmission

telephone wires as well as over other media. The

broadband ISDN speed is around 2 MBPS to 1

GBPS and the transmission is related to ATM.

The broadband ISDN communication is usually

made using the fiber optic cables.

O

ATM- A synchronous Transfer Mode (ATM) is

a switched wide area network based cell relay

protocol designed by ATM forum and adopted

by (ITU-T). International Telecommunication

Union-Telecommunication Standard Section

(ITU-T) efficient for call relay transmits all

information such as video or voice.

High Speed LANs- The IEEE 802.3 to 802.6

LAN is data transfer rates in the range of 10

Mbps to 16 Mbps served. The high speed LAN

that is emerged broadly categorized into three

types on taken passing, successors of Ethernet

and switching technology. High speed LANs

with data transfer rate of 100 Mbps to more.

There are varieties of Fast Ethernet such as 100-

Base-Tx, 100-Base-Fx and 100-Base-Tu etc.

O

Cellular Radio- Cellular radio is a form of

broadcast radio used widely mobile

communication specifically wireless modems

and cell phones. A cell phone to access web,

send and receive e-mail. A cell phone is a

telephone devices that uses high frequency radio

waves to transmit voice and digital data

messages.

Communications Satellite

A communication satellite is a space station

receives microwave signal earth based station

amplifies a signal. Transmission from an earth

based station to a satellite is an uplink.

Transmission from a satellite to an earth-based

station is a down link. There are three

communication satellite such a as Geo Stationary

Earth Orbit (CEO), Low-Earth-Orbit (CEO) and

Medium-Earth-Orbit (MEO).

O

Geosynchronous Earth Orbit/Geo-stationary

Earth Orbit- Geosynchronous orbit is the

Geostationary orbit Geosynchronous orbit

include O' to earth's equatorial plane (that is

directly above the equator). Line-of-sight

propagation is sending and receiving antennas be

locked into each other location. A satellite moves

faster or slower than the Earth's rotation is useful

only for short periods.

LEO Satellites- Low-Earth-Orbit (LEO)

satellite polar orbits. The altitude is between 500

and 2000 km with a rotation period of 90 to 120

min. The satellite is a speed of 20,000 to 25000

km/h. Low-Earth-Orbit satellites orbits are

commonly used for communication military

reconnaissance, spying and other imaging

application.

Switching

In large networks, switching technology

determines the best path for data transmission,

from the sender to the receiver.

Switching techniques are used to connect

switching techniques are used to connect systems

to perform auto-one communications.

Switching

Circuit

Switching

Packet

Switching

Message

Switching

Virtual Circuit

Approach

Datagram

Approach

Switching and TCP/IP Layers- There are four

switching at TCP/IP layer.

Computer Network

114

YCT

Switching at Physical Layer- Physical layer

can have only circuit switching. There are no

packets exchanged at the physical layer. Physical

layer allow signal to travel in one path or

another.

Switching at Data Link Layer- Data link layer

is packet switching. Packets means frames or

cells. Packet switching at the data link layer done

using virtual circuit approach.

Switching at Network Layer- Network Layer is

packet switching. Network layer can be used

virtual circuit approach or datagram approach.

Switching at Application Layer- Application

layer is a message switching. The

communication at application layer occurs by

exchanging messages. We can say that

communication using email is a kind of message

switched communication.

Circuit Switched Networks

A circuit network is made of a set of switches

connected by physical links in which each link is

divided in to n channels. ISDN is an example of

circuit switched network.

I

II

A

One link, n channels

A

A

Path

M

A

IV

CIRCUIT-SWITCH NETWORK

The actual communication in a circuit switch

network requires three phases are connection

setup, data transfer and connection teardown.

1. Setup Phase- Setup phase two parties (or

multiple parties in a conference call) can

communicate a dedicated circuit needs to be

established. The end systems are normally

connected through dedicated lines to the

switches.

2. Data Transfer Phase- After the

establishment of the dedicated circuit (channels)

the two parties can transfer data.

3. Teardown Phase- When one of the parties

needs to disconnect, a signal is sent to each

switch to release the resources.

Packet-Switched Network

In a computer network, communication between

two ends is done in blocks of data called packets,

this allows us to make switches work for both

storages and forwarding because a packet is an

independent entity that can be stared an later can

be sent in.

Packet 1

Packet 1

Packet 2

Packet 2

Packet 2

There are two type of packet switched network.

(i) Datagram networks

(ii) Virtual Circuit Networks

Datagram networks- Datagram networks are

referred to as connection less networks. There

are no setup or teardown phases. Each packet is

treated the same by a switch regardless of its

source or destination.

i. Routing tables- The routing tables are

dynamic and updated periodically. The

destination addresses and the corresponding

forwarding output ports are recorded in the

tables.

ii. Destination address- The destination address

is the header of the packet in a data gram

network remains the same during the entire

journey of the packet.

· ATM (Asynchronous Transfer Mode) is

fundamental packet switching.

Virtual-Circuit Networks

C

End System

R

Z

A

B

Z

Switches

X

End System

End System

R

K

End System

D

Computer Network

115

YCT

A virtual-circuit-switched network is across

between a circuit-switched network and a data

gram network. There are some characteristics of

a virtual circuit switched network such as

i. There are setup and teardown phases in

addition to the data transfer phase.

ii. Resource can be allocated in setup phase

circuit switched network or on demand as in

a datagram network.

iii. A virtual circuit network is normally

implemented in data link layer. While circuit

switched network is implemented physical

layer and datagram network in the network

layer.

Addressing- Virtual-circuit network two types

addressing are involved such as global and local

(virtual-circuit identifier)

Important factor of (ARP) Protocols

· Address Resolution Protocol (APR) is used to

get MAC address of a node by providing IP

addresses.

· ARP is used to find the MAC addresses that

corresponds to an IP address.

· The ARP protocol is one of the auxiliary

protocol defined in the network layer. It maps

an IP address to a logical link address. ARP

accepts IP address from the IP protocol maps

the address to the corresponding link layer

address and pass to the data link layer.

· The data link layer is responsible to creation

and delivery of a frame to another node. It is

responsible for packetizing (framing), flow

control and error control, congestion control

along the link.

· Link layer protocols three types of addresses

such as unicast, Multicast and broadcast.

Unicast- Address Unicasting one-to-one

communication. A frame unicast address

destination is destined only one entity in the

link. Example A3:34:54:11:92:F1 It is

separated by colons.

Multicast address- Multicast address one-to-

many communication. Example A2:34:45:11:92:F1

Broadcast address- Broadcasting one to all

communication. Example FF:FF:FF:FF:FF:FF

0

Redundancy- The control concept in detecting

or correcting error is redundancy. Redundant bits

are added by the sender and removed by the

receiver. It is allows the receiver to detect or

correct corrupted bits.

. An error-detecting code can detect only the type

of errors for which it is designed other of errors

may remain undetected.

· A single-bit error is the same for us as a burst

error called error correction. The number of

error and the size of message are important

factors. We can divide coding schemes into two

broad categories block coding and convolution

coding.

· Minimum hamming distance for error detection

is set of code words. The minimum hamming

distance is a smallest hamming distance

between all possible pairs of code words.

· Minimum distance for linear block codes are

number of non-zero valid code word with the

smallest number.

· Parity check code error detection is a linear

block code.

· Error detection technique is based on a binary

division Cyclic Redundancy Check (CRC).

· Cyclic Redundancy check is a subset of cyclic

code (CRC) is used in network such as LAN,

WAN. It is used to binary division error

detection technique.

· Checksum is an error detecting technique

applied to a message of any length. Checksum

technique is used at the network and transport

layer rather than the data-link layer.

· Data link control (DLC) is connectionless or

connection oriented. DLC is a net way and

transport layer protocol.

· Data Link Control (DLC) is procedure for

communication between two adjacent nodes

such as node to node communication. Data link

control function include control function

include framing and flow error control.

Computer Network

116

YCT

Connection less Protocol- Connectionless

protocol frames are sent from one node to next

without any relationship between the frames.

Frames are not numbered and there is no sense of

ordering.

Connection Oriented Protocol- Connection-

oriented protocol is a logical connection

established between two nodes. Connection

oriented protocol some point-to-point protocol.

Same wireless LAN, and some WAN.

Connection oriented protocol are rare in wired

LAN.

Protocol

Description

PPP

Point-to-point protocol provide the

services of physical layer. But to control

and manage the transfer of data link

layers. PPP does not provide any flow

control. Error control is also limited to

error detection. PPP uses a character

oriented frame. It is a link layer protocol

such as link control protocol.

HDLC

High level Data Link Control (HDLC) is

a bit oriented protocol for

communication over point-to-point and

multipoint link. HDLC is a three types of

frames, information frame (I-frame),

supervisory frame (s-frames) and

unnumbered frames (u-frames).

Media Access Control (MAC)

Random-access

protocols

Controlled-access

protocols

Channelization

protocols

ALOHA

+Reservation

+ FDMA

CSMA

+Polling

TDMA

CSMA/CD

Token passing

CDMA

CSMA/CA

Media Access Control is a sub-layer in the data

link layer.

ALOHA- Aloha is random access method. It

was designed for a radio (wireless) LAN, but it

can be used on any stared medium. The original

ALOHA protocol is called pure ALOHA. Pure

ALOHA is vulnerable time a station send frame.

Slotted ALOHA was invented to improve the

efficiency of pure ALOHA.

O

TDM- Time Division Multiplexing is requires

the transmitter and receiver to be synchronized

periodically.

Description

CSMA/CD

CSMA/CD is reduce the possibility of

collision but it is not eliminate it.

Carrier Sense Multiple Access with

collision detection CSMA/CD

transmission and collision detection

are continuous processes. We do not

sent the entire frame and then look for

the collision. CSMA/CD as the media

access method Ethernet LAN as token

passing, Token Ring, Token Bus.

CSMA/CA

Carrier Sense Multiple Access with

collision (CSMA/CA) is a wireless

network. Collision are avoided through

the use of CSMA/CA three strategies

such as Inter frame space, contention

window, acknowledgements.

IEEEI 802 Standard for LANs (MAC)

LLC-Logical Link Control

MAC: Media Access

Control

Data-link layer

Ethernet

MAC

Token Ring

MAC

Token

Bus

MAC

Physical layer

Ethernet

Physical

Layer

Token Ring

Physical

Layer

Token

Bus

Physical

Layer

Transmission media OSI or TCP/IP suite

Transmission media IEEE standard

. IEEE 802.16 standard for Wi-Max technology.

HUB

A hub is a device that operates only in the

physical layer. A repeater is a multiport device is

called hub. A hub or a repeater is a physical layer

device. Type of Hub- Active Hub, Passive Hub,

Intelligent Hub.

HUB

Sent

Maintained

Discard

Discard

A

B

C

D

Computer Network

117

YCT

Routers

A router is a three layer device operates in the

physical layer. Data-link layer, network layer. A

router is an internetworking devices. A router

change the link-layer addresses in a packet.

I

10 Gigabit

LAN

Gigabit LAN

Gigabit LAN

Switch

Switch

System

System System

System

Dynamic Host configuration Protocol

(DHCP)- DHCP is an application layer program

using the client server helps TCP/IP at the

network layer. DHCP to assign permanent IP

address is the host and router.

Bridge

A bridge operates data link layer. A bridge is a

repeater add on functionality filtering by reading

the MAC address source and destination. Bridge

is used inter connecting two LAN working same

protocols.

Gateway

Gateways are protocol converters and operate at

any network layer. Gateways are generally more

complex than switch or routers. A gateway is

also called protocol converter.

Tunneling

Tunneling is used in virtual private networks

(VPNs). It can also setup efficient and source

connections between networks, enable the

unsupported network protocol. A VPN is a

secure, encrypted connection over the public

shared network. VPN is a Transport Layer

Security (TLS) protocol operate layer 6 and layer

7 of OSI model. TLS is sometimes called SSL

(Secure Socket Layer).

Fragmentation

Fragmentation is a process divided packets into

smaller pieces (fragments) so that resulting

pieces can travel across link smaller Maximum

Transaction Unit (MTU) that original packed

size. The network layer fragmentation data when

the maximum size of a data gram exceeds the

maximum size of data that can retained in a

frame. There are three type of fragmentation.

External fragmentation, Internal fragmentation,

Data fragmentation.

Firewalls

Firewalls provide protection against outside

cyber attackers by shielding your computer or

network from malicious or unnecessary network

traffic. There is a two types of firewall.

i. Packet-Filter firewall- A packet-filter

firewall is a router that uses a filtering table to

decide packet must be discard (not forward). It is

based on network layer and transport layer.

ii. Proxy Firewall- A proxy firewall is a

network security system that protect network

resource by filtering messages at the application

layer.

Routing -> Routing Algorithms

i. Distance-vector Routing- DVR is used to

find the least cost (shortest distance) between

a source node (using the Bell man-ford

Equation).

ii. Link state routing is select the best least-cost

route to transfer the data packets between the

sender/source and receiver/destination.

iii. Path-Vector-Routing is not actually used in

an internet and is mostly designed to route a

packet between ISP. Example BGP is a path

vector routing protocol.

Congestion Control

Congestion control a number of packets send to

the network is greater than the capacity of the

network. It can handle the number of packets a

network.

Computer Network

118

YCT

Cryptography

Cryptography is technique of securing

information and communication to achieve

message integrity and confidentiality and

exception. The cryptographic parameter client

and server a 48 byte master secret is created from

the pre-master secret by applying two hash

function (SHA-1 and MDS).

Public key

Public key cryptography is used for email traffic,

such as with the standard encryption method

S/MIME, for digital signatures as well as for

cryptographic protocol such as SSL/TLS, SSH

and HTTPS.

Secret key

Secret key cryptography is also called symmetric

cryptography because the same key is used to

both encryption and decryption the data. Secret

key crypto graphic include Advanced Encryption

Standard (AES). Triple Data Encryption

Standard (3DES) and Rivest Cipher 4 (RC4).

Domain Name System

DNS is a host name for IP address translation

service. It is application layer protocol for

message exchange between clients and servers.

DNS is a distributed data base internet service

that translate domain name to IP address. TCP/IP

protocol use the IP address.

Electronic Email Security

Email security is the process of ensuring the

availability, integrity and authenticity of email

communication by protecting against the risk of

email threats.

Name Server

Name server are work as a directory that

translates domain names in to IP addresses.

Symmetric Key Cipher

A symmetric key cipher uses the same key for

both encryption and decryption. A key can be

used for bidirectional communication.

Asymmetric key cryptography is based on

applying mathematical function to the number.

Asymmetric key cryptography is a use to public

key and private key.

Electronic Email

Electronic mail allows users to exchange

messages. When the request arrives the server

provides the service. Electronic mail is an on

way transaction.

Email-Architecture

A

Mail Server

Mail Server

B

E-mail Sender

E-mail Receiver

Internet

LAN/WAN

Client

Server

Client

Server

Server

Client

(1) MTA

(2) MTA

(3) MAA

SMTP Protocol

SMTP Protocol

Pop or IMAP

Protocol

Protocol

Description

SMTP

Simple Mail Transfer Protocol is an

internet standard communication

protocol for electronic mail

transmission message transfer agents

use SMTP to send and receive mail

messages.

POP3

Post Office Protocol Version 3 (POP3)

provides access to an inbox stored in an

email server. It executes the down load

and delete operation for messages.

MIME

Multipurpose Internet Mail Extensions

allows an e-mail message a non-ASCII

file such as a video image or a sound

and it provide mechanism transfer non

text characters to text characters.

IMAP4

Internet Message Mail Access Protocol,

version 4 is an application layer

protocol that operates for receiving

emails from mail server. Users have

remote access to all the contexts.

Domain Name System Resource Records

Resource records are used to store data domain

names and IP addresses. Each resource record

specifies information about particular object. The

server uses these records to answers queries for

hosts in its zone.

Computer Network

119

YCT

10.

PROGRAMMING IN

C and C++

A token is the smallest element of a program that

is meaningful in the compiler.

Identifiers

Special

characters

Keywords

Token

Constants

Operators

Strings

Identifier refers to name given to entities such as

variables, functions, structures, array etc.

Identifiers must be unique.

Keywords is reserved word. It can't use as a

variable name and constant name.

auto

break

case

char

const

double

else

continue

default

do

enum

extern

float

for

goto

if

int

long

register

return

short

signed

sizeof

static

struct

switch

typedef

union

unsigned

void

volatile

while

Constant is a name given to the variable. It can't

altered or changed during execution once

defined.

String is a sequence of characters terminated

with a null character '\0' strings are defined as an

array of characters. Example-

Char str[] = "YCT"

Index 0 1 2

Str

YCT

Operators are used to perform the operations on

variables and value.

Operators

Arithmetic

Relational Logical

Bitwise

Assignment

Others

Arithmetic Operators

Arithmetic operators are used to perform

mathematical operations.

Operators

Meaning of Operators

+

Addition, Adds two values

–

Subtraction, Subtracts one value

from another

*

Multiplication, Multiplies two

values

/

Division, Divides one value by

another

%

Remainder after division

++

Increment, increase the value of a

variable by 1

--

Decrement, Decreases the value of a

variable by 1

Relational Operators

Relational Operators are used to checks the

relationship between two operands.

Operators

Meaning of Operator

==

Equal to

! =

Not equal

>

Greater than

<

Less than

>=

Greater than or equal to

<=

Less than or equal to

Logical Operators

Logical operators are used to determine the logic

between variable or values and return either 0 or 1.

Operators

Operators Meaning

&&

Logical and, Returns true if the both

statements are true.

ǁ

Logical or, Returns true if the one

of the statements is true.

!

Logical Not, Reverse the result,

returns false if the result is true.

Programming in C & C++

120

YCT

Bitwise Operators

Bitwise operators are used to perform bit level

operations.

Operators

Meaning of Operators

&

Bitwise AND

|

Bitwise OR

^

Bitwise XOR (Exclusive OR)

<<

Left Shift

>>

Right Shift

~

Bitwise complement

Assignment Operators

Assignment operators are used to assign values

to variables.

Operators

Meaning of Operators

=

Simple Assignment

* =

Multiplication Assignment

/=

Division Assignment

% =

Remainder Assignment

+ =

Addition Assignment

-=

Subtraction Assignment

<<=

Left Shift Assignment

>>=

Right Shift Assignment

& =

Bitwise AND Assignment

A=

Bitwise exclusive OR Assignment

|=

Bitwise inclusive OR Assignment

Other Operators

Operators

Meaning of Operators

Sizeof()

To return the actual sizeof any

given variable

&

To return the address of any given

variable

*

Pointer to a variable

? :

Conditional expression or ternary

operator

->

Member selection operator

,

Comma operators linked related

expression together.

Special Characters

Special symbols have some special meaning and

they can't be used for other purposes.

Symbol

Meaning

Symbol

Meaning

~

Tilde

/

Slash

#

Pound sign

|

vertical bar

$

Dollar sign

\

back slash

%

Percent

sign

`

Apostrophe

^

Caret

-

Minus sign

&

Ampersand

=

Equal

*

Asterisk

<

Opening angle

bracket

(

Left

parenthesis

>

closing angle

bracket

)

right

parenthesis

?

Question mark

–

Underscore

{

Left brace

+

Plus sign

}

Right brace

'

Comma

[

Left bracket

.

Period

]

Right bracket

:

Colon

11

Quotation mark

.

,

Semicolon

O

Data types in C- There are several different

ways to store data in C and they are all unique

from each other. The types of data that

information can be stored as are called data type.

Data Type

Primary

User Defined

Derived

Integer

Class

Function

Character

Structure

Array

Floating Point

Union

Pointer

Double Floating

Point

+ Enum

Reference

Void

Typedef

O

Control Structure: LOOPS- A loop is used to

repeat a block of code until the specified

condition is met.

Control Statements

Selection

Statement

Iterative

Statement

Jump Control

Statement

If, If-else,

Nested if-else,

else if ladder

While, Do

while, For

Break,

Continue,

Goto, Return

For Loop

Syntax:

for(init statement; testexpression; updatestatement)

{

//body of loop

}

Programming in C & C++

121

YCT

O

How for loop works:

1

initstatement

Test

Expression

False

True

For body Loop

Update Expression

O

/* Calculation of simple interest for 3 sets p, n

and r */

main(){

int p, n, count;

float r, si;

for (count =1; count <= 3; count

= count + 1)

{

printf("Enter values of p, n and r");

scanf("%d %d %f", &p, &n, &r);

si = p * n * r/100;

printf("simple interest = Rs. %f\n", si);

}

}

Flow-Chart of Program

Start

Count = 1

is

No

Count = Count + 1

Count <= 3

Stop

Yes

Input

p, n, r

Si = p*n*r/100

Print

si

Nested for Loop- A for loop inside another for

loops is called nested for loop.

Syntax-

for(init;condition;increment) {

for(init;condition;increment) {

//statement of inside loop

}

//statement of outer loop

}

Flow-Chart of Nested for Loop

Outer for loop

start

init expression

Outer for loop

Test

Condition

False

inner for loop

start

inner for loop

test

condition

False

True

Block of statement

Update Expression

of inner for loop

Stop

Update expression

of outer for loop

Stop

Consider the program given below.

main(){

int r, c, sum;

for (r=1; r <= 3; r++){

for(c=1; c <= 2; c++){

sum =r+c;

printf("r = %d c=%dsum = %d\n", r, c,

sum);

}

}

}

While Loop- The while loop, loops through a block

of code as long as a specified condition is true.

Programming in C & C++

122

YCT

Syntax-

While(condition) {

//statement of

body

}

1

Text

Expression

True

While loop

body

Understand operation of the while loop by

chart-

Start

Count = 1

is count < = 3

No

input p, n, t

Stop

si = p*n*r/100

print si

Count = count ++

Do/While Loop- This loop will execute the

code block once, before checking if the condition

is true, then it will repeat the loop as long as the

condition is true.

Syntax-

do

{

//block to be executed

}

while (condition);

!

do

while

loop body

True

Test

Condition

False

Selection Statements

1. If statement

Syntax-

if(condition)

{

statement execute if

statement is true

}

Flow-Chart of if statement

Start

False

if condition

True

If body

Statement just

below if

Exit

2. If-else statement-

Syntax-

if(condition) {

//execute block if condition true

} else {

//execute if condition false

}

Flow-Chart of if-else

Start

Condition

False

True

Statement in

if branch

Statement in

else branch

Stop

3. Nested if-

Syntax-

if(condition 1)

{

//execute if condition 1 true

if(condition 2){

//execute if condition 2 true

} else { execute if condition 2

false

}

}

else {

execute if condition 1 false

}

Programming in C & C++

123

YCT

Flow-Chart of Nested if

1. Break Statement Syntax-

//specific condition

break;

Start

if condition

False

Nested if

condition

Flow-Chart of break statement

True

False

Nested if

body

Loop body

starts

if body

Nested else

body

Statement

just below if

Condition to

break from

loop

True

Break

Exit

False

4. If-else ladder-

Syntax-

2. Continue statement

if(test expression) {

//statement

} else if {

Syntax-

Continue;

Flow-Chart of continue

//statement

}

else if{//statement

}

Loop body

starts

Condition to

continue next

iteration

.

True

Continue

.

.

else {//statement

}

False

Flow-Chart of Ladder if -else

Execute remaining

part of loop

body

Start

Condition1

Yes

Statement1

Condition2

Yes

Statement2

Array and Strings

O

Arrays- Array are used to store multiple values

in a single variable, instead of declaring separate

variables for each values.

Condition3

Yes

Statement3

Statement4

int arr[8]->array size

Statement

below it

array name

data type

O

Access the element of an Array-

Exit

First Index

Last Index

Jump Statements

It is used to interrupt the flow of the program or

escape a particular section of the program.

First element>

(at index 0)

0

---

1

2

Programming in C & C++

124

YCT

Example-

int main(){

int myFirstIndex[] = {25, 40, 70, 150};

printf("%d", myFirstIndex[0]);

return 0;

}

output =25

O

Array in Loop-

Example-

int main()

{

int arr [] = {5, 10, 15, 17, 20};

int i = 0;

while (i <5)

{

printf("%d", arr[i]);

i++;

}

return 0;

}

Output = 5 10 15 17 20

0

Multidimensional Arrays-

A multidimensional array is an array of arrays.

Syntax-

data_type array_name[size 1][size2] ..... [sizeN];

Multi-dimension

Array

Two dimension

Array

Three dimension

Array

Example-

Column 0

Column 1

Column 2

Row 0

2

3

4

Row 1

5

6

8

int main(){

int matrix[2][3] = {{2,3,4},

{5,6,,8} };

int i,j;

for (i=0; i<2; i++){

for(j=0;j<3; j++){

printf("%d\n", matrix

[i][j]);

}

}

return 0;

}

Output:

2

3

4

5

6

8

Strings- Strings are used for storing

text/characters.

-

Strings Initialize

Char c[] = "ab";

+ Char c[20] = "ab";

+ Char c[] = {'a','b','\0');

+ Char c[6] = {'a','b', '\0');

C[0] [1] C[2]

a

b

10

Example-

int main(){

char greetings[] = "Hello YCT";

printf("%s", greetings);

return 0;

}

Output = Hello YCT

Memory Address

The memory address is the location of where the

variable is stored on the computers. Memory

address is in hexadecimal form.

Pointers

Pointers are used to store the address of variables

or memory location.

Syntax-

datatype *var_name;

Declare a pointer variable must be a * before its name.

How to pointer works

var

int var = 10;

10

#2008

20

30

S

int *ptr = & var;)

*ptr =20;

int *ptr = & ptr; )

** ptr =30;

S

Programming in C & C++

125

YCT

Example-

main(){

int a;

pirntf("%d", &a); //print address of a

return0;

}

Output = 0x7ffe59c7a1e4

Note- Output can be assigned different address in

different runs.

Example-

int main(){

int* PC, C;

C=32;

printf(" Address of C:%d\n", & c);

printf("value of C:%d\n\n", C);

PC = & C;

printf("Address of pointer PC:%d\n"PC);

printf("Content of pointer PC:%d\n\n", *PC);

C=11;

printf("Address of pointer PC:%d\n", PC);

printf("content of pointer PC:%d\n\n", * PC);

*PC = 2;

printf("Address of C:%d\n", &C);

printf("value of C: %d\n\n", C);

return 0;

}

Output-

Address of C : 0x7ffd485f65ec

value of C: 32

Address of pointer PC: 0x7ffd485f65ec

Content of pointer PC: 32

Address of pointer PC: 0x7ffd485f65ec

Content of pointer PC: 11

Address of C: 0x7ffd485f65ec

Value of C: 2

Functions

0

Functions- A function is a block of code which

only runs when it is called.

Syntax-

void myFunct(){

//declaration

//code to be executed(definition)

}

Function

Standard Library

Functions

User Defined

Function

Programming in C & C++

O

Standard Library Functions- Library functions

are used to defined in header files.

Some Header Files

conio.h

It is type of console output/input header

file.

stdio.h

It is a standard type of output/input header

file.

time.h

The function that are time related

math.h

The function are related to math

operations.

errno.h

The function are related to error handling

functions.

print()

The function send formatted output on the

screen. This function defined in the stdio.n

header file.

Ctype.h

Character type functions

assert.h

Program assertion functions

User defined function- Working flow of user

defined function

#include<stdio.h>

void functionName(){

=

}

int main(){

=

functionName();

=

}

function names are identifiers and should be

unique.

User Defined Function

1. No arguments and no return value

2. No arguments and a return value

3. Arguments and return value

4. Arguments and with return value

1. No Arguments and no return value-

Syntax-

void function_name(){

//no return value

return;

}

2. No arguments and a return value-

Syntax-

return_type function_name()

{

//execute program

return value;

}

126

YCT

3. Arguments and No return value-

Syntax-

void function_name(type1 argument1,

type2 argument2, ..... typeN argumentN)

{

//execute program

return;

}

4. Arguments and with return value-

Syntax-

return_type function_name(type1 arguments1,

type2 arguments2_typeN arguementN)

{

//execute program

return value;

}

Recursion

A function that calls itself is known as a

recursive function and technique is known as a

recursion. This technique provides a way to

break complicated problems down into simple

problems which are easier to solve.

Working of Recursion

Void recurse()

Recursive

call

{

recurse();

3

int main()

{

recurse();

3

Sum of Natural Numbers-

#include <stdio.h>

int sum (int n);

int main(){

int number, result;

printf("Enter a positive integer");

scanf("%d", & number);

result=sum(number);

printf ("sum = %d", result);

return 0;

}

int sum(int n) {

if (n! = 0)

return n+ sum(n- 1);

else

return n;

}

Output- Enter a positive integer:6

sum =21

Structure

A structure or struct is a collection of variables

(different types) under a single name.

Structure using the struct keyword and

declare each of its members inside curly braces.

Syntax-

struct structureName {

datatype member1;

datatype member2;

};

Example-

struct keyword

tag or structure

tag

Struct Person {

char name [50];

int CitNo;

float salary;

};

Members or fields

of structure

(.) Symbol Access the structure members.

Example-

struct myStructure {

int myNum;

char myLetter;

};

int main(){

struct my StructureS1;

S1.myNum=13;

S1.myLetter = 'B';

printf("my number:%d\n",S1.myNum);

printf("my letter:%c\n",S1.myLetter);

return 0;

}

Output-

my number: 13

my letter : B

Programming in C & C++

127

YCT

Keyword typedef

Output-

Imaginary Part : 9

We use the typedef keyword to create an alias

Real Part : 5.25

name for data types.

Integer: 6

Example-

O

Structure and Pointers- Pointer to structure

#include <stdio.h>

members are accessed using arrow (->) operator.

#include <string.h>

#include<stdio.h>

typedef struct person {

struct Point {

char name[50];

int a, b;

int dtdNo;

};

float salary;

int main(){

} person;

struct Point p1 = {1,2};

int main(){

struct Point *p2 = &p1;

person p1;

printf("%d%d", p2 ->a, p2-> b);

strcpy(p1.name, "Rahul");

return 0;

p1. dtdNo=1010;

}

p1.salary = 9000;

Output: 1,2

printf("Name; %s\n", p1.name);

-

Structure and functions- Structures can be

printf(" department No: %d\n",p1.dtdNo);

passed as function arguments like all other data

printf("salary:%.2f", p1.salary);

types. We can pass individual members of a

return0;

structure, and entire structure.

}

Example-

Output-

#include <stdio.h>

Name: Rahul

struct student {

Department No. 1010

char name[40];

Salary: 9000

int age;

-

Nested Structure- Nested struct within a struct.

float salary;

# include <stdio.h>

};

struct complex {

void display(struct students);

int img;

int main(){

float real;

struct students S1;

};

printf("Enter name:");

struct number {

scanf("%[^\n]%*c", S1.name);

struct complex comp;

printf("Enter age: ");

int integer;

scanf("%d", &S1.age);

} num1;

printf("Enter salary: ");

int main(){

scanf("%f", &S1.salary);

num1.comp.img =9;

display(S1);

num1.comp.real =5.25;

return 0;

num1.integer = 6;

}

printf("Imaginary Part;

void display(struct students)

%d\n", num1.comp.img);

{

printf("Real Part:%2f\n",

printf("\n Displaying information\n");

num1.comp. real);

printf("Name:%s", s.name);

printf("Integer:%d", num1.integer);

printf("In Age: %d", s.age);

return 0;

printf("In salary: %f",s.salary);

}

}

Programming in C & C++

128

YCT

Output-

Enter name: Rahul

Enter age: 29

Enter salary: 9000

Displaying information

Name : Rahul

Age : 29

Salary : 9000

O

An Array of structures as function

arguments- An array is a collection of similar

data types. A group of structures of the exact

definition is known as an array of structures.

Example-

#include <stdio.h>

struct details {

char name [10];

char sec [10]

float per;

};

void print_struct (struct details str_arr[]);

int main(){

struct details student[3]={

{"Rahul", "A", 90.5},

{"Pramod", "B", 85.5},

{"Vibhav", "C", 98.5},

};

void print_struct(struct details

str_arr[]) {

int i;

for(i=0; i<3; i++){

printf("Name:%s\n",

str_arr[i].name);

printf("Section:%s\n", str_arr[i].sec);

printf("percentage: % .2f\n",str_arr[i].per);

printf("\n");

}

}

Output-

Name: Rahul

Section: A

Percentage: 90.5

Name: Pramod

Section: B

Percentage: 85.5

Name: Vibhav

Section: C

Percentage: 98.5

Unions

Union is a user defined data type in C, which

stores a collection of different kinds of the data,

just like a structure. The keyword union is used

to declare the union in C.

Structure

Union

Union Person {

Struct Person {

char a; //size 1byte

float b; //size 4byte

} obj;

char a;

float b;

} obj;

memory

sharing

allocation

storage equal to

largest one

YCT YCT

obj(structure object)

YCT & YCT,

5 byte

obj(union object)

4 byte

Syntax-

Union UnionName

{

//member definitions

};

Example-

#include <stdio.h>

#include <string.h>

union course {

char website [50];

char subject [50];

int price;

};

void main() {

union course c;

strcpy(c.website,"yct.com");

printf("website: %s\n", c.website);

strcpy(c.subject, "The c programming

of Language");

printf("Book Author: %s\n", c.subject);

c.price = 100;

printf("Book Price: %d\n", c.price);

}

Output-

Website: yct.com

Book Author: the c programming language

Book Price : 100

O

Pointers to Unions- We can have pointers to

unions and can access members using the arrow

operator (->).

# include <stdio.h>

union test {

Programming in C & C++

129

YCT

int a;

char b;

};

int main(){

union test p1;

p1.a = 50;

union test*p2 = & p1;

printf("%d %c", p2 -> a, p2 -> b)

return 0;

}

Output-50

OOPs Concepts

O

Object Oriented Programming System-

OOPS

Class

Objects

Encapsulation

Abstraction

Inheritance

>Polymorphism

Class- A class can be considered a container

containing data variables and functions.

Human Being as a class-

Body parts

Eyes

Nose

Ears

+Data

Arms

Functions

Walk()

Sec()

Talk()

+Functions

0

Object- Objects are the instances of the class.

When a class is defined, no memory is allocated

but when it is instantiated memory is allocated.

Class person {

char name [30];

int id;

public:

void getdetails(){}

};

int main(){

person p1;//p1 is a boject.

}

object take up space in memory and have as

associated address like a record in Pascal or

structure or union in C.

Encapsulation- Keeping the data and function

into a single unit like a capsule.

Consider a real life example of encapsulation in a

company, there are different sections like

accounts section, finance section, sales section

etc. The finance section handles all the financial

transaction and keeps records of all the data

related to finance.

O

Abstraction- It is a process of hiding irrelevant

details from the user.

Abstraction

Data abstraction

Control abstraction

Example-

#include <iostream>

using namespace std .;

class implement abstraction {

private:

int a, b;

public;

void set (int x, int y) {

a = x;

b = y;

}

void display(){

cout << "a=" << a << endl

cout << "b=" << b << endl

}

};

int main(){

implement abstraction obj;

obj.set(10, 20);

obj.display();

return 0;

}

Output-

a =10

b =20

0

Inheritance- Inheriting features from a base

class into a derived class.

The class which inherits/takes the features in

known as the derived class and the class whose

features if inherited is called the base class.

Programming in C & C++

130

YCT

Example-

Polymorphism

Talk

Walk

See

Hear

Compile time polymorphism

Human

Being

Runtime polymorphism

Compile time

Polymorphism

Male

Female

Given

birth

Function overloading

Operator overloading

Inheritance

Runtime

Polymorphism

> Single Inheritance

Virtual function

> Multiple Inheritance

Example of Function Overloading-

> Hierarchical Inheritance

> Multilevel Inheritance

Hybrid Inheritance

#include <iosterm>

using namespace std;

class Yct{

public:

Yct(){

cout << "Yct can give a writer"

<< endl;

}

#include <iostream>

using namespace std;

class Yct{

public:

void fun(int x) {

cout << "value of X is"

<< x << endl;

}

void fun(double x) {

cout << "value of x is"

<< x << endl;

}

void fun(int x, int y) {

cout << " value of x and y is"

<< x << ", " << y << endl;

}

};

int main(){

Yct obj1;

obj1.fun(5);

obj1.fun(5.52);

obj1.fun(55, 50);

return 0;

}

Example-

};

class Yct computer {

public:

Yctcomputer(){

cout << "department of

computer" << endl;

}

};

class Man: public Yct, public

Yctcomputer {};

int main(){

Man b1;

return 0;

}

Output-

value of x is 5

value of x is 5.52

value x is and y is 55, 50.

Operator Overloading

Output- Yct can give a writer

Department of computer

Polymorphism- Redefining the way something

works either by changing the method of

performing it or changing the parts using which

it is done.

> Overloading unary operator

> Overloading binary operator

> Overloading binary operator

using a friend function

Programming in C & C++

131

YCT

O

In unary operator function no arguments should

be passed. It works only with one class objects.

In binary operator overloading function there

should become argument to be passed.

The operator overloading function must precede

with friend keyword and declare a function class

scope, friend operator function takes two

parameter in a binary operator varies are

parameter in a unary operator.

Example Operator Overloading-

#include <iostream>

using namespace std;

class count {

private:

int value;

public:

count(): value(10){}

void operator ++(){

++value;

}

void display(){

cout << "count:" << value

<< endl;

}

};

int main(){

count count1;

++count1;

count1.display();

return0;

}

Output- count:11

O

Constructor and Destruction- A constructor is

a special member function with exact same name

as the class name.

The constructor name is the same as the class

Name because, compiler uses this character to

differentiate constructors from the other member

function of the class.

A constructor must not declare a return type or

void because it is automatically called and

generally used for initializing values.

Constructor

Default constructor

> Para-meterized constructor

> Copy constructor

Programming in C & C++

O

Default Constructor- A constructor with no

arguments called default constructor.

Syntax-

Class CLASS_NAME

{

public:

CLASS_NAME()

{

}

// other member functions

};

O

Para-meterized Constructor- It contains

parameters in the constructor definition and

declaration.

Syntax-

class class_Name

{

public:

Class_Name(datatype variable)

{

}

Example-

};

#include <iostream>

using namespace std;

class Rectangle {

private:

double length;

double breadth;

public:

Rectangle(double l,double b){

length = l;

breadth = b;

};

}

double calculateArea() {

return length * breadth;

}

int main(){

Rectangle obj1(10, 5);

Rectangle obj2(13, 8)

cout << "Area of Rectangle1:"

<< obj1.calculateArea();

cout << "Area of Rectangle2:"

<< obj2.calculateArea();

return 0;

}

132

YCT

Copy Constructor- A copy constructor is a

member function that initialize an object using

another object of the same class.

Constructor Overloading- Overloading in

constructor are the constructors with the same

name and different parameters.

Example-

#include<iostream>

using namespace std;

class constructor {

public:

float area;

constructor(){

area = ();

}

constructor(int a, int b) {

area = a*b;

}

void display(){

cout << "Area:" << area << endl;

}

};

int main(){

constructor obj;

constructor obj2(22, 40);

obj.display();

obj2.display();

return;

}

Output-

Area: 0

Area: 880

O

Destructors- Destructors are usually used to

deallocate memory and do other cleanup for a

class object and its class members when the

object is destroyed.

A destructor is a member function with the same

name as its class prefixed by a ~(tilde).

Class x {

public:

//constructor for class x

x():

//Destructor for class x

~();

};

Destructor takes no arguments and has no return

type. Its address can't be taken.

Example-

# include<iostream>

using namespace std;

int count = 0;

class Test{

public:

Test(){

count++;

cout << "In No. of object created:

It" << count;

}

~Test(){

cout << "In No object destroyed

:\t" << count;

-- count;

};

}

main(){

Test t, t1

return 0;

Output-

No. of object created: 1

No. of object created: 2

No. of object destroyed: 2

No. of object destroyed: 1

Templates

Templates are primarily implemented for crafting

a family of classes or functions having similar

features.

Templates

Class templates

Function templates

0

Functions templates- A functions template

defines a family of functions.

Syntax-

template<parameter_list>

function_declaration

export template <parameter_list>

function_declaration

The general form of a function template is.

Syntax-

template<class type> ret_type

func_name(parameter list)

{

//body of function

}

Programming in C & C++

133

YCT

Example-

# include<iostream.h>

#include<conio.h>

template<class swap>

void swapp(swap & i, swap & j) {

swap t;

t =i;

i=j;

j=t;

}

int main(){

int e, f;

char g, r;

float x, y;

cout << "In please insert 2 integer values"

cin>>e>>f;

swapp(e, f);

cout << "In Integer values after swapping"

cout <<<<< "\"‹‹"\n\n";

cout"In please insert2 character

values:";cin>>g>>r;

swapp(g, r);

cout << "In character values after

swapping:";

cout << g << "\"‹"\n\n";

cout << "In please insert 2 Float

values:"; cin>>x>>y;

swapp(x, y);

cout << "In the resultant float values after

swapping:";

cout << x << ",\t" << y << "\n\n";

}

Output-

Please insert 2 Integer values: 10 15

Integer values after swapping: 15 10

Please inert 2 character values: A B

Character values after swapping : B A

Please inert 2 Float values: 2.2 4.4

The resultant float values after swapping:

4.4 2.2

O

Class Template- A class template defines a

family of classes.

Syntax-

template class name<argument-list>;

extern template class name<argument-list>;

Example-

#include <iostream>

using namespace std;

const size =3;

template <class T>

class vector {

T*V;

public:

vector(){

v = new T [size];

for(int i = 0; i<size; i++)

v[i]=0;

}

vector (T* a){

for(int i =0; i<size; i++)

v[i] = a[i];

T operator*(vector & y) {

T sum = 0;

for (int i=0; i <size; i++)

sum + = this ->v[i] *y.v[i];

return sum;

}

}

3;

int main(){

int x[3] = {1,2, 3};

int y[3] = {4, 5, 6};

vector <int> v1;

vector <int> v2;

v1 =x;

v2 = y1

int R = v1*v2;

cout << "R=" << R << "In";

return 0;

}

Output-

R = 32

Function Template with multiple

Parameters

Function template use more than one generic

data type in the template statement, using a

comma (,) separated list.

Syntax-

template<class T1, Class T2,

>

returntype functionname (arguments of types

T1, T2, __ ){

= body of function

}

Programming in C & C++

134

YCT

Overloading of template function

A template function may be overloaded either by

template functions or ordinary functions of its

name.

Example-

#include <iostream>

#include <string>

using namespace std;

template <class T>

void display (T x) {

cout << "Template display:" << x << "\n";

}

void display(int x) {

cout << "Explicit display:" << x << "\n";

}

int main(){

display(1000);

display(10.25);

display('C');

return 0;

}

Output-

Explicit display: 1000

Template display: 10.25

Template display: C

Exception handling

Exception handling is a mechanism that

separates code that detects and handles

exceptional circumstances from the rest of your

program. Exception basically built upon three

keyword, namely, try, throw and catch.

Try- The keyword try is used to preface a block

of statements which may generate exception.

You use a function try block to indicate that you

want to detect exception in the entire body of a

function.

try block syntax-

> try-{-statements-}- handler

F andra ,

Function try block syntax-

> try

function body

member_initializer_list

handler

Catch block syntax- You can declare a handler

to catch many types of exceptions. The objects

that a function can catch are declared in the

parentheses following the catch keyword.

Syntax-

> Catch(-exception_declaration-)-

{-statement -}->

Throw expressions- You use a throw

expression to indicate that your program has

encountered an exception.

Syntax-

> throw

L

assignment_expression

the type of assignment_expression can't be an

incomplete type, abstract class type, or a pointer

to an incomplete type other than the following

types.

void*

const void *

volatile void *

const volatile void *

The catch block that catches an exception must

immediately follow the try block that throws the

exception. The general form of these two blocks

are

-------

try {

throw exception;

//block of statements

which detects and

throws an exception

}

Catch (type arg) {

//block of statements that

-- //handles the exception

}

-----

Example-

#include <iostream>

using namespace std;

void divide(int x, int y, int z) {

Programming in C & C++

135

YCT

cout << "In we are inside the function\n";

if((x-y) != 0){

int R = z/(x-y);

cout << "Result+" << R << "\n";

} else {

throw(x-y);

}

int main(){

try {

cout << "we are inside the try

block\";

divide(10, 20, 30);

divide(10, 10, 20);

} catch (int i) {

cout << " Caught the exception\n";

return 0;

}

}

Output-

We are inside the try block

We are inside the function

Result =- 3

We are inside the function

caught the exception.

Multiple Catch Statements

It is possible that a program segment has more

than one condition to throw an exception. In such

cases, we can associate more than one catch

statement with a try (much like the conditions in

a switch statement).

Syntax-

try { try block}

Catch(type1 arg) {

//Catch block1

}

Catch(type2 arg){

//Catch block2

}

Catch(typeN arg) {

//Catch blockN

}

Example-

#include <iostream>

using namesapce std;

void test(int x) {

Programming in C & C++

try{

if(x == 1) throw x;

else

if(x == 0) throw x;

else

if(x ==- 1) throw 1.0;

cout << "End of try-block\n";

}

catch(char c) {

cout << "Caught a character\n";

}

catch(int m) {

cout << "Caught an integer\n"

}

catch(double d) {

cout << "Caught a double\n";

}

cout << "end of try_Catch system\n\n";

}

int main(){

cout << "Testing Multiple Catches\n";

cout << "x == 1\n";

test(1);

cout << " x == 0\n";

test(0);

cout << "x ==- 1\n";

test (-1);

cout << "x == 2\n";

test(2);

return 0;

}

Output-

Testing Multiple Catches

x == 1

Caught an integer

End of try_catch system

x == 0

Caught a character

End of try catch system

x ==- 1

Caught a double

End of try_catch system

x == 2

End of try black

End of try catch system

136

YCT

Re-throwing an exception

A handler may decide to re-throw the exception

caught without processing it. In such situations,

we may simply invoke throw without any

arguments as show below throw;

Example-

# include <iostream>

using namespace std;

void divide(double x, double y) {

cout << "inside function\n";

try{

if(y == 0.0)

throw y;

else

cout << "Division=" << x/y << "\n";

}

Catch(double){

cout << "Caught

double

inside

function\n";

throw;

}

cout << "End of function\n\n";

}

int main(){

cout << "Inside main\n";

try

{

divide(10.5, 2.0);

divide(20.0, 0.0);

}

Catch (double) {

cout << "Caught double inside

main\n";

}

cout << "End of main\n";

return 0;

}

Output-

Inside main

Inside function

Division = 5.25

End of function

Inside function

Caught double inside function

Caught double inside main

End of main

Instantiation

The creation of a new instance of the class is

called instantiation. Memory is allocated for that

object and the class construction runs.

There are three different ways of

instantiation an object through constructors.

Instantiation

Through Default Constructor

Through Parameterized Constructor

Through Copy Constructor

Steam- In C++ stream refers to the stream of

characters that are transferred between the

program thread and I/O. Stream classes in C++

are used to input and output operations on files

and I/O devices.

Stream Classes- The C++ I/O system contains a

hierarchy of classes that are used to define

various streams to deal with both the console and

disk files.

iOS

pointer

istream

ostream

input

stream but

output

isotream

istream_withassign

iostream_withassign

ostream_withassign

Stream classes for console I/O operations.

As seen the above iOS is the base class for

istream and ostream which are in turn base

classes for iostream.

Unformatted I/O Operations

Overloaded operators >> and << :- We have

used the objects cin and cout (pre defined in the

iostream file) for the input and output of data of

various types.

Cin>variable1> variable2> .... >variableN

This is the general format for reading data from

the keyword.

Cout << item1 << item2 <....... ‹itemN

This is the general format for displaying data on

the screen.

get() and put() function- The classes istream

and ostream define two member functions get()

Programming in C & C++

137

YCT

and put() respectively to handle the single

character input/output operations.

get()

get(char*)

get(void)

Example-

get(char*) version assigns the input character to

its argument.

get(void) version returns the input character.

#include <iostram>

using namespace std;

int main(){

int count = 0;

char c;

cout << "Input Text\n";

cin.get(c);

while(c! = '\n'){

cout.put(c);

count++;

cin.get(c);

}

cout << "InNumber of character =

" << count << "\n";

return 0;

}

Input text

object oriented programming

Output-

object oriented programming

Number of characters = 27

When we type a line of input, the text is sent to

the program as soon as we press the RETURN

key. The program, reads are characters at a time

using the statement cin.get(c); and displays it

using the statement cout.pute(c) ;. The process is

terminated when the newline character is

encountered.

O

getline() and write() function- We can read and

display a line of text more efficiently using the

line oriented input/output function getline() and

write(). The getline() function reads a whole line

of text that ends with a newline character. This

function can be invoked by using the object cin.

cin.getline(line, size);

Example-

#include <iostream>

using namespace std;

int main(){

int size = 20;

char city[20];

cout << "Enter City Name:\n";

cin>>city;

cout << "City name;" << city << "\n\n";

cout << Enter city name again; \n";

cin.getline(city, size);

cout << "City name now:" << city << "\n\n";

cout << "Enter another city name:\n";

cin.getline(city, size);

cout << "New city name:" << city << "\n\n";

return 0;

}

Output-

First run

Enter city name:

Delhi

City name: Delhi

Enter city name again:

City name now:

Enter another city name:

Chennai

New city name: Chennai

Second run

Enter city name:

New Delhi

City name: New

Enter city name again:

City name now: Delhi

Enter another city name:

Greater Bombay

New City Name: Greater Bombay.

Formatted Console I/O Operations

Formatting the output these features include.

· iOS class functions and flags

· Manipulators

· User defined output functions

Programming in C & C++

138

YCT

Functions

Task

width()

To specify the required field

size for displaying an output

value

precision()

To specify the number of digits

to be displayed after the

decimal point of a float value

fill()

To specify a character that is

used to fill the unused portion

of a field

setf()

To specify format flags that

can control the form of output

display

Unsetf()

To clear the flags specified

Manipulators

Manipulators

Equivalent ios function

setw()

width()

setprecision()

precision()

setfill()

fill()

setiosflags()

setf()

resetiosflags()

unsetf()

The addition to these functions supported by the

C++ library.

Designing Our Own Manipulators- We can

design our own manipulators for certain special

purpose.

ostream & manipulator(ostream & output)

{

return output;

}

Example-

#include <iostream>

#include <iomanip>

using namespace std;

//user defined manipulators

ostream & currency (ostream & output) {

output << "Rs";

return output;

}

ostream & form (ostream & output) {

output.setf(ios :: showpos);

output.setf(iso :: showpoint);

output.fill('*');

output.precision(2);

output .<< setiosflags(ios :: fixed)

<< setw(10);

return output;

}

int main(){

cout << currency << form << 7864.5;

return 0;

}

Output- Rs ** + 7864.50

Console program file interaction flow-

External Memory

Data files

Write

data

(to files)

Read data

(from files)

Program file interaction

7

Internal Memory

Program Unit

cout << console program interaction

cin>>

(get data

from

keyboard)

Console Unit

(Put data to

screen)

Screen

1

Keyboard

Classes for file stream operations

The I/O system of C++ contains a set of classes

that define the file handling methods.

Class

Contents

filebuf

Its purpose is to set the file buffers

to read and write. Contains

openprot constant used in the

open() of file stream classes. Also

contain close() and open() as

members.

fstreambase

Provides operations common to the

file stream. Serves as a base for

fstream, ifstream and of stream

class. Contains open() and close()

functions.

Programming in C & C++

139

YCT

ifstream

Provides input operations.

Contains open() with default input

mode. Inherits the functions get(),

getline(), read() seekg() and tellg()

functions from istream.

ofstream

Provides output operations.

Constains open() with default

output mode. Inherits put(),

seekp(), tellp() and wrtie(),

function from ostream.

fstream

Provides support for simultaneous

input and output operations.

Contains open() with default input

made. Inherits all the functions

from istream and ostream classes

through iostream.

Opening and Closing a file

The first method is useful when we use only one

file in the stream. The second method is used

when we want to manage multiple files using one

stream.

Opening and closing a file

Using the constructor

function of the class

Using the member

function open() of the class

0

Opening files using constructor

We know that a constructor is used to initialize

an object while it is being created.

Create a file stream object to manage

the stream using the appropriate class. That is to

say, the class ofstream is used to create the

output stream and the class ifstream to create the

input stream.

Initialize the file object with the

desired filename.

ofstream outfile("results");//output only

ifstream infile("data");//input only

Example-

#include <iostream.h>

#include <rstream.h>

int main(){

ofstream outf("item");

cout << "Enter item name:";

char name[30];

cin>>name;

outf>> name;

outf << name << "\n";

cout << Enter item cost:";

float cost;

cin>>cost;

outf << cost << "\n";

outf.close();

ifstream inf("item");

inf>>name;

inf>>cost;

cout << "\n";

cout << "item name": << name << "\n";

cout << "item cost:" << cost << "\n";

inf.close();

return 0;

}

Output-

Enter item name: CD-ROM

Enter item cost: 350

Item name : CD-ROM

Item cost : 350

0

Opening files using open()- The function

open() can be used to open multiple files that use

the same stream object.

Example-

#include <iostream.h>

#include <fstream.h>

int main(){

ofstream fout;

fout.open("Country");

fout << "United States of America\n";

fout << "United Kindom\n";

fout << "south Korea\n";

fout.close();

fout.open("Capital");

fout << "Washinton\n";

fout << London\n";

fout << "Seoul\n";

fout.close();

Const int N = 80;

Programming in C & C++

140

YCT

Char line [N];

ifstream fin;

fin.open("Country");

cout << "contents of country file\n";

while(fin){

fin.getline(line, N);

cout << line;

}

fin.close();

fin.open("capital");

cout << "In contents of capital file\n";

while(fin) {

fin.getline(line, N);

cout << line;

}

fin.close();

return 0;

}

Output-

Contents of Country file

United States of America

United Kingdom

South Korea

Contents of capital file

Washington

London

Seoul

Updating a file Random Access

Updating is a routine task in the maintenance of

any data file. The updating would include one or

more of the following tasks.

· Displaying the contents of a file

· Modifying an existing item

· Adding a new item

· Deleting an existing item.

This can be easily implemented if the file

contains a collection of items/objects of lengths.

In such cases, the size of each object. Can be

obtained using the statement.

int object_length=sizeof(object);

Then, the location of a desired object, say the

mth object, may be obtained as follows.

int location = m* object_length

The location gives the byte number of the first

byte of the mth object. We can set the file pointer

to reach this byte with the help of seekg() or

seekp().

0

Error Handling During file operations- A file

which we are attempting to open for reading does

not exist.

. The file name used for a new file may already

exist.

· We may attempt an invalid operation such as

reading past the end of file.

· There may not be any space in the disk for

storing more data. We may use an invalid file

name.

· we may attempt to perform an operation when

the file is not opened for that purpose.

Error Handling functions

Function

Return value and meaning

eof()

Return true (non-zero value) if end of

file is encountered while reading

otherwise return false (zero)

fail()

Returns true when an input or output

operation has failed

bad()

Returns true if an invalid operations is

attempted or any unrecoverable error

has occurred. If it is false, it may be

possible to recover from any other

error reported and continue operation.

good()

Return true if no error has occurred.

This means, all the above functions

are false. For instance, if file.good() is

true, all is well with the stream file

and we can proceed to perform I/O

operation when it returns false, no

further operations can be carried out.

Programming in C & C++

141

YCT

11.

WEB TECHNOLOGY

HTML

HTML is the standard markup language for

creating web pages. HTML stands for Hypertext

Markup Language and describes the structure of

a web page. HTML elements tell the browser

how to display the content.

<! DOCTYPE html> - Declaration defines that this

document is HTML5 document.

<html> - Element is the root element of an HTML

page.

<head> - Element contains meta information about the

HTML page.

<title> - Element specifies a title for the HTML page

(which is shown in the browser's title bar or in

the pages tab)

<body> - Element defines the documents body and is a

container for all the visible contents such as

headings, paragraph, images, hyperlinks, tables,

lists etc.

HTML Page Structure

<html>

<head>

<title> page title</title>

</head>

<body>

<h1> This is a

heading </h1>

<p> This is a

paragraph </p>

</body>

</html>

Version of HTML

Years

Version

1991

First Versions of HTML

1995

HTML 2.0

1997

W3C Recommendation 3.2

1999

W3C Recommendation 4.01

2000

W3C Recommendation XHTML 1.0

2008

WHATWG HTML5 first Public Draft

2012

WHATWG HTML5 Living standard

2014

W3C Recommendation HTML5

2016

W3C Recommendation HTML5.1

2017

W3C Recommendation HTML5.1 2nd

Edition

2017

W3C Recommendation HTML5.2

HTML tag and Element

HTML element defined by a start tag some

content and an end tag like.

Element

<tagname> some content <tagname>

HTML Tag and Attributes

HTML attributes provide additional information

about elements. Attributes are always specified

in the start tag and attributes usually come in

name/value pairs like, name = "value".

Example- The <a> tag defines a hyperlink. the

href attributes specifies the URL of the page the

link goes to.

<a href = "http://www.yct.com">

visit YCT</a >

Some Important Tags

Tag

Description

<! >

Defines a comment

<! DOCTYPE>

Defines the document type

<a>

Defines a hyperlink

<abbr>

Abbreviation or an acronym

<address>

Defines contact information for

the author/owner of a document

<area>

Area inside an image map

<article>

Defines an article

<aside>

Defines content aside from the

page content

<audio>

Embedded sound content

Web Technology

142

YCT

<b>

bold the text

<base>

The base URL/target for all

relative URLs in a document

<blockquote>

A section that is quoted from

another source

<body>

Documents of body

<br>

Single line break

<button>

A clickable button

<canvas>

Used to draw graphics, on the fly

via scripting (usually javascript)

<code>

A piece of computer code

<col>

Specifies column properties for

each column within a <colgroup>

element

<colgroup>

A group of one or more columns

in a table for formatting

<data>

Adds a machine readable

translation of a given content.

<datalist>

A list of predefined options for

input controls

<dd>

Description/value of a term in a

description list

<details>

Defines additional details that the

user can view or hide.

<dialog>

A dialog box or window.

<div>

A section in a document

<dl>

Defines a description list

<dt>

Defines a term/name in a

description list

<embed>

A container for an external

application.

<fieldset>

Groups related elements in a

form.

<figcaption>

Defines a caption for a <figure>

element

<figure>

specifies self contained

<font>

Defines font, color and size for

text

<footer>

A footer for a document or section

<form>

HTML form for user input

<frame>

Defines a window in a frameset

<frameset>

Defines a set of frames

<h1>or <h6>

Defines HTML headings.

<head>

Contains metadata/Information

for the document.

<header>

A header for a document or

section.

<i>

Defines a part of text in an

alternate voice or mood.

<img>

Defines an image.

<input>

An input control.

<label>

Defines a label for an <input>

element.

<legend>

A caption for a <fieldset>

element.

<li>

A list item.

<link>

Defines the relationship between a

document and an external

resource.

<map>

Defines an image map.

<mark>

marked/highlighted text

<meta>

metadata about an HTML

document.

<meter>

Defines a scalar measurement

within a known range.

<nav>

Defines Navigation links.

<object>

Defines a container for an

external application.

<ol>

Defines an ordered list.

<optgroup>

Defines a group of related options

in a drop-down list.

<option>

An option in a dropdown list.

<output>

The result of calculation.

<picture>

Defines a container for multiple

image resources.

<script>

Defines a client-side script.

<section>

A section in a document.

<small>

Defines smaller text.

<source>

Defines multiple media resources

for media elements.

Web Technology

143

YCT

<span>

A section in a document.

<style>

Defines style information for a

document.

<sub>

Subscripted text.

<summary>

Defines a visible heading for a

<details> element.

<sup>

Defines superscripted text.

<svg>

A container for SVG graphics.

<table>

Defines a table.

<tbody>

Groups the body content in a

table.

<td>

Defines a cell in a table.

<textarea>

A multiple input control.

<time>

a specific time

<track>

Defines text tracks for media

element (<video> and <audio>)

<var>

Defines a variable.

<video>

Defines embedded video content.

<wbr>

A possible line-break.

Absolute URLs and Relative URLs

A full web address are using an absolute URL in

the href attribute.

Example-

<a href="https://www.google.com/">Google</a>

A local link (a link to a page within the same

website) is specified with a relative URL

(without the "https://www"),

Example-

<a href="html_page.php">HTML File

</a>

Link to an Email Address

Use mailto: inside the href attribute to create a

link that opens the user's email program (to let

them send a new email.)

Example-

<a href="mailto:yct@gmail.com">

Send Mail </a>

HTML Image- The HTML <img> tag is used to

embed an image in a web page. The <img> tag is

empty, it contains attributes only and does not

have a closing tag <img> tag has two attributes

src- Specifies the path to the image

alt- Specifies an alternate text for the image.

Example-

<img src="imageName" alt="AltName">

HTML Favicon- A favicon is a small image

displayed next to the page title in the browser

tab. To add a favicon to your website, either save

your favicon image to the root directory of your

web server, or create a folder.

Add favicon

<link

rel =- "icon"

type="image/icon"

href="favicon path">

List

A list is a record of short pieces of related

information or used to display the data or any

information on web pages in the ordered or

unordered form.

List

Unordered list

Ordered list

Unordered List

An unordered list starts with the <ul> tag. Each

list item starts with the <li> tag list items will be

marked with bullets by default.

Unordered list marker- Use the CSS property

list_style_type, define the style of the list item

marker.

disc- item marker to a bullet

circle- item marker to a circle

square- list item marker to a square

none- the list items will not be marker

Example-

<ul style="list-style-type: square;">

<li> Rahul </li>

<li> Raj </li>

</ul>

Ordered list

An ordered list starts with the <ol> tag. Each list

item starts with the <li> tag. The list by default

marked will numbers.

ordered list used to type attributes type

defines the list item marker.

type = "1" => by default

type = "A" => Item numbered with upper case

Web Technology

144

YCT

type = "a" => Item numbered with lowercase

type = "I" => Item numbered with upper roman

numbers

type = "i" => Item numbered with lower roman

numbers

Example-

<ol type = "1, A , a, I, or i">

<li> Rahul </li>

<li> Raj </li>

</ol>

List Tags-

<ul> => Defines unordered list

<ol> => Defines ordered list

<li> => A list item

<dl> => Description list

<dd> => The term in a description list

Head Element

The <head> HTML element contains machine

readable information (metadata) about the

document.

like <title>, <style>, <meta>, <link>, <script>

and <base>

<meta> element- The <meta> element is

typically used to specify the character set, page

description, keywords, author of the document

and viewport settings.

Example-

The character set used-

<meta charset = "UTF-8">

Keywords for search engines-

<meta name = "keywords" content = "HTML,

CSS, Javascript">

A description of your web page-

<meta name = "description" content =" Free

online PDF">

The author of page-

<meta name = "author" content ="YCT">

Refresh document every 30 seconds-

<meta http_equiv = "refresh" content="30">

Setting the viewport to make your website look

good on all devices.

<meta name = "viewport" content = width =

device-width, initial-scale =1.0">

HTML tags

Semantic Element

Non-semantic

Semantic Elements

Semantic elements have meaningful names

which tells about type of content like header,

footer, table, ..... etc.

Semantic Elements- < article>, <aside>,

<details>, <figcaption>, <figure>, <footer>,

<header>, <main>, <mark>, <nav>, <section>,

<summary>, <time>.

Non-semantic Elements

Non-semantic categories as their names don't tell

anything about what kind of content is present

inside them <div> and <span> is non-semantic

elements.

Form

HTML form on a web page allows a user to enter

data that is sent to a server for processing.

<form> element is a container for different

types of input elements such as: text fields,

checkboxes, radio buttons, submit buttons etc.

Form Attributes-

Action- The action attributes define the action to

be performed when the form is submitted.

Target- The target attribute specifies where to

display the response that is received after

submitting the form.

target value => _blank, _self, parent, top,

framename.

Method- The method attributes specifies the

HTTP method to be used when submitting the

form data.

method = "get"

method = "post"

Method

Get

Post

Get method is mainly used at the client side to

send a request to a specified server to get contain

data or resources. It is send to limited data.

Post method sent to the server is stored in the

request body of the HTTP request.

Web Technology

145

YCT

Multimedia

Multimedia comes in many different formats. It

can be almost anything you can hear or see, like,

images, music, sound, video, records, films,

animations and more.

Common Video Formats

Format

File

MPEG

.mpg

.mpeg

AVI

.avi

WMV

.WMV

QuickTime

.mov

Realvideo

.rm

.ram

Flash

.swf

.flv

ogg

.ogg

WebM

.webm

MPEG-4 or MP4

.mp4

Note- Only MP4, WebM and Ogg Video are

supported by the HTML standard.

Common Audio Formats- MP3 is the best

format for compressed recorded music. The term

MP3 has become synonymous with digital

music.

Format

File

MIDI

.mid

.midi

RealAudio

.rm

.ram

WMA

. wma

AAC

.aac

WAV

. wav

Ogg

.ogg

MP3

.mp3

Note- Only MP3, WAV and Ogg audio are

supported by the html standard.

Web Storage

Web storage can store data locally within the

users browser.

Web storage

LocalStorage

SessionStorage

LocalStorage- Stores data with no expiration

date and gets cleared only through JavaScript or

clearing the browser cache/locally stored data.

SessionStorage- Stores data only for a session

meaning that the data is stored until the browser

(or tab) is closed. Storage limit is larger than a

cookie (at most 5 MB).

Web Worker- Web workers are multithreaded

object which is used to execute JavaScript in the

background without affecting the performance of

the application or webpage.

Server Sent Events (SSE)

A server sent events is when a web page

automatically gets updates from a server via an

HTTP connection. This is a one way connection.

The event source object is used to receive server

sent event notification.

Events

Description

onopen

When a connection to the server is

opened.

onmessage

When a message is received.

onerror

When an error occurs.

DHTML

DHTML stands for Dynamic HTML, it is totally

different from HTML. DHTML is based on the

properties of the HTML, JavaScript, CSS and

DOM which helps in making dynamic content.

DHTML is used to create interactive and

animated web pages that are generated in real

time, also known as dynamic web pages so that

when such a page is accessed the code.

HTML- HTML stands for Hyper Text Markup

Language and it is a client side markup language.

It is used to build the block of web pages.

JavaScript- It is client side scripting language

that enables you to create dynamically updating

Web Technology

146

YCT

content, control multimedia, animate images and

pretty much everything else.

CSS- CSS is a language of style rules that we

use to apply styling to our HTML content, for

example setting background colors and fonts and

laying out our content in multiple columns.

DOM- DOM is known as a Document Object

Model which act as the weakest links in it.

XML

XML stands for Extensible Markup Language. It

was designed to store and transport data. It is

called extensible because it allows the author of

the document to defines the markup elements by

their own.

Advantages of XML-

. XML support Unicode, all most all the human

readable written language can be

communicated using XML.

· It can be used to render data structure i.e

records and lists and trees.

. XML needs another software application called

parser. An XML document is very strict while

maintaining a standard.

. XML is used both on and offline for storing and

processing data.

. XML allows validation of the document using

XSD or schematron. These are types of the

schema for validating XML documents.

Difference Between XML and HTML

XML was designed to carry data with focus on

what data is.

HTML was designed to display data with focus

on how data looks.

XML tags are not predefined like HTML tags

are.

In XML all elements must have a closing tag.

XML tags are case sensitive.

XML Declaration- XML declaration is not a

tag. It is used for the transmission of the meta

data of a document.

Syntax-

<? xml version = "1.0" encoding = "UTF-8"?>

This line represents the XML prolog or XML

declaration. The XML prolog is optional. It if

exists, it must come first in the document.

The version = "1.0" is the version of the XML

currently used.

The encoding = "UTF-8" specifies the character

encoding used while writing an XML document.

XML Valid and Well Formed- XML document

must be well formed. Document must conform to

all XML syntax rules. Document conform to

semantic rules, which are usually set in an XML

schema or a DTDC (document type definition).

Example-

<? xml version = "1.0" encoding = "UTF-8"?>

<message>

<warning>

Hello Rahul

</warning>

</message>

XMLHttpRequest Object

The XMLHttpRequest object can be used to

request data from a web server.

· Update a web page without reloading the page.

· Request data from a server after the page has

loaded.

· Received data from a server after the page has

loaded.

· Send data to a server in the background.

XMLHttpRequest Properties

readyState- Indicate the status of the

connection.

Status- It contains the http response code string

from server.

StatusText- It contains the http response string

from the server.responseText. It contains the

response in text format from the server.

responseXML- It contains the response XML

from server.

getAllResponseHeaders- It returns all the

headers name as string.

OverrideMimeType- It is used to set the mime

type which is used to treat the response data type

to be treated as text or XML type.

DTD- DTD stands for Document Type

Definition. DTD defines the structure and the

legal elements and attributes of an XML

document.

Web Technology

147

YCT

Schema- XML schema describes the structure of

an XML document. XML document with correct

syntax is called "Well Formed".

JavaScript

JavaScript is a programming language that

execute on the browser. It turns static HTML

web pages into interactive web pages by

dynamically updating content, validating form

data controlling multimedia animate images and

almost everything else on the web pages.

Versions of JavaScript- In the years 1996, a

standards organization called ECMA (European

Computer Manufacture Association).

International carved out standard specifications

called ECMA script (ES).

ECMAScript Editions

Version

Official Name

Description

ES1

ECMAScript1

(1997)

First edition

ES2

ECMAScript2

(1998)

Editorial changes

ES3

ECMAScript3

(1999)

Added regular

expressions added

try/Catch Added

Switch Added do-

while

ES4

ECMAScript4

Never released

ES5

ECMAScript5

(2009)

Added "strict mode",

JSOn support,

string.trim(),

Array.isArray() and

Added Array

iteration methods

Allows trailing

commas for object

literals.

ES6

ECMAScript

(2015)

Added let and const,

default parameter

values and Added

Array.find(),

Array.findIndex()

ECMAScript

(2016)

Added exponential

operator ( ** ),

Array.includes()

ECMAScript

(2017)

Added string,

padding,

object.entries(),

object values()

added async

functions and shared

memory, Allows

trailing commas for

function parameters.

ECMAScript

(2018)

Added rest/spread

properties,

asynchronous

iteraction, and

promise.finally(),

ReqExp

ECMAScript

(2019)

String.trimstar()

string.trimEnd()

Array.flat(),

object.fromEntries

optional catch

binding

ECMAScript

(2020)

The Nullish

Coalescring

operator( ?? )

Variable

Variables are containers for storing data (storing

data values.)

Define Variables

Using var

Using let

Using const

Using nothing

Data type

Primitive

Non-Primitive

String

Object

Number

Array

Boolean

RegExp

Undefined

Null

Symbol

BigInt

Web Technology

148

YCT

BigInt- JavaScript BigInt variables are used to

store big integer values that are too big to be

represented by a normal JavaScript number.

Undefined- A variable without a value has the

value undefined. The type is also undefined.

Null- The null value represents the intentional

absence of any object value. It is treated as false

for Boolean operations.

Regular Expression- A regular expression is a

sequence of characters that forms a search

pattern. Regular expressions are often used with

the two string methods search() and replace().

The search() method uses an

expressions to search for a match and returns the

position of the match.

The replace() method returns a

modified string where the pattern is replaced.

Regular Expression Modifiers- Modifiers can

be used to perform case insensitive more global

searches.

Modifier

Description

i

Perform case insensitive matching

g

Perform a global match(find all

matches rather than stopping after

the first match)

m

Perform multiline matching.

This Keyword

The this keyword refers to an object. Which

object depends on how this is being invoked.

Note- This is not a variable. It is keyword you can't

change the value of this.

Example-

<html>

<body>

<p id="demo"></p>

<script>

const person = {

firstName: "Rahul",

lastName: "Kumar",

id: 1001,

fullName: function() {

return this. firstName +" " +

this.lastName;

}

};

document.getElementById("demo").

innerHTML = person.fullName();

</script>

</body>

</html>

Output-

Rahul Kumar

Arrow Function

Arrow function allow us to write shorter function

syntax.

let myFunction = (a, b) => a*b;

Example-

<html>

<body>

<p id="demo"></p>

<script>

let hello = " ";

hello = ()= {

return "Hello World";

}

document.getElementById("demo").innerHTML

= hello();

</script>

</body>

</html>

Modules

Modules allow you to break up your code into

separate files modules are imported from

external files with the import statement. And also

rely on type = "module" in the <script> tag.

Example-

<html>

<body>

<p id = "demo"> </p>

<script type = "module">

import message from

"/message.js";

document.getElementById("demo").inner

HTML = message();

</script>

</body>

</html>

Web Technology

149

YCT

Export

Name Export

Default Export

Named Export

Inline individually

All at once at the bottom

Syntax-

1. Export variable_name = value;

2. Variable_name = value;

export {variable_name}

Java

Java was developed by James Gosling at

SunMicro system in the year 1995, later acquired

by oracle corporation. It is a simple

programming language. Java is an object

oriented programming language with its runtime

environment. It is combination of features of C

and C++ with some essential additional concepts.

Java

Uses

Features

Mobile Applications

>Object Oriented

>Desktop Applications

Platform Independent

Web Applications

Simple

Games

Secure

Database connection

Portable

Web Servers and

Application Servers

Robust

Multi threaded

Distributed

Servlets

Servlet is a server side java program module that

handles client requests and implements the

servlet interface. Servlets can respond to any

type of request and they are commonly used to

extend the application hosted by web servers.

Servlet is a web component that is deployed on

the server to create a dynamic page.

Properties of servlets are as follows- Servlets

work on the server side. Servlets are capable of

handling complex requests obtained from the

web server.

Servlet Architecture-

Web server

HTTP

Request

Web browser

HTTP

Response

Servlet Program

Data

base

Execution of Servlets-

1. The clients send the request to the web server.

2. The web server receives the request.

3. The web server passes the request to the

corresponding servlet.

4. Servlet process the request and generates the

response in the form of output.

5. The servlet sends the response back to the web

server.

6. The web server sends the response back to the

client and the client browser displays it on the

screen.

Applets

An Applet is a java program that can be

embedded into a web page. It runs inside the web

browser and works at client side. An Applet is

embedded in HTML page using the APPLET or

OBJECT tag and hosted on a web server. Applet

are used to make the website more dynamic and

entertaining.

Lifecycle of Applet

init()

start()

paint()

stop()

destroy()

When an Applet begins, the following methods

are called in this sequence.

1. init()

2. start()

3. paint()

Web Technology

150

YCT

When an Applet is terminated the following

sequence of method calls takes place.

1. stop()

2. destroy()

init()- The init() method is the first method to be

called. This is where you should initialize

variables. This method is called only once during

the run time of your Applet.

start()- The start() method is called after init(). It

is also called to restart an Applet after it has been

stopped.

paint()- The paint() method is used to paint the

Applet. It provides graphics class object that can

be used for drawing oval, rectangle, arc etc.

stop()- The stop() method is called when a web

browser leaves the HTML document containing

the applet, when it goes to another page.

destroy()- The destroy() method is called when

the environment determines that your Applet

needs to the removed completely from memory.

There are two standard ways to run an

Applet-

1. Executing the Applet within a java compatible

web browser.

2. Using an Applet viewer.

1. Using java enabled web browser- To

execute an Applet in a web browser we have to

write a short HTML text file that contains a tag

that loads the Applet. We can use APPLET or

OBJECT tag for this purpose.

<applet code = "HelloWorld" width = 200

height = 60>

</applet>

2. Using Applet Viewer- This is a easiest way

to run Applet. To execute HelloWorld with an

Applet viewer, you may also execute the HTML

file shown earlier.

If the preceding HTML file is saved with

Hello World html, then the following command

line will run Hello World.

appletviewer RunHelloworld.html

Python Programming

Python is a general purpose, dynamic, high-level,

and interpreted programming language.

It supports an Object Oriented programming

approach to develop applications and

It is used in web development, data science,

creating software prototypes, and so on.

Fortunately for beginners, Python has simple

easy-to-use syntax and this makes Python an

excellent language to learn to program for

beginners.

History of Python

Python was created by Guido van Rossum, and

first released on February 20, 1991.

The name of the Python programming language

comes from an old BBC television comedy sketch

series called Monty Python's Flying Circus.

Keywords in Python programming

In Python, keywords are case sensitive and they

are reserved words. That means we cannot use

keywords as a variable or function.

Keywords are used to define the syntax and

structure of the Python language.

Following are some keywords available in Python

programming language.

False await

else

import

pass

None break

except

in

raise

True class

finally

is

return

and

continue

for

lambda

as def

from

nonlocal

while

assert del

global

not

with

async elif

if

or

yield

try

Note :- All the keywords except True, False and None are

in lowercase and they must be written as they are.

Python Identifiers

An identifier is a name given to entities such as

class, functions, variables, etc.

It helps to differentiate one entity from another.

Rules for Defining Identifiers

1. An identifier cannot start with a digit.

For example-

a1( valid declaration)

But 1a is not a valid declaration.

2. Keywords cannot be used as identifiers.

For example-

assert = 1

3. Special symbols such as !, @, #, $, % etc.

cannot be used as an identifier.

For example-

b$ =3

Web Technology

151

YCT

Variables in Python

Defining variables-

In Python, variables are containers for storing data

values.

Variable is a name that is used to refer to memory

location. Variables in python are also known as an

identifier and used to hold value.

For example-

a =10

x = "welcome to yct"

print(a)

print(x)

Output-

10

welcome to yct

Data Type in Python

Every value in Python has a data type. Since

everything is an object in Python programming,

data types are actually classes and variables are

instances (object) of these classes.

Following diagram demonstrates the various types

of data types in python programming language.

Python - Data Types

Numeric

Boolean

Set

Dictionary

Sequence

Integer

Float

List

Tuple

Complex

Number

String

Type Conversion in Python-

The process of converting the value of one data

type such as (integer, string, float, etc.) to another

data type is known as type conversion. There are

two types of type conversion.

Implicit Type Conversion

In Implicit type conversion, Python automatically

converts one data type to another data type.

For example-

Converting integer to float-

N_int =5

N_float = 5.5

N_new = N_int + N_float

print("datatype of N_int:",type(N_int))

print("datatype of N_float:",type(N_float))

print("Value of N_new:",N_new)

print("datatype of N_new:",type(N_new))

After running the above code we get output as :-

datatype of N_int: < class 'int'>

datatype of N_float: < class 'float'>

Value of N_new: 10.5

datatype of N_new: < class 'float'>

Explicit Type Conversion

In explicit type conversion, users convert the data

type of an object to required data type and for that

we use the predefined functions such as int(),

float(), str(), etc to perform explicit type

conversion.

Syntax-

<required_datatype>(expression)

For example- To add string and integer data types using

explicit type conversion.

a =50

b ="100"

result1 = a + b

b = int(b)

result2 = a + b

print(result2)

Output-

Traceback (most recent call last):

File "", line 1, in

TypeError: unsupported operand type(s) for +:

'int' and 'str'

150

In the above example, variable a is of the number

data type and variable b is of the string data type.

When we try to add these two integers and store

the value in a variable named result1, a TypeError

occurs as displayed in the output. So, in order to

perform this operation, we have to use explicit

type casting. As we can see in the above code

block, we have converted the variable b into int

type and then added variables a and b. The sum is

stored in the variable named result2, and when

printed it displays 150 as output, as we can see in

the output block.

Web Technology

152

YCT

Python Namespace

A namespace is a collection of names and python

implements namespaces as dictionaries.

A namespace allows us to have unique names for

each object If we don't know, this is just a quick

reminder to tell us that strings, lists, functions, etc.

everything in python is an object.

In other words, we can say that the role of a

namespace is like a surname.

Namespaces are of basically three types :-

1. Built-in Namespace- It includes functions and

exception names that are built-in in Python.

2. Global Namespace- It includes names from

the modules that are imported in the project. It is

created when we include the module and it lasts

until the script ends.

3. Local Namespace- It is created when the

function is called and the scope ends when the value

is returned.

if ... else Statement in python

If statement

Syntax-

if test exp:

statement(s)

if ... else Statement

Syntax-

if test exp:

Body of if

else:

Body of else

if ... elif ... else

Syntax-

if test exp:

Body of if

elif test exp:

Body of elif

else:

Body of else

Loop in Python Programming

For loop- A for loop is used for iterating over a

sequence (that is either a list, a tuple, a dictionary,

, or a string).

Syntax-

for val in sequence:

loop body

For example-

fruits =["mango", "banana", "orange"]

for x in fruits:

print(x)

Output-

mango

banana

orange

While Loop- With the help of while loop we can

execute a set of statements as long as a condition

is true.

Syntax-

while test_expression:

body of while

For example-

i=1

while i < 5:

print(i)

i += 1

Output-

1

2

3

4

Break Statement in Python

With the help of break statement we can stop the

loop even if the while condition is true.

For example-

Exit the loop when i is 4.

i=1

while i < 8:

print(i)

if (i == 4):

break

i+=1

Output-

1

2

3

4

Pass Statement in Python

In Python programming, the pass statement is a

null statement. It is generally used as placeholder.

Syntax-

pass

Web Technology

153

YCT

Errors and Exceptions in Python

Syntax Errors- when error caused by not

following the proper syntax of the language is

called syntax error or parsing error.

Exceptions- when errors occurring at runtime

(after passing the syntax test) are called

exceptions or logical errors.

List

List are used to store multiple items in a single

variable. List are created using square brackets.

List items are ordered, changeable and allow

duplicate values. And list first item has index [0]

and second item has index [1].

Example- list =["Rahul", "Raj", "Kumar"]

print(list)

Output- ['Rahul', 'Raj', 'Kumar']

List Methods

Method

Description

append()

Adds an element at the end of the

list

clear()

Removes all the element from the

list

copy()

Returns a copy of the list

count()

Returns the numbers of element

with the specified value

index()

Returns the index of the first

element with the specified value

insert()

Adds an element at the specified

position

pop()

Removes the element at the

specified

remove()

Removes the item with the

specified value

reverse()

Reverses the order of the list

sort()

Sorts the list

Tuple- Tuples are used to store multiple items in

a single variable. A tuple is a collection which is

ordered and unchangeable and tuples are written

with round brackets. Tuple items are indexed the

first item has index [0] and second index[1].

Example-

tuple =("Rahul", "Yct", "Raj")

print(tuple)

Output- ("Rahul", "Yct", "Raj")

Tuple Methods

Method

Description

count()

Return the number of times a

specified value occurs in a tuple

index()

Searches the tuple for a specified

value and returns the position of

where it was found

Set- Sets are used to multiple items in a single

variable and it is collection which is unordered,

unchangeable and unintexed sets are written with

curly brackets. Sets can't allow duplicate value.

Example-

theset = {"Rahul", "Kumar", "Raj" "Rahul")

print(theset)

Output-

("Kumar", "Raj", " Rahul")

Set Methods

Method

Description

add()

Adds an element to the set

clear()

Remove all the elements

from the set

copy()

Returns a copy of the set

difference()

Returns a set containing the

difference between two or

more sets

differecne_update()

Remove the items in this

set that are also included in

another, specified set

pop()

Removes an element from

the set

remove()

Remove the specified

element

union()

Return a set containing the

union of sets

update()

Update the set with the

union of this set and others

Web Technology

154

YCT

Dictionary- Dictionaries are used to store data

value in key value pairs. It is written with curly

brackets. A dictionary is a collection which is

ordered, changeable and is not allow duplicates.

Example-

thedict={"brand": "Ford",

"Model":" Mustang",

"year": 1954

}

print(thedict)

Output- {'brand': 'Ford', 'Mode': 'Mustang', 'year' "

1954}

Dictionary Method

Method

Description

clear()

Removes all the elements

from the dictionary

copy()

Returns a copy of the

dictionary

get()

Returns the value of the

specified key

items()

Returns a list containing a

tuple for each key value

pair

keys()

Returns a list containing

the dictionary's keys

pop()

Removes the element with

the specified key

popitem()

Removes the last inserted

key value pairs

update()

Updates the dictionary

with the specified key-

value pairs

values

Returns a list of all the

values in the dictionary

setdefault()

Returns the value of the

specified key. If the key

does not exist, insert the

key with the specified

value

Array

An array is a special variable which can hold

more than one value at a time. In order to create

Python arrays. You will first have to import the

array module.

Array Import

Using import array at the top of the

file. You would then go to create an

array using array.array().

Instead of having to type array.array()

all the time, use import array as arr at

the top of the file or arr.array().

Use from array import* with*

importing all the functionalities

available.

Example-

import array as arr

numbers = arr.array('i', [10, 15, 20])

print(numbers)

Output-

array('i',[10, 15, 20])

Methods of array

Method

Description

append()

Adds an element at the end of the list.

clear()

Removes all the elements from the list.

copy()

Returns a copy of the list.

count()

Returns the number of element with the

specified value.

index()

Returns the index of the first element

with the specified value.

insert()

Adds an element at the specified

position.

pop()

Removes the element of the specified

position.

remove()

Removes the first item with the

specified position.

reverse()

Reverses the order of the list.

Web Technology

155

YCT

Module

A module to be the same as a code library. A file

containing a set of function you want to include

in your application. A file with the file extension

.py.

How to use Module and Variable- The module

we just created by using the import statement.

Module create variables of all types (arrays,

dictionaries, objects).

Example-

file name mymodule.py

company={

"Name": "Yct",

"Model": 1993,

"City": "Prayagraj"

}

So, import the module named my module and

access the company.

import mymodule

x= mymodule.company["model"]

print(x)

Output- 1993

Exception Handling in Python

When exceptions occur, the Python interpreter

stops the current process and passes it to the

calling process until it is handled. If not handled,

the program will crash. These exceptions can be

handled using the try statement.

RegEx in Python

A regular expression is a sequence of characters

that defines a search pattern. A pattern defined

using RegEx can be used to match against a

string.

Iterators in Python-

An iterator is an object that implements the

iterator protocol. In other words, an iterator is an

object that implements the following methods:

iter_ - It returns the iterator object itself.

next_ - It returns the next element.

Generators in Python-

Python generators are a simple way of creating

iterators.

A generator is a special type of function which

does not return a single value, instead, it returns

an iterator object with a sequence of values.

In a generator function, a yield statement is used

rather than a return statement.

File Handling in python

Python has a number of functions for creating,

reading, updating, and deleting files. The key

function for working with files in Python is the

open() function. The open() function takes two

parameters; filename, and mode.

f = open(filename, mode)

There are four different modes for opening a file :-

"r" - Read - Opens a file for reading

"a" - Append - Opens a file for appending

"w" - Write - Opens a file for writing

"x" - Create - Creates the specified file

Web Technology

156

YCT

12.

SOFTWARE ENGINEERING

Software Development Life Cycle

(SDLC)

SDLC is a process followed for a software

project, within a software organization. It

consists of a detailed plan describing how to

develop, transit, replace, maintain and alter or

enhance particular software.

SDLC defines a methodology for improving the

quality of software and the overall development

process.

Graphical representation of the various stages

or steps of a typical SDLC:

Maintenance

Deployment

Planning

Analysis

or

Defining

Testing

SDLC

Designing

Coding

Building or

Developing

The SDLC is a structured process that enables

the production of high-quality, low-cost software

in the shortest production time. The goal of the

SDLC is to produce superior software that meets

and exceeds all customer expectations and

demands, by the following of above

stages/steps :-

Stage 1

Planning- Project planning is all about "What

do we want?" It is vital role in the software

delivery life cycle since this is the part where the

team estimates the cost and defines the

requirements of the new software.

Stage 2

Analysis-Analyzing maximum information

from the client requirements for the software,

the team has to discuss each details and

specification of the product with the customer

and then analyze the requirements keeping the

design code of the software in mind.

Stage 3

Designing- In this stage, Developers will first

outline the details for the overall application as

input and software architecture of the end user.

0

Designing helps the overall system architecture.

0

It serves as input for the next phase of the model

such as user interface, system interface, network,

and network requirements and database.

In designing phase, there are two kinds of

design documents :-

Brief description of each module.

HLD

(High-Level

Design)

Interface relationship between modules.

Complete architecture diagram.

LLD

(Low-Level

Design)

Functional logic of the module.

Database tables including type, size.

Complete details of the interface.

Stage 4

Building or Developing- In this stage, the

actual development starts and the product is

built. If the design is performed in a detailed and

organized manner, code generation can be

accomplished without much hassle. Hence,

programming code is generated as per DDS

during this stage.

Software Engineering

157

YCT

Stage 5

Coding or Implementation- Coding starts once

the developer gets the design document. The

software design is translated into source code. It

means translating the design to a computer-

legible language. File conversion, user training,

and new changes to the system are belong to this

stage/phase.

Stage 6

Testing- Testing is done by testing team to

verify that the functionality of entire application

works according to the customer requirements.

By finding some bugs/defects, the team fixes

them and sends back for a re-test. This process

continues until the software is bug-free, stable

and working according to the business needs of

that system.

Stage 7

Deployment or Installation- Product is

deployed in the production environment or first

UAT (User Acceptance Testing) depending on

the customer expectation, then based on the

feedback given by the project manager, the final

software is released and checked for deployment

issues if any.

Stage 8

Maintenance- If any issue comes up in

deployment phase and needs to be fixed or any

enhancement, it is taken care by the developers

by using following three activities, because

maintenance phase of SDLC is most effected

during costly faults is introducing:

Bug Fixing

Upgradation

Enhancement

Basic SDLC Methodologies

Although SDLC is a project management having broad

sense, seven more methodologies can be leveraged to

achieve specific results with different attributes.

Waterfall Model

Iterative Model

Prototype

model

Spiral Model

Agile Model

Big Bang

Model

V-Model

Waterfall Model- It is linear and straight-

forward and requires development teams to

finish one phase of the project completely before

moving on the next.

Hence, the outcome of one phase acts as input

for the next phase. This model is not suitable for

accommodating projects.

Example-

Requirements

Specification

Design

Evaluation

Testing

Iterative Model- This model focuses or stresses

on repetition and repeat testing. Developers

create a version rapidly for relatively less cost,

then test and improve it through successive

versions.

Example-

Requirements-

Specification

Evaluation

Design

Testing Implementation

Software Engineering

158

YCT

Spiral Model- Spiral model starts with analysis.

This model is flexible compared to other

methodologies. Projects pass through four main

phases again and again in a metaphorically spiral

motion. It is a risk-driven process model. It

resembles in its emphasis on repetition and

project risk factor is considered which is

inefficient for smaller projects. Until the

software retires, it will continue.

Example-

Spiral model has four phases :-

Planning

Risk

Analysis

Evaluation

Engineering

V-Model- This model is also known as

verification and validation model. In this model,

verification and validation goes hand-in-hand

i.e. development and testing goes parallel as it

includes tests at each stage of development. V-

model joins by coding phase.

Example-

Verification Phase

Validation Phase

Requirements

Acceptance Testing

Design

1

System Testing

High level Design

Integration Testing

Low level Design

Unit Testing

Coding

Prototype Model- In this model, the prototype

is developed prior to the actual software. This

model has limited functional capabilities and

inefficient performance when compared to the

actual software. It gets the valuable feedback

from the customer. Feedbacks are implemented

and the prototype is again reviewed by the

customer for any change.

Example-

Start

Requirement

gathering

Quick

Design

Building

Prototype

Stop

Engineer

Product

Refining

Prototype

Customer

Evaluation

Agile Model- It is a group of Iterative and

incremental model. In this model, any product is

broken into small incremental builds as this

model focuses more on flexibility rather than on

requirement while developing any product. New

features can be added easily in this model.

Agile does not rush the team to deploy the

product to customers but to perform testing at

the end of each sprint.

Test

Specific Requirements

Deploy

Design

Feedback

Build

Example-

Deploy

Test

Review

Sprint

1

Develop

Plan

Design

Deploy

Test

Review

Sprint

Develop

2

Plan

Design

Deploy

Test

Review

Sprint

3

Develop

Plan

Design

Software Engineering

159

YCT

Big Bang Model- This model is used for

smaller projects and experimental life cycle

designed to inform other projects within same

company.

Time

Release

Software

Product

Big Bang

Model

Resource

Money

Effort

This model is flexible because it doesn't follow

any rigorous procedures or processes. It starts

with little planning and moves to the coding

stage because it does not have requirements of

much scheduling and planning.

Money and efforts are put together as the input

and output come as a developed software which

might be or might not be the same as the

requirements of customer, in this model.

Software Metrics: Software Project

Management

Software Metrics- It is standard measurement

for the estimation of quality, progress, health

and testing of software characteristics which are

measurable or countable and quantifiable. It

includes measuring software performance,

planning work items, productivity and many

other uses.

Classification of software Metrics

Software Metrics

Process Metrics

Product Metrics

Change Metrics

Developer Metrics

Static Metrics

Dynamic Metrics

Size

Metrics

Design

Metrics

Control

Flow

Metrics

Information

Metrics

Weighted

Metrics

Data

Structure

Metrics

Software

Science

Metrics

Test

Ability

LOC

Token

Count

Function

count

Process

Metrics

These are the measures

of various characteristics

of the software development.

These are the measures of

Various characteristics of the

software product.

Product

Metrics

Example-

Efficiency of detection of

fault and removal them

Software size and complexity

software reliability and quality&

Two

Important

Characteristics

Software Engineering

160

YCT

Types of software Metrics

Process Metrics

2

Product Metrics

Internal Metrics

5

4

External Metrics

6

Project Metrics

7

Hybrid Metrics

Manual Test Metrics

It defines a

projects,

characteristics

and execution.

Productivity

Quality,

Efficiency and

Portability are

process metrics

Base Metrics

Calculated Metrics

It defines a

Product's over-

all quality and

resources

To Provide base

metrics,

analysts collect

data throughout

the test cases'

development and

execution. These

metrics are send

to test leads and

Project manager

by generating a

project status

report. It is quan

-tified using -

To create cal-

culated metrics,

data from base

metrics are

used. To track

Project progress

at the module,

tester and other

levels, the test

lead collects

information and

transform it into

more useful

Information

These metrics

are combination

of product,

process and

resource metrics

Example- cost

per FP(function

Point)

It defines a

Product's size,

design perform-

ance quality and

complexity.

These metrics

are used for

measuring pro-

perties that are

viewed to be

greater import-

ance to a

developer.

Example- LOC

(Lines of code)

These metrics

are used for

measuring

Properties

that are viewed

to be greater

importance to

the user

Example- Relia

-bility, usability

Portability,

fuctionality,etc.

=> The total

number of test

cases.

=>The total

number of test

cases completed

=>In analysis cycle, the metrics must be

recognized.

=>It defines the QA metrics that have been

identified.

Create a

Strong

conclusion

reports for the

paper and

distribute

them to the

belonging

stake holders

by gathering

input from

them.

In order to

process the

metrics,

educate

the testing

team on the

data points

that must

be collected

and

informed

about the

metrics-

Analysis

Report

Test Metrics

Life cycle

Communi-

cation

Evaluation

To calculate the value

of the metrics using the data

collection, data should be captured

and verified.

Software Engineering

161

YCT

Formula for Test metrics

If anyone wants to get the percentage of the test cases, the following formula can be useful ;-

Sr. No.

Percentage (%) of

Formula

1.

Test cases executed

No. of test cases executed

×100

Total no. of test cases

2.

Test case effectiveness

No. of detected defects

×100

No. of running test cases

3.

Passed test cases

Total no. of test run

×100

Total no. of test executed

4.

Failed test cases

Total no. of failed test cases

×100

Total no. of test executed

5.

Blocked test cases

Total no. of blocked tests

×100

Total no. of test executed

6.

Fixed defects

Total no. of flaues fixed

×100

No.of defects reported

7.

Rework effort ratio

Actualrework efforts

×100

Totalactual efforts

8.

Accepted defects

Defects accepted

Total defects

×100

9.

Defects deferred

Deferred defects for future use

×100

Total defects reported

Let's take an Example to Calculate Test Metrices

Sr. No.

Testing Metrics

Data retrieved while developing

test cases

1.

No. of requirements

5

2.

No. of test cases

40

3.

Total no. of test cases

200

4.

Total no. of test cases executed

164

5.

No. of passed test cases

100

6.

No. of failed test cases

60

7.

No. of blocked test cases

4

8.

No. of unexecuted test cases

36

9.

Total no. of defected test cases

20

10.

Accepted defects

15

11.

Defects deferred for future use

5

12

Fixed defects

12

Software Engineering

162

YCT

Solution for the above example is written below :-

Test cases executed

No. of test cases executed

164

1.

×100 ⇒ーー×100 ⇒82

Total no. of test cases written

200

No. of detected defects

20 ×100=>12.2

2.

Test cases effectiveness

×100=>

No. of running test cases

164

Total no. of failed test cases

×100=>

60

×100=>36.59

3.

Failed test cases %

Total no. of test cases executed

164

Total no. of blocked tests

Blocked Test cases %

4 ×100 =>2.44

164

4.

×1004_x100=>2.44

Total no. of test cases executed

Total no. of flaws fixed

×100=>

12

5.

Fixed defects %

×100=>60

No. of defects reported

20

Defects accepted

15

20

×100=>75

6.

Accepted defects %

×100=>

Total defects

Deferred defects for future use

7.

Defects deferred

x100 >_x100 =>25

20

Total defects reported

Software Project Management (SPM)

Project- A project is a collection of tasks as inputs and

outputs needed to achieve a particular goal while a

software project is the complete procedure of software

development.

Software Project Management- It is a proper way of

planning, leading, execution, supervision and control of

software project. It is also a discipline and skill for

organizing and managing software projects. It is

necessary to incorporate user requirements along with

budget and time constraints.

Software Engineering

163

YCT

Different types of management

Requirement

Management

Release

management

Risk

Management

Change

Management

Conflict

Management

Software

configuration

Management

Requirement management

It is an ongoing process throughout the project.

It is the process of recording, tracking prioriti-

zing, analyzing, documenting, supervising

followed by controlling change and informing

related stakeholders.

Risk management

Analysing and identifying the risks that is

followed by the coordinated and cost-effectlive

application are performed by risk management

because its resources are used to reduce,

operate, control, minimize the possibility or

effect of unfortunate events or to maximize the

opportunity

Conflict management

Just you know that the goal/ aim of conflict

management is to improve learning, group

outcomes, including performance or efficacy

within an organizational setting because it is

such a process as restricts the negative or bad

aspects of conflict during increasing the

positive aspects.

Software configuration management

It is the act or process of monitoring , controll-

ing, tracking, or regulating changes to the

software. In this management, revision control

and inauguration of baseline creation are

included.

Change management

In this systematic approach, dealing with a

methodological manner, the transition or

transformation of an organization goals,

processes, objective procedures technologies

are assisted individuals in adapting to change.

Release management

It ensures that the organization delivers new

and enhanced products needed to the customers.

Release management is also known as planning

scheduling, managing, controlling and

deploying release of tasks. While maintainng

the integrity of the current product, it fulfills

the customer's need.

Software Engineering

164

YCT

Aspects/Features of Software Project Management

Planning

Execution

Budget

Leading

Time

Management

Control

Monitoring

Maintenance

The above list of focus areas that can tackle the broad

upsides of the software project management and by

following them any organization can protect the integrity

of the software.

Needs/Requirements of Software Project

Management- For any software organization while

staying within the customers budget and completing the

product on time, delivering a high-quality product is an

essential part. time, cost and quality are the triple factors

of many factors including both internal and external

which may impact the other two.

Time

Cost

Scope

Quality

Down sides of Software Project Management

Costs are high/expensive

Complexity will be increased

Communication overhead

Lack of creativity/originality

If one wants to engage software project management

technique to put in place, these initiatives can be costly

and time consuming. One could need instruction since

one's team will also be utilizing them. A project may

need help of professional or subject experts depend on

situation.

It is multi-step difficult procedure tending to complicate

things excessively which may lead to provide confusion

among team. Project having a larger scope especially if it

doesn't have a dedicated team.

For the software project management, when we hire

individuals, new hires join our company with or without

having company's culture then they can be kept at

workforce as small as possible. Resulting that the cost of

communication tends to soar.

Sometimes. project managers provide little or no space

for creativity. To initiate rigid standard, the team leaders

either put much focus on management or put strict time

on staff, or encourage creativity. That is why an

organization can build and ship code quickly else it

opens up new doors to achieve more objectives.

Who

is

Project

Manager

?

A project manager is a person who

makes both large and small

projects and all types of decisions

and is responsible for planning,

designing, monitoring, controlling,

executing and closure of a project.

1

Role of a Project Manager

1. As a leader - What the team is expected is leaded

and guided by a project manager by providing them

direction to make them understandable.

2. As a medium - A project manager may be a

medium between his clients and team if he

coordinates them and transfers all related

information from clients to his team and reports to

the senior management.

3. As a team motivator - To encourage team member

to work properly for the successful completion of

the project.

Software Engineering

165

YCT

4. As a team organizer - To organize teams to deliver

on an outcome such as functions, structure and

communications etc.

5. As a mentor - A team must have an attachment

guided by a mentor to his team at each step to

provide a recommendation in the right direction.

Planning and

Tracking

Project

Managing

Configuration

Managing

Project

Resource

1.

7.

Software

Management

Activities

Managing

Project

Communication

1(i)

6.

Managing

Scope

2.

5.

Managing

Scheduling

3.

4.

Managing

Estimation

Managing

Project Risk

1. Planning and Tracking Project - Planning and

tracking projects are multiple processes or tasks that

are executed before the construction of the software

product starts, by managing project resource.

2. Managing Scope - Scope management avoids price

and time overrun and clearly defines what would do

and what would not.

3. Managing Estimation - It figures out the size (line

of code), efforts, cost as well as time.

The line of code depends on the users or their needs.

By the help of efforts, a developer can quickly

estimate how big team are needed to inform the

software.

The time can be easily determined when size and

efforts are estimated.

Cost includes size, quality, hardware,

communication, training, licenses, tools and skilled

manpower.

4. Managing Project Risk - The following risks in a

project consist of all activities like monitoring,

analyzing, preparing and identification of the plan :-

The experienced team (staff) leaves the project and

the new team joins it.

Changes in organization, requirements,

technologies, environment, business competition and

misinterpreting needs.

5. Managing Scheduling - It refers to roadmap with

specified order within time slot allotted to each

activity. It defines various tasks, milestones and

arrangement by keeping many factors in mind.

It is necessary to find out multiple tasks, break down

them into smaller, and manageable modules,

estimate time frame for each task, calculate the total

time from start to finish, etc.

6. Managing Project Communication - Effective

communication from planning to closure in the

success of a project, it plays a vital role and bridges

gap between clients, team members, organizations as

well as other project creator or developer by

following many steps like planning, sharing,

feedback and closure.

7. Managing Configuration - It controls the changes

in software like need, design, functions and

development of the project. Configuration

management is needed because several people work

on software, help to build coordination between

suppliers, run on multiple systems, change in need,

budget, schedule, etc. by performing many tasks

including identification, base-line, change control,

status accounting, audits and reviews.

Baseline defines completeness of a phase, change

control ensures all changes made to software system

by using many steps like identification, validation,

analysis, control, execution and close request.

Software Engineering

166

YCT

Project Estimation Techniques

There are two broadly recognized techniques :-

Decomposition Technique

Empirical Estimation Technique

It Assumes the software as a product of various

compositions. It has two main model.

It uses derived formula to make estimation based on LOC

or FPs

Line of code (LOC)

Function Points (FPs)

PUTNAM Model

COCOMO

In the software product,

In the software product,

It maps time and efforts

Software products are divided

LOC estimation is

FPs estimation is

needed with software size.

into three categories of

completed on behalf of

completed

The PUTNAM model is

software organic, semi-

number of line of codes.

on behalf of number of

made by Lawrence H.

detached and embedded by

function points.

Putnam, which is based on

cocomo, which stands for

Norden's frequency

COnstructive COst MOdel,

distribution (Rayleigh

developed by Barry W.

curve)

Boehm.

COCOMO-1 Model

Two

Types of

COCOMO

Model

This model is also called Basic COCOMO which is used to

give an approximate estimation of projects' various parameters.

Example- Business system, Payroll management system,

Inventory management system.

This model is developed at the University of Southern California.

In this model, whole software is divided into different modules

which calculate the development time, and efforts.

Example- Report generator, spreadsheet, etc.

COCOMO-2 Model

Difference between COCOMO-1 and COCOMO-2

COCOMO-1

COCOMO-2

It provides estimates of effort and schedule.

It provides the estimates that represent one standard

deviation.

It is useful for waterfall model of SDLC (Software

Development Life Cycle).

It is useful in non-sequential, rapid development.

It is based on linear reuse formula.

It is based on non-linear reuse formula.

Effort exponent is determined by 3 development

models.

Effort exponent is determined by 5 scale factors.

Size of software stated in terms of lines of code

(LOC).

Size of software stated in terms of object points (OPs),

Function Points (FPs) and Line of Code (LOC).

Software Engineering

167

YCT

COCOMO Model in Brief -

Cost estimation model developed by Boehm in 1981.

Regression model based on LOC (no of Lines of Code)

Predicts the effort (E) and schedule (D) of product based on size of software.

A cocomo model addresses the area of application composition model, early design state model and Post

architecture model.

Based on size

(i) Organic

1. Basic COCOMO Model

Example- Data processing, Inventory management system etc.

(ii) Semi-Detached 2. Intermediate model

Example- OS, DBMS, etc.

(iii) Embedded

3. Detailed or Complete Model

Example- ATM, Air Traffic Control, etc.

Intermediate model is an expansion of basic cocomo model while complete cocomo model is an expansion of

intermediate cocomo model.

(1)

Basic model

KLOC model

a1

a2

b1

b2

E=al(KLOC) ª2 P.M

(2-50) Organic

2.4

1.05

2.5

0.38

D=b1 (E)b2 M

(50-300) Semi-detached

3.0

1.12

2.5

0.35

Productivity=

KLOC

E

(>300) Embedded

3.6

1.2

2.5

0.32

Where E=effort, D=development time.

(2)

Intermediate model

Model

(Attribute)

15 Cost Drivers

E=al(KLOC)ª2 * EAF

(Effort Adjust Factor)

Product

RELY, DATA, CPLX (Complexity)

MODP, TOOL, SCED

TIME, STOR, VIRAT, TURN

ACAP, AEXP, PCAP, VEXP, LEXP

D=b1Eb2

Project

System

Personnel

Software Engineering

168

YCT

Advantages

(3)

Detailed/Advance model

Ep=u(E)

D=TD

Disadvantages

Easy to estimate the total cost of

the project and to implement with

various factors.

It limits the accuracy of software

cost and ignores needs. hardware

issues and customer skills. It mostly

depends on time factors.

Example- 1=>

Suppose a project was estimated to be 400 KLOC.

Calculate the effort and development time for each of the

three models i.e., organic, semi-detached and embedded.

Solution-

(i) Organic mode,

E=al*(KLOC)ª2 PM

E=2.4 *(400)1.05=1295.31 PM

D=b1(E)b2.M

D=2.5*(1295.31)0.38=38.07 PM

(ii) Semi-detached mode,

E=3.0*(400)1.12=2462.79 PM

D=2.5*(2462.79)0.35=38.45 PM

(iii) Embedded mode,

E=3.6*(400)1.20=4772.81 PM

D=2.5*(4772.8)0.32=38 Pm

Example- 2=>

A project size of 200 KLOC is be developed. The

team has average experience on similar type of project.

The Project schedule is not very tight. Calculate the

effort, development time, average staff size and

productivity of the project.

Solution- The most appropriate mode for 200 KLOC is

semi-detached mode.

Hence, E=3.0(200)1.12=1133.12 PM

D=2.5(1133.12)0.35=29.3 PM

Average staff size (ss) = - Persons.

D

E

1133.12

= 29.3

= 38.67 Persons.

Productivity =

KLOC

E

200

=

1133.12

= 0.1765 KLOC/PM

Productivity = 176 LOC/PM

The following figure shows a plot of estimated effort

versus product size.

Embedded

Semi-detached

Organic

Estimated

Effort

Effort versus product size

Software Engineering

169

YCT

PUTNAM Model in Brief

Putnam Stated that Rayleigh-Norden curve that can be

used to relate the number of delivered lines of code to the

effort and the time needed to develop the product.

The Putnam expression is

L=CKK

1/34 4/3

td

Rayleigh curve

Effort

Time

Where K=total effort expended in PM

L=Product size in KLOC

td=time expended (development time)

Ck = Constant

2 poor software dev. environment

8 good

11 excellent

or K=

K3/C3 td4

or K=C/td4

For the same product size, c=L3/Ck3 is a constant

or

K1

K2

= t4d2 /t4d,

or Ko 1/ t4d

or Cost oc 1/ ta

According to the Putnam, project effort is inversely

proportional to the fourth power of the development

time. E = K/(TD ** 4)

This formula predicts zero effort for infinite development

time.

With respect to the size of

the project, we are

discussing risk and

uncertainty rises multifold.

Many tools are available

of which a few are

described below-

Gantt Chart

It shows the project schedule with respect to time period which was devised by Henry Gantt in 1917. It is also

known as a horizontal bar chart which represents activities and time schedule for the project.

Time

Activities

Week 1

Week 2

Week 3

Week 4

Week 5

Week 6

Week 7

Week 8

Week 9

Week 10

Planning

Design

Coding

Testing

Delivery

Software Engineering

170

YCT

Activities

Planning

Design

Coding

Testing

Delivery

Start

Week1

Week3

Week6

Week7

Week10

End

Week3

Week5

Week8

Week9

Week10

Duration

3

3

3

3

1

PERT CHART

Pert stands for Project Evaluation and Review

Technique. Its main objective is the analysis through its

three time values associated with each activity. These

are: Optimistic value, the pessimistic value and the most

likely value.

The optimistic time (to) => is the shortest possible time

in which activity can be finished.

The pessimistic time (tp) => represents the longest time

the activity could take if everything goes wrong.

The most likely time (tm) => is the estimate of normal

time the activity would take.

Expected time (te) => It is the average time on activity

taken if it was to be repeated on large number of times,

i.e.

te =

(to + 4.tm + tp)

6

Frequency

Optimistic Most

Pessimistic

likely

Variance (o)=> It is the variance of activity given by the

following formula :-

62=[(tp-to)/6]2 =(tp-to)2

36

Example-

The following characteristics have eight activities

(A, B, C, D, E, F, G and H) of a small project :-

Time Estimates (in weeks)

Activity

Preceding

Activity

Optimistic

time

(to)

Most

likely

time

(tm)

Pessimistic

time

(tp)

A

None

2

4

12

B

None

10

12

26

C

A

8

9

10

D

A

10

15

20

E

A

7

7.5

11

F

B, C

9

9

9

G

D

3

3.5

7

H

E, F, G

5

5

5

(i) Determine the critical path.

(ii) Draw the pert network

(iii) Prepare the activity schedule

(iv) What is the probability that the project will be

finished within the time limit if a 30 week

deadline is imposed?

Solution- The shortest time and variance of each activity

is computed by the following formula for the given

network data-

te =

to + 4tm + tp

6

and o =

(tp - to)2

36

teof A =

2+4×4+12

6

30

=~= 5

6

te of B =

10+4×12+26

6

84

6

=

=14

=

= 9

8+4×9+10

54

te of C =

6

6

te of D =

10+4×15+20

90

6

=

= 15

6

7+4×7.5+11

48

teof E =

=

=

8

6 6

9+4×9+9

54

te of F =

=

= 9

6

6

Software Engineering

171

YCT

te of G =

3+4×3.5+7

=

= 4

6

6

teof H =

5+4×5+5

30

6

24

=

= 5

6

20

20

7

D

G

15

4

1

A

2

E

V

5

H

6

0

0

5

5

5

8

24

24

5

7

29

29

B

C

F

14

9

9

MI

3

14 15

PERT Network Diagram

o of Α =

(12-2)2

36

100

36

9

=

=

25

o of B = (26-10)2 256 64

36 36 9

gof C= (10-8)2 4 1

36

36 9

(20-10)2 100 25

oof D =

36

36

9

o of E =

(11-7)2

=

=

16

4

36 36 9

Gof F (9-9)2 _0

36

36

=0

o of G =

(7-3)2 16 4

=

=

36

36 9

(5-5) 0

=0

o of H =

36

36

Activity

σ

Earliest Time

Latest

Time

Start

Finish

Start

Finish

A

25/9

0

5

0

5

B

64/9

0

14

1

15

C

1/9

5

14

6

15

D

25/9

5

20

5

20

E

4/9

5

13

16

24

F

0

14

23

15

24

G

4/9

20

24

20

24

H

0

24

29

24

29

The critical path of the project is 1-2-3-4-5-6,

critical activity being A ,D ,G and H.

The expected project is the sum of duration of each

critical activity =5+15+4+5=29 weeks.

25 25 4

9

Variance of project= - +-+-+0 = 6

9

9

Software Design

System Design

User Interface Design

Design level Metrics

Detailed Design

Object Oriented Design

Function Oriented Design

Software design is a process or mechanism in which,

using a set of primitive components and subject to

constraints, any agent can create a specification of a

software artifact to fulfill goals and can transform user

requirements into some suitable form to help the

programmers in coding and implementation. Software

design usually involves problem solving and solution

planning. It has above many design mainly the

following :-

Frontend Design

Backend Design

Full stack Design

Desktop Design

Web Design

Database Design

Mobile Design

Cloud Computing

Objectives of Software Design

Correctness

Completeness

Flexibility

Efficiency

Consistency

Maintainability

Correctness- As per the need of the user, software

design should be correct.

Completeness- The design should be complete like

modules, external interfaces and data structures.

Flexibility- As per the need, it should be flexible to

modify or alter.

Efficiency- All resources should be used by the program

with efficient.

Consistency- The consistency should be maintain in the

design.

Maintainability- The design should be so simple in

order that it can be easily maintainable by other

designers.

Software Engineering

172

YCT

Software Design Levels / Metrics

There are many software design levels of which we

can divide into three main categories. These are ;-

Architectural Design

High-Level Design

Detailed Design

Architectural Design- This first level design is highest

summarize edition of the system that determines the

software or application as a method with more elements

interactive with each where the designers obtain the idea

or thought of a suggested domain or province. It chooses

the overall structure and ignores the internal details.

High-Level Design- This second level design represents

multiple components and cooperation with each. It is an

identification of modular arrangement, different modules

and relationship among them. This design also defines

the interface among each module. High Level Design is

also known as preliminary design like a tree diagram

called the structure chart.

Detailed Design- This third level design determines the

logical structure, data structure and algorithms of the

different modules in comparison to previous module

designs and implementations. The accomplishment part

which will be finally seen by the system, dealt with this

detailed design.

Function Oriented Design

How the module should be interconnected and

needed for the system based on SRS (Software

Requirement Specification) are focused by the function

oriented design. In this approach or method, the design is

decomposed into a set of interacting units which have

clearly defined by the following categories :-

Data Dictionaries

DFD (Data Flow Diagram)

Structure charts

Object Oriented Design

Object Oriented Design (OOD) is the process in

which the system is viewed as a group of entities or

objects. This process permits the creation of a software

solution based on object notion. Each object handles its

state data among them, and responsible for its own data.

In other words, every object belongs to a class.

Objects

Classes

Messages

Abstraction

Encapsulation

Inheritance

Polymorphism

Objects- It inherits a class's attributes and operations

involved in solution design. For an instance, banks,

company, person and users are considered as objects.

Classes- These are generic descriptions of objects which

are class instances that define all the properties and

methods. A Class encapsulates the data and procedural

abstractions described by attributes. A super class is

generally a set of classes from where both attributes and

operations can be inherited by a sub class.

Messages- Massages consist of the integrity of the goal

object that is the name of requested operation and action

needed to. complete the function. All objects are

communicated by massage passing.

Abstraction- Abstraction handles the complexity in

object oriented design. It is also the removal of the

unnecessary and amplification of the essentials.

Encapsulation- Encapsulation is also known as

information hiding concept or concealing. The data and

operations are tied to a single unit. It not only bundles or

groups a vital information of an object together but also

restricts access to the operation, method and data from

the out access to the operation, method and data from the

outsider world.

Inheritance- To be staked hierarchically, OOD permits

similar classes, where lower or sub classes can be

implemented, imported, reused variables and functions

from their immediate super classes. This OOD's

characteristics is called an inheritance because it makes

its easier to define and create a specific and generalized

classes respectively.

Polymorphism- Polymorphism provides a program the

ability to redefine techniques for derived classes. It

permits a specific routine to uses different types of

variables at different times. Polymorphism is a feature /

technique or mechanism where similar tasks or functions

performed depending.

upon how the service is invoked, then the respective

portion of code gets executed.

Software Engineering

173

YCT

User Interface Design

The user interface is the frontend application view or

the visual part of an application or operation system

through which any user interacts with a computer or

software in order to use software. How commands are

given to computer or software and how data are

displayed on the screen are determined by interface

design which is mainly of two types :-

Text Based User Interface or Command

Line Interface

It provides a command prompt, where the user types

the predefined commands in their syntaxed order. The

predefined commands are needed to be remembered by

the users. It is also known as Command User Interface

(CUI).

Graphical User Interface

It provides the simple interactive interface to the

users to interact with the system. Using GUI, users

interpret the software because GUI can be a group or

combination of both hardware and software.

Interface Validation

Phase4

Users tasks

Phase 1

Phase3

Inplementation

Phase2

Interface design

Coding and Testing

Coding-

Coding is the process or phase which is used to

transform a system's design into a computer language

format. This phase is concerned with the specification of

software translating design into the source code. Source

code writing is necessary done by the coders or

programmers who are independent people.

To develop a dynamic and reliable software, coding

is an essential part of software.

By using coding, we can transform a system's design

into a programming language.

Programmer should implement a well defined coding

known as coding standard.

By using coding standards, our code will be easily

understandable, easy debugging, error-free according

to needs.

The coding standards are the guidelines or rules how to

write the code so that overall coding becomes

understandable.

The programmer should use-

-> Less global variable

-> Exception handling mechanism

-> Naming convention for global and local

variable or constant.

-> Comments for better understanding.

-> Maximum 1 to 20 line of code in a phase.

-> Very clever or easy code.

-> Different identifier for multiple purpose.

-> Name of variable and method not in short

form.

Goals of Coding

To reduce the cost

of later phases.

To translate the design into a

computer language format.

Making the program

more readable.

.

Testing-

Testing means software testing finding out the bugs

in the developed software or existing software. In other

words, find software errors and verify that application or

system is fit for use or not. Preventing bugs reducing

development costs and improving performance are the

benefits of testing.

There are two main types of testing.

1.

2.

Black Box Testing

White Box Testing

or

or

Functional Testing

Structured Testing

Black Box Testing or Functional Testing-

In this testing, the tester does not have the

knowledge of the coding. In this testing, we only check

the functionality of the software that is input is passing

correctly and related output is producing or not.

Software Engineering

174

YCT

White Box Testing or Structured Testing-

In this testing, the tester has the knowledge of

coking and internal structure of existing software

whether the internal structure is correct or not.

Types of Testing

Besides above two types of testing there are many

different types of software tests, these are-

1. Unit Testing-

This test is used to check the independent and

individual unit or module of software. A unit is the

smallest testable component of software.

2. Integration Testing-

This test integrates all the modules one by one and

checks the compatibility issues (Whether one

module is compatible with another or not).

3. System Testing-

In this testing, a coder puts the software in different

environment and checks whether the software is

compatible with new environment or not.

4. Stress Testing-

In this testing, the tester checks how the system

behaves with heavy load it means the capability of

software how much loaded software can handle

before it fails.

5.

. Performance Testing-

It checks the speed and effectiveness of the software

to make sure that it generates the result within the

specified time or real life load systems. Performance

means how the software performs under different

workloads.

6. Usability Testing-

It validates how well a customer can use a system or

web application to complete a task. In other words,

the coder checks the GUI part created by developer

whether GUI part or design of software is user

friendly or not.

7. Unit Testing-

It is done by the customer to verify and check the

delivered product or whole system works as

intended or customer acceptation.

8. Alpha Testing-

In this testing, the developer feeds the input and

measures the output because this testing is the last

testing done by the developer side just before the

delivery of the product.

9. Beta Testing-

In this testing, customer checks the functionality and

features of the software and provide suggestions to

the developer team whether the software is

providing good results or not.

10. Functional Testing-

It checks the functions by emulating business

scenario based on functional needs. To verify these

functions, Black box testing is used in common way.

11. Verification Testing-

It checks the product whether it is being built by the

coder in correct way or not.

12. Validation Testing-

It checks the built product whether it is completing

customer's requirements or not.

13. Big Bang Testing-

In this testing methodology all components or

modules of a system are combined together and

tested as a whole. This testing is of two types-

Top Down Integration- In this approach, firstly the

higher level modules are integrated then secondly,

the lower level modules are integrated. This testing

is also known as trickle-down approach.

Bottom Up Integration- In this approach, firstly the

lower level modules are integrated then the higher

level modules are integrated. This testing is also

known as bubble-up approach.

Software Quality and Reliability

Software Quality-"A quality product does exactly what

the users want it to do."

The software products have the several quality factors-

Portability

Usability

Reusability

Correctness

Maintainability

A quality can be measured a number of ways, two of

them give excellent insights into the product's stability-

1. Between testing and actual delivery, the number of

errors and defects are discovered in the system.

2. The amount of time or the Mean Time to Defect

(MTTD) are discovered prior to and after delivery to

the customer between bugs or errors.

Software Engineering

175

YCT

Having fewer errors, bugs, defects, a higher MTTD is

associated generally with better overall quality.

The software quality assurance is an umbrella

activity for checking the quality of software

whether the software we are making is quality full

or not.

Software Reliability

It is a probability of failure-free software operation

for a specified period of time within particular

environment. It is a dynamic system characteristics or

execution event.

The failure of software depends on two factors-

1. No. of faults being evaluated in software.

2. Operational profile of execution of the software.

Types of Time

1. Execution Time- The actual CPU time that the

software takes during its execution.

2. Calendar Time- Normal or regular time that we use

on a daily basis.

3. Clock Time- Actual time that is elapsed while the

software is executing. This time also includes the

time that the software spends while waiting in the

system.

Software Failure Mechanism

Software failure may due to bugs, ambiguities,

oversights or misinterpretation.

The software failure are classified as-

1. Transient Failure- It occurs only with particular

inputs.

2. Permanent Failure- It appears on all inputs.

3. Recoverable Failure- It can be recovered by the

system without operator's help.

4. Unrecoverable Failure- It can be recovered by the

system with operator's help only.

5. Non-corruption Failure- This failure doesn't corrupt

system's data or state.

6. Corrupting Failure- This failure damages the

system's data or state.

Reliability Testing or Software Testing

Reliability tests are designed to measure the ability

of system to remain operation for long period of

time.

It is typically expressed in terms of Mean Time to

Failure (MTTF).

The average of all time intervals between successive

failure is called the MTTF.

After a failure is observed, the developers analyze

and fix the defects or bugs that consumes

sometimes, it is called the Repair Time.

Types of Reliability Testing

=> Each function of the software

should be executed at least

once.

1.

Feature

Testing

=> Interaction between functions

should be reduced.

=> Each function should be

properly executed.

2.

Regression

Testing

=> It is performed whenever any

new functionality is added

and old functionalities are

removed.

3.

Load

Testing

=> It is used to determine whether

the application is supporting the

needed load or not.

Above three Reliability Testing are the main testing

to test software functionalities but there are many more

sub testing-

4.

Stress

Testing

=> It involves subjecting the system

to high levels of usage to identify

performance that can cause the

system to fail.

5.

Endurance

Testing

=> It involves running the system

continuously for an extended

period of time to identify issues

such as memory leaks.

6.

Spike

Testing

=> It involves subjecting to system

to sudden, unexpected increases

in load or usage to identify

performance, that can cause system

to fail.

Software Engineering

176

YCT

There are three main categories of reliability testing-

Modeling

Measurement

Improvement

1. Modeling

Predictive Modeling- It is a statistical technique

using machine learning and data mining. It is used to

predict and forecast future outcomes. It reduces time,

effort and costs in forecasting.

Estimation Modeling- It is a technique which is used

to find out the cost estimates to develop and test

software algorithm, equations, etc.

2. Measurement

It is a technique by which measurement of reliability

testing is performed by using following methods-

Mean Time Between Failure (MTBF)- It measures

the reliability testing in terms of mean time between

failure.

Mean Time to Failure (MTTF)- It is the time

between two consecutive failures.

Mean Time to Repair (MTTR)- It is known as the

time taken to fix the failure.

Measure of Reliability Testing

Sr. No.

Metric Analysis

Methods

1.

Mean Time to Failure (MTTF)

Total time

Number of units tested

2.

Mean Time to Repair

(MTTR)

Total time for maintenance

Total repairs

3.

Mean Time Between

Failure (MTBF)

Mean Time to Failure (MTTF)

+

Mean Time to Repair (MTTR)

4.

Occurrence Rate of Failure

1

Mean Time to Failure (MTTF)

5.

Probability of Failure

Number of Failures

Totalcases considered

6.

Availability

Mean Time of Failure (MTTF)

Mean Time Between Failure (MTBF)

Example- Find out the calculation of Mean Time to

Failure (MTTF), where the total time and the number of

unit tested are needed.

Solution-If the values are as below, the Mean Time to

Failure (MTTF) is calculated as :-

Total time

MTTF =

Number of units tested

100

=-= 2.5

40

Advantage of Software Reliability

It is used for data preservation.

It helps to avoid software failure

- It helps the system upgrade process to be straight-

forwarded.

Greater productivity is given by system efficiency and

higher performance.

Clean Room Approach

This approach was first proposed by Mills, Dyer and

Linger during the 1980s.

In software engineering, clean room is an approach

to produce quality software. It follows a set of principles

and practices for gathering needs, designing, testing,

coding, managing, etc which improves the quality of the

Software Engineering

177

YCT

product and increases productivity by consisting the

following four key processes-

1. Management- It consists of project mission,

resources, risk, schedule, training, analysis,

configuration, etc.

2. Specification- It consists of function, analysis,

needs, usage, incremental planning by

considering the first process of each increment.

3. Development- it consists of correctness,

reengineering, verification, incremental design,

etc. by considering the second process of each

increment.

4. Certification- It consists of test planning,

modeling, statistical training, certification

process, etc. by considering the final process of

each increment.

There are some tasks which occur in clean room

approach-

1. Increment Planning-

· It adopts the incremental strategy, which is

developed.

. It creates each increment's functionality,

project size, and clean room schedule.

. According to the plan, each increment is

integrated and certified in proper time which

is needed to be care taken.

2. Requirement Gathering- A more detailed

description of the customer level need is done

and developed by using the traditional

techniques like analysis, design, coding, testing,

and debugging.

3. Box Structure Specification- To describe the

functional specification, box structure is used.

The behavior, data and procedure in each

increment are separated and isolated by the box

structure.

4. Formal Design- By using black box structure

approach, the clean room design is a natural and

seamless extension of specification that is called

as clear boxes and state boxes that is also

known as component level design.

5. Correctness Specification- The clean room

team conducts the exact series of rigorous

correctness specification that starts with the

highest level testing or box structure and moves

forwards to the design detail and then moves

forwards to the design detail and then to the

code. By applying a set of "Correctness

Questions", its first level occurs or takes place.

If these do not signify or demonstrate, the

specification correctness, more formal and

mathematical methods are used.

6. Code Generation, Inspection and

Verification- The box structure specification is

represented in a particular language which is

translated into the appropriate programming

language by using technical reviews for the

semantic conformance of box structure and

code. At last, correctness verification is

conducted for the source code.

7. Statistical Test Planning- The clean room

activity is organized, analyzed, conducted,

planned, designed the projected usage of

software in parallel specification, verification

and code generation.

8. Statistical Use Testing- Designing a finite

number of test cases is always necessary

because exhaustive testing of software is

impossible. Use statistical technique to execute

a set of tests derived from a statistical sample of

possible execution by all users from a targeted

population.

9. Certification- The increments are certified and

ready for integration, once the verification,

inspection, all errors and usage testing have

been correctly completed.

Box Structure in Clean Room Process

Model

In clean room engineering, box structure is a

modeling approach. A box is like a container that

contains the details of system or aspects. By using the

following three types of boxes that are independent to

deliver the required information in each box

specification-

1. Black Box- It identifies the system's behaviour to

respond specific events.

Software Engineering

178

YCT

2. State Box- It identifies the operation or sate data that

are similar to the objects by representing the history

of the black box.

3. Clear Box-It identifies the transition function used by

state box. The procedural design for the state box is

included by the clear box.

Benefits of Clean Room Approach

Clean Room approach delivers high quality

products, reduces developing cost and overall project

time, saves resources, and increases productivity.

Software Reengineering

It is an activity that improves one's understanding of

software or prepares or improves the software itself for

increased maintainability, reusability, evalvability.

2.

Reverse

Engineering

Abstract

view

Forward

Engineering

1.

3.

Existing

System

Re-enginerering

system

Software reengineering is a process of software

development or examination and alteration of a system to

reconstitute in a new form. It also changes a "bad" design

into a "good" design. This process encompasses a

combination of sub processes like inventory analysis,

reverse engineering, restructuring, re-documentation,

forward engineering code and data restructuring, etc.

By variety of reasons, re-engineering can be done-

=> It adds new features.

=> It substitutes high casts.

=> It improves maintainability.

=> It adds new regulations and compliance.

=> It boosts up productivity.

=> It improves opportunity.

=> It reduces risks.

=> It saves and optimizes time.

Inventory

Analysis

Forward

Engineering

Document

Reconstructing

Data

Reconstruction

Reverse

Engineering

Code

Reconstructing

Booch Method

Booch method is widely used on object-oriented

analysis and design process. This method was authored

by Grady Booch when he was working for Rational

Software. This method consists of the following five

activities in its macro process :-

Analysis, Design, Conceptualization, Evolution,

Maintenance .

Macro process- This process consists of the above five

activities, in which the conceptualization takes into

account the perspective of the customer, while the

analysis develops a model by defining classes, attributes,

inheritance, method, etc. The design develops an

architecture. Evolution relates the implementation, and

the maintenance maintains the delivery of the product by

adding new requirements and eliminating bugs.

The Unified Modeling Language (UML) supersedes

the notation aspect of the Booch method from

which UML features the graphical elements form

the Object-Modeling Technique (OMT).

Micro Process- This process is a description of day to

day activities. Each macro process has its own micro

process which consists of the following phases that are

identified by Micro Process :-

Classes, objects, object semantics, related to

programming, object relationship, object interface,

abstraction and implementation.

Software Engineering

179

YCT

Example- Lets illustrate a Booch diagram related to a

BankAccount (Super class) having two attributes

SavingAccount and CheckingAccount that inherit the

super class :-

BankAccount

(Super class)

inherits

inherits

SavingAccount

CheckingAccount

Advantage of Booch method-

This method consists of many diagrams as class,

object, state transition, module, process and interaction.

Disadvantage of Booch method-

This method doesn't use all symbols and diagrams

while it defines a lot of symbols for almost every design

decision.

Rumbaugh Method

It is an approach very friendly and easy

methodology used to develop manageable object-

oriented because it is the closet to the traditional

approach. Rumbaugh method is also known as OMT

(Object Modeling Technique) used in the real world for

designing and modeling of software. OMT includes the

four stages (analysis, designing system, designing object

and implementation).

Additionally, OMT is always broken down into

three different parts or models (object, dynamic,

functional). These three models are similar to traditional

system.

Example- Lets illustrate a Rumbaugh diagram related to

a Bank-Account having the transaction between

customer and Bank Account :-

Jacobson Method

Jacobson method is used to plan, design and implement

object-oriented software which covers the entire life

cycle and stress traceability between different phases

both backward and forward. It is also known as Object-

Oriented Software Engineering (OOSE). This method is

broken down into five models or parts :-

Requirements, Analysis, Design, Implementation, and

Testing model. Jacobson method is also called Object-

Oriented Business Engineering (OOBE). The visual,

textual and structural methods were formulated by Ivar

Jacobson in 1986.

Use cases-

It needs the scenario for understanding system.

No clear flow of events with non-formal text is

needed.

With a clear flow of events to follow, text is easy to

read.

Formal style using pseudo code.

It governs interaction between the various actors.

How and when the use case begins and ends.

How and when of data storage and usage ends.

How the constraints of the problem domain are

handled.

Example- Lets illustrate a Jacobson method ordering

kiosk system, which relies on the customer for order

same as the receipt relies on the kiosk for order :-

BankAccount

Chef

Place order

Customer

Customer

owned

by

Account Number

Balance

Account

Transaction

Kiosks

Transaction

Name ...

Adress ...

getBalance ()

withdraw ()

deposit ()

Value ()

Prepares order

Receipt

Software Engineering

180

YCT

13.

CLOUD COMPUTING

Introduction -

Cloud computing is on-demand access via the internet

which contains a significant pool of resources including

servers, storage, database, analytics, software,

networking and intelligence over the cloud (internet).

Cloud

Computing

If any user uses an online service to send emails,

documents, watch movies, listen to music, send

pictures, play games then these all are made possible

behind the scene by cloud computing. It generally used

to store, backup and recover data. By using the

following you can -

> Store, backup and recover data.

> Stream audio and videos.

> Deliver software on demand from one place to

another.

> Analyze, test and built applications.

Cloud based storage makes your data possible

to save them to a remote database rather than

keeping/storing them on a hard drive or local

storage device.

O

Cloud computing provides more options for

people and business as cost savings, increase

productivity, speed and efficiency, performance

and security that are benefits for users.

Example of cloud computing - Google Drive,

One Drive, Box or Dropbox, etc.

Features of Cloud

There are many cloud features-

$

?

Automation

&

Archestration

Performance

Monitoring

Cost

Management

Governance

&

compliance

Security

Migration/Images

configuration

management

Applications,

computations

storage, networks

Instance and

billing

management

Risk, Audits

service and

resource

governance

Encryption mobile

or endpoint

security

Types of Cloud Computing

Private Cloud - A private cloud is the service and

infrastructure that are maintained on a private network,

because it refers resources that can be physically located

on the company's or organization's on-site data center.

Rarely, even some organizations pay third-party service

to be built and hosted by private cloud.

Public Cloud - This service is sold on-demand by the

minute or hour through long-term commitments because

a third-party CSP (Cloud Service Provider) provides the

service over the internet. In this cloud, all hardware,

software, servers, storage and other infrastructure are

owned and managed by the CSP.

Hybrid Cloud - A hybrid cloud is the combination of

public cloud and private cloud services. It is used to

Cloud Computing

181

YCT

store/share applications and data to both physical

storage and cloud storage. It provides company's

business greater flexibility and deployment.

Advantage of Cloud Computing

> Cloud based software promises to reduce IT

complexity and costs.

> It offers companies from all fields to use software

from any device via a native app or a browser.

> It provides a number of benefits that is why users

can carry their files to other devices remotely or

seamless manner.

> By using Dropbox and Google Drive, users can

check, send emails on any computer and can store

files.

> It makes possible for users to backup, share, store

their files, music and photos.

> It can provide security to users' files, documents,

in the event of a hard drive crash.

Disadvantage of Cloud Computing

> There are naturally risks with all the efficiencies,

speed, innovations that come with cloud

computing.

> When security comes to a sensitive medical

records, it has always been a great concern.

> Encryption protects the vital information.

> All the files, documents and data disappear when

the encryption key is lost.

> The company's servers may fall victim to natural

disasters, internal errors (bugs), and even power

outages maintained by cloud computing.

Types of Cloud Services (IaaS, PaaS, SaaS)

SaaS

PaaS

IaaS

There are four broad categories that are fallen

into by most cloud computing services; they

consist of the following-

On Premises or

On-site

IaaS

PaaS

SaaS

Application

Application

Application

Application

Data

Data

Data

Data

Runtime

Runtime

Runtime

Runtime

Middleware

Middleware

Middleware

Middleware

O/S

O/S

O/S

O/S

Virtualization

Virtualization

Virtualization

Virtualization

Servers

Servers

Servers

Servers

Storage

Storage

Storage

Storage

Networking

Networking

Networking

Networking

You manage

Other manages

1. IaaS (Infrastructure as a Service)-

It is a computing infrastructure managed over

internet. IaaS is also called HaaS (Hardware as a

Service). It helps users to avoid the cost and

complexity of purchasing and managing physical

servers. Users have an allocated storage capacity

and can start, stop, access and configure the

Virtual Machine (VM) and storage as required.

Apart from the above resources, the IaaS also

offers-

> Virtual machine disk storage

> Load balancers

> Virtual local area networks (VLANs)

> IP addresses

> Software bundles

Example- Google Compute Engine (GCE),

Microsoft Azure, Linode, DigitalOcean, Amazon

Cloud Computing

182

YCT

Web Services (AWS), Racksapace, Cisco Meta

cloud.

Characteristics of IaaS-

Resources are available as a service.

Services are highly scalable, dynamic, flexible.

GUI and API based access.

Automated administrative tasks.

2.

PaaS (Platform as a Service)-

It is a created platform for the programmers

to develop, test, run and manage the applications,

so that users can access these tools over the

internet using APIs, web portals or gateway

software. PaaS offers runtime environment for

applications to be developed. It has a feature of

point-and-click tool that enables non-developers

to create web applications.

Example- Windows Azure, Heroku, Force.com,

Google App Engine, Apache Stratos, AWS

Elastic Beanstalk, Magento Commerce Cloud

and OpenShift, etc.

Characteristics of PaaS-

Integrates with web services and databases.

Accessible to various users via the same

development application.

Supports multiple languages and frameworks.

Provides an ability to Auto-scale.

Builds on virtualization technology, so that

resources can easily be scaled up or down as

per the company's needs.

3.

Saas (Software as a Service)-

It is a web service by which users can access the

applications with the help of internet connection

and web browser on their phone, tablet or PC. It

is also called 'on-demand software' in which the

applications are hosted by a cloud service

provider.

Example-ZenDesk, Slack, Google Apps,

BigCommerce, SalesForce, Dropbox, Cisco

WebEx, and GoToMeeting, etc.

Below are the several SaaS applications-

> Help desk applications

> Billing and invoicing system

> Human Resource (HR) solutions

> Customer Relationship Management (CRM)

applications

Characteristics of SaaS-

Updation are applied automatically so users

are not responsible for hardware and software

updates.

Managed from a central location.

Hosted on a remote server.

Accessible over the internet.

The services are purchased on the pay-as-per-

use basis.

Virtualization-

It is a creation or technique of a virtual (rather

than actual) version of something such as a

server, a desktop, a storage device (RAM), an

operating system or network resources which

allow to share a single physical instance.

Creating a virtual machine over existing

operating system and hardware is known as

Hardware virtualization. The machine on which

the virtual machine is going to create is called a

Host Machine.

S

E

VM

=

Processor

R

V

E

R

VM

=

RAM

VM=

ROM

VM

=

Network

Hypervisor

(VMM)

ÎT

Types of Virtualization-

1. Hardware virtualization

2. Operation system virtualization

3. Server virtualization

4. Storage virtualization

Cloud Computing

183

YCT

Cloud Services Requirements

Efficiency/Cost Reduction

Data Security

Scalability

Control

Disaster Recovery

Mobility

Market Reach

Automatic Software Update

Cloud and Dynamic Infrastructure

Service Management

1.

2.

Asset Management

Virtualization & Consolidation

3,

4,

Information infrastructure

Energy Efficiency

5

6.

Security

7.

Elasticity /Resilience

Cloud Service Management

The cloud service management system offers

standardization, support desk, operational control,

monitoring, and consistent service delivery needed for

private, public, and hybrid cloud platforms by using the

following -

1. Simplify user interaction with IT

Service catalog enables standards and speeds up

the delivery.

2. Enable policies to lower the cost

Automated provison & decommission speed up

delivery and assets respectively.

3. Enhance system administrator Efficiency

Migration from various management isolates full-

fledged service.

Cloud Deployment Models

Using cloud deployment models, business

processes, application, data and any type of IT

resource can be provided as a service and

delivered to the users. These deployment models

are-

1. Public clouds- In this model, a business rents

the capability and pays for what is used on-

demand.

Advantages- Minimal investment, No setup

cost, Infrastructure management is not required,

No maintenance, Dynamic scalability required.

Disadvantages- Less secure, Low customization.

2. Private clouds- In this model, a business

essentially turns its IT environment into a cloud

and uses it to deliver services to their users.

Advantages- Better control, Data Security and

Privacy, Support Legacy System, Customization.

Disadvantages- Less scalable, more costly.

3. Hybrid Clouds- Hybrid clouds combine

elements of public and private clouds. By using

Cloud Computing

184

YCT

this model, you may host the app in a safe

environment.

Advantages- Flexibility and control, cost,

security.

Disadvantages- Difficult to manage, slow data

transmission.

4. Community or Commodity Clouds-

Community clouds are managed by groups of

people, communities and agencies especially

government to have the common interests

working on the same mission.

Advantages- Cost effective, security, shared

resources, collaboration and data sharing.

Disadvantages- Limited scalability, Rigid in

customization.

5. Shared Private Clouds- This is a shared

compute capacity with variable usage-based

pricing to business units that are based on service

offerings, accounts, datacenters. To take over or

buy infrastructure made available through

account consolidations, it needs on internal profit.

6. Dedicated Private Clouds- It has IT service

catalog with dynamic provisioning. It depends on

standardized Service-Oriented Architecture

(SOA) assets, that can be broadly deployed into

new and existing accounts and is a lower-cost

model.

7. Dynamic Private Clouds- It allows client

workloads to dynamically migrate to and from the

compute cloud as required.

8. Multi Clouds- It combines the resources of

public and private clouds as the name implies. It

is similar to the hybrid cloud deployment model.

Instead of merging public and private clouds, this

cloud uses many public clouds to improve the

reliability of the services.

Advantages- Reduced Latency, High availability

of service.

Disadvantages- Complex, security, issue.

Cloud Infrastructure

It is the need of the hour to reduce the risks and

cost associated with business, it is becoming at

the same time vital to increase the agility and

quality of the IT infrastructure by consisting of

the following :-

Management Software-

It helps the infrastructure to be

maintained and configured.

Deployment Software-

It helps the application to be

deployed and integrated on the cloud.

Hypervisor

It is a low-level program or firmware that acts as a Virtual Machine

Manager (VMM).

Network-

It is the key component

that allows the users to

connect cloud services

over the internet

Server-

It offers many

services as allocation,

monitoring, de-allocation

by helping to compute

the resource sharing.

Storage-

It makes

cloud computing more

reliable by keeping

multiple replicas of

storage.

Cloud Computing

185

YCT

Types of Hypervisor

1. Type 1 Hypervisor- It is also called bare-metal or

native. It is a layer of software installed directly on

top of a physical server. It is mainly found in

enterprise environment.

Pros

Cons

Example

VM (Virtual

Machine)

Mobility

Limited

functionality

VMware,

vSphere with

Security

Complicated

Management

ESX/ESXi,

Oracle VM,

Microsoft

Hyper-V, Lynx

Secure

Resource over

allocation

Price

2. Type 2 Hypervisor- It is also called hosted

hypervisor which is installed and run inside the

physical host machine's operating system. It is

found in environments with a small number of

servers.

Pros

Cons

Example

Easy to manage

Less flexible

resource

management

Oracle VM

VirtualBox,

VMware

Workstation

Pro/ VMware

Fusion

Convenient for

testing

Performance

Allows access

to additional

productivity

tools

Security

GRID COMPUTING

To accomplish a joint task, a grid is made up of a

number of resources and layers or distributed

architecture of various computers connected by

networks. On a network, all machines collaborate

under a common protocol because all tasks are

difficult for a single machine to handle.

A grid computing network consists of three types

of machine names- Control node, Provider, and

User and layers names- Lower layer, Middle

layer and Upper layer.

A grid computing works like the following

figure.

Control node is also known as server.

Provider is also known as grid node.

User

Grid

Node

Control

Server

Java client

.Net client

Task

C++ client

For the efficient execution, grid computing breaks down

each task into small fragments and each fragment is

processed parallel. For example.

A = (4 × 7) + (3 ×8)+(2×9)

Step 1: A = 28 + (3 × 8)+ (2 ×9)

Step 2: A = 28 + 24 + (2 × 9)

Step 3: A = 28 + 24 + 18

Step 4: A = 70

Advantages of Grid Computing-

All machines with various operating systems can

use a single grid computing network.

Across different physical locations, the tasks can

be done or processed parallel while users don't

have to pay money for them.

Servers are not needed because it is not

centralized.

Disadvantages of Grid Computing

For some applications, licensing may make it

restrictive.

Many groups are reluctant with sharing

resources.

O

The grid software is still in the involution stage.

Cloud Computing

186

YCT

Key Components of Grid Computing

Workload & Resource

Data Management

User Interface

Security

Schedulor

Types of Grid Computing

Computational

Collaborative

Manuscript

Modular

Data Grid

Applications of

Grid Computing

Life Science

Engineering-oriented

applications

Data-Oriented

applications

Scientific research

collaboration

Commercial

applications

Grid computing is important for several

reasons as efficiency, cost, and flexibility in the

financial services, gaming, engineering and

entertainments.

Cluster Computing

A cluster is a type of parallel or distributed

processing system, which consists of a collection

of interconnected stand-alone computer working

together as a single, integrated computing, A

cluster generally refers to two or more computers

(nodes) connected together.

Cluster computing is important to resolve the

demand and process services in a faster way. It

ensures the computational power to be always

available. It gives a single strategy as it is

inexpensive, unconventional to the large server.

Applications of Cluster Computing

Weather forecasting

Flight simulation

Earthquake simulation

Image rendering

Petroleum exploration

Various e-commerce applications

Advantages of Cluster Computing-

> Cost effectiveness

> Processing speed

> Improved flexibility

> High performance

> Easy to manage

> Expandability

> Scalability

> Availability

Disadvantages of cluster Computing-

> High cost due to its high hardware and its

design.

> Problem in finding bugs or faults.

> More space is needed to manage and monitor

the infrastructure may increase.

Types of Cluster Computing

1. High availability (HA) Clusters- It is used

to face failure issues. It is also called

failover cluster. In this cluster, services and

applications may be made available to

different nodes if a node declines.

2. Load-balancing Clusters- It allocates all

the incoming traffic or request resources

among several nodes that run the equal

machines and programs having similar

content. In this cluster, services or requests

are distributed amongst all the nodes if a

node declines.

3. High Performance (HP) Cluster- It is

designed to take benefit of the parallel

processing of all nodes. It utilizes super

computers to resolve computational

problems.

4. High Availability + Load Balancing- The

combined performance of high-availability

and load balancing clusters provides an ideal

solution. This cluster is generally used for

FTP server, web, news and e-mail.

Cloud Computing

187

YCT

Classification of Cluster

1. Open Cluster- This type of cluster causes

enhanced security concerns and needed by

every node accessed through the web or

internet.

2. Close Cluster- It is good for

computational tasks and needs fewer IP

addresses. This type of cluster provides

increased protection to the nodes that are

hidden behind the gateway node.

Cluster Computing Architecture

It is a group of workstations or computers

connected via speed interconnections.

These workstations work together as a

single, integrated computing resources,

that are designed with arrays. A node

having input and output functions,

memory, an operating system, works either

with a single or a multiprocessor.

Two or more nodes are generally

connected to a single line.

Every node might be connected

individually through a LAN network.

Parallel Applications

Sequential Applications

Parallel Programming Environment

Cluster Middleware

Work

station1

Work

station2

Work

station3

Work

station4

Work

station5

Work

station6

Communication Switch

Types of Clustering

Hierarchical Clustering

Partitioning Clustering

Agglomerative

Divisive

K-means

Fuzzy C-means

1. Hierarchical Clustering- Hierarchical clustering

has a bottom up approach if it uses a tree-like

structure in agglomerative clustering.

A

B

C

It begins with each element as a separate

successively more massive clusters :-

a

b

c

d

e

f

bc

de

def

bcdef

abcdef

Hierarchical clustering has also a top-down approach

if it uses top-down tree like structure. It begins with the

whole set and proceed to divide it into success cluster.

Cloud Computing

188

YCT

abcdef

bcdef

bc

def

de

a

b

C

d

e

f

2. Partitioning Clustering- This clustering is divided

into two sub-types, first one is K-means clustering

and second one is Fuzzy C-means.

The objects are divided into many clusters

mentioned by the number 'K' in K-means

clustering. It is divided into two clusters C1 and C2

but both have the similar characteristics.

C2

C1

While in Fuzzy C-means clustering, objects

have the similar characteristics but a single object

cannot belong to two different clusters because it is

very similar to K-means.

Example-

(i) A cricket game having runs scored by the player

and wickets taken by the players.

(ii) Academic performance

(iii) Diagnostic systems

(iv) Wireless sensor networks

(v) Search engines

How does K-Means Clustering work?

K-Means clustering works like following

flowchart :-

Start

Converge

Elbow point (k)

If clusters

are stable

Measures the distance

Grouping based on

minimum distance

If clusters

are unstable

+

Reposition the centroids

-

DBSCAN- In image processing, machine learning,

data-mining and other fields are widely used by

DBSCAN. DBSCAN is a data clustering algorithm

based on density. It is widely used with the

increasing size of clusters. It is also used for

applying new data partitioning and merging

method, by using KD tree Get neighbours query.

OPTICS- It is similar to DBSCAN. It is useful for

identifying clusters of different densities. It is also a

data clustering algorithm based on density. OPTICS

extracts the clustering structure. This algorithm

builds a density representation by creating core

distance and reach-ability distance.

STING- It is a statistical information grid-based

approach which follows a hierarchical approach to

divide the spatial area into rectangular cells similar

to a quadtree. This approach separates the high

level cells into multiple smaller cells which can be

simply computed and stored.

CLIQUE- It is a grid based density based

technique or algorithm. In grid based algorithm, the

CLIQUE divides the space of distance into a grid

structure, while in density based algorithm, a

cluster is a maximal set of connected dense units in

a subspace. With respect to the value of records,

this algorithm is very scalable.

Advantages of CLIQUE- DBSCAN, K-Means and

Farthest First are outperforms in accuracy and

execution time by CLIQUE algorithm. It is one of

the simplest methods which is able to find clusters

and any number of clusters.

Disadvantage of CLIQUE- The estimation will

take place and correct clusters will not be able to

find if the size of the cell is unsuitable for a set of

high values.

Cloud Computing

189

YCT

Beowulf Cluster

It is a multi-computer architecture consisting of

multiple client nodes and a single server connected

through internet. The word "Beowulf" is originated

from an old English poem having the same name. A

group of identical and commodity grade computers

is called Beowulf cluster. This cluster differs from

others in its behaviour of working on many

operating systems-

V Kerrighed

V MOSIX

v DragonFly BSD

V Rocks Cluster Distribution

V PelicanHPC

v Cluster knoppix

A Beowulf cluster have the following

characteristics-

v A private network with dedicated processors, and

easy replication for multiple vendors.

It is a free and open source software scalable

with Input-Output and no custom components.

It is an Apache open source framework. It is

written in java that allows distributed execution

using programming models. The hadoop's

environment provides distributed storage and

computation across computer clusters. By the help

of two major layers, it is designed to scale up from

a single server to thousands of servers. Its two

layers are -

(i) Computation/processing layer (MapReduce)

(ii) Storage layer (HDFS)

The main purpose of hadoop is, it utilizes a large

cluster of commodity hardware to keep and store

big size data by working on MapReduce

programming algorithm. For example- Yahoo,

Facebook, eBay, Netflix are using hadoop in their

organization to deal with big data.

The hadoop consists of the following mainly four

components:

1. MapReduce- It is like a data-structure or an

algorithm. MapReduce performs the

distributed processing in parallel in a hadoop

cluster to work so fast. It has only two phases

namely Map and Reduce that are utilized. Any

big data are inputted, they go through Map and

Reduce phases until they got executed in

output form. Map function breaks the data

blocks (big data input) into tuples which works

as input to Reduce function. Then the Reduce

function combines the tuples into set of tuples

and performs summation and sorting type jobs.

Finally they are sent to the output terminal in

the output format.

Map()

Big

Data

Input

Reduce()

Map()

Output

Reduce()

Map()

Map function does many tasks as

RecordReader, Combiner, Partitionar, etc and

Reduce function also does many tasks as

shuffle and sort, Reduce and Produce output

format.

2. HDFS- HDFS stands for Hadoop Distributed

File System. It works on commodity hardware

and utilizes storage permission. It is used to

store data in large chunk of blocks to the

following two nodes-

(a) NameNode (Master)- It is used to guide

the Datanode (slaves) because it works as a

master in Hadoop cluster.

Cloud Computing

190

YCT

(b) DataNode (Slaves)- It is used to utilize or

store the data in Hadoop cluster because it

works as a Datanode.

3. YARN- It is a framework on which

MapReduce works. YARN works two

operations- Job Scheduling and Resource

Management. Job scheduler divides a big task

into small jobs and Resource management

manages all the resources that are made

available for running Hadoop cluster. YARN

performs its tasks by using many features-

as Multi- Tenacy, Scalability, Compatibility

and cluster Utility.

4. Hadoop Common- It is also known as

common utility used by HDFS, MapReduce

and YARN. Hadoop common utilities are Java

files or Java library or Java script needed for

other components. It solves the hardware

failure if it occurs in hadoop framework.

Advantages of Hodoop

Hadoop has an ability to store large amount of

data.

Hadoop has high flexibility and high

computational power.

Hadoop's tasks are independent i.e. open source.

It has linear scaling.

Disadvantage of Hadoop

Hadoop is not more effective for small data.

Hadoop has hard cluster management and

stability issues.

Hadoop concerns the security.

Hadoop has complexity, latency, limited support

for real time processing and limited support for

structured data.

Hadoop has data security, limited support for Ad-

hoc queries, for graph and machine learning.

Oozie

It is a Java web application used to schedule

hadoop jobs. Multiple jobs are combined

sequentially into one logical unit of tasks by

oozie. For Hadoop, oozie is a workflow scheduler

that permits users to create Directed Acyclic

Graphs of workflow.

Oozie consists of two parts :-

(a) Workflow engine- It is responsible to run

and store workflows of Hadoop jobs as

MapReduce, Hive and Pig. If workflow

engine specify a sequence of actions to

execute, then workflow job has to wait.

(b) Coordinator engine- Based on predefined

schedules and data availability, coordinator

engine runs workflow jobs.

Success

Begin

Start

MapReduce

Program

Notify

Client of

Success

End/Stop

Successful

completion

Error

Notify client

of error

Kill

unsuccess

termination

Oozie can manage the lifecycle of the jobs and

timely execution of thousands of workflows.

Anyone can easily start, stop, suspend

(terminate) and re-run the jobs as oozie is very

much flexible and it has command line interface

as well as client API.

Mahout

The name mahout came from Apache Hadoop

which uses an elephant's logo. A Mahout is one

who drives an elephant. It is an open source

project also. Many popular machine learning

techniques such as classification,

Cloud Computing

191

YCT

recommendation and clustering are implemented

by Mahout. Developers are enabled to use

optimized algorithm by highly scalable machine

learning liabrary that is called Mahout.

Mahout contains Java liabraries

for common math algo.

It analyzes large

sets of data

Features of Mahout

It includes vector and

matrix liabraries.

It offers the coder, a ready to use

framework.

High Touch

It is hands-on for customers who require a lot of

interaction and less reliance on digital

engagement with any company. It is used to boil

down to how frequently the customer can be

contacted.

In other words, to support the customers through

the pre- and post-sale phases, a high touch

model, a human first method is used. It is often

used when a customer needs direct guidance to

navigate a complex process. It includes in-

person-meeting, webinars, video chat, demos and

phone calls, etc.

Benefits of high touch- The main benefits of a

high touch method are that customers feel like

they are receiving special attention and

customers can tap into as much support as they

require.

Characteristics of high touch

> Little to no human interruption during on-

boarding.

> To deliver value on automation tools, heavy

emphasis is occur.

> Executing task and accomplishing goals can

quickly be started by customers.

Low Touch

It is also an on-boarding model or method that is

largely self serve in nature. Low touch model is

opposite of a high touch model. It simply doesn't

have man power or the resources to provide a

high tough experience to each customer so it is

attractive to new, and small companies.

Benefits of low touch- Low touch model takes

very little time out of customer access team's that

is one of the biggest benefits.

Characteristics of low touch-

> Little to no human interruption during on-

boarding.

> To deliver value on automation tools, heavy

emphasis is occur.

> Executing task and accomplishing goals can

quickly be started by customers.

High, Low, No-Touch Partner Program

Segmentation

Strategic Partner

E

888

High touch

Programmatic

Partner

Low touch

Opportunistic

Partner

No-touch

When high-value reoccurs, it is said High touch

customer service. On the other hand, when

company uses automation to digitally engage

with customers, it is called low touch customer

service while neither high-value reoccurs nor

company uses automation to digitally engage, it

is called no-touch customer service.

Cloud Computing

192

YCT