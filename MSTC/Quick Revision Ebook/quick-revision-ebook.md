Computer Science & 
Engineering / Information 
Technology 

CAPSULE 

Quick Revision 
Key Notes, Terms, Definitions and Formulae  

Use Full for :  
• UGC-NET/JRF  /  GATE  /  IES  /  PSU  /  UPPSC  AE/Polytechnic  Lecturer/LT  Grade/ 
NIELIT/ISRO • UPPCL AE • UPRVUNAL AE • UJVNL AE • KVS NVS PGT • DSSSB 
• PTCUL • ASSAM PSC • APPSC • BPSC • CGPSC • GUJRAT SC • HPPSC • UPSC         
• MPPSC • Rajasthan  Basic  Computer  Teacher  •  J&KPSC  •  Kerala  PSC  •  Karnataka 
PSC •  KPCLAE  •  ISRO  Scientist/Engineer  •  OPSC  •  RPSC  •  TNPSC  •  Punjab  PSC           
• Maharashtra  PSC  •  BHEL  ET  •  TANGEDCO  AE  •  TELANGANA  PSC  •  JUVNL 
AEE  •  CIL  MT  •  RRB  SSC  •  SJVNL  ET  •    TSGENCO  AE  •  VIZAG  STEEL  MT             
• TAMILNADU TRB Polytechnic Lecturer  

CHIEF EDITOR  
Anand Kumar Mahajan 
COMPILED & WRITTEN BY 
Computer Science & Information Technology Expert Group 
EDITORIAL OFFICE 
12, Church Lane Prayagraj-211002 
Mob. : 9415650134 
Email : yctap12@gmail.com 
website : www.yctbooks.com 
PUBLISHER DECLARATION 
Edited and Published by A.K. Mahajan printed for YCT Publications Pvt. Ltd.  
and Printed by Lakshmi Narayan Printing Press, Prayagraj.  
In order to publish the book, full care has been taken by the Editor and the  
Publisher, still your suggestions and queries are welcomed.  
In case of any dispute, the Judicial area will be Prayagraj. 

Rs. : 495/- 

 
 
 
 
 
 
 
INDEX 

(cid:1)  Computer Organization and Architecture ...................................... 3-10 

(cid:1)  Data Structures & Algorithm ......................................................... 11-27 

(cid:1)  Discrete Mathematics ...................................................................... 28-35 

(cid:1)  Digital Logic................................................................................. .... 36-49 

(cid:1)  Database Management System........... ............................................ 50-65 

(cid:1)  Theory of Computation ................................................................... 66-78 

(cid:1)  Compiler Design ............................................................................... 79-85 

(cid:1)  Operating Systems ......................................................................... 86-103 

(cid:1)  Computer Networks ..................................................................... 104-119 

(cid:1)  Programming in C & C++ .......................................................... 120-141 

(cid:1)  Web Technology ........................................................................... 142-156 

(cid:1)  Software Engineering .................................................................. 157-180 

(cid:1)  Cloud Computing ......................................................................... 181-192 

2 

 
 
 
 
 
 
   01.   Computer Organization and 
 Architecture 

(cid:1)  Von  Neumann  Architecture  (Stored  Memory 

   Bus Arbitration–The overall control which decides 

Program) 

who will control the master bus line. 

Logic

(cid:1)  Various General Purpose Registers– 

• Address Register 
• Data Register 
• Accumulator 
• Program Counter 

• Instruction Register 
• Temporary Register 
• Input Register 
• Output Register 
Type of Bus– There are three type of Bus. 
• Address Bus 
• Data Bus 
• Control Bus 

There are two approaches to bus arbitration. 
• Centralization bus arbitration 
• Distributed bus arbitration 

  Register– 

1. Memory  Address  Register  (MAR)  hold  on 

address of the memory unit. 

2. PC–Program Counter 
3. IR–Instruction Register 
4. R–Processor Register 
Computer register are designated by capital letters. 
Register Transfer– R2 ← R1 
5. DR – Data Register 
Bus and Memory Transfers– 

  Common Bus- It consists of a set of common lines 
one for each bit of a register  through  which binary 
information is transfered one at a time. 
  Control  Signal–Determine  which 

is 
selected  by  the  bus  during  each  particular  register 
transfer. 
Bus System for four Register– 
•  In  general  bus  system  will  multiplex  K  register 
of n bits each to produce an n-line common bus. 
•  The  number  of  multiplexers  needed  to  construct 
the  bus  is  equal  to  n,  the  number  of  bits  in  each 
register. 

register 

•  The size of each multiplexer must be K×1 since it 

multiplexer K data lines. 

•  The  address  bus,  which  is  a  unidirectional  path 
way that allows information to travel in only one 
direction,  carries  information  about  where  data 
will be stored in memory. 

•  The  data  bus  is  a  bidirectional  path  way  that 
carries  the  actual  data  (information)  to  and  from 
the main memory. 

•  The  control  bus  carries  the  control  and  timing 
signals  needed  to  coordinate  the  activities  of  the 
entire computer. Think of this as a traffic cop. 

Bus Transfer–  

Bus ← R2, R1 ← BUS 

  ⇒ R1 ← R2 

Computer Organization and Architecture 

3 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  Memory Transfer– Read : DR ← M[AR] 
Write : M[AR] ← R1 

  Where, 

DR → Data Register 
AR → Address Register 

  Micro-operations– Micro-operations classified into 
four  categories  Address  Register  ←  Program 
counter 
1. Register Transfer Micro-operations 
2. Arithmetic Micro-operation 
3. Logic Micro-operation 
4. Shift Micro-operation 
 Register  Transfer  Micro-operations-  These  type 
of  micro  operations  are  used  to  transfer  from  one 
register to another binary information. 

• Right shift 

  Arithmetic  shift–  Applied  on  signed  number  after 
the shift sign of the number should remain same. 
Left  shift–  It  is  same  as  logical  left  shift  but  it  is 
allowed only when sign is not going to change. 

Example– 

  Arithmetic Micro-operation 
1. Addition – R3 ← R1 + R2 
2. Subtraction – R3 ← R1 – R2 
← +

2

R

5. Increment – 

4. 2's complement – 

3. 1's complement – 

+  
R R 1
1
R←  
2
← +  
R 1
2

3
2R
2R
← +  
R 1
1
← −  
R 1
1
          Arithmetic shift – The increment and decrement 
micro operations are implemented with a binary up-
down counter. 
Logic micro operation– 
1. OR – 

6. Decrement – 

← ∨
R

1
R

R

R

R

1

1
R

1

2. AND – 

3. XOR – 

R

1

4. Compliment – 

5. X-NOR – 

R

R

1
3
← ∧
R
R
2
3
← ⊕  
R
2
3
R←  
1R
← ⊙  
R
R
2
3

1

Shift Micro operation– 
• Logical shift 
• Circular shift (Rotation) 
• Arithmetic shift 
Logical Shift– There are two types 
• Left shift 

Example–

1011

→

1 0 1 1 0
×

=

0 1 1 0

• Right shift. 

Example– 

1011

→

0 1 0 1 1
×

=

0 1 0 1

  Circular shift– There are two types 

• Left shift 

  Right shift– 

(cid:1)  Instruction format– 

•  A  group  of  bits  which  instructs  computer  to 
perform some operation. 
ISA  (Instruction  Set  Architecture)  Collection  of 
all instruction CPU supports. 
Type of Instruction (Based on Operation) 
• Data Transfer – MOV, LDI, LDA 
• Arithmetic & Logic – ADD, SUB, AND, OR 
• Machine Control – EI, DI, PUSH, POP 
• Iterative – LOOP, LOOPE, LOOPZ 
• Branch – JMP, CALL, RE T, JZ, JNZ 
Type  of 
Instruction 
Information) 
• 4-Address Instruction 
• 3-Address Instruction 
• 2-Address Instruction 
• 1-Address Instruction 
• 0-Address Instruction 

(Based  on  Operand 

Types  of  CPU  Organization–  The  number  of 
address  fields  in 
the  instruction  format  of  a 
computer  depends  on  the  internal  organization  of 
the registers. 
There are three types of organization. 
1. Single Accumulator Organization 
2. General Register Organization 
3. Stack Organization (LIFO) 

1.   Single 

Accumulator  Organization– 

The 
instruction format in this type of computer user one 
address field. 

Example–  
  ADD × AC ← AC + M[X];  
  AC → Accumulator Register 
2.   General  Register  Organization  uses  three  and  two 

address instructions. 

Computer Organization and Architecture 

4 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
            
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Example– 
  ADD R1, R2, R3 = R1 ← R2 + R3 
  ADD R1, R2 = R1 ← R1 + R2 

3.  Stack  Organization  uses  zero  and  one  address 
instruction. 

Example–(i) PUSH (ii) ADD 

In  a  general  register  CPU  organization  there  are 
eight general purpose register and ALU can perform 
32-different operation. 
The number of selection line of each multipliers for 
selecting the operand = 3 (23 =8)  
The number of bits in operation code= 5(25 = 32) 
The length of the control word = 5 + 3 + 3 + 3 = 14 
(for 3-address instruction) 
Addressing Mode 

The  way  of  operand  are  choosen  during  program 
execution  is  dependent  on  the  addressing  mode  of 
instruction. 
The addressing mode may reduce the number of bits 
in the addressing field of the instruction. 
Instruction  Cycle–  CPU  performs  6  phases  to 
execute an instruction. 

Fetch cycle – Instruction fetch 
Execution cycle – from decode ...... to write back 
Type of addressing mode– 
•  

Implied  Mode–  Operand  is  specified  Implied 
in the definition of instruction.  
Used for zero address and one address instruction. 
Immediate  Mode–  Operand 
is  directly 
provided as constant. 
No  computation  required  to  calculate  effective 
address. 

•  

•  Register  Mode–  Operand  is  present  in  the 

register. 
Example–  LDR1 ⇒ AC ← R1 
Register number is written in instruction. 
•   Register  Indirect  Mode–  Register  contains 
address of operand rather than operand itself. 
Example– LD (R1) ⇒ AC ← M[R1] 

•  Auto 

Increment  or  Auto  Decrement 
Addressing  Mode–  Special  case  of  register 
indirect addressing mode. 
Example–  
LD(R1) + ⇒ AC ←M[R1], R1 ← R1 + 1 

•  Direct 

Addressing  Mode 

(Absolute 
addressing  mode)–  Actual address is  given in 
instruction. 
Use to access variables 
Example– LD ADR ⇒ AC ← M[ADR] 
Indirect Addressing Mode– 
Using 
parameters. 
2 memory access required. Where the effective 
address is stored in memory. 

implement  pointers  and  passing 

to 

• 

Example– LD@ADR ⇒ AC ← M[M[ADR]] 

•   Relative  Address  Mode–  In  this  mode  the 
content of the program counter (PC) is added to 
the  address  part  of  the  instruction  in  order  to 
obtain the effective address. 
Example– LD$ADR ⇒ AC ←M[PC + ADR] 
#  Relative  addressing  is  often  used  with 
branch-type instruction. 

•  Base  Register  Mode–  Used 

in  program 

relocation of programs in memory.   

(cid:1)  Indexed Addressing Mode–  
  → Use to access or implement array efficiently. 
  → Multiple Registers required to implement. 
  →  Any  element  can  be  accessed  without  changing 

instruction. 
Example– 

 LD AD R(x) ⇒ AC ← M [ADR + X] 

Arithmetic Logic Unit (ALU) 
(cid:1)  Inside  a  computer,  there  is  an  (ALU)  which  is 
capable of performing logical operations (e.g AND, 
OR,  Ex-OR,  Invert  etc.)  in  addition  to  arithmetic 
operation  (Addition,  Subtraction  etc.).  The  control 
unit  supplies  the  data  required  by  the  ALU  from 
memory or from input devices and directs the ALU 
to  perform  a  specific  operation  based  on  the 
instruction fetched from memory. 

Cache Memory 

Cache memory faster than main memory.  

  Cache hit– It required element present in cache that 

called cache hit. 

  Hit  latency–  Time  taken  to  find  out  whether 
element present on the cache or not that is called hit 
latency. 

  Cache  miss–  It  required  element  not  present  in 

cache, that is called 'Cache miss'. 

Computer Organization and Architecture 

5 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  Miss  latency–  Time  taken  to  get  something  from 
main  memory  and  then  place  it  into  the  cache  and 
then read that's called miss latency. 
Page  hit–  It  required  element  present  in  main 
memory. 
Page fault– It required element not present in main 
memory. 
Tag  directory–  Tag  directory  say  that  required 
element present in tag on not. 
(cid:1)  Introduction to Direct mapping–  

• Taking  about  disk  and  main  memory  we  talking 

about paging. 

• Talking about Cache and main memory we talking 

about blocks. 

• Block size = lines size. 

6

=0111

•  Smallest  addressable  unit  in  the  memory  called 
word. 
Let's 
1w = 1B (means system is byte addressable) 
  Block size = 4 word 

  No. of  black in main memory = 128/4 = 32 block 
  No. of Lines in Cache = 16/4 = 4 lines 

Physical address contain = 128 = 27 = 7 bits 
Processure generate address = 

Offset
00 20
01 21

10 22
11 23

Example–  

Main memory size = 128 KB 

  Cache size = 16 KB 
  Block size = 256 B 
  Tag bits = 3 bit 
  Tag directory size = ?  

Solution – 

 Main memory size 128 KB 
= 210 *128 B 
= 210 *27 B 
= 217 B 
Computer Organization and Architecture 

Block size = 256 B = 28 B 

No. of Block 

=

=

9
2 bit

17
2

8
2

Cache size = 16 KB = 214 b 

Offset

  Number of line 

Cache size
Block size
Tag directory size = (Tag size * No. of lines) 

6
2 bit

8
2

=

=

=

14
2

= (3*26) bit 

(cid:1)  Fully  Associative–  The  associative  memory  stores 
both  the  address  and  content  (data)  of  the  memory 
word.  This  permits  any  location  in  cache  to  store 
any word from main memory. 

Offset

Block no. = 32 = 25 = 5 bit 
Block offset = 4 = 22 = 2 bit 

(cid:1)  Set-Associative  Mapping–  The  set  associative 
mapping is an improvement over the direct mapping 
in  that  each  word  of  cache  can  store  two  or  more 
word of memory under the same index address. 

Total number of set 

=

  K is number of way 
Example–  

No.of lines
K

4 way set associative cache lines = 128 
Lines size = 64 word 
Physical address = 20 bits 
Tag, set and word field are? 

Solution– 

  Number of lines 

=

Cache size
Lines size

6 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Cache size = 26 * 27 = 213 word 

Sets 

=

Lines
Set size

=

7

2

2

2

5

=

2

Tag = 9, Set = 5, Word = 6 

(cid:1)  Locality of Reference– 
1. Spatial locality 
2. Temporal locality    
• If a word is accessed now then the word adjacent 
to it (close proscimity) will be accessed next. 
•  Keeping  more  words  in  a  block  affects  spatial 
locality (block size). 
•  If  a  word  is  referenced  now  then  the  same  word 
will be referenced again in future. 
• LRU is used in temporal locality. 
(cid:1)  Cache Replacement Algorithms– 

•  Replacement  policy  is  required  for  associative 
mapping  and  set  associative  mapping  but  not  for 
direct mapping. 
• Replacement policies are aimed to minimize miss 
Penalty for future references. 

Example–  Consider  the  cache  has  8  blocks  for  the 
memory  reference  (5,  12,  13,  17,  4,  12,  13,  17,  2, 
13, 19, 13, 43, 61, 19). What is the hit ratio for the 
following cache replacement algorithms. 
(i) FIFO 
(ii) LRU 
(iii) Direct mapping 
(iv) 2-way set associate 

(i)  FIFO 





M
5,

M
12,

M
13,

M
17,

M
4,

H
12,

H
13,

H
17,

M
2,

H
13,  

M
19,

M
13,

M
43,

M
61,

H
19





  Hit ratio 

  Miss 

=





=




10
15

5
15

×

100

×

100





=




2
= ×
3

100
3

=

33

1
3

100

=

66

2
3

(ii)  LRU 





M
5,

M
12,

M
13,

M
17,

M
4 ,

H
12,

H
13,

H
17,

M
2 ,

H
13,  

M
19,

H
13,

M
43,

M
61,

H
19





, 12 , 13 , 17 , 4 , 12 , 13 , 17 , 2 , 13 , 19 , 13, 

5(
43, 61, 19) 




=

  Hit ratio 

6
15

×

100

=

40





  Miss 

=

9
15





×

100

=

60





(iii) 
M 


5,  

M
19,








H
13,

M
5,

M
12,

M
13,

Direct 
M
M
M
12,
4,
17,

mapping 

M
13,

M
17,

M
2,

M
13,  

M
43,

M
61,

M
19





Line number = B.No mode 4 

Cache hit ratio 

=

1
15





×

100





=

6.66

  Miss ratio 

=

14
15





×

100





=

93.333

(iv) 2-way set associate 
17
4
12
H,
M,
M,

17
M,

12
H,

13
M,

13
H,

2
M,

13
H,  

5
M,




19
M,

13
H,

43
M,

61
M,

19
M





Line no. = (i mod 2) 

i → Block number 

  Hit ratio 

=

5
15





×

100





=

33.33

  Miss ratio 

=

10
15





×

100





=

66.66

Computer Organization and Architecture 

7 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Control Processing Unit 
  CPU  Control  Design–  There  are  two  major  types 

of control organization. 
(i) Hardwired Control 
(ii) Micro programmed control  

  Hardwired  Control  Unit–  Control 

is 
implemented  with  gates,  flip-flops,  decoders  and 
other digital circuits. 

logic 

Difference 
Programming and Vertical Micro Programming 

Horizontal 

between 

Micro 

Horizontal Micro 
Programming 

Control Word Large 

Vertical Micro 
Programming 

Control  word 
small 

is 

Parallelism is high 
Faster 

No parallalism 
Slower 

1. 

2. 
3. 

  Advantage–  Can  be  optimized  to  produce  a  faster 

mode of operation. 

Difference between Hardwired Control Unit and 
Micro Programming Unit 

  Disadvantage–  Rearranging 

the  wires  among 

various components is difficult. 

Hardwired 
Control Unit 

Micro Programming 
Unit 

1.  Fixed Instruction 
2.  High speed 

3.  Expensive 
4.  Complex 

Example– 
Intel 
8085,  Motorola 
6802  Tilog  80  and 
Reduce 
any 
Instruction 
Set 
Computer (RISC) 

Instruction can flexible 
Slower 
compared 
hardwired instruction 

to 

Relatively cheap 
Simple 
Example–  INTEL  8080, 
Motorola  68000  and  any 
complex 
instruction  set 
computer. 

Difference between RISC and CISC 

RISC 
number 

Less 
instruction 

of 

CISC 
number 

More 
instruction 

of 

Fixed length instruction 

Simple Instruction 
Limited addressing 

Easy  to  implement  using 
hardwired control unit 

length 

Variable 
instruction 
Complex Instruction 
More 
& 
addressing modes 

complex 

Difficult 
using hardwired 

to 

implement 

One cycle per instruction  Multiple 

cycle 

per 

Register 
register 
to 
arithmetic operation only  

instruction 

Register  to  memory  & 
memory 
register 
to 
operations 
arithmetic 
possible 

More number of registers  Less number of registers 

Example–  Consider  the  following  processor  design 

characteristics. 
(i) Register to register arithmetic operation only 
(ii) Fixed length instruction format 
(iii) Hardwired control unit 

  Which  of  the  characteristics  above  are  used  in  the 

design of a RISC processor? 
(a) i and ii only 
(c) i and iii only 

(b) ii and iii only 
(d) i, ii and iii 

(cid:1)  Micro-Programmed Control Unit– Control Logic 

is implemented with micro programmed. 

  Advantage–  Updating  the  control  logic  is  easy. 
Disadvantaged–  Slower  than  hardwired  control 
unit. 

Control Word Sequencing 

Example–  CPU  has  64  distinct  instructions  each 
takes  8  micro  operation  micro-

instruction 
instruction– 
(i) Signals (128 bits) 
(ii) Mux select [16 mux inputs] 
(iii) Address 

  What is size of control memory? 
Solution– Total micro operations = 64*8 
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

Computer Organization and Architecture 

8 

YCT 

 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
IO Organization 

Peripheral Device– Devices connected to processor 
externally are known as peripherals. There are three 
type–  
• Input Devices 
• Output devices  
• Storage devices 
Input/Output Subsystem Of Computer– Provides 
an  efficient  mode  of  communication  between 
control system & outside word. 
Input/Output  Interface–  Provides  a  method  for 
transferring  information  between  internal  storage 
(memory & registers) & external I/O devices. 

• Serial and Parallel Transmission 
(i) Serial Transmission 

(ii) Parallel Transmission 

Difference between Serial and Parallel  
Serial 
Need of shift register 

Parallel 
No  need  of  shift 

register 

Burst errors 

Bit errors 

Costless 
More reliable 

Cheaper 
Less reliable 
Used to more distance  Used 

to 
distance 
  Asynchronous Transmission– Data 

less 

 is  sent  in 
form  of  byte  or  character.  This  transmission  is  the 
half-duplex  type  transmission.  In  this  transmission 
start bits and stop bits are added with data. 
Example– 
• Email 
• Forums 
• Letters 
Synchronous  Transmission–  Data  is  sent  in  form 
of  blocks  or  frames.  This  transmission  is  the  full-
duplex 
receiver, 
synchronization is compulsory. 

type.  Between 

sender  and 

Example– 

• Chat rooms 
• Telephonic conversations 

Example- 
  How  many  8  bit  characters  can  be  transmitted  per 
second 
serial 
communication  link  using  a  parity  synchronous 
mode of transmission with 1 start bit, 8 data bits, 2 
stop bits and 1 parity bit. 

(bits/sec) 

9600 

baud 

over 

Solution– 

For 1 char = 1 + 8 + 2 + 1 = 12 bits 

Characters transmitted 

=

9600
12

=

800 char / sec

(cid:1)  Mode of transfer– 3-way to perform I/O 

• Programmed I/O 
• Interrupt driven I/O 
• DMA 
Programmed I/O  
{1. Read the status flag. 
2. It data is not available (status = 0) then go to step 
1. 
3. Move the data}  
• Waste time processor 
• Mostly devices time to transfer 1 byte. 

(cid:1)  Interrupt Initiated IO– 

•  IO  device  has  a  provision  (interrupt  signal)  to 
inform to CPU about communication 

  When CPU receives interrupt– 

• It completes execution of current instruction  
• Saves the status (PC, PSW etc.) of current process 
onto the stack 
• Branches to service the interrupt 
•  Resumes  the  previous  process  by  taking  out  the 
values from stack. 

(cid:1)  DMA (Direct Memory Access) 

•  Enables  data  transfer  between  I/O  and  memory 
without CPU intervention. 
• Need a hardware : DMAC 
Starting Address – Memory Address starting from 
where data transfer should be perform. 

  Data Count– No of bytes or word to be transferred. 

(cid:1)  Modes of DMA Transfer 

• Burst mode (all data transfer at the same time) 
• Cycle stealing (it happen word by word) 
•  Interleaving  DMA  (Whenever  CPU  does  not 
require  system  buses  (doing  internal  work)    then 
only control of the buses given to DMAC). 

Computer Organization and Architecture 

9 

YCT 

 
 
 
 
 
 
  
 
 
  
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
(cid:1)  Flynn's Classification of computer 

•  SISD–  Single  Instruction  Stream,  Single  Data 

n = 500, K = 5, tp = 15 
processing time of pipeline = (K + n – 1)tp 

Stream 

Example– Von-neamann 
•  SIMD–  Single  Instruction  Stream,  Multiple  Data 

Stream 

Example– Pipeline processor   
•  MISD–  Multiple  Instruction  Stream,  Single  Data 

Stream only hypothetical 

•  MIMD  –  Multiple  Instruction  Stream,  Multiple 

Data Stream 

Example–  Multiple  Pipelines 

(Super  Scalar 

Computer (ILP)) 

(cid:1)  Pipelining 

•  Pipelining  is  useful,  when  same  processing  is 

applied over multiple inputs. 

• Technique to decompose a sequential process into 

sub-operations. 

• Sub-operations performed in all segments. 
• Task: one operation performed in all segments. 

(cid:1)  General Consideration about pipeline 

•  Consider  a  K  segment  pipeline  with  clock  cycle 

time = tp to perform n tasks. 

Time required to perform 1st task = K*tp 
Time  required  to  perform  remaining  (n  –1)  tasks  = 

(n–1)tp 

Time required for all n tasks = (K+n–1)tp 
(K + n – 1) is total cycle. 
•  Consider  a  non-pipeline  system  that  takes  tn  time 

to perform a task 

Time required for n task = n*tn 
•  Performance  of  a  pipeline  is  given  by  speed  up 

ratio. 

Speed up ratio 

=

−

Non pipeline time
Pipeline time

S

=

n * t
n
)
K n 1 t
+ −

(

p

as the number of task increases, n>>K (Ignore K–1) 

S

ideal

=

t
t

n

p

Latency– Time after machine takes next input. 
• Latency in non-pipeline = tn   
• Latency in pipeline = tp 
Throughput–  No  of  input  processed  per  unit  of 

time  

=

n
) p
K n 1 t
+ −

(

Ideal case– 

Throughput

=

1
t

p

= (5 + 500 – 1)15 
= 504 × 15 
= 7560 n sec 

(cid:1)  Instruction Pipeline 

If pipeline processing is implemented on instruction 
cycle. 
IF : Instruction fetch 
ID : Instruction decode & Address calculation 

  OF : Operand Fetch 
EX : Execution 
  WB : Write Back 
6
3
I1 IF ID OF EX WB

4

1

2

5

7

8

9

10

11

12

13

14 15 16

IF

I2
I3
I4

I5
I6

I7
I8

ID OF EX WB
ID OF
IF
IF

ID OF

EX WB

EX WB

IF

−

−

IF

ID OF EX WB

I9
  Assume  in  cycle  number  5,  I4  decoded  as  branch 

ID OF EX WB

IF

instruction. 
By  standard    ⇒  Branch  decision  is  made  in 
'Execution' phase. 
•  After  execution  phase  next  instruction  can  be 

fetched. 

  Actually only instruction executed (n = 6) K = 5 for 

n input, no. of cycles = K+ n – 1 

        = 5 + 6 – 1  
       = 10 

3 cycles are extra (stall cycles because of branch) 
Total = 10 + 3 = 13 cycles 
Total execution time = cycle * tp 

(cid:1)  Pipeline Hazards– Situations that prevent  the  next 
instruction  from  being  executing  its  designated 
clock cycle. 
• Hazard lead to have stall cycles  
There are three type– 
1. Structural Hazard/Resource Conflict 
2. Data Hazard/Data Dependency 
3. Control Hazard/Branch difficulty 
Structural  Hazard–  When  multiple  instruction 
need same resource. 

  Control  Hazard–  All  Instruction  who  change  the 
program counter leads to control hazard because of 
branch instruction. 

  Data Hazards Classification– 

•  RAW 

(Read  After  Write) 

[Flow/true  data 

dependency] 

Example–  Consider  a  5  stage  pipeline  with  cycle  time 
of  15  ns.  Calculate  processing  time  of  pipeline 
for 500 tasks. 

• WAR (Write After Read) [Anti Data dependency] 
•  WAW 
[Output  data 

(Write  After  Write) 

dependency] 

Computer Organization and Architecture 

10 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
 
 
 
 
 
 
 
   
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   02. 

DATA STRUCTURE AND 
 ALGORITHM 

DATA STRUCTURE 
Data- Data is a collection of raw, unorganized facts and 
details  like  text,  observations  figures,  symbols,  and 
descriptions of things etc. 
Data  can  be  record  and  does  not  have  any  meaning 
unless processed. 
Information-  Information  is  processed,  organized,  and 
structured data. 
Definition  of  data  structure  –  A  data  structure  is  a 
collection of data, generally  organized so that items can 
be stored and retrieved by some fixed techniques.  

Data structure operation 

Insertion- Add a new data in the data structure. 

  Example– 

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

Merging-  Combining  the  data  of  two  different  sorted 
files into a single sorted. 
Example-  

Traversing-  Accessing  Each  data  Exactly  one  in  the 
data  structure  so  that  Each  data  item  is  traversed  or 
visited. 
Example-  

Arrays in Data structure 

Array-  Array  is  a  fixed  size  sequenced  collection  of 
data items of same type.  
• Access a particular element = array name [index] 

= Int a [  ] 

• data items are stored in continuous locations. 
How the data is to be accessed, how  you can calculate      
the address. 

    a[0]=6, a[1]=2, a[2]=4, a[3]=3, a[4]=0    
Formula- 
                Address of a[i] = Base +i * (size of data type) 

i = 0, 1, 2……..(n - 1) 
n = size of array 

                  so if want to,  i = 2; 

Int size   = 4 bit 

= 100+2×4 
= 108  

• Random Access taking Constant time. 

         data- 20, 30, 10, 5, 6       
30 

20 

10 

5 

6 

Searching- Final the location of data in data structure. 
Example-  
6 
a[1] 

30 
a[4] 

20 
a[3] 

5 
a[0] 

10 
a[2] 

• Name [LB:UB]   LB ≤ UB 

                    Search = 10 → a[2] 

Data Structure and Algorithm 

11 

 LB = Lower Bound 
 UB = Upper Bound 

YCT 

 
 
 
 
 
  
 
 
 
         
                   
 
 
       
   
 
  
   
 
 
                  
 
 
 
 
 
 
 
 
 
Operation On Linked List- 
1. Creation - This operation are used to created a linked 
list in this node is created and linked to the Another 
node. 

2. Insertion- This operation is used to insert a new node 

in the linked list. 

3.  Deletion-  In  this  operation,  elements  can  be  deleted 

at the starting of the list. 

4.  Traversing-  It  is  a  process  of  going  through  all  the 
nodes of linked list from one End to the other end. 

Type of Linked List 

•  Singly  Linked  List-  A  singly  linked  list  is  a 
unidirectional  linked  list.  It  is  the  simplest  type  of 
linked list in which every node contains some data and a 
pointer to the next node of the same data type. 

• 
Doubly  Linked  List-    A  doubly  linked  list  is  a 
bidirectional  linked  list  that  contains  a  pointer  to  the 
next as well as the previous node in sequence.  

• Circular Linked List- A circular linked list is that in 
which the last node contains the pointer to the first node 
of the list.  

•  Circular  Doubly  Linked  List-  A  circular  doubly 
linked  list  is  a  mixture  of  a  doubly  linked  list  and  a 
circular linked list. 

Size of array = UB-LB+1 
Consider an array A [6:18]. 

Total number of element in array 
By formula 
       Size of array  = UB – LB+1 

= 18 – 6 + 1 
= 13  

Searching Array– 
•   Searching an array means to find a particular element 
in  the  array.  The  search  can  be  used  to  return  the 
position  of  the  element  or  check  if  it  exists  in  the 
array. 

•   Linear Search 
  Average  
  Best   
  Worst  
•   Binary search 
  Average  
  Best  
  Worth  
• Pointer is an address of another variable 

Time complexity 
O (n) 
O (1) 
O (n) 
Time complexity  
O (log n) 
O (1) 
O (n) 

Example–   

int b = 10; 
int* P;             b 

P 

10 

200 

P = & b; 

200  204 

(cid:1) 2-D Array 
The two-dimensional array can be defined as an array of 
array. 
2D array syntax– 

data type array_name [row][columns]; 

Representation of 2-D Arrays in memory 
Row major order- 

 a [i][j] = B+((i*n)+ j)*size. 

IF start (0,0) 

A [i][j] = [((i-1)*n+(j-1))*size + Base if start (1,1) 

Colom major 

A [i][j] = ((i*m) + i)*size + Base  

Linked List 

A  Linked  list  is  a  Linear  data  structure  in  which  the 
elements are not stored at contiguous memory location. 
•   A liked list is a dynamic data structure. 
•   Each  element  is  called  a  node  which  has  two  part, 
info  part  stores  the  information  and  pointer  part 
which  point to the next element.   

Data Structure and Algorithm 

12 

YCT 

 
 
 
 
 
 
 
   
 
          
 
 
 
  
  
 
   
 
 
 
Representation of Linked List– 
• A data item 
• An address of another node 
We wrap both the data item and the next reference in a 
struct as. 
Syntax– 

Struct node  

{ Int data; 
Struct node*next; 
}; 

(cid:1) Linked list Applications 
  • Dynamic memory allocation. 
  • Implemented in stack and queue. 
  • In undo functionality of software. 
  • Hash tables, graphs. 

STACKS 

Stack is a non-primitive linear data structure. 
It is an ordered list in which addition of new data item 
and deletion of already existing data item is done from 
only one End know as Top of Stack (TOS). 

•  It  follows  the  LIFO  pattern,  which  means  the  last 
added element will be the first to be Removed from the 
stack.  
(cid:1) Stack has two operation–  1. PUSH Operation 

Stack Notation- There are three stack notation. 
•  Infix  Notation-  Where  the  operator  is  written  in 
between the operands. 
Example-  

A + B  

+  operator 
A, B operands 

•   Prefix  Notation-  In  this  operator  is  written  before 

the operands. It is also know as polish Notation. 

          Example-  +AB 
•   Post  fix  Notation-  In  this  operator  is  written  After 

the operands. It is also know as suffix Notation. 

          Example-  AB+ 
•  Convert  the  following  Infix  to  prefix  and  postfix 

for (A + B)* C/D+E ∧ F/G 
Prefix –  
(A+B)* C/D + E ∧ F/G  
+ AB* C/D + E ∧ F/G 

* C/D + E^F/G 

R1 * C/D+^ EF/G 

R1 * C/D+R2/G 
R1 */CD + R2/G 

R1*R3 + R2/G 
R1*R3 + /R2G 

R1*R3 + R4 
*R1R3 + R4 

R5 + R4  
+R5R4 

Let + AB = R1R1 

Let ^ EF = R2 

Let /CD = R3 

Let /R2G = R4 

Let *R1R3 = R5 

PUSH  Operation-  Every  PUSH  operation  TOP  is 
incremented by one. 

+*R1R3/R2G 
+*+AB/CD/AEFG 

2. POP Operation 

  Now enter the value of R5, R4, R3, R2, R1 

TOP = TOP + 1 
In case the Array is full no new Element is added. This 
condition  is  called  stack  full  or  stack  over  flow 
condition. 
•  The  process  of  adding  a  new  element  of  the  TOP  of 
stack is called PUSH operation. 
POP  Operation-  The  process  of  Deleting  an  element 
from the top of stack is called POP. 
After  Every  POP  operation 
decremented by one. 
TOP = TOP-1  

the  stack  TOP 

is 

(This is called operation stack underflow). 

Post fix-  

(A+B)*C/D+E ∧ F/G 

  AB+*C/D+E ∧ F/G 

R1*C/D+EF ∧ /G 

R1*C/D+R2/G 
      R1*CD/+R2/G 

R1*R3+R2/G 
R1*R3+R2G/ 

R1*R3+R4 
R1R3*+R4 

R5+R4+ 

Let AB+=R1 

Let EF ∧ =R2 

Let CD/ = R3 

Let R2G/=R4 

Let R1R3*=R5 

Data Structure and Algorithm 

13 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Now Enter the value of R5,R4,R3,R2,R1 

R5R4+ 
R1R3*R4+ 
  AB+CD*R2G/+ 
  AB+CD* EF ∧ G/+ 

QUEUE 

•   Queue is a Non primitive Linear data structure. 
• The first added Element will be the first to be remove 
from  the  queue  that  is  the  reason  queue  is  called 
(FIFO) type list.   

•   Get highest priority ( ): Returns the highest priority 
item. operation implemented  by linear searching the 
highest priority item in array. O(1).  

•  Delete  highest  priority  ():  Removes  the  highest 
priority  operation  can  be  implemented  by  first 
linearly searching an item, the removing the item by 
moving all subsequent items one position back. (time 
O(logn)).   

•  Heap  is  generally  preferred  for  priority  queue 
implementation  because  heaps  provide  better 
performance compared array or linked list. 

•   In queue Every insert operation Rear is incremented 
by one. (R = R + 1) and every delete operation front 
is increment by one. 

Circular Queue- A circular queue is one in which the  
insertion of a new element is done at very first location  
of queue is full. 

•   A  circular  queue  overcome  the  problem  of  utilized 

space in linear queues implemented as arrays.  

BINARY TREE 

•   Binary tree is a finite set of data item which is either empty 
of  consists  of  a  single  item  called  root  and  two  disjoint 
binary tree called the left sub tree and right sub tree. 

•   In Binary  tree,  every  node can have  maximum  of  two 
children which are known as left child and right child. 

Types of Binary Tree 
Full  Binary  Tree-  A  Binary  tree  is  full  if  every  node 
has 0 or 2 child. 

BASIC OPERATION OF QUEUE 

•   Enqueue: Add an element to the end of the queue. 
•   Dequeue:  Remove an element from the  front of the 

queue. 

•   Is Empty: Check if the queue is Empty. 

•   Is full: Check if the queue is full. 

• Peek: Get the value of the front of the queue without 

removing it. 

Application of Queue- 
•   CPU scheduling, Disk scheduling  

•   Handling of interrupts in real time system 

•   Call center phone system use Queues to hold people  

calling them in order. 

• Unlike stack, Queue is also considered as the ordered 
list of the data the ordered list of the data that has a 
similar data type. 

Priority  Queue-  Priority  Queue  is  an  Extension  of 
queue with following properties. An element  with high 
priority  is  dequeued  before  an  element  with  low 
priority. 
Operations- 
•   Insert (item, priority): Inserts an item with given 

priority time (O(logn)). 

Data Structure and Algorithm 

14 

YCT 

 
 
 
 
 
 
 
 
Complete  Binary  Tree-  A  Binary  tree  is  complete 
Binary tree if all level are completely filled. 

Internal nodes = 

m
2









• Every node has max. (m-1) keys 
• Min key:- root node → 1 

all other

=

m
2









−

1

GRAPH  
Graph  in  data  structure  are  non  linear  data  structure 
made  up  of  a  finite  number  of  vertices  and  the  edges 
that  connect  them.  Graph  in  data  structure  are  used  to 
address  real  problem  in  which  it  represents  the  real 
problem  in  which  it  represents  the  problem  area  as  a 
network  like  telephone  networks,  circuit  network  and 
social network. 

This graph has a set of vertices 
V = { 1, 2, 3, 4, 5} and a set of edges 
E = {(1,2), (1,3), (2,3), (2,4), (2,5), (3,5), (4,5)} 
Operation Of Graph In Data Structure 

• Creating graphs 
• Insert vertex 
• Delete vertex 
• Insert edge 
• Delete edge 

to 

traversal 

techniques 

implement  a  graph 

Graph Traversal Algorithm–  
Graph traversal is a subset of tree traversal. There are  
two 
Algorithm. 
1. Breadth - first Search or BFS 
2. Depth – first – search or DFS 
BFS- Two data structure for traversing the graph. 
•   Visited array (size of the graph) 
•   Queue data structure 
•   Using the FIFO concept. 
•   Until the queue is not empty and no vertex is left to 

be visited. 

BFS 1 2 3 4 5 6  

Perfect  Binary  Tree-  A  Tree  in  which  all  internal 
nodes  has  two  children  and  all  leaves  are  at  the  same 
level in which all level has 2n children. 

Traversal of Binary Tree  
1. Preorder traversal (NLR) Node left Right  
2. In order traversal (LNT) Left Node Right 
3. Post order traversal (LRN) Left Right Node 
Example- 

B-Tree 
B-Tree is a self-balancing tree. in most of the other self- 
balancing searching ( like AVL and Red-Black tree). It  
assumed that everything is in the main memory. 
Time complexity of B-Tree 

Algorithm  Time complexity 

Search 

Insert 

Delete 

O (logn) 

O (logn) 

O (logn) 

Properties of B-Tree 

•   All nodes of the leaf must be on the same level. 
•   At least two root nodes are required. 
•   Each B-Tree node a maximum of m children. 
•   Each node in a B- tree includes at least m/2 children,  

except the root and the leaf node. 

•   Maintains sorted data. 
•   Minimum children: 

leaf = 0 
root = 2 

Data Structure and Algorithm 

15 

YCT 

 
 
 
 
 
                
 
 
 
DFS-  The  (DFS)  algorithm  traverses  or  explores  data 
structure such as trees and graphs. The DFS algorithm  
begins  at  the  root  nodes  and  examines  each  branch  as 
for feasible before backtracking. 
•   Examine any two data structures for traversing the graph. 
•   Visited array (size of the graph) 
•   Stack data structure 
•   Using the FIFO principle. 
•   Stack data structure is not empty. 

DFS  1 2 4 5 3 6  

Application of graph 
•  The  friend  suggestion  system  on  facebook  is  based 

on graph theory. 

•   Graph transformation system manipulate graph in memory 
using  rules.  Graph  databases  store  and  query  graph–
structure data in a transaction–safe permanent manner. 

Difference between stack and Queue 

Stack 
The collection of element 
in last in first out (LIFO). 

Queue 
The  collection  of  Element 
in first in first out (FIFO) 

Objects  are  inserted  and 
removed  at  the  same  end 
called TOP of sack. 

Objects  are 
inserted  and 
removed from different ends 
called Front and Rear end. 

Insert  operation  is  called 
PUSH operation. 

Insert  operation  is  called 
Enqueue operation. 

Delete operation is called 
POP operation. 

Delete  operation  is  called 
Dequeue operation. 

In  stack  There 
is  no 
wastage of memory space. 

In Queue there is a wastage 
of memory space. 

Plate  counter  at  marriage 
Reception  is  an  Example 
of stack. 

Students  standing  in  a  line 
at fees counter is an  
Example of Queue. 

Linear Data structure 

The linear data structure are 
comparatively 
to 
implement 

easier 

Non-Linear Data 
structure 

linear  data 
The  non- 
structure 
are 
comparatively  difficult 
implement 
and 
understand  as  compared 
to linear data structure. 

data 

The 
element 
connect  to  each  other 
hierarchically. 

The data element connect to 
each other sequentially. 

It  is  not  easy  to  traverse 
in multiple runs 

You can traverse in a single 
run. 

It is memory friendly. 

It is not very memory friendly. 

Map, Graph, Tree 

List, Array, Stack, Queue  

Array 
Array  is  a  collection 
of 
Homogeneous 
(same) data type. 

Size  of  an  Array  is 
fixed 

Linked list 
Linked-list  is  a  collection 
of node (data & address) 

Size of list is not fixed. 

Memory  is  allocated 
from stack. 

Memory  is  allocated  from 
heap. 

Work with static data 
structure 

Work  with  dynamic  data 
structure. 

Array  Element  are 
independent  to  each 
other. 

Linked  list  Element  are 
depend to each other. 

Array  take  more  time 
(Insertion & Deletion) 

Linked-  list  take  less  time 
(Insertion & Deletion) 

Tree 
There is a unique node 
called root in tree. 

Graph 

There is no unique node. 

Tree is a collection of 
node and edges. 
Ex- T{node, Edges} 

Graph  is  a  collection  of 
vertices/nodes and edges. 
Ex G = {V,E} 

There  will  not  be  any 
cycle/loops. 

In  this  Pre-order,  In-
order  and  post  order 
Traversal. 

There can be loops/cycle. 

this  BFS  and  DFS 

In 
traversal. 

HEAP DATA STRUCTURE 
A  Heap  is  a  special  Tree-based  structure  in  which  the 
tree is complete binary tree. 

A B C D E F G

1

2 3 4 5 6

7

Data Structure and Algorithm 

16 

YCT 

 
 
 
 
 
 
Formula- 

if a Node is at index  i  
its left child is at = 2*i 
its right child is at = 2*i+1 

it parent is at = 

i
2







  

(This is true when your heap is starting from index 1.) 
If  you  represent  a  binary  tree  in  an  array  then  they 
should  not  be  any  empty  locations  or  gaps  in  between 
the elements bins from first element to last element in  
between anywhere. 
•  Height  of  a  complete  binary  tree  will  be  minimum 
only that is log n. 

HEAP 

•   Search key (24, 52, 91, 67, 48, 8 3) 
•   Hash Table 
•   Hash  Function (K  mod 10, K  mod n, Mid, Square ) 

folding method. 

K mod n = (n-1) 
       ↓ 
24 mod 10 =4 
52 mid 10= 2 
91 mod 10=1 
67 mod 10=7 
48 mod 10=8 
83 mod 10=3 

Max  Heap-  A  max  heap  is  a  complete  binary  tree  in 
which the value in each internal node is greater than or 
equal  to  the  values  in  the  children  of  the  node.  Max 
heap data structure is useful for sorting data using heap 
sort. 

20 > 8, 16 

50 > 30, 20 

30 > 15, 10 
Min  Heap-  A  min  heap  is  a  heap  where  every  single 
parent  node  including  the  root,  is  less  than  or  equal  to 
the  value  of  its  children  nodes.  The  most  important 
property  of  a  min  heap  is  that  the  node  with  the 
smallest,  or  minimum  value,  will  always  be  the  root 
node. 

20 < 32, 25 

30 < 35, 40 

 10 < 30, 20 
Operations of Heap 
• Heapify– a process of creating a heap from an array. 
• Insertion– time complexity O (log N) 
• Deletion – time complexity O (log N) 
• Peek–To check or find the most prior element in the  
heap. 

HASHING 
Hashing is a technique or process of mapping keys and 
values into the hash table by using a hush function. It is 
done for faster access to elements. 
•   Hashing storing and Retrieving data in O (1) time. 

B-Tree & B+Tree 

 Data is stored in leaf 
as  well  as  internal 
nodes 

Data is stored only in leaf 
nodes. 

Leaf nodes not linked  
together  

Linked 
Linked list. 

together 

like 

Searching  is  slower 
deletion complex 

is 
Searching 
deletion 
easy 
from leaf node) 

faster, 
(directly 

ALGORITHM 

Analysis of Algorithms 
•   A well defined procedure to solve a specific problem 

is called Algorithm. 

•   Data structure + Algorithm = Programming  

•  Algorithms Criteria 

Data Structure and Algorithm 

17 

YCT 

 
 
 
 
 
 
 
 
 
 
   
 
 
 
              
                        
 
 
 
Asymptotic Notations 

Asymptotic  notations  are  abstract  notation  for  describe 
the  behavior  of  Algorithm  and  determine  the  rate  of 
growth of a function. 

1. Big O Notation 
  • The Big O Notation defines an upper bound of an 
the  worst-case 

it  gives 

algorithm.  Therefore, 
complexity of an algorithm. 

  •  O  (g(n))  =  {f(n):  there  exist  positive  constants  C 

and n0 such that 

O ≤ f (n) ≤ Cg(n)  

for all n > n0 

2. Omega (Ω) Notation:  
Omega  notation  represents  the  lower  bound  of  the 
running time of an algorithm. thus, it provides the best 
case complexity of an algorithm. 

3. Theta (θ)  Notation: 

Theta  notation  encloses  the  function  from  above  and 
below.  It  is  used  for  analyzing  the  average  case 
complexity of an algorithm. 
(
f n

(
C g n
2

(
C g n
1

≤

≤

)

)

)

f(n) = θ(g(n))  
Worst  Case  Analysis–    The  case  that  causes  a 
maximum number of operation to be executed. 
Best  Case  Analysis–  The  case  that  causes  a  minimum 
number of operations to be executed . 
Average  Case  Analysis–  We  take  all  possible  inputs 
and  calculate  the  computing  time  for  all  of  the  inputs, 
sum all  calculate values and divide the sum by the total 
number of inputs. 

BUBBLE SORT 

Algorithm– 
1.   Start with an array of unsorted numbers 
2.   Defines  a  function  called  'bubblesort"  that  takes  in 
the array and the length of the array as parameters. 
3.   In the function, create a variable called "sorted" that 

is set to false. 

4.   Create  a  for  loop  that  iterates  through  the  array 
starting  at  index  0  and  ending  at  the  length  of  the 
array –1 

5.   Within  the  for  loop,  compare  the  current  element 

with the next element in the array. 

6.   If the current element is greater than the next elements, 

swap their positions and set "sorted" to true. 
7.   After the for loop, check if "sorted" is true. 
8.   If  "sorted"  is  true,  call  the  "bubblesort"  function 
again with the same array and length as parameters. 
9.   If "sorted" is false, the array  is  now sorted and  the 

function will return the sorted  array. 

10. Call  the  "bubbleSort"  function  with  the  initial 
unsorted array and its length as parameters to befin 
the sorting process. 

•  It is stable sorting techniques. 
•  Recursive relation in Bubble sort. 

C C
1

2

≥

0, n

≥

n , n
0

0

≥

1

     T(n) = T (n-1) +n         

Data Structure and Algorithm 

18 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
•  It is In place sorting 
•  Time complexity = θ (n2) 

Space complexity = 1 + n 
= θ (n) 

Best case = θ (n) 
Worst case = θ (n2) 
Average case = θ (n2) 

SELECTION SORT 

Algorithm– 
1.  Initialize minimum value(min_idx) to location 0. 
2.  Traverse  the  array  to  find  the  minimum  element  in 

the array. 

= θ (n2) 

                           space = θ(n) 
• Stable sorting 

QUICK SORT 
• It is Divide and conquer technique. 
• It is unstable sorting 
• Best case = θ (n logn) = Average case 
   Worst case = θ (n2) 
• Recursive 

T(n) = 2T(n/2)+n 

Using master theorem 

θ (n logn) 

3.  While traversing if any element smaller than min_idx 

is found then swap both the values. 

4.  Then,  increment  min_idx  to  point  to  the  next 

• Number of comparison = 

−
n(n 1)
2

Merge Sort 

element. 

5.  Repeat until the array is sorted. 
• Recursive relation 
       T(n) = T (n - 1) +(n - 1) 

• Max swap = (n-1)   Complexity θ(n) 
• Min swap = 0 

• It is unstable sorting 

INSERTION SORT 
Algorithm–  To  sort  an  array  of  size  N  in  ascending 
order: 
1.  Iterate from arr[1] to arr[N] over the array. 
2.  Compare the current element (key) to its predecessor. 
3.  If  the  key  element  is  smaller  than  its  predecessor, 
compare it to the elements before. Move the  greater 
elements  before.  Move  the  greater  elements  one 
position up to make space for the swapped element. 

• Number of comparison– 

max

=

)
(
n n 1

−

2

min = n – 1 

• Best case = θ(n) 
  Worst case & Average case = θ(n2) 
• Insertion sort = Position +Shifting 
• It is highly affected due to order of input.  
• Recursive time T (n) = T (n-1)+n 

Algorithm– 

MergeSort(arr[],l,r) 
If r > 1 
1.  Find  the  middle  point  to  divide  the  array  into  two 

halves. 

middle m = l + (r – 1)/2 

2.  Call mergeSort for first half: 

Call mergeSort(arr, l, m) 

3. Call mergeSort for second half: 

Call mergeSort(arr, m + 1, r) 

4. Merge the two halves sorted in steps 2 and 3: 

Call merge(arr, l, m, r) 

• It is stable sorting. 
• It is pure divide & conquer. 
•  Recursive– 

T(n)= 2T(n/2)+n 

• Complexity–  
    Best case = Average case = Worst case  = θ(n logn)  
RADIX SORT 

• It is counting Based sorting. 
• It is outplace sorting 
• Q (n k) 

• Q (n*R) space complexity. 

RECURSION 
A recurrence is an equation or inequality that describes a 
function in terms of its values on smaller inputs. To solve a 
Recurrence Relation means to obtain a function defined on 
the natural numbers that satisfy the recurrence. 
• There are four methods for solving Recurrence 
(i) Substitution method  (iii) Iteration method 
(ii) Recursion tree           (vi) Master method 

Data Structure and Algorithm 

19 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
                     
 
 
 
 
 
(i) Substitution method– 

T(n)

n
1

= 
− +
T(n 1) 1 n


T(n) T(n 1) 1

− +

=

Substitution T(n 1)

−

=
>

0
o
∵


∴ − =





− +
T(n) T(n 1) 1......(i)
−
T(n 1) T(n 2) 1.......(ii)

=

+

T(n)

=

[T(n 2) 1] 1

+ +

−

}
{
From equ (ii)

x

T(n) T(n 2) 2

=

−

+

T(n) T(n 3) 3

−

+

=
⋮

Continue for k time

⋮
⋮

T(n) T(n k) k

=

−

+

T(n) T(n n) n

=

−

+

Assume n k

− =

0

∴ =
n

k

T(n) T(0) n

=

+

T(n) 1 n

= +

∴ θ

(n)

(ii) Recursion Tree – 

T(n)=

1




− +
T(n 1) n

n

=

0

n

>

0





0+1+2…….n-1+n= 

+
n(n 1)
2

+
n(n 1)
2

T(n)

=

θ

2(n )





T(n)=T(n-2)+n-1]+n…...(ii) 
T(n)=T(n-3)+(n-2)+(n-1)+n……(iii) 
            : 
            : Continue of k time 
            : 
T(n)=T(n-k)+(n-(k-1))+(n-(k-2)+……+(n-1)+n 
          Assume n-k=0 
                     n k∴ =  
T(n)=T(0)+1+2+3+…..n-1+n 
+
n(n 1)
2
+
n(n 1)
2

T(n)=1+

       =1+

= θ

(n)

2

•  T(n) = 2T(n 1) + 1
   By solving recursion tree 

−

 1+2+23+…..+2K = 2k+1   (This is GP series) 
= θ(2n) 
(iv) Master theorem for Decreasing function 

T(n)= aT(n-b)+f(n) 
a>0, b>0 and f(n)=O(nK) where K≥0 
Case 
• If a<1          • If a=1            • If a>n 
 O(nk)              O(nK+1)             O(nKan/b) 
 O(f(n))           O(n*f(n))          O(f(n)an/b) 
• Master Theorem for Dividing function 
a  T(n)=a T(n/b)+f(n) 

 (i) logb

                    a≥1 

(ii) b> f(n)=θ(nklogPn) 

 Case1: if logb
 Case2: if logb

a>k them θ(nlogb
a=k 

a) 

If P>-1  θ(nklogp+1n) 
If P=-1  θ(nklog log n) 
If P<-1  θ(nk) 

 Case3: If logb
                                 If P < 0 O(nk) 

a<K   If P ≥ 0 θ(nklogpn) 

T(n) = 2T(n/2) + 1 
a = 2, b = 2, f(n) = O(1) = θ(n0log0n) 
log2
Case1: θ(n1) 

2 = 1 > K = 0 

Recurrence Relation 

T(n) = T(n 1) + 1   

−

T(n) = T(n 1) + 1   

−

O(n)

2
O(n )

(iii) Iteration Method–
n

T(n)=

− +
T(n 1) n n

1




=

0

>

0





T(n)=T(n-1)+n                       { T(n) T(n 1) 2
T(n)=[T(n-1)+n-1]+n…..(i)   {T(n-1)=T(n-2)+n-1 

− +

=

∵

−

T(n) = T(n 1) + log n   O(n logn)
)

(
T n = T n 1 + n

3
   O(n )

−

(

)

2

T(n) = T(n 2) + 1    

−

n
2

(
)
O n   

2
T(n) = T(n 100) + n   O(n )

−

Data Structure and Algorithm 

20 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
     
 
 
HUFFMAN CODING 

KNAPSACK PROBLEM 

•  Huffman Coding is a famous greedy Algorithm. 
•   It is used for the lossless compression of data. 

•   A  Knapsack  (kind  of  shoulder  bag)  with  limited 

weight capacity. 

•   It used variable length in encoding. 

•  Few items each having some weight and value. 

•   It assigns variable length code to all the Characters. 

•   There are two knapsack problem. 

Prefix rule– 

•   Huffman coding implements a rule know as a prefix  

coding 

1. Fractional knapsack problem.  
2. 0/1 Knapsack problem. 

Fraction knapsack problem 

•   This is to prevent the ambiguities while decoding 

•   It  ensures  that  the  code  assigned  to  any  character  is 
not  a  prefix  of  the  code  assigned  to  any  other 
character. 

•   As the name suggest, items are divisible here. 

•   For each item, compute its value/ weight. 

•  Arrange  all  the  items  in  decreasing  order  of  their 

value/weight ratio. 

•   There are two major steps in Huffman Coding. 

 Put as many items as you can into the knapsack. 

1.  Building a Huffman tree from the input characters 
2.  Assigning code to the characters by traversing the 

Human tree. 
Huffman Tree- 
Step.1 Create a leaf node for each Character of the test. 

•  Leaf  node  of  a  character  contains  the  Occurring 

frequency of the character. 

Step.2 Arrange all the nodes in increasing order of their  
frequency value. 

•   Considering  the  first  two  nodes  having  considering 

the first two nodes having minimum frequency. 

•  The  frequency  of  this  new  node  is  the  sum  of 

frequency of those two nodes. 

Step.3 Make the first node as a left child and the other 
node as right child of the newly created node. 
Step.4  Keep repeating step 2 and step 3 until all the  
nodes from a single tree. 

Time complexity- 

•  Extract Min( ) is called 2*(n-1) times if there are n nodes.  

•  As extract Min( ) cells min Heapify, it take O (logn) time. 
  Thus,  Overall  time  complexity  of  Huffman  coding 

become O(n logn).  

Example- ABBCDBCCDAABBEEEBEAB 

Time Complexity– 

•   If the items are already arranged in the required order 

then while loop takes O (n) time. 

•   Average time complexity of Quick sort is O (n logn) 

Example– 
       Object  :   O     1 
2 
       Profits  :   P     10  5 
3 
       Weights :   W     2 

3 
4 
15  7 
7 
5 

5 
6 
1   4 

6 
7 
18  3 
1 

P
W

5 1.3 3 1 6 4.5 3

                      x    (1  2/3   1    0   1    1    1) 
                              x1  x2    x3  x4   x5  x6  x7 
n = 7, M= 15 

∑

x W 1 2

= × + × + × + × + × + ×

3 1 5 0 7 1 4 1 1

i

i

2
3

= + + + + + + =

2 2 5 0 1 4 1 15

∑

x P
i
i

= ×

1 10

=

54.6

+ × + ×

+ × + ×
5 1 15 1 6 1 18 1 3

+ ×

2
3

Constraint
∑

x W m≤
i

i

Objective 

max

ix P∑  

i

OPTIMAL MERGE PATTERN 

Given  n  number  of  sorted  files,  the  task  is  to  find  the 
minimum  computations  done  to  reach  the  optimal 
merge  pattern,  when  two  or more  sorted  files  are  to  be 
merged  altogether  to  form  a  single  file,  the  minimum 
computation  are  done  to  reach  this  file  are  known  as 
Optimal merge pattern. 

Data Structure and Algorithm 

21 

YCT 

 
 
                    
  
 
Example-   List– x1, x2, x3, x4, x5 
Size– 20 30 10 5 30 

Fun (Si, Vj)= 

min







fun(S , K) C(V , K)

+

j

+
i 1
C(V , D) if S
i

j

=

S

f

i

−

1




  


Total cost of merging =∑di*xi 
 di = distance of each node 
The size of each node = xi 

So,   
Total number of merging  
                  = 3×5+3×10+2×20+2×30+2×30 = 205 

DYNAMIC PROGRAMMING 

•   It is used to solve optimization solution . 
•   Breaks down the complex problem into simpler sub-

problems. 

•   Find optimal solution to these sub-problems. 
•   Store the results of sub-problems. (memorization) 
•  Reuse 

that  same  sub-problem 

then  so 
calculated more than once. 

is  not 

•  Finally calculate the result of complex problem. 
•   Overlapping sub problems & Optimal Substructure. 
 Type of Dynamic Programming– 
•   Multistage Graph 
•  Floyd Warshall 
•   Bellman Ford Algorithm 
•  0/1 Knapsack 
•  Optimal Binary Tree 
•  Reliability Design 
•  Longest common subsequence (LCS) 
•  Matrix chain Multiplication 

MULTISTAGE GRAPH 
Multistage  graph  is  a  data  structure  that  is  used  to 
represent a graph in which the vertices are divided into 
a  number  of  levels.  The  edges  of  the  graph  are  also 
divided into a number of levers. The multistage graph is 
also called a Hierarchical graph. 

Where, S=stage, V = Vertex, F= final stage 

  Minimum cost = 11 

Path 

Time Complexity = O (V + E)   

(E is edge) 

FLOYD-WARSHALL 

The  strategy  adopted  by  the  Floyd-Warshall  algorithm 

is  Dynamic  programming.  The  running  time  of  the 

Floyd-Warshall  algorithm  is  determined  by  the  triply 

nested  for  loops  of  lines  3-6.  Each  execution  of  line  6 

takes O(1) time. The algorithm thus runs in time θ (n3). 

Example– 

Ak[i, j] = min







−
K 1
A [i, j]




A [i, k] A [k, j]
+



−
K 1

−
k 1

K S +∀

i 1

Time Complexity = O(n3) 

Space Complexity = O(n3) 

Data Structure and Algorithm 

22 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
•   On encountering an entry whose value is not same as 
the  value  stored  in  the  entry  immediately  about  it, 
mark the row label of that entry. 

•   After  all  the  entries  are  scanned  the  marked  labels 
represent  the  items  that  must  be  put  into  the 
knapsack. 

Example-  

Value of V 

O/1 Knapsack problem 
m = 8   P = {1, 2, 5, 6} 
n = 4    w = {2, 3, 4, 5} 

V[4, 5] = max[V[3, 5], {V[3, 5-5]+6]} 

           = max[5, 0] = 5 

V[4, 6] = max[V[3, 6], {V[3, 6-5]+6]} 

         = max[6, 6] = 6 

V[4, 7] = max[V[3, 7], {V[3, 2]+6]} 

         = max[7, 7] = 7 

V[4, 8] = max[V[3, 8], {V[3, 3]+6]} 

         = max[7, 8] = 8 

0 1 2

3

4

5

6 7 8

P W 0 0 0 0 0 0 0 0 0 0
i
0 0 1 1 1 1 1 1 1
1

2

1

i

2
5
6

3
4
5

2 0 0 1 2 2 3 3 3 3
3 0 0 1 2 5 5 6 7 7
4 0 0 1 2 5 6 6 7 8

Solution 

x
1
0





x

2
1

x

3
0

x

4
1





=

{

}
2, 6

Optimal Binary Search Tree 
A  set  of  integers  are  given  in  the  sorted  order  and 
another array to frequency count. Our task is to create a 
binary search tree with those data to find the maximum 
cost for all searches. 
Example- 

1

10

4

2

20

2

3

30

6

4

40

3

Key

frequency

Formula–

[i, j]= min{C[i, k-1]+C[k, j]}+w(i, j)   i<k≤j 

Bellman Ford Algorithm 

go on relaxing all the edges(n 1) times

−

n

=

number of verites

+
if ([u] c(u, v)
+
=

d[v])
d[v] d[u] c(u, v)

<

Edges- 
(A, B), (A, C), (A, D), (B, E), (C, E), (D, C), (D, F), (E, 
F), (C, B) 
We are done algorithm 5 time. 

A-0, B-1, C-3, D-5, E-0, F-3 

Single Source Shortest Path 

Time Complexity = O(E(|v|-1) 

= O(E.V) 
= O(n2) 

0/1 Knapsack Problem 

• Consider– Knapsack weight capacity = w  

  Number of items each having some weight 

and value = n 
• Problem solving steps– 
(i)  Draw a table say 'T' with (n+1) number or row and 

(w+1) number of column. 

(ii)  Fill  all  the  boxes  of  0th  row  and  0th  column  with 

zeroes as  

(iii) Start filling the table  row wise top to bottom from 

left to right. 

Using formula 

V[i, w]=max{v(i-1, w), v[i-1, w-w[i]]+P[i]} 

Here V [i, w]= maximum value of  the selected items  
if we can take items 1 to i and weight restrictions of w. 
•   This step leads to completely filling the table. 
•  Then  value  of  the  last  box  represents  the  maximum 

possible value that can be put into the knapsack. 

•   The knapsack to obtain that  maximum profit. 
•   Consider the last column of the table. 
•   Start scanning the entries from bottom to top. 

Data Structure and Algorithm 

23 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
l
l

= − =
j
= − =
j

0
i
i 1

So, 

l

= − =
j

i

2

C[0,1]

=

4

C[1, 2]

=

2

C[2, 3]
C[3, 4]

=
=

6
3

3
=
C[0, 2] 8, C[1,3] 10 , C[2, 4] 12

=

=

3

Using formula 

l = j – i = 3 

l = j – i = 4 

w(0, 4)=

4

∑  
f (i)

=
i 1

C[0, 3] = 203, C[1, 4] = 163 

C[0, 4] = 263 
Matrix Chain Multiplication 

A1           A2                   A3 
A2×5            B5×10                     C10×3 
P0×P1           P1×P2                 P2×P3 

Left side              
(BC)5×3 = B5×10 C10×3 = 5×10×3 = 150 
M [2, 3] = M [2, 2] + M [3, 3] + 5×10×3=150 
(ABC)2×3 = A2×5(BC) = 2×5×3 = 30 
M [1, 3] = M [1, 1] + M [2, 3] + P0×P1×P3 
             = 0+150+30 = 180 
Right side 
(AB)2×10 = A2×5 .B5×10 = 2×5×10 = 100 
M [1, 2] = M [1, 1] + M [2, 2] + 2×5×10 =100 
(ABC)2×3 = (AB)2×10 C = 2×10×3 = 60 
M [1, 2] = M [1, 2] + M [3, 3] + P0×P1×P3 = 160 
Formula using 
M (i, j) = min {M [i, k] + M [k + 1, j] + Pi-1 Pk Pj 

                       i ≤ k < j 

Example- A2×1    B1×3    C3×4    D4×5 
M [1, 2] = M [1, 1] + M [2, 2] + 2×1×3 = 6 
M [2, 3] = M [2, 2] + M [3, 3] + 1×3×4 = 12 
M [3, 4] = M [3, 3] + M [4, 4] + 3×4×5 = 60 
 So by formula 
2

1 2 3 4

4

3

1

1 0

2

3

4

6

0

20 42

12 32

0

60

0

1

2

3

4

1 1 1

2 3

3

                     A (B(CD)) 
    Time Complexity  
                                 = O (n3) 

= O (n) 

DIVIDE AND CONQUER 

•    Divide:  In  this  step,  we  will  break  the  problem  into 

sub-parts by recursion. 

•  Conquer:  We  will  solve 

the  smaller  subparts 
recursively. It the sub problem is small, then we can 
solve it instantly. 

•   Application of divide and conquer Algorithm 

(i) Binary search  
(ii) Merge sort 
(iii) Quick sort 
(iv) Strassen's Matrix Multiplication. 
(v) Karatsuba Algorithm 
(vi) Stassen's Algorithm. 

GREEDY ALGORITHM 

•   A  greedy  algorithm  is  a  problem  solving  approach 
like subtract and conquer and dynamic programming, 
which  is  used  for  solving  optimality  problem(one 
solution), out of all feasible solution. 

•   Minimum spanning tree 
•   Single source shortest path 
•   Huffman coding 
•   Optimal merge pattern 

KRUSKAL'S ALGORITHM 

•   Kruskal's Algorithm is a famous greedy Algorithm. 
•   It  is  used  for  finding  the  Minimum  spanning  tree 

(MST) of a given graph. 

•   The  given  graph  must  be  weighted,  connected  and 

undirected. 

•   Simple draw all the vertices on the paper. 
•   Connect  these  vertices  using  edges  with  minimum 

weights such that no cycle gets formed. 

Example- 

Weight of the MST 

= Sum of all edge weights 
= 1+2+4+5+6=18 units 

Worst case time complexity 

= O(E logV) or O(E logE) 

SINGLE SOURCE SHORTEST PATH 

•  Dijkstra  Algorithm 

is  a  very 

famous  greedy 

Algorithm. 

•   It  is  used  for  solving  the  single  source  shortest  path 

problem. 

Data Structure and Algorithm 

24 

YCT 

 
 
 
 
 
 
 
 
                  
 
 
 
 
 
 
 
 
 
 
•   Dijkstra algorithm work only for connected graphs. 
•   Dijkstra algorithm work only for those graphs that do 

not contain any negative weight edge. 

•  The  actual  Dijkstra  algorithm  does  not  output  the 

shortest paths 

•  Dijkstra  algorithm  works  for  directed  as  well  as 

undirected graphs. 

Dijkstra Algorithm Steps–  
Step-01 In the first step. two set are defined . 
•   One  set  contains  all  those  vertices  which  have  been 

included in the shortest path tree. 
•   In the beginning, this set is empty. 
•   In  the  beginning,  this  set  contains  all  the  vertices  of 

the given graph. 

Step-02 Two variables are defined as  
•   ∏[v] which denotes the predecessor of vertex 'v) 
•   d  [v]  which  denotes  the  shortest  path  estimate  of 

vertex 'V' from the source vertex. 

Initially, the value of these variables in set as– 
•   The  value  of  variable '∏  '  for  each  vertex  is  set  to 

NIL. i.e. ∏[v] = NIL. 

•   The value of variable 'd ' for source vertex is set to 0 

i.e. d[s] = 0  

  The value of variable 'd 'for remaining vertices is set 

to ∞ i.e. d[v]∞ 

Step-03 
• Among unprocessed vertices, a vertex with minimum 
value of variable d is chosen. 
• Its outgoing edges are relaxed. 
•  After  relaxing  the  edges  for  that  vertex,  the  sets 
Created in step-01 are updated. 
Edge relaxation–  
edge(a, b)- 

• It is employed to identify the shortest path. 
• It is very popular in the Geographical Maps. 
• The telephone network makes use of it. 
Application– 
• To determine the quickest route. 
• In application for social networking 
• Within a phone network. 
     Time complexity is O(E log V) 
     Space complexity is O(V) 

BACK TRACKING 
Back  tracking  uses  brute  force  approach  to  solve 
problem.  Brute  force  approach  say  that  for  any  given 
problem  generate  all  possible  solution  and  pich    up 
decided    solution  .  Back  tracking  uses  Depth-  first- 
search to generate state space tree. 
 Brute force Approach– 
Example–  

Let B1 B2 G1    {B=Boy 
{G=Girl 

Seating arrangement       
    State space tree – n=3 

N-Queens Problem 
The N Queen is the problem of placing N chess queens 
on  an  N×N  Chessboard  so  that  no  two  queens  attack 
each other. 
Formula– 
Maximum number of nodes 

=

1

+

i

n


∑ ∏



=
i 0

=
j 0

−
(N j)





Here,  d[a]  and  d[b]  denotes  the  shortest  path  estimate 
for vertices a and b respectively from the source vertex 
'S' 
Now 
        If d[a]+w<d[b] 
        then d[b]= d[a]+w and ∏[b]=a 
this is called as edge relaxation. 
Advantages– 
• It is used in google map  

•  Time  complexity:  O(N!)  which 
maximum number of queens placed. 
• Space complexity: O(N2) for the board. 

Graph Coloring 

represent 

the 

•   How many number of nodes = Cn+1 

Data Structure and Algorithm 

25 

YCT 

 
 
 
 
 
•   Coloring of graph constitutes coloring vertices edges 

Using formula 

of the graph. 

•  Coloring  all  the  vertices  of  a  graph  is  the  property 

that no two adjacent vertices have same color. 

[Always try to color with minimum colors] 

HAMILTONIAN CYCLE 
The Hamiltonian  cycle is the cycle. graph which visits 

all  the  vertices  in  graph  exactly  once  and  terminates  at 

the staring node. It may not include all the edges. 

Step 

•   In any path, vertex i and (i+1) must be adjacent. 

•   1st and (n-1)th vertex must be adjacent. 

•   Vertex i must not appear in the first (i-1) vertices of 

 g(i, S)=

min{C
←
k S

ik

+

−
g(k,S {k}}

So 

 g(1{2, 3,4})= 

k

 g=Cost   

min {C g(k{2,3, 4)} {k}}
←
{2, 3, 4}

−

1k

 g(2, φ)=5,  g(3, φ)=6            [φ is null value] 

 g(4, φ)=8,  g(2,{3})=15 

 g=(2, {4})=8,  g(3,{3})=5 

 g(3, {4})=5,  g(4, {2})=5 

 g=(4,{3})=6, g(4, {2})=25 

 g=(4,{2, 3})=23 

Last values 

any path. 

•   With  the  adjacency  matrix  representation  of  the 

g

=

graph,  the  adjacency  of  two  vertices  can  be  verified 

=

(1,{2,3, 4} min{C

=

+

g(2,{3, 4}, C

+

g(3,{2, 4}}

13

12
g(4,{2,3})}

+

C

14
min{10 25,15 25, 20 23}

+

+

+

in constant time. 

•   Maximum number of nodes 

=

min{35, 40, 43}

g(1,{2,3, 4})

=

35

 •   Complexity 

=

−
(n 1)!
2

T(n) = O(n2) 

(cid:1)  Traveling  Salesman  Problem  using  Dynamic 

Programming 

1

2

3

4

1 0


2 5


3 6

4 8


10 15 20

0
13
8

9
0
9

10
12
0








BRANCH AND BOUND 

•   An algorithm design technique, primarily for solving 

hard optimization problem. 

•   Guarantees that the optimal solution will be found 

•   Does  not  necessarily  guarantee  worst 

case 

polynomial time complexity. 

•   But  tries  to  ensure  faster  time  on  most  instances 

Basic Idea. 

•  Model the entire solution space as a tree. 

  Search  for  a  solution 

in 

the 

tree  systematically, 

eliminating parts of the tree from the search intelligently. 

•   Important  technique  for  solving  many  problems  for 

which  efficient  algorithms  (worst  case  polynomial 

time) are not know. 

Optimization problems– 

•  Set of input variables I 

•  Set of output variables O 

               Minimum Cost = 35 

•   Set of constrains cover the variables. 

Data Structure and Algorithm 

26 

YCT 

• Values of the output variables define the solution space. 

 
 
  
 
 
     
        
 
 
 
  
•   Set of feasible solutions. 

Techniques– 

•   Set of solutions that satisfy all the constraints. 

• Comparisons tree 

•   Objective function F:S  →R (also called cast function) 

• Oracle and adversary argument 

•   Gives a value F(s) for each solution S∈ S. 
Optimal solution– 

• State space method 

Non –Deterministic Algorithm– 

•   A Solution S∈ S for which F(S) is maximum among 
or 

a  maximization 

all  S∈ S(for 
minimum(for a minimization problem). 

problem) 

Job searching– 
Using problem solving 

1. FIFO – Queue 
2. LIFO – Stack 

3. Least – Cost 

Outcome  of  Non  deterministic  Algorithm  will  be 

restricted to specific set of possibilities.  

(1)  Choice (S): Arbitrarily choose one element from set S. 

(2)  Failure ( ): Signal an unsuccessful solution. 

(3)  Success ( ): Signal an successful solution. 

Example- Searching x on A [1:n], n≥1 on success  

returns of it A[j]=x or returns 0 otherwise. 

•  Job sequencing with deadline 

(1)  j=Choice (1,n); 

Upper  =  sum  of  all  penalties  except  that  included 
solution 
Cost= sum of penalties till that last job considered 

(2)  If (A [j]==x) then {write (j); success} 

(3)  Write (0); Failure(); 

NP-Hard and NP–Complete 

job 1

2

3

Penalty
5
deadline 1

time

1

10
3

2

6
2

1

4

3
1

1

U

=

C

=

Pi

Pi

∑

∈
i s

∑

∈
i S
K

Upper

= ∞

19 14 9 8

Polynomial time 

linear search-n 

Binary search-logn 
Insertion sort-n2 

Marge sort-n logn 
Matrix mullipliction-n3 

Exponential time 
0/1 Knapsack- 2n 
Traveling SP-2n 
Sum of subsets-2n 
Graph coloring cycle-2n 
Hamiltonian cycle-2n 

 NP-Hard- If every problem in NP can be polynomial  

time reducible to a problem 'A' is called NP Hard. If 'A'  

Could be solved in polynomial time then every problem  

in NP is 'P'.  

NP- complete: A problem, if it is in NP and NP-Hard,  

then it is said to be. 

NP-Complete problem. 

Solution–   

Ĉ=5 
u=8 
J2, J3=16 
J1J4=8 

LOWER BOUND THEORY 

L(n) to be the running time of an algorithm A, then g(n) 
is the  lower bound of the algorithm  A. It there are two 
constants C and N such that 

L(n)>=C*g(n), for n>n  

Note–If  NP-Hard  or  NP-Complete 
polynomial time, then NP=P 

is  solved 

in 

•  If NP-Hard or NP- Complete problem is proven to be 

not solvable in polynomial time, then P!=NP 

  But,  till  date  it  is  not  possible  to  find  out  whether 

NP= P or not. 

•   Status of NP is still unknown.   

Data Structure and Algorithm 

27 

YCT 

 
 
 
 
 
       
 
                 
     
 
  
 
 
   03.   DISCRETE MATHEMATICS 

LOGIC 

Propositional  Logic–  A  declarative  sentence  to 
why we can assign one and only one truth value. 
i,e.  True or False 

Derived Operators & Properties 
(↑, ↓, ⊕, →, ↔) 

  Truth Table 

Example–  
•
London is a city. True
• × =
2 3

..False

5

Propositional





• + =
x 2

5

th

•

15 August is independence day
Logical Connective or Operators 

Propositional

Not





P Q P Q P Q P Q P
F F
F T

⊕
F
T

↓
T
F

↑
T
T

T F
T T

T
F

F
F

T
F

Q P

→
T
T

F
T

Q

↔
T
F

F
T

Example– P→Q ≡ Q' →  P Q Q P

+  this is true.  

+

≡

The  following  symbols  are  used  to  represent  the 
logical connectives. 

AND 
OR 
NOT 
EX-OR 
NAND 
NOR 
If.....then 
If and only if  ↔ (Biconditional) 

∧ (Conjunction) 
∨ (Disjunction) 
¬ (NOT) 
⊕ 
↑ 
↓ 
→ (Implication) 

Primary 

Secondary 

Tautology–  An  atomic  proposition  cannot  be 
tautology.  So  a  compound  proposition  which  is 
always true is called as 'tautology.' 
(
∨ (cid:1) 
P

)
  Contradiction–  A  compound  proposition  which  is 

Example– 

P

Example– 

always false is called a contradiction. 
(

)
  Contigency– A compound position which is neither 
a tautology nor a contradiction is called contigency. 

(cid:1) 

∧

P

P

F

≅

Example– 

P → q, P ∨ q, P ∧ q, P ↔ q 

Truth Table of primary operator AND (∧) OR (∨) ¬ 

Satisfiable function of satisfiability– 

A ∧ B 

(not) 
A ∨ B 

¬ A  ¬ B 

F 
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

T 
F 
T 
F 

A 

F 
F 
T 
T 

B 

F 
T 
F 
T 

  Properties 

•  A  compound  proposition  which 

is  not  a 

contradiction is called satisfiable function. 
•  A satisfiable function can be a tautology also. 
Arguments 

The argument is a set of statements or propositions 
which contains premises and conclusion. The end of 
last  statement  is  called  a  conclusion  and  the  rest 
statements are called premises. 

Commutative Law

Associative Law

  An argument is denoted by the following expression 

p q
p q

∨ = ∨
∧ = ∧

q p
q p

p

∨

p

∧

(
(

q r

)
∨ =
)
∧ =

q r

(
(

∨
p q

∧
p q

)
)

∨

r

∧

r

as follows. 

P1, P2 ........ Pn $ Q  
  Where  P1,  P2  ........  Pn  is  the  premises  and  Q  is  the 

Distributive Law

Identity Law

conclusion. 

p

∨

p

∧

(
(

q r

)
∧ =
)
∨ =

q r

(
(

∨
p q

∧
p q

)
)

∧

∨

(
(

∨
p r

∧
p r

)
)

P F P
∨ =
∧ =
P T P

Compliment

p P ' T
p P ' F

∨
∧

=
=

Example– 

(i) P + Q + P' = P + P' + Q = 1 + Q = 1 
(ii) P ∨ (P' ∨ Q) = (P ∨ P') ∨ Q 

= 1 + Q = 1 Tautology 

Example– 

• Every mother is a woman. 
• All women is caring 
• Therefore, every mother is caring. 
Rules of Inferences 

In  logical  reasoning  (an  argument  or  proof),  a 
certain  number  of  propositions  are  assumed  to  be 
true  and  based  on  that  assumption  some  other 
propositions  are  derived. There  are  some  important 
reasoning or rules of inferences. 

Discrete Mathematics 

28 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
of 

Implicant form 

P → (P ∨ Q) 

Sr.  
No. 

Rules 
Inference 

1.  Addition 

P
P Q∴ ∨

2. 

Conjunction P 

P ∧ Q → P ∧ Q 

Q
P Q∴ ∧

3. 

Simplification 
P Q
∧
∴
Q

(P ∧ Q) → Q 

4.  Modus  ponens 

(P ∧ (P → Q))→ Q 

P 

→
P Q
∴
Q

5.  Modus 

tollens 

(¬ Q ∧ (P → Q)) → ¬ P 

¬ Q 

P
→
∴¬

Q
P

6.  Disjunctive 

(¬ P ∧ (P ∨ Q)) → Q 

syllogism ¬ P 
P Q
∨
∴
Q

7.  Hypothetical 

8. 

R
R

syllogism  P  → 
Q 
→
Q
∴ ⇒
P
Constructive 
Dilemma 
(P→Q)∧(R→S
) 

P R
∨
∴ ∨
Q S

9.  Destructive 

Dilemma 
(P→Q)∧(R→S
) 

¬ ∨ ¬
Q
S
∴¬ ∨ ¬
P
R

((P→Q)∧(Q→R))→(P→R
) 

(P→Q)∧(R→S)∧(P∨R)→(
Q∨S) 

(P→Q)∧(R→S)∧(¬Q∨¬S
) → (¬ P ∨ ¬R) 

Example–  If  you  study  hard  you  will  pass  the  exam.  I 
studied hard. Therefore I will pass the exam, can 
be translated as 
P : I study hard 
Q : I will pass the exam (P → Q, P)  ⊣  Q 
This  argument 
the  well-formed 
formulas  (P  →  Q)  ∧  (P)  →  Q  is  a  tautology.  It 

is  valid 

if 

can  be  verified  that,  it  is  indeed  a  tautology  & 
therefore the given argument is valid. 
Rules of inference for quantified 

propositions 
1. (US) Universal instantiation → (specification) 

∀

∴

(
)
xP x
( )
P a

 valid for any element 

  'a' in the universe of discourse. 
2.  (ES)  Existential  specification  (Instantiation) 
→ 
∃

  valid  for  some  elements  'c'  in  the 

(
)
xP x
( )
P c

∴

universe of discourse. 
3.  (UG)  Universal  Generalization  →  If  P(a)  is 
true for all elements in the universe of discourse 

( )
P a
(
xP x

∴∀

)

)

∴∃

4.  (ES)  Existential  Generalization    →  If  P(c)  is 
valid  true  for  some  element  in  universe  of 
discourse. 
( )
P c
(
x P x
Equivalences → 
(1) ∀x{P(x) ∧ Q(x)} ⇔ {∀x(P(x))}∧{∀xQ(x)}  
If  we  replace  ∀x  with  ∃x,  the  above  statement 
does not hold good. 
i.x ∃x{P(x) ∧Q(x)}  ⇔  ∃xP(x)∧∃xP(x) 
It is a tautological implication 
∃x{P(x)∧Q(x)} ⇒ {∃xP(x)}∧{∃xQ(x)} 
Properties of quantifiers– 
(1) ∀xP(x) →∃xP(x) 
(2) ∀x∀y P(x, y) ↔ ∀ y ∀xP(x, y) 
(3) ∃ x ∃ yP(x, y) ↔ ∃y ∃x P(x, y) 
(4) ∃ x∀y P(x, y) → ∀y ∃x P(x, y) 

Graphical  Representation  of  Relation  between 
Sentences Involving two quantifiers. 

TRANSLATIONS 

∀ ⇒ "For all", "Every", "Any", "All", (→) ∃ ⇒ 
"Their exist", "Same", "a", "an" (∧) 

Example–  

Birds can fly 
Assumption 
  B(x) : x is bird 
  F(x) : x can fly 
  Domain : Univers 

Discrete Mathematics 

29 

YCT 

 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Solution: 

  ∀ x (B(x) →F(x)) 

Example– 

Some birds can fly 
Assumption 
B(x) : x is Birds 
F(x) : x can fly 
Domain : Universe 

Solution: 

∃ x(b(x) ∧F(x)) 

Combinatorics 

Fundamental Principle of counting 

•  Sum  Rule–  Let  an  event  occur  thru  process-1  in 
'm'-way  and  thru  process-2  in  'n'-ways  'non-over 
lapping'  then  total  number  of  ways  of  occurrences 
of event will be 'm + n'. 

•  Product  Rule  →  If  event  ε1  can  occur  thru  m-
ways  and  another  independent  event  E2  can  occur 
thru n-way then total number of ways of occurrence 
of E1 and E2 will be 'm.n'. 

Note– It between two processes order is possible then it 

will be considered by itself in multiplication. 

•  Bijection  Rule–  Number  of  favorable  way  of 
occurrence of an event 

(iv) combination without repetition 

n

C

r

=

n!
)
−
r! n r !

(

(v) Combination limited repetition 

Generating function 

(vi) Combination unlimited repetition 
n – 1 +  r

rC  

(vii) Distribution 
(viii) Principle of Inclusion Exclusion 
(ix) Pigeon Hole Principle 
Recurrence  Relations–  Let  a0,a1,a2  ...  an  be  a 
sequence of real number. 
  an = f(an–1, an–2, .....) 
Arithmetic sequence 
{a, a + d, a + 2d, .....} 
the  recurrence  relation  is  an  =  an–1  +  d  (n≥1) 
where a0 = a 
Geometric sequence 
{a, ar, ar2, ar3 ......} 
The recurrence relation 
an = an–1.r (n≥1) a0 = a 
There are two type of recurrence relation 

= total number of ways unfavorable – number of ways 

• Linear  • Non-linear 

Permutations 

  (cid:1)  An  arrangement  of  (or)  ordered  selection  of 

objects is called a permutation. 

The formula of counting this is 

n

P
r

=

n!
)
−
n r !

(

= ×
n

(

)
− ×
n 1

(

)
− ×
n 1

(

−
n 2

)

.....(n–r +1) 

Combinations– Let n, r integers. If n ≥ r for the 
set of n elements a sub set of r element is called a 
"combination". 

Formula– 

n

C

r

=

n!
)
r! n r !
−

(

Nine categories of problem 
(i) Permutation without repetition 

n

P
r

=

n!
)
−
n r !

(

Generating Function– 
Let  {a0,  a1,  a2......an}  be  a  sequence  of  real 
number, then a function f(x) defined by 
f(x)  =  a0,  a1x,  a2x2  +.....  +  an.x12  +  ...  is  called 
generating function of the sequence. 
It  the  sequence  contains  infinitely  many  terms 
then 

∞

(
f x

)

= ∑

(

a .x
n

)n

=
n 0
Set Theory 

Set→  A  set  can  be  defined  as  a  well-defined 
unordered collection of distinct element. 

Example–  A = {1, 2, 3, 4, ......, ∞} 

S = {x/(x is a positive integer)} and 1≤x≤10 
S = {1, 2, 3, ....., 10} 

Null set (empty set)–  A set  with  no elements is 
called a "Null/empty set" denoted as 'φ'.,{}. 

(ii) Permutation limited repetition 

Example– A = {x/x is a prime number and 8≤x≤10} 

n!
n1!* n2!*.....

Subset– If every element of A is also an element 
of B then A is subset of B. 

(iii) Permutation unlimited repetition 

nr 

Example–  A = {a, b, c} so A ⊆ B 
B = {a, b, c} 

Discrete Mathematics 

30 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Proper Subset– Any subset of A which is not a 
trivial subset of A is called proper subset of A. It 
is denoted by 'C'. 
Power set of a Set– If A is  a finite set then set 
of all subsets of it is denoted by P(A). 

Example– If A = {a, b, c}, then P(A) = {φ}, {a}, {b}, 

{c}, {a,b}, {b,c}, {c,a},{a, b, c}} 

Note– If |A| = n the |P(A) | = 2n. 

Universal  Set–  Set  of  all  objects  under 
discussion. It is denoted by 'U'. 
Example:- Let A={1,2,3,}, B={4,5,6} 

(iii) (B – A) = (B ∩ AC) 
(iv) (A ∪ B)C = (AC ∩ BC) 

(c)  For  any  3  set  →  A,  B,  C  the  following 
properties hold good. 

(1) If A ⊆ B, then A∪ B = B and A ∩ B = A 
(2) (AC)C = A 
(3) Commutative laws 

(i) 

(A ∪ B) = (B ∪ A) 

(ii)   (A ∩ B) = (B ∩ A) 

(iii)   (A ⊕ B) = (B ⊕ A) 

A∪B ={1,2,3,4,5,6,} 

(4) Associative laws 

Complement  of  a  set–  If  A  is  any  set  then 
complement  of  A,  denoted  by  A   or  AC  defined 
as 

AC = {x/x∉A and x ∈ ∪} 

Set Difference– If A and B are two set, then A – 
B = {x/x ∈ A and x∉ B} 

Example:- 
 A= {1, 2, 3}, B = {2, 4, 6}  

then A – B = {1, 3} 
Set Union– If A and B are two sets then,  

A∪B = {x/x∈ A or x ∈ B or x ∈ A∩B} 

Set Intersection → If A and B are two set then,  

A∩B = {x/x∈ A and x ∈ B} 

Note–  If  A∩B  is  empty  set,  then  A  and  B  are  called 

disjoint sets. 

Symmetric Difference/Boolean sum– 

 A∆B/A⊕B = {x/x ∈ A or x ∈ B but x ∉ A∩B} 

Note– The symmetric difference of A and B  

 (a) 

⊕ =

)
A B

(
)
(
− ∪ −
B A
A B A B
)
(
= ∪ − ∩
B A

(
(b)   (i) (A – B) = (A ∩ BC) 

)

(ii) (A ∩ B) 

(i) 

(A ∪ B) ∪ C = A ∪ (B ∪ C) 

(ii)   (A ∩ B) ∩ C = A ∩ (B ∩ C) 

(iii)   (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C) 

(5) Distributive law 

(i)  A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) 

(ii)   A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) 

(6) Demorgans laws 

(A ∪ B)C = (AC ∩ B C) 
(i) 
(ii)   (A ∩ B) C = (AC ∪ BC) 
(iii)  A – (B ∪ C) = (A – B) ∩ (A – C) 

(iv)   A – (B ∩  C) = (A – B) ∪ (A – C) 

(7) Idempotent property 

(i) A ∪ A = A 

(ii) B ∩ B  = B 

(8) Absorption laws 

(i) A ∪ (A ∩ B) = A 

(ii) A ∩ (A ∪ B) = A 

(9) Modular laws 

(i) (A ∪ B) ∩ C = A∪ (B ∩ C) iff A ⊆ C 

(ii) (A ∩ B) ∪ C = A ∩ (B ∪ C) iff C ⊆ A 

(10) A ∪ φ A , A ∩ φ = φ 

A ∪ U = U, A ∩ φ = φ 
A  ∪ AC = U, A ∩ AC = φ 

Relation–  Let  A  &  B  be  two  sets  and  some 
elements of A be in certain correspondence with 
some  elements  of  B  then  that    correspondence 
defines  a  relation  between  those  element  of  the 
two set. 
Domain  and  Range  of  Relation–  Let  R  be  a 
relation  from  A  to  B    then  the  elements  of  A 
which  are  in  relation  are  said  to  be  domain  and 
the element of B  which occur in R constitute in 
range of R. 

Discrete Mathematics 

31 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Example–  If  R  =  {(1,  p),  (1,  q),  (2,  q)}  be  a  relation 

then 

Domain = {1, 2}, Range = {p, q} 

Properties of Relation– 

(1) Reflexive relation– A relation R is reflexive 

if for all x∈ A, (x, x) ∈ R 

Example– Let   A = {1, 2}& B = {1, 2, 3} 

R = {(1, 2), (2, 2), (1, 3)} 

Note–  A  relation  R  is  not  reflexive  then  it  is  called 

irreflexive. 

LATTICE 

(2)  Symmetric  Relation–  A  relation  R  is 

  Maximal  element–  In  a  poset,  if  an  element  is  not 

symmetric if (a, b) ∈ R then (b, a) ∈ R 

related to any other element. 

Example– 

A = {1, 2} & B = {1, 2, 3} 

  Minimal  element–  In  a  poset,  if  no  element  is 

R = {(1, 2), (2,1), (2, 2)} 

related to an element. 

(3)  Transitivity  of  a  relation–  A  relation  R  is 

transitive  if  (x,  y)∈R  &  (y,  z)∈R  then  (x, 

z)∈R 

Example– The relation "less then or equal to (≤) i.e. 1 < 

2 & 3 < 4 then 1 < 4. 

Equivalence  Relation–  A  relation  R  is  called 
equivalence relation in A, if 

(1) R is reflexive 

(2) R is symmetric 

(3) R is transitive 

Partial  Order  Relation–  A  relation  R,  defined 
on a set A is called a partial order relation if it is 

 (i) Reflexive 

(ii) Anti symmetric  

(iii) Transitive 

Anti symmetric– If a ≤ b & b ≤ a are true iff a = 
b  so  relation  is  anti-symmetric.  The  set  A  with 
the partial order relation R is called POSET. 

So  (R, ≤) is POSET. 

Total  Order  Relation–  A  partial  order  relation 
R  in  a  set  A  is  called  total  order  relation  if  for 

every element a, b, ∈ A either a R b or b R a or a 
= b. 

To Set–  A  set  with total order relation is called 
To Set. 

Example–  Let  (P,  R)  be  a  poset  and  P  =  {1,  2,  3,  4, 

5}and R is relation of division. 

  We  know  that  3,  4  &  5  are  not  related  to  any 
element.  So,  3,  4  &  5  are  maximal  element  but  no 
element is related to 1. So, 1 is minimal element. 
  LOWER BOUND AND UPPER BOUND 
Upper  Bound–  Let  (P,  R)  be  a  poset  and  B  be  a 
subset of P element x∈A is a upper bound of B if B 
if y is related to x for every y∈B. 

Lower  Bound–  An  element  x∈A  is  a  lower  bound 
of B if x is related to y for every y∈B. 

Function– Let X and Y are two set. a rule in which 
every element of X assigned to unique element of Y, 
then this rule is called Function. 

It is written as f:X→Y. 

Domain  And  Range  of  the  function–  If  f  is  a 
function from A to B then A is called domain and B 
is co-domain.  
Range of Function– The set of all those elements of 
B which are related with elements of A is called the 
range of f. Evidently Range f⊆ B. 

Kind of Function 

(i)  One-one  Function–  Let  f:A→B  be  a  function  it 
is called one-one if x ≠ y ⇒ f(x)  ≠ f(y) for x, y ∈ A 
or if f(x) = f(y) ⇒ x = y. 

HASSE DIAGRAM 
  A graphical representation of a partial order relation 
in  which  all  arrowhead  are  understood  to  be 
pointing upward is known as the Hasse Diagram. 

Example– Let A = {1, 2, 3, 4, 6, 8} be ordered by the 

Example– Let f : R→R s.t f(x) = ax+b, a≠0 

f(x) = f(y) 

  ⇒ f(ax + b) = ay + b 

  ⇒ ax = ay 

  ⇒ x = y 

relation "a divides b". 

Note– If f is not one-one then it is called many one. 

Discrete Mathematics 

32 

YCT 

 
 
 
 
   
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Onto Function– A function f : A → B is called onto 
if Range f = B. 

Bijective–  Let  f:  A  →  B  be  a  function  and  it  is 
called bijective if f is one-one and onto. 

INVERS AND COMPOSITION OF FUNCTION 

Inverse  function–  If  f  :  X  →  Y  is  a  bijection  then 
there always exist pre image f–1(a) of each element a 
of y and this will be a unique element of y. 

Composition function– If f : A → B and g : B → C 

be  two  function  then  the  function  gof : A

C→ ; 

where  gof(x)  =  g[f(x)]  for  all  x  ∈  A  is  the 
composition function of f and g.  

Groups 
Algebraic  structure–  A  non-empty  set  S  is  called 
an  algebraic  structure  with  respect  to  the  binary 
operation '*'. 

then (S, *) is an algebraic structure (N, +) (Z ,+), (Z–
1), (R, +, x) are all examples of algebraic structures. 

Semi-Groups–  An  Algebraic  structure  (S,  *)  is 
called a semi group. 

(a*b)*c = a*(b*c) ∀ a, b, c ∈ S 

* is associative on S. 

  Monoid– An Semigroup (S, *) is called a monoid. 

(i) '*' is closed on G. 

(ii) '*' is associative & 

(iii) e ∈ G such that ∀ a∈M, e*a = a = a*e 

such  an  element  'e'  is  unique  and  is  called  the 
identity element for the monoid. 

Note– Every monoid is a semigroup  the converse is not 

true. 

Group–  An  algebraic  structure  (G,  *)  is  called  a 
group. If the binary operation satisfies the following 
postulates. 

1. Closure property: a * b ∈ G ∀ a, b ∈ G 

2. Associativity : (a*b)*c = a*(b*c)∀a, b, c ∈ G 

3.  Existence  of  identity:  There  exists  an  element 
e∈G such that e*a = a = a*e ∀ a ∈ G. the element e 
is called identity for '*' is G. 

4. Existence of inverse: 
Thus a–1 is an element of G, such that a*A–1 = a–1*a = e 
Abelian  Group  or  Commutative  group–  A  group 
G is said to be abellan.  

Commutative: a * b = b * a ∀ a, b ∈ G. 

Subgroup– Let (G*) be a group. A subset H of G is 
called a sub group of G if (H, *) is a group. 

Cyclic Groups– A group (G, *) is said to be cyclic 
if  there  exists  an  element  a  ∈  G  such  that  every 
element of G can be  written  as 'an'  for some integer 
"n"; then a is called generating element. 
Example– G = {1, –1} is a cyclic  group of order 2 
with respect to multiplication. 
The generator of G = –1. 

  GRAPH THEORY 

Graph–  A  Graph  G  is  mathematical  structure 
consisting  of  two  sets  V  and  E  share  V  is  a  non-
empty  set  of  vertices  and  E  is  a  non-empty  set  of 
edges. 

V1

e1

V2

Basic Termenology– 
(1)  Trivial  Graph–  A  graph  consisting  only  one  vertex 

and no edge. 
Example– 0 

(2)   Null  Graph–  A  graph  consisting  n  vertices  and  no 

edge. 

Example– 0000 

(3)   Directed  Graph–  A  graph  consist  the  direction  of 

edges then is called directed graph. 
V2

V1

e1

e5

e2

e3

e4
(4)   Undirected  graph–  A  graph  which  is  not  directed 

V4

V3

then it is called undirected graph. 

(5)   Self  loop  in  a  graph–  If  edge  having  the  same. 
Vertex as both its end vertexes is called self loop. 

Example– 

e1

V

(6)   Proper  edge–  An  edge  which  is  not  self  loop  is 

called proper edge. 

(7)  Multi  edge–A  collection  of  two  or  more  edge 

having identically end point. 

Example– 

e1, e2, e3 are multi edge 

Discrete Mathematics 

33 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(8)   Simple  graph–  A  graph  does  not  contain  any  self 

loop and multi edge.  

(9)   Multi  graph–  A  graph  does  not  contain  any  self 
loop but contain multi edge is called multi graph. 

V1

e1

e2

e4

V2

V3
(10) Pseudo graph– A graph contain both self loop and 

e3

e5

V4

multi edge is called pseudo graph. 

V1

e1

V2

e7

V6

e6

e5

e2

e3

V3

e4

V5

V4
(11)  Incidence  and  Adjacency–  Let  ek  be  an  edge 
joining  two  vertices  V1  &  V2  then  ek  is  said  to  be 
incident of V1 & V2. 
Two  vertices  are  said  to  be  adjacent  if  there  exist 
and edge joining this vertices. 

Example– 

V1

e2

V2

e1

e3

V3

Here  e1  is  incident  of  V1  &  V2  and  V1  &  V2  are 
adjacent but V3 & V4 are not adjacent. 

(12)  Degree  of  Vertex–  The  degree  of  vertex  V  in  a 
graph G written as d(V) is equal to number of edges 
which  are  incident  on  V  with  self  loop  counted 
twice. 
Example– 

(13)  Isolated  Vertex  &  Pendant  Vertex–  A  Vertex 
having  0  is  called  isolated  vertex  and  a  vertex 
having degree 1 is called pendant vertex. 

(14)  Finite  and  Infinite  Graph–  A  graph  with  a  finite 
number  of  vertices  as  well  as  edge  is  called  finite 
graph otherwise is infinite graph. 

Some Important Graph– 
(i)  A simple connected graph is said to be complete 
if each vertex is connected to every other vertex. 

Example– 
(ii) Regular Graph– A graph G is said to be regular 
if  every  vertex  has  the  same  degree.  If  degree  of 
each  vertex  of  graph  G  is  K,  then  it  is  called  K-
regular graph. 

Bipartite– If the vertex set V of a graph G can 
(iii) 
be partilioned into two non-empty disjoint subset X and 
Y in such a way that edge of G has one end in X and 
one end in Y. Then G is called bipartite. 
Note– If a graph is connected then it will not bipartite. 
(4)  Sub  graph–  Let  G(V,  E)  be  a  graph.  Let  V  be  a 
subset  of  V  and  let  E  be  a  subset  of  E  whose  end 
point belong to V: The G(V, E) is a graph and called 
a sub graph of G(V, E). 
Decomposition  of  Graph–  A  graph  is  said  to  be 
decomposition into two sub graph G1 and G2 if G1 ∪ 
G2 & G1 ∩ G2 = null graph. 

HAND SHAKING THEOREM 
The sum of the degree of the vertices of a graph G is 
equal to twice the number of edges in G. 

  ⇒ 

n

∑

=
i 1

(
deg V
1

)

= ×

2 Number of edges

  MATRIX REPRESENTATION OF GRAPH 
(1)  Adjacency  Matrix–  Let  a1  denote  the  number  of 
edges  (Vi,  Vj)  then  A  =  [aij]m×n  is  called  adjacency 
matrix of G if 

a

ij

(

)

1 if v , v is an edges
j
= 


other wise

0

i

Here  d(V1)  =  2,  d(V2)  ,=  4,  d(V3)  =  2,  d(V4)  =  3, 
d(V5) = 2, d(V6) = 2, d(V7) = 1, d(V8) = 0 

if (V1, Vj) is an edges otherwise 
(2)  Incidence  Matrix–  Let  G  be  a  graph  with  m 
vertices V1, V2, ..... Vm and n edges e1, e2,e3 ..... en 
  Let a matrix M = [Mij]m×n defined by 

Discrete Mathematics 

34 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
m

ij

1 If the vertex V is incident on the ij

i

= 



0 If V is not incident on ij
2 If V is an end of the loop ij

i

i

Path Matrix– Suppose G is a simple directed graph with 
m vertices then path matrix P and Bm have same non zero 
entries where Bm = A1 + A2 + A3...... Am. 
  Where A is adjacency matrix 

ISOMORPHISM OF GRAPH 

Definition– Two graphs G1 & G2 are isomorphic if 
(i)   Number of vertices are same. 
(ii)  Number of edges are same. 
(iii)  An equal number of vertices with given degree 
(iv)  Vertex correspondence & edge correspondence valid. 
Homeomorphic Graph 
Two graph G and G' are said to be homeomorphic if they 
can be obtained from the same graph. 
Note–If  G  &  G'  are  homeomorhpic  they  need  not  be 
insomorphic. 
WALK, TRAIL and PATH 

(1) Walk– A walk is a finite alternating sequence v1 
e1 v2 e2 v3 e3 ... vn en of vertices and edges beginning 
and ending with same or different vertices. 

(i)   Length of the walk– The  number of edge  is called 

length of the walk. 

(ii)  Closed & open walk– A walk is said to be closed if 
its  origin  &  terminus  vertex  (V0  =  Vn)  is  equal 
otherwise it is called open walk. 
Trail: Any walk having different edges called trail. 
Cycle– A closed trail is called circuit. 
Path:  A  walk  is  called  path  if  all  vertices  are  not 
repeated. 
Cycle– A closed path is called cycle. 
EULERIAN PATH– A path in a graph is said to be 
an  Eulerian  path  if  it  traverses  each  edge  in  the 
graph once and only once. 
EULERIAN  GRAPH–  A  connected  graph  which 
contain a Eulerian circuit is called Eulerian graph. 
HAMILTONIAN  PATH–  A  path  which  contain 
every  vertex  of  a  graph  G  exactly  once  is  called 
Hamiltonian graph. 
HAMILTONIAN CIRCUIT– A circuit that passes 
through each of the vertices in a graph G exactly one 
except  the  starting  vertex  &  end  vertex  is  called 
Hamiltonian circuit. 
HAMILTONIAN  GRAPH–  A  connected  graph 
which  contain  Hamiltonial  circuit 
is  called 
Hamiltonian Graph. 

  WEIGHTED  GRAPH–  A  graph  is  called  weighted 
graph if a non-negative integer W(e) associate to each 
edge and this W(e) is a weight of corresponding edge. 
GRAPH COLORING– Painting all the vertices of a 
graph  with  colours  such  that  no  two  adjacent  vertices 
have the same color is called coloring of graph. 
CHROMATIC  NUMBER–  The  least  number  of 
colors required for coloring of a graph G is called its 
chromatic number. 

Note–1.  The chromatic number of graph G is denoted by 

X(G). 
If X(G) = K, then the graph is called K-chromatic. 

2. 
3.  Chromatic number of null graph is 1. 
4.  Chromatic  number  of  complete  graph  Kn  of  n 

5. 

vertices is n. 
If a graph is circuit with n vertices then. 
(i) It is 2-chromatic if n is even 
(ii) If is 3-chromatic if n is odd. 

TREE AND ITS PROPER TIES 

TREE–  A  tree  is  a  connected  graph  without  any 
loop or circuits. 
Rooted  Tree–  A  rooted  tree  is  a  tree  in  which  one 
vertex is root. 
SPANNING  TREE–If  G  is  any  connected  graph  a 
spanning tree in G is a subgroup T of G, which is a tree. 

  Minimal  Spanning  Tree–  Let  G  be  a  weighted 
graph. A minimal spanning with minimum weight. 
Algorithms For Minimal Spanning Tree 
KRUSHKAL's Algorithm  

  Working Rule 

(i)  Choose an edge of minimal weight  
(ii) Al  each  step,  choose  the  edge  whose  inclusion 
will not create a circuit. 
(iii) If G has n vertices stop after (n–1) edges. 

Example– 

  Weight = 3+1+2+1=7 
(2) PRIM'S ALGORITHM 
Working Rule– 
(i)   Select  any  vertex  &  choose  the  edge  and  smallest 

weight from G  

(ii)  At each stage, choose the edge of smallest weight joining 
a vertex already included to vertex not yet included. 

(iii) Continue until all vertices are included. 

Discrete Mathematics 

35 

YCT 

 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    04.  

DIGITAL LOGIC 

Number System 

Decimal System– 
It is a positional number system that uses 10 as a base to represent different values. Therefore, this number system is 
also known as base 10 number system. In this system, 10 symbols are available for representing the value. These 
symbols include the digits from 0 to 9.  
Example,  the  value  237  which  comes  before  the  decimal  point,  is  called  integer  value  and  the  value  25,  which 
comes after the decimal point, is called fraction value. 

Digital Logic 

36 

YCT 

 
Octal  system–    The  octal  system  is  the  positional  number  system  that  used  base  8  to  represent  different  values. 
Therefore,  this  number  system  is  also  known  as  base-8  system.  As  this  system  uses  base  8,  eight  symbols  are  a 
available for representing the value in this system. These symbols are the digits 0 to 7.  
Example, The octal number 215.43 represents the decimal value 141.5469. 

Hexadecimal  system–  The  hexadecimal  system  is  a  positional  number  system  that  uses  base  16  to  represent 
different  values.  Therefore,  this  number  system  is  known  as  base-16  system.  As  this  system  uses  base  16,  16 
symbols are available for representing the value in this system. These symbols are the digits 0-9 and the letters A, B, 
C, D, E and F. The digits 0-9 are used to represent the decimal value 0 through 9 and The letters A, B, C, D, E and F 
are used to represent the decimal value 10 through 15.  
Example, the hexadecimal number 4A9.2B represents the decimal value 1193.1679. 

Decimal to non-decimal conversions 

The decimal to non-decimal (binary, octal or hexadecimal), conversions use the step given below. 
Step 1: Divide the given number by the base value of the number system in which It is to be converted. 
Step 2 : Note the remainder. 
Step 3: Keep on dividing the quotient by the base value and note the remainder till the quotient is Zero. 
Step 4 : Write the noted remainders in the reverse order (from bottom to top). 

 (i) Decimal to Binary conversion– 
Let us now convert a decimal value to its binary representation and verify that the binary equivalent of (65)10 is 
(1000001)2. 

Digital Logic 

37 

YCT 

 
 
 
 
 
 
 
 
(ii).Decimal to Octal conversion– 
The following example illustrate the method of converting decimal number 98 into its equivalent octal number. 

(iii).Decimal  to  Hexadecimal  conversion–  The  following  example  illustrate  the  method  of  converting  decimal 
number to its hexadecimal equivalent. 

Non-decimal to Decimal  Conversions 

The  non-decimal  to  decimal  conversions  can  be  implemented  by  taking  the  concept  of  place  values  not 
consideration  we  can  use  the  following  steps  to  convert  the  given  number  with  base  value  to  its  decimal 
equivalent, where base value can be 2, 8 and 16 for binary, octal and hexadecimal number system, respectively. 
Step 1 : Write the position number for each alphanumeric symbol in the given number. 
Step 2 : Get positional value for each symbol by raising its position number to the base value symbol in the given 
number. 
Step 3 : Multiply each digit with the respective positional value to get a decimal value.  
Step 4 : Add all these decimal values to get the equivalent decimal number. 
(i).  Binary  Number  to  Decimal  Number  conversion–  The  following  example  illustrate  the  method  of 
converting binary number (1101)2 to decimal number. 

      1 
Digit→  
     1 
Positional value→   23 
     2º 
Decimal Number→ 1× 23  +  1×22  +  0×21  +  1× 2º 

      1 
      22 

     0 
     21 

Therefore, 

8      +    4      +    0     +   1  
(1101)2 = (13)10 

= (13)10 

(ii). Octal number to Decimal number conversion– The following example shows how to compute the decimal 
equivalent of an octal number (257)8. 

Digit→  
Positional value→ 
Decimal Number→  

 2 
  5 
  82 
83 
2× 82   + 5×81      +  
128      +       40       +   
(257)8 = (175)10 

7 
81 
7×80 
7  = (175)10 

Therefore, 

Digital Logic 

38 

YCT 

 
 
 
 
 
 
 
 
 
 
    
 
 
               
   
(iii). Hexadecimal Number to Decimal number conversion– The following example Shows how to compute the 
decimal equivalent of an Hexadecimal (3A5)16. 

Digit→  
          3   
Positional value→     162   
Decimal Number→ 3× 162     +    10×161         +  
160      +  
(3A5)16 = (933)10 

    A 
   161 

768         +  

Therefore, 

  5 
 16º 
5×160 

5            = (933)10 

Conversion from Binary number to Octal number and Vice-versa 
(i) Binary number to Octal  Number- Given a binary number, an equivalent octal number representation by 3 
bits is computed by grouping 3 bits from right to left and replacing each 3-bit group by the corresponding octal 
digit.  In  case  number  of  bits  in  a  binary  number  is  not  multiple  of  3,  then  add  required,  number  of  0s  on  most 
significant position of the binary number 
Example – Convert (10101100)2 to octal number. 
Make group of 3-bits of the 
given binary number (Right to left)     
Write octal number for each 3- bit  group.     2 
Therefore, (10101100)2 = (254)8 
(ii) Octal number to Binary number–  Each octal digit is an encoding for a 3-digit binary number. Octal number 
is converted to binary by replacing each octal digit by a group of three binary digits.   
Example–  Convert (705)8 to binary number. 
0 

 101 
   5 

100 
  4 

010 

5 

7 

Octal digit →  
 Write  3-bits binary 

value  for each digit →  
Therefore, 

000 
111 
(705)8 = (111000101)2 

101 

Conversion  from Binary number to Hexadecimal number and vice-versa 
(i)  Binary  Number  to  Hexadecimal  Number–  Given  a  binary  number,  its  equivalent  hexadecimal  number  is 
computed  by  making  a  group  of  4  binary  digits  from  right  to  left  and  substituting  each  4-bit  group  by  its 
corresponding computed by making a group of 4  binary digits from right to left and substituting each 4-bit group 
by its corresponding hexadecimal alphanumeric symbol. If required, add 0 bit on to have number of bit in a binary 
number as multiple of 4. 

Example–  Convert (0110101100)2 to hexadecimal number. 

           Make group of  4-bits of 

the given binary number (Right to left) 
Writ hexadecimal symbol for each group→1 

0001 

1010 
  A 

1100 
  C 

Therefore, (0110101100)2 = (1AC)16 
(ii).  Hexadecimal  number  to  Binary  number–  Each  hexadecimal  symbol  is  an  encoding  for  a  4-digit  binary 
number. Hence, the binary equivalent of a hexadecimal number is obtained by substituting 4-bit binary equivalent 
of each hexadecimal digit and combining them together. 
Example. Convert (23D)16 to binary number. 
Hexadecimal digits→  
Write 4-bit binary for each digit→ 0010  
Therefore, (23D)16 = (001000111101)2 

  3 
0011 

  D 
1101 

  2 

Conversion from octal number to hexadecimal number 
The given octal number can be converted' into its equivalent hexadecimal number in two different  steps. Firstly, 
We need to convert the given octal number into its binary  equivalent.  After obtaining the binary equivalent,  we 
need to making a group of 4 binary digits from Right to left and substituting each 4-bit group by its corresponding 
hexadecimal alphanumeric symbol. In this type of conversion,  we need to represent each digit in the octal number 
to its equivalent 3-bit binary number. 
Example– Convert the octal number (365)8 into its hexadecimal number. 
 3 
Octal digits→ 

 6 

 5 

 Write 3-bits binary value 

for each digit→   

011 

110 

101 

Regrouping into 4-bits of 

the binary number (Right to left)→ 0000  1111 

0101 

for each group→  
Therefore, 

Digital Logic 

Write hexadecimal symbol 

  0 

   F 
   5 
(365)8=(F5)16

39 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
Conversion of a Number with Fractional Part. 

(i) Fractional part of Decimal number to Binary number. 

Example. Convert decimal number (0.25)10 to binary. 

Since the fractional part is 0, the multiplication is stopped. Write the integer part from top to bottom to get binary 
number for the fractional part. 

Example–  Convert (0.675)10 to binary. 

Therefore, (0.25)10 = (0.01)2 

Since  the  fractional  part  (.400)  is  the  repeating  value  in  the  calculation,  the  multiplication  is  stopped,  write  the 
integer part from top to bottom to get binary number for the fractional part. 
Therefore, (0.675)= = (0.1010110)2 

(ii) Fractional part of Decimal number to Octal Number. 
Example– Convert (0.625)10 to Octal Number. 

Since the fractional part is 0, the  multiplication is stopped,  write the integer part from top to bottom to get octal 
number for the fractional part . 

(iii) Fractional part of Decimal number to hexadecimal number. 

Therefore, (0.625)10 = (0.50)8 

Example– Convert (0.675)10 to hexadecimal. 

Since the fractional part (.800) is repeating, the multiplication is stopped, Write the integer part from top to bottom 
to get hexadecimal equivalent for the fractional part. 
Therefore, (0.675)10 = (0.AC)16 

Non-decimal Number with Fractional part to Decimal Number System 

 (i) Fractional part of Binary number to Decimal number. 
Convert (0.111)2 into decimal number. 
    1 
0. 
Digit→   
    2-2 
Fractional value→ 
Decimal value→   

 1 
 2-1 
1×2-1   +    1×2-2     +   1×2-3 

      1 
      2-3 

Therefore,  

Digital Logic 

0.5     +      0.25    +   0.125 = 0.875 

(0.111)2  =  (0.875)10 

40 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
         
 
 (ii) Fractional part of octal number to Decimal number. 
⇒ Convert (0.12)8 into decimal number. 
Digit→   
   0. 
Fractional value→  
Decimal value→    

1 
8-1  
1×8-1         +  

2 
8-2 
2×8-2 
    0.125        + 
(0.120)8  = (0.15625)10 

Therefore 

0.03125 = 0.15625 

 (iii) Fractional part of Hexadecimal number to Decimal number 
⇒ Convert (0.58)16 into decimal number. 
Digit→   
Fractional value→  
Decimal value→   

0. 

5 
16-1 
5×16-1        +  
 0.3125        + 

8 
16-2 
8×16-2 
0.03125 = 0.34375 

Therefore,  

(0.58)16 = (0.34375)10 

Fractional Binary Number to Octal or Hexadecimal Number 

Example– Convert (10101100.01011)2 to octal number. 
Make perfect group of 3-bits→ 
Write octal symbol for each group →  
Therefore, 
 Note– Make 3-bit groups from right to left for the integer part and left to right for the fractional part. 

(10101100.01011)2 = (254.26)8 

100    .  010 
  4        .    2 

110 
  6 

010 
2 

101 
  5 

Example– Convert (10101100.010111)2 to hexadecimal number. 
make perfect group of 4-bits→ 
Write hexadecimal symbol for each group→    A 
Therefore,  

(10101100.010111)2 = (AC.5C)16 

1100   .  0101 
   C      .     5 

 1010 

1100 
   C 

Binary coded Decimal (BCD) systems 

  Weighted 4-bit BCD code- 

Example– Represent the decimal number 5327 in 
weighted BCD code. 
⇒ The given decimal number is 5327 
The  corresponding  4-bit  8421  BCD  representation  of 
decimal digit. 

Therefore,  The  8421  BCD  representation  of  decimal 
number (5327)10 is (0101001100100111)2 
Example–  Convert  the  decimal  number  (87.34)10  to 
weighted BCD code. 
⇒ The given decimal number is 87.34 
The  corresponding  4-bit  8421  BCD  representation  of 
decimal digit 

Therefore,  The  8421  BCD  representation  of  decimal 
number (87.34)10 is  (1000 0111.0011 0100)2. 
Excess-3 BCD Code–  
Example– Convert the decimal number 85 to XS-3 BCD 
code. 
⇒ The given decimal number is 85. now, add 3 to each 
digit of the given decimal number as– 

8 + 3 = 11 
5 + 3 = 8 
The corresponding 4-bit 8421 BCD representation of the 
decimal digit– 

Therefore,  the  XS-3  BCD  representation  of  the  decimal 
number 85 is 1011 1000. 

Digital Logic 

41 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Gray Code 
The Gray code or reflected binary code is an ordering 
of  the  binary  number  system  such  that  two  successive 
values differ in only one bit. Gray cods are very useful 
in the normal sequence of binary number generated by 
the  hardware  that  may  cause  an  error  or  ambiguity 
during the transition from one number to the next. The 
Gary  code  is  not  weighted  that  means  it  does  not 
depends  on  positional  value  of  digit.  This  cyclic 
variable  code  that  means  every  transition  from  one 
value to the next value involves only one bit change.  
Binary  to  Gray  code  conversion–  We  can  convert  a 
number represented in the binary form to the Gray we 
need to remember the following two rules:-  
(i)  The most significant Bit (MSB) of the Gray code is 
always equal to the MSB of the given binary code.  
(ii) Other Bits of the output gray code can be obtained 
by  XORing  binary  code  but  at  that  index  and 
previous index.    

Example-  Convert  the  Binary  number  1011  to  its 
equivalent Gray coded number. 

Hence, the Gray coded equivalent of the binary number 
1011 is 1110. 
Gray  to  binary  conversion-  We  can  convert  the  gray 
coded number to its binary equivalent by remembering 
the following two major rules. 
(i) The most significant bit (MSB) of the binary code is 
always equal to the MSB of the given gray code. 
(ii) Other bits of the output binary code can be obtained 
by checking gray code bit at that index. If current gray 
code  bit  is  0,  then  copy  previous  binary  code  bit,  else 
copy invert of previous binary code bit. 
Example-  Convert  the  Gray  coded  number  11010011 
to its binary equivalent. 

One's complement system 
1's  complement  of  a  binary  number  is  another  binary 
number  obtained  by 
i.e. 
transforming the 0 bit to 1 and the 1 bit to 0.  

toggling  all  bits 

it, 

in 

Example- 1's complement of '1100' is '0011' 
Two's complement system 
2's complement of a binary number is 1, added to the 1's 
complement of the binary number. 
Exmaple- 2's complement of 1100 is ? 
1's  complement  of  1100  is  0011  added  1,  to  the  is 
complement. 

2's complement of '1100' is '0100' 
(cid:1)  Boolean Algebra  
Commutative 
Law 
Associative Law 

• A+B = B+A 

• A.B = B.A 

• A+(B+C) = (A+B)+C  
• A.(B.C) = (A.B)C = ABC 
•  A(B+C) = AB + AC 
•  A+(B.C) = (A+B).(A+C) 
•  (A+B)(C+D) =AC+AD+BC+BD 

+  
•  A (A.B) A B

+

=

=
=
=

    • A(A+B) =A 
+   
+     

•  A AB A
+
•   A AB A B
+
•  A AB A B
+
• ORing-A+A+A + ........ = A 
• ANDing- A.A.A ....... = A 
• A.0 = 0 
• A.1 = A 
•  A.A 0=  

• A.A = A 

• A+A = A 

• A+0 = A 

• A+1 = 1 
• (A+B).(A+C) = A + BC 

=  
•  A A 1
+

•  AB AC BC AB AC

+

+

=

+

=
• A.B A B

+  • A B A.B

+ =

AND ↔ OR 
• Taking all literals as it is. 

•  Complement literals individually 

Distributive 
Law 

Absorption law 

Idempotence 
Law 

AND  
Operation 
Theorem 
OR  Operation 
Theorem 

Transposition 
Theorem 

Consensus or  
Redundancy 
Theorem 
Demorgan’s 
Theorem 
Duality 
Theorem 

Complementary 
Theorem 

Hence, the binary equivalent of gray coded number 
11010011 is 10011101. 

•  A A=

Involution 
Theorem 
Note :-  
(cid:2)  Maximum possible minterm or maxterm = 2n 
n22  
(cid:2)  Maximum possible logical expression = 

Digital Logic 

42 

YCT 

 
 
 
 
 
 
 
 
 
 
 
(cid:2)  Maximum possible self dual expression = 
(cid:2)  AND,  OR,  NAND,  NOR,  XOR  and  X-NOR-  Gate 

−

n 122

follow commutative law 

(cid:2)  AND,  OR,  XOR,  and  X-NOR-  Gate  follow 

associative law 

(cid:2)  NAND  and  NOR-Gate  does  not  follow  associative 

law 

(cid:1)  Logic Gates  
(cid:2)  Logic Gate is a electronics switch which performs the arithmetic and logic function. 
(cid:1)  Basic Gates 
Gate 
Symbol 
NOT  

Diode circuit 

Truth table 

Transistor 

Switch table 

AND  

OR  

(cid:1)  Universal Gate 
NAND  
Gate 

NOR 
 Gate 

Digital Logic 

43 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Diagram 

Truth Table 

(cid:1)  FET as a Switch 

Gate 

JFET 
NOT Gate 

as 

MOSFET as 
NOT Gate 

(cid:1)  Special Purpose Gates 
Gate 

Symbol 

Truth Table 

EX-
OR 

EX-
NOR 

(cid:2) In EXOR operation 
• For BUFFER 
CIRCUIT ⇒ Logic '0' 
• For   INVERSION 
CIRCUIT ⇒ Logic '1' 

(cid:2) In EXNOR operation  
• For BUFFER 
CIRCUIT ⇒ Logic '1'  
• For INVERSION 
CIRCUIT ⇒ Logic '0' 

Logic gates 

No.  of  NAND 
Gate required 
1 
NOT 
2 
AND 
3 
OR 
4 
EX-OR 
5 
EX-NOR 
1 
NAND  
4 
NOR 
(cid:3) Remember point 

No.  of  NOR 
Gate required 
1 
3 
2 
5 
4 
4 
1 

(cid:2)  AND Gate is also called all or nothing gate  
(cid:2)  AND Gate works as a series switch 
(cid:2)  OR Gate is also called any or all Gate 
(cid:2)  OR Gate works as a parallel switch 
(cid:2)  EX-OR gate acts as odd number of  “1’s detector”. 
(cid:2)  EX-OR  gate  is  used  for  even  parity  generator  and 

detector. 

(cid:2)  EX-OR gate is known as stair case switch. 
(cid:2)  EX-NOR gate acts as even number of “1’s detector”. 
(cid:2)  EX-NOR gate is used for odd parity generator. 
(cid:2)  XOR-Gate is also called anti-incidental logic gate. 
(cid:2)  A 0 A
(cid:2)  A 1 A work as inverter
(cid:2)  X-NOR-Gate  is  also  called  equivalence  gate  or 

work as buffer

⊕ = →

⊕ = →

equality detector or co-incident logic gate. 

= →

= →

(cid:2)  A 0 A work as inverter
⊙
(cid:2)  A 1 A
⊙
(cid:2)  NOR and NAND are special logic gates 
⊕ ⊕ = ⊙ ⊙  
(cid:2)  A B C A B C
(cid:2)   A⊕A⊕A⊕ ………n times  

work as Buffer

=

⊙

= 0, (if n = even) 
  = A, (if n = odd) 
(cid:2)  A⊙A⊙A⊙ …………n times   = 1, (if n = even) 
= A, (if n = odd) 
⊕ = ⊕ = ⊙   (cid:2)   A B A B
⊕ = ⊙  
⊙

(cid:2)  A B A B A B
(cid:2)  A B A B A B

= ⊕
Positive logic 
Negative logic 
AND- Gate 
OR- Gate 
OR- Gate 
AND- Gate 
NAND- Gate 
NOR- Gate 
NOR- Gate 
NAND- Gate 
(cid:1)  Positive logic and Negative logic system 
(cid:4)  Positive logic 
(cid:2)  Logic  ‘1’  voltage  level  is  higher  than  logic  ‘0’ 

Bubbled logic 
NOR- Gate 
NAND- Gate 
OR- Gate 
AND- Gate 

Digital Logic 

voltage level 

44 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
(cid:2)  Logic  ‘0’  voltage  level  is  lower  than  logic  ‘1’ 

voltage level 
(cid:4)  Negative logic 
(cid:2)  Logic  ‘0’  voltage  level  is  higher  than  logic  ‘1’ 

voltage level 

(cid:2)  Logic  ‘1’  voltage  level  is  lower  than  logic  ‘0’ 

voltage level 

(cid:1)  Representation of Boolean functions 

(cid:2)  Maximum no. of Boolean expression or function = 
(cid:4) 

n22  
Sum  of  Product  (SOP)  :  Each  product  term  is 
known  as  minterm.  SOP  form  (Σm)  is  used  when 
output is logic 1. Ex.-  (
ABC

ABC

ABC

+

+

)

(

)

(

)

+ +
A B C . A B C . A B C

(cid:4)  Product  of  Sum  (POS)  :  Each  product  term  is 
known  as  maxterm.  POS  form  (ΠM)  is  used  when 
output is logic ‘0’. 
) (
Ex.-  (

+ +
(cid:3) Remember point 
(cid:2)   Maximum possible minterm or maxterm = 2n 
(cid:2)   Maximum possible self dual function = 
(cid:2)  AND-OR  logic  =  NAND-NAND  logic  (Used  in 

+ +

n –122

) (

)

SOP). 

(cid:2)  OR-AND Logic = NOR-NOR logic (Used in POS). 

(cid:1)  Combinational Circuits   

Circuit Diagram 

Half Adder 

Full Adder 

Half 
subtractor 

Full 
subtractor 

Digital Logic 

(cid:1)  Karnaugh Map (K - Map]  
(cid:2)   A  systematic  &  simple  way  of  minimization  of 

Boolean algebra. 

(cid:2)  Minimization using K-map, the solution is not unique. 
(cid:2)   “Gray Code” is used in K-map. 
(cid:2) 
 Number of cells = 2n,  n = Number of variables. 
(cid:4)  Don’t  Care  -    Considered  when  this  is  helping  in 

minimization of Boolean algebra. 
Implicants = Number of minterms/maxterms 

(cid:2) 
(cid:2)   Prime implicants = Number of pairs 
(cid:2)   Essential  Prime  Implicants=  Number  of  prime 

implicants without redundant terms  

(cid:1)   Digital Logic Circuits 
Combinational Circuit 
Present  output  depends  only 
on present input. 

on 

Sequential Circuit 
output 
Present 
depends 
both 
present  input  as  well 
as past output. 
Memory is present. 
Slower.  
Harder to Design. 
Feedback present. 
Clock pulse required. 
Data storing system. 

Ex.- Flip-flop, Latch, 
Counter, Register, 
serial adder etc. 

Implement by 
• 5- NAND gates 
• 5- NOR gates 
• 3- (2 × 1) MUX  
• 2- (4×1) MUX   
•  2-  H.A+  1  OR 
gate 
• 9- NAND gate 
• 9- NOR gate 
• 7- (2 × 1) MUX 

• 5- NAND gates 
• 5- NOR gates 
• 3- (2 × 1) MUX 
• 2- (4×1) MUX 

•  2-  H.S  +  1  OR 
gates 
• 9- NAND gates 
• 9- NOR gates 
• 7- (2 × 1) MUX 

YCT 

No memory present.  
Faster. 
Easy to design. 
No feedback present. 
No clock pulse required. 
Arithmetic operation and 
Boolean operation. 
Ex.- Adder, Substractor, 
Decoder, Encoder, Comparator 
MUX, D-MUX, parallel adder, 
ROM, RAM etc. 

Formula 

=

S AB AB A B
= ⊕  
+
C = A.B 

S = A ⊕ B ⊕ C 
   ABC ABC ABC ABC

=

+

+

+

Co 

(
= ⊕

)
A B .C AB

+

      = AB + BC + CA 

= ⊕  
D AB AB A B

=

+

oB AB=

= ⊕ ⊕  
D A B C

=

+
ABC ABC ABC ABC

+

+

B0

=

(

)
A B .C AB

⊙

+

AB AC BC

+

+

=

45 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
 
 
 
 
In parallel  adder for two n-bits numbers requires-  

• 
  (cid:2)   n Full Adder  
  (cid:2) 
  (cid:2) 

(n–1) F⋅A + 1 H⋅A 
(2n–1) H⋅A + (n–1) OR Gate 

Circuit Diagram 

MUX 

D-MUX 

Decoder 

Encoder 

Specification 
(cid:2) Named as- 
(cid:2)  Data Selector  circuit  (cid:2) Many to One circuit 
(cid:2)  Universal logic circuit (cid:2) Parallel to serial converter 
(cid:2)  Wave form generator  (cid:2) Data Routing 
(cid:2)  m =2n = no. of input lines, no. of output line = 1 
      n = number of select lines 
(cid:2) Named as - 
(cid:2)  Data Distributor circuit     (cid:2) One to many circuit 
(cid:2)  Serial to Parallel Converter 
(cid:2)  Single Input to multiple output 
(cid:2)  No. of input line =1, no. of output lines = 2n 
  No. of select lines = n  
(cid:2)  It  is  a  combinational  logic  circuit  that  converts 
binary  information  from  n  bit  input  lines  to  a 
maximum 2n o/p lines  

(cid:2)  Decoders are used to convert a particular code- 
•   Binary to octal (3×8 lines decoders) 
•   Binary to Hexadecimal (4×16 line decoders) 
•   BCD to decimal (4×10 line decoders) 
•  BCD to 7-Segment display. 
•  The total number of output line m ≤ 2n 
• Decoders are widely used memory system of computer.  
(cid:2) Inversion of Decoder circuit is known as Encoder. 
(cid:2) Encoder is used to convert other codes to binary 

such as - 

•  Octal to Binary encoder (8×3 lines) 
•  Decimal to BCD encoder (10×4 lines) 
•  Hexadecimal to Binary encoder (16×4 lines) 

(cid:1)   Sequential Circuits  
Latch 
Latches use level 
triggering  

No clock pulse 

Build from gates 

Flip-flop 

Flip-flops use edge 
triggering. 

Clock pulse 

Build from latch 

The output changes as per 
the input till enable is 
high. 

The output changes as 
per the input only at 
triggering point. 

Buffer 

• 1 bit memory element. 
• 2 Stable states  
• Bi-stable Multi-vibrator 

Output cannot predict 

Output can predict (0/1) 

(cid:1)  Triggering      Triggering  is  used  to  initiate  the 

operation of latches or flip-flops. 

(cid:4)  Level trigger   
(cid:2)  Edge trigger   
(cid:1)  Clock In Flip-Flop  
(cid:4)  Setup  Time  :  The  time  period  required  to  hold  the 
incoming data before the arrival of clock pulse. 

(cid:2)   This is of the order of 50ns. 
(cid:4)  Hold  Time  :  The  time  period  required  to  hold  the 
incoming  signal  information  after  the  arrival  of 
clock pulse. 

(cid:2)   This is in order of 10-20 ns.  
(cid:2)     Setup Time > Hold Time. 

Digital Logic 

46 

YCT 

 
 
  
 
 
 
 
 
 
 
 
 
 
 
Flip-
Flop 

SR 

JK 

D Flip-
flop 

T  flip-
flop 

Logic Diagram 

Graphical Diagram 

Truth Table 

Characteristics  
Equation 

Q  = S + R Q  
n

n+1

Q = JQ + KQ  
n
n

n+1

Qn+1 = D 

Q

+ =
n 1

+
TQ TQ
n

n

= ⊕  
T Q
n

tpw  <  tpd (FF)  <  T   (cid:2) Edge triggering 

(cid:4)   To Avoid Race Around - 
(cid:2) 
(cid:2)   Master-Slave FF 
(cid:1)   Registers   
(cid:2)   Register is a memory device, which is used for data 

storage & shifting. 

(cid:2)   Register is a group of flip-flops & gates. 
(cid:2)    For n-bit data, the n-flip-flops are required. 
(cid:1)  Shift Register  
(cid:2)  Data can be shifted by single bit. 
(cid:4)    Four types of shift Registers   
Register  Presentation 

Clock pulse 

SISO 

SIPO 

PISO 

PIPO 

Input  Output 

n 

n 

1 

1 

(n–1) 

0 

(n–1) 

0 

(cid:1)   Conversion of Flip-flop   

(cid:1)  Excitation table 
S 
Qn 
J  
0 
0 
0 
1 
0 
1 
0 
1 
x 
1 
X 
x 
(cid:4)  Applications of Flip-flops   

Qn+1 
0 
1 
0 
1 

R 
x 
0 
1 
0 

K 
x 
x 
1 
0 

D 
0 
1 
0 
1 

T 
0 
1 
1 
0 

Serial and Parallel data storage, Data Transfer, 
Serial to Parallel Converter, Parallel to serial converter 
Latch, Counter,  Frequency division, memory 

(cid:3) Remember point 
(cid:2) 

 Race-around  condition  occurs  in  JK-FF  to  store  1- 
bit of Information. [J = K = 1], tpd (FF) << tpw. 
Condition 

always 

(cid:2)   Race-around 

arises 

in 

“Asynchronous circuits.” 

Digital Logic 

47 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
      
 
 
 
 
 
 
 
 
 
(cid:2)  Time delay for SISO shift register- 

∆ =

t N T N

× =

×

1
f

c

fc = Clock frequency 

N = Number of FFs.  
T = Time period of Clock pulse 
 All shift Registers made of JK-FFs. 
In storage registers mostly D flip-flops are used. 

(cid:2) 
(cid:2) 
(cid:1)   Counters  
(cid:2)   Counter is formed by the cascading of FFs. 
(cid:2)   Counter are basically used for – 
(cid:2)   Counting of the number of clock pulses. 
(cid:2)   Frequency division    (cid:2) Timers  (cid:2) In RADAR 
(cid:2)   Frequency Measurement  (cid:2) Wave form generation 
(cid:2)   In each count the binary data is known as “State of 

counter.” 

(cid:2)   Number of states counted by a counter is known as 

‘modules of counter’. 
If  M = Modules = Mod = Total Number of states 

n2≤
      n = Number of bits or flip-flop then   M 
(cid:2)   M = 2n ⇒ Binary Counter or ripple counter 
(cid:2)   M < 2n ⇒ Non-Binary Counter or BCD counter 
(cid:2)  Counters are classified in two categories. 
i.   Asynchronous Counter [Ripple Counter/Series 

Counter] 

ii.  Synchronous Counter [Parallel Counter] 

(cid:2)  Modulus of counter 
(cid:2)  Known as MOD or MOD number 

MOD 2≤

n

Where n = Number of flip-flop 

f

out

=

f
in
N

(cid:2)  Binary Counter 

If  the  sequence  of  the  states  is  either  ascending  or 
descending  order  than  the  counter  is  called  binary 
counter. It is also called as (2n:1) scalar counter 

(cid:2)  Variable modulus counter 
(cid:2) 

It is counter in which the maximum number of state 
can be changed. 

Note:  The  final  state  of  the  counter  sequence  is  called 

It is used as frequency divider circuit 

the terminal counter. 
(cid:4)  Application of counter 
(cid:2) 
(cid:2) 
(cid:2) 
(cid:2)  Output Frequency of two Cascaded Counters  

It generate a required sequence bit 

It create time delay 

Overall Mod of Counters = M.N 

Synchronous counter 

Asynchronous counter 

Overall Output frequency = 

f

=

o

Same  clock  pulse 
is 
applied to individual flip-
flop. 

 Clock  Signal  is  applied 
only the first flip-flop. 

(cid:2)    For n-bits counter if delay for each Flip-flop is tpd 

then total clock period – 

f
i
M.N

Any sequence can be 
generate. 

Fixed sequence [Upper or 
Down] 

T

CLK

n.t≥

(
pd ff

)

, 

f

CLK

≤

1

n.t

(
pd ff

)

f

max

=

1

n.t

(
pd ff

)

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
i.   Ring Counter / End 
Carry Counter 
ii.   Twisted Ring 

Counter / Johnson 
Counter 

iii.   Synchronous-series 
carry counter 

iv.  Synchronous-parallel 

carry counter 

Types: 
i.  Ripple Up Counter 
ii.  Ripple Down 
Counter 

iii.  BCD Counter (Non-

Binary) 
 iv. Up counter 
v.   Down counter 

(cid:4)  Synchronous counter 

(cid:4)  Ring Counter 

Digital Logic 

48 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:2)  Ring counter works as SISO 

(cid:2) 

(cid:4) 

It is also called n:1 counter 

Johnson Counter 

(cid:2)  Maximum count value = (2n–1) 

(cid:2)   Synchronous-series carry counter, 

f

CLK

≤

1
)
n – 2 t

t

pd (FF)

+

(

pd AND Gate

(

)

(cid:2)  Synchronous-parallel carry counter, 

(cid:1)  Trick to Identify Counter (Ripple counter)   

Clock (Triggering) 

Output 

Counter  

Positive edge 

Negative edge 

Q 

Q  

Q 

Q  

Down-counter 

Up-counter 

Up-counter 

Down-counter 

(cid:1)  3-bit up-down ripple counter 

f

CLK

≤

t

pd(FF)

+

1
t

pd AND Gate

(

)

If  M = 1 (cid:5) up counter,        If M = 0 (cid:5) down counter

(cid:2) 

It is the ‘fastest counter”. 

Counter 

Number 

Unused 

Output 

(cid:3) Remember point 

of states, 

state 

frequency 

(cid:2)   The  Ring  counter  and  Johnson  counter  are  not  use 

M 

10 

BCD/Mod-10 

counter 

Ring counter 

n 

6,  

(2n – M) 

2n – n 

Johnson/Ring 

2n 

2n – 2n 

Twisted counter 

(cid:1)  Asynchronous counter 

(cid:4) 

3-bit binary ripple up counter 

fo 

fo = 

f

o

=

f

o

=

if
10

f
i
n

f
i
2n

(cid:4) 

3-bit binary ripple down counter 

for counting purpose. 

(cid:2)  Johnson Counter also known as- 
(cid:2)   Twisted Ring counter 

(cid:2)   Mobies Counter 

(cid:2)   Switch tail Ring Counter   

(cid:2)   Creeping counter 

(cid:2)   Walking counter 
(cid:2)   In  ring  counter  all  flip-flops  output  frequency 

remain same but phase shift is different and equal to 
3600/n, (where, n= number of state) 

(cid:2)   “Lock out” problem occurs in non-binary counter. 

(cid:2)    JK, SR, D and T are called synchronous Input. 

(cid:2)    Reset and Set are called Asynchronous Input. 

(cid:2)    “Preset” always make the output to ‘1’. 

(cid:2)    “Clear” always make the output to ‘0’. 

(cid:2)    “Glitch” is an unwanted spike in the signal. 

(cid:2)    MOD-16 counter could also  be called a “divide-by-

16 counter”. 

Digital Logic 

49 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   05.   DATABASE MANAGEMENT 
SYSTEMS 

Introduction to DBMS 

Characteristics of DBMS 

(cid:1)  It user a digital repository established on a server to 

store and manage the information.  

(cid:1)  It  can  provide  a  clear  and  logical  view  of  the 

process that manipulates data.   

  Database management system is the combination of 

(cid:1)  DBMS  contain  automatic  backup  and  recovery 

two words. 

Database + Management System = DBMS 
Data base 

It is a collection of related data. 

  Data  base  management  system  is  a  collection  of 
programs  that  enables  users  to  create  and  maintain 
the database. 

Structured Database 

Structured  data  is  highly  specific  and  is  stored  in 
predefined format. 

Structured data store in relation form 

Example– IRCTC, University 
  Unstructured–  Unstructured  data  is  information 
that either does not have a predefined data model or 
is not organised in a pre-defined manner. Example- 
Web pages. 

(cid:1)   

procedures. 

(cid:1)  It contain ACID properties which maintain data in a 

healthy state in case of failure.   
(cid:1)  It is used to provide security of data. 
Application of DBMS 
1.  Banking–  for  maintaining  customer  information, 

loans and banking transactions. 

2.  Universities–  for  maintaining,  student  records, 

registration etc. 

3.   Railway Reservation– for checking the availability 

of reservation in different trains, tickets etc. 

4.  Sales–for 

customer, 

product 

and 

purchase 

information. 

5.   Hospital  system–  the  hospital  system  which  deals 

with in patients as well as out-patients. 

(cid:1)  DBMS can also be define as a interface between the 
application  program  and  the  operating  system  to 
access and manipulate that database. 

to  manage 

(cid:1)  Database management system is a software which is 
the  database  for  example– 
used 
MYSQL,  ORACLE  etc.  are  a  very  popular 
commercial  database  which  is  used  in  different 
applications. 

Advantages of DBMS 

•  Control  database  redundancy–  It  can  control 
data  redundancy  because  it  stores  all  the  data  in 
one single database file and that recorded data is 
placed in the database. 

Database Management Systems  

50 

YCT 

 
 
 
 
 
 
 
  
 
 
 
 
 
 
•  Data  sharing–  In  DBMS,  the  organization  users 
of  an  organization  can  share  the  data  among 
multiple users. 

•  Easily  maintenance– 

easily 
maintenance  due  to  the  centralized  nature  of  the 
database system. 

can 

be 

It 

•  Multiple  user  Interface–  It  provides  different 
like  graphical  user 

types  of  user 
interface, application program interfaces. 
Disadvantages of DBMS 

interface 

•  Cost  of  Hardware  and  Software–  It  requires  a 
high  speed  of  data  processor  and  large  memory 
size to run DBMS software. 

  Size– It occupies a large space of disks and large 

memory to run them efficiently. 

•  Complexity–  Database  system  creates  additional 

complexity and requirements. 

File System Vs DBMS 

File  based  system  were  an  early  attempt  to 
computerize the manual system. 
Example– 

(cid:1)  Consider an example of students file system. 
(cid:1)  The  student  file  will  contain  information  regarding 

the student (rollno., studentName etc.).   

(cid:1)  We have subject file that contain information about 
the  subject  and  result  regarding  the  result.  File 
which contains the information regarding the result. 

Basic 

DBMS 

File System 

Sharing 

of 

Data  sharing  is 

So, it is not easy 

Data 

easy 

to share data 

Security  and 

DBMS  provides 

The  file  system 

protection 

good  protection 

does  not  have  a 

mechanism 

crash 

mechanism 

Cost 

The 

database 

The  file  system 

system 

expensive 

design 

is 

to 

approach 

cheaper 

design 

is 

to 

Data 

Due 

to 

the 

There  exists  a 

Redundancy 

Centralization 

lot 

and 

the database, the 

duplication 

of 

of 

Inconsistency 

problems 

of 

data  which  may 

data  redundancy 

lead 

to 

and 

inconsistency 

inconsistency 

are controlled 

Structure 

The 

database 

The  file  system 

structure 

complex 

design 

is 

to 

approach  has  a 

simple structure 

2 tier layer 

DBMS 
(cid:1)  A  data  base  is  a  well-organized  collection  of  data 

that are related in a meaningful. 

(cid:1)  Different users but stored only one in a system. 
(cid:1)  The  various  operation  performed  by  the  DBMS 

system are Insertion, Deletion, Selection etc. 

(cid:1)  2 

tier  architecture  also  called  client  server 

architecture.   

(cid:1)  direct communicates 

example– Indian Railway 

(cid:1)  The application on client side interact directly with 

the data base present at the server side.   

Figure, duplication of data is reduced due to 
centralization of data. 

Database Management Systems  

51 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3 tier architecture 

  Network  Model–  The  network  database  model 

allows each child to have multiple parents. 

(cid:1)  All 

the  web  application  are  kind  of  3 

tier 

architecture.   

(cid:1)  There  is  no  direct  communication  between  client 

and server. 

  Application  Server–  This  called  business  layer.  It 
act  as  a  middle  layer  between  the  client  and  the 
database  server  and  exchange  partially  processed 
data. 

  Data base layer– The data or information is stored. 
  Client layer– The main purpose is to communicate 

with the application layer. 
Schema– 
is 
representation of the database. 
There can be multiple tables in a schema. 

Schema 

actually 

a 

logical 

DATA MODELS 
(cid:1)  Data model is the modeling of the data description, 
data  semantics  and  consistency  constraints  of  the 
data. 

Four Types of DBMS System are– 

• Hierarchical data base 
• Network data base 
• Relational data base 
• ER model data base  

  Hierarchical  DBMS  –  In  a  Hierarchical  database, 
model data is organized in a tree-like structure. Data 
is  stored  Hierarchically  (top  down  or  bottom  up) 
format. 

  Relational  Model–  Relational  DBMS  is  the  most 
widely  used  DBMS  model  because  it  is  one  of  the 
easiest. 
ER  Model–  ER  model  is  based  on  the  notion  of 
real-world entities and relationship among them. 
ER  Model  creates  entity  set,  relationship  set; 
general attributes and constraints. 

DBMS LANGUAGES 
  Data  base  languages  are  used  to  read  update  and 

store data in a database. 

•   DDL  –  Data  Definition  Language.  (CREATE, 
DROP,  ALTER,  TRUNCATE,  COMMENT, 
RENAME) 

•   DML  –  Data  Manipulation  Language.  (INSERT, 

UPDATE, DELETE, SELECT) 

•   DCL–Data Control Language (GRANT, REVOKE) 
•   TCL  –  Transaction  Control  Language  (COMMIT, 

ROLLBACK) 

DDL (Data Definition Language) 
DDL  actually  consists  of  the  SQL  commands  that  can 
be used to define the database schema.  
CREATE–  It  is  used  to  create  the  database  or  its 
objects  (Like 
table,  Index,  function  views  store 
procedure and triggers). 
There are two CREATE statements available in SQL. 

1. CREATE DATABASE 
2. CREATE TABLE   

CREATE  DATABASE–  The  CREATE  DATABASE 
statement is used to create a new data base in SQL. 
Syntax–  

CREATE DATABASE database_name; 

Example– 

SQL>CREATE DATABASE Employee; 
In  order  to  get  the  list  of  all  the  database,  you  can 
use SHOW databases statement. 
SQL > SHOW DATABASE; 

  CREATE  TABLE–  The  CREATE  TABLE 
statement is used to create  table in  SQL  we  know 
that a table comprises of rows and columns. 

Database Management Systems  

52 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Syntax– 

CREATE TABLE table_name 
( 
Column1 data_type(size), 
Column2 data_type(size), 
Column3 data_type(size), 
....... 
); 

Example  Query–  This  query  will  create  a  table 
students with three columns, RoLL_No, NAME and 
SUBJECT. 
CREATE TABLE students 
( 
RoLL_No int(3) 
  NAME Varchar (20), 

SUBJECT Varchar (20), 
); 

  DROP– 
•   DROP  is  used  to  delete  a  whole  database  or  just  a 

table. 

•   A  DROP  statement  in  SQL  removes  a  component 
from  a  relational  database  management  system 
(RDBMS). 

Syntax– 
  DROP object object_name; 
Example– 
  DROP TABLE table_name; 

table_name:  Name  of  the  table  to  be  deleted. 
DROP DATABASE database_name; 
database_name:  Name  of  the  data  base  to  be 
deleted. 
TRUNCATE– It is used to remove all records from 
a  table,  including  all  spaces  the  TRUNCATE 
TABLE  my  table  statement  is  logically  equivalent 
to  the  DELETE  FROM  my  table  (without  a 
WHERE clause). 

Syntax–  

TRUNCATE TABLE table_name; 

  DROP Vs TRUNCATE– 
•   Truncate  is  normally  ultra  fast  and  its  ideal  for 

deleting data from a temporary table. 

•   Table  or  database  deletion  using  DROP  statement 

cannot be rollback so it must used wisely. 
To delete the whole database 
  DROP DATABASE student_data; 
  After running the above query  whole database  will 

be deleted. 
To truncate student_details table from  student_data 
database. 
TRUNCATE TABLE student_details; 

•   ALTER (ADD, DROP, MODIFY) 
  ALTER  TABLE  is  used  to  add,  delete/drop  or 
modify columns in the existing table. It is also used 
to  add  and  drop  various  constraints  on  the  existing 
table. 

  ALTER TABLE_ADD– 

•   ADD is used to add columns into the existing table. 

Syntax–  
  ALTER TABLE table_name; 

ADD(Columnname1 datatype, 
Columnname2 datatype, 
....... 

columnnamen datatype); 

ALTER TABLE_DROP– 
•   DROP COLUMN is used to drop column in a table. 
Syntax– 
  ALTER TABLE table_name; 
  DROP COLUMN column_name; 
  ALTER  TABLE_MODIFY–  It  is  used  to  modify 

the existing columns in a table. 

syntax–  
  ALTER TABLE table_name; 
  MODIFY Column_name column_type; 
  QUERY: 

TO  ADD  2columns  AGE  and  COURSE  to  table 
student. 

  ALTER  TABLE  student  ADD  (AGE  number  (3), 

COURSE Varchar(40)); 

DML 

The SQL commands that deals with the manipulation of 
data  present  in  the  database  belong  to  DML  and  this 
includes most of the SQL statements. 
SELECT  statement–  select  statement  is  used  to  fetch 
data  from  relational  database.  SQL  select  statement  or 
SQL select query is used to fetch data from one or more 
than one tables. 
Syntax– One Column: 
  Here  column_name  is  the  name  of  the  column  for 
which  we  need to fetch data  and table_name is  the 
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

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
INSERT INTO statement– 

INSERT  INTO  student  of  SQL  is  used  to  insert  a 
new row in a table. 
INSERT  INTO 
value2, value3 .......); 

table_name  VALUES  (value1, 

Example– 
  method1 (Inserting only values): 

INSERT INTO student values ('5' 'HARSH' WEST 
BENGAL; 19;) 

Method2 

(Inserting  values 

in  only 

specified 

columns); 

INSERT INTO student(Roll_NO, Name, Age) 
  VALUES ('5' PRATIK, '19'); 
UPDATE statement– 

The  UPDATE  statement  in  SQL  is  used  to  update 
the data of an existing table in database. 

Basic syntax– 
  UPDATE Table Name 

SET  Column_name1  =  value,  column_names2  = 
value ...... 

  WHERE condition;  
Example- 

SQL > update EMPLOYEES 
SET EMP_SALARY = 10000 

  WHERE EMP_AGE > 25; 
Example- 

SQL > UPDATE EMPLOYEES 

SET EMP_SALARY = 120000 
  WHERE EMP_NAME = 'APOORV'; 

  DELETE  statement–  The  DELETE  statement  in 
SQL is used to delete existing records from a table. 

Syntax–  
  DELETE FROM table_name WHERE 

some_condition;   

DCL (Data Control Language) 

GRANT– Give users access privileges to database. 
REVOKE– Withdraw users access privileges given by 

using the GRANT command. 
TCL (Transaction Control Language) 
COMMIT – Commit a Transaction 
ROLLBACK– rollback a transaction in case of any 
error occurs. 

SAVE POINT– Set a save point with in a transaction. 
ACID Properties 
  ACID  properties  are  used  for  maintaining  the 
integrity of database during transaction processing. 

  ACID  in  DBMS  stands  for  atomicity,  consistency, 

Isolation and Durability. 

  Atomicity–  A  transaction  is  a  single  unit  of 

operation.  You  either  execute  it  entirely  or  do  not 
execute it at all. There cannot be partial execution. 
  Consistency–  Once  the  transaction  is  executed,  it 
should move from one consistent state to another. 
  Durability–  After  successful  completion  of  a 
transaction,  the  changes  in  the  database  should 
persist. Even in the case of system failures. 

Relational Model Concepts 
1.   Attribute–  Each  column  in  a  table.  Attributes  are 
relation  e.g. 

the  properties  which  define  a 
students_Rollno, Name, etc. 

2.   Tables–  In  the  Relational  model  the  relations  are 

saved in the table format. 
Tuple–  It  is  nothing  but  a  single  row  of  a  table, 
which contains a single record. 

  Relation schema– A relation schema represents the 

name of the relation with its attributes. 

  Degree– The total number of attributes which in the 

relation is called the degree of the relation. 

  Cardinality – Total number of rows present in the 

Table. 

  Relation key – Every row has one, two or multiple 

attributes, which is called relation key. 

ER Model 

ER Model stands for an entity-Relationship model. 
It is a high-level data model. 

Example– Suppose we design a school database. 

ER Diagram 

1.   Entity– An entity many be any object, class, person 

or place. 
Ex– Manager, product, employee etc. 

Database Management Systems  

54 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(a) Weak entity– An entity that depends on another 
entity called a weak entity. 

Loan

Installment

2.   Attribute–  The  attribute  is  used  to  describe  the 

property of an entity. 
For example– Id, age, contact number, name etc. 

(a)  Key  attribute–  The  key  attribute  is  used  to 
represent  the  main  characteristics  of  an  entity 
represent a primary key. 

(a)  One-to-one  relationship–  When  only  one 
the 
instance  of  an  entity 
relationship. 
Example–  A  female  can  marry  to  one  male  and  a 
male can marry to one female. 

is  associated  with 

(b) One-to-many relationship 
Example–  Scientist  can  invent  many  inventions, 
but  the  invention  is  done  by  the  only  specific 
scientist. 

(c) Many-to-one relationship 
Example– Student enrolls for only one course, but a 
course can have many students. 

(b)  Composite  attribute–  An  attribute 
that 
composed  of  many  other  attributes  is  known  as  a 
composite. 
The composite attribute is represented by an ellipse. 

(d) Many-to-many relationship 
Example–  Employee  can  assign  by  many  projects 
and project can have many employees. 

Notation of ER Diagram 

(c)  Multivalued  Attribute–  An  attribute  can  have 
more than one value. 

  A student can have more than one phone number. 

(d)  Derived  attribute–  It  can  be  represented  by  a 
dashed ellipse. An attribute that can be derived from 
other attribute. 

Integrity Constraint 

3.   Relationship–    Diamond  or  rhombus  is  used  to 
represent the relationship.  A  relationship is  used  to 
describe the relation between entities. 

Database Management Systems  

55 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
1.   Domain  Constraints–  Defined  of  a  valid  set  of 

4. Key constraints– Its entity set uniquely. 

values of an attribute. 
Example– 

ID 

1000 

1001 

1002 

1001 

NAME 

Tom 

Johnson 

Kate 

Morgan 

17 

SEMESTER  AGE 
1st  
2nd  
3rd  
8th  

24 

22 

21 

2.   Entity  Integrity–  The  entity  integrity  state  that 

primary key value can't be null. 
Example–  

3.  Referential  Integrity–  Referential  integrity  in 
DBMS is based on primary and foreign key. the rule 
defines that a foreign key have a matching primary 
key. 
Example– 
<Employee> 

EMP_ID 

EMP_NAME  DEPT_ID 

<Department> 

DEPT_ID  DEPT_NAME  DEPT_ZONE 

The  rule  states  that  the  DEPT_ID  in  the  employee 
table  has  a  matching  valid  DEPT_ID  in  the 
Department table. 

To  allow 

join  Primary  Key  and 

Foreign Key have same data types. 

EMP_ID 

EMP_NAME 

DEPT_ID 

01 

02 

03 

Rahul 

Kumar 

Raj 

D01 

D02 

D03 

Not allowed because all row must be unique. 

KEY IN DBMS 
(cid:1)  Key is dbms is an attribute or set of attributes which 
helps  you  to  identify  a  row  (tuple)  in  a  relation 
(table). 

(cid:1)  Key help you to identify any row of data in a table. 
In  a  real  world  application,  a  table  could  contain 
thousands of records. 
There are mainly seven different types of key. 
Super  Key–  A  super  key  is  a  group  of  single  or 
multiple keys which identifies row in a table. 
Primary Key– Primary key is a column or group of 
columns in a table that uniquely identify every row 
in that table. 

  Candidate Key– Candidate key is a set of attributes 
that  uniquely  identify  tuples  in  a  table  Candidate 
key is a super key with no repeated attributes. 

  Alternate Key– Alternate key is a column or group 
of  columns  in  a  table  that  uniquely  identify  every 
row in that table. 
Foreign Key– Foreign key is a column that creates 
a  relationship  between  two  tables  the  purpose  of 
foreign  key  is  to  maintain  data  integrity  and  allow 
navigation  between  two  different  instances  of  an 
entity. 

  Compound Key– Compound key has two or more 
attributes  that  allow  you  to  uniquely  recognize  a 
specific record. 
Surrogate  Key–  An  artificial  key  which  aims  to 
uniquely  identify  each  record  is  called  surrogate 
key.  
Primary Key Example–  
CREATE TABLE PERSONS ( 

Primary Key 

Foreign Key 

ID int Not NuLL 
LastName varchar(255), 
first Name varchar(255), 

DEPT_ID  DEPT_NAME 

DEPT_ZONE 

  Age int, 

D01 

D02 

D03 

Computer 

Science 

Art 

East 

West 

South 

PRIMARY Key (ID) 
); 
Create Primary Key (ALTER TABLE statement) 

Database Management Systems  

56 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Syntax– 

the syntax to create a primary key using the ALTER 
TABLE statement in SQL is; 
  ALTER TABLE table_name; 

Syntax: σp(r). 
•  σ is the predicate. 
• 
•   p is prepositional logic.  

r stands for relation which is the name of the table. 

ADD CONSTRAINT constraint_name, 
PRIMARY Key (column1, column2, ...... 

column_n); 

FOREIGN KEY ON CREATE TABLE 
 the  following  SQL  creates  a  FOREIGN  KEY  on 
the  "personID"  column  when  the  "orders"  table  is 
created. 
CREATE TABLE ORDERS ( 
order ID int NOT NuLL,  
orderNumber int NoT NuLL, 
personID int, 
PRIMARY KEY (orderID), 
Foreign KEY (person ID) REFERENCES 

persons (person ID) 
  ); 

Relational Algebra 

Relational  Algebra  is  procedural  query  language, 
which  take  relation  as  input  and  generates  relation 
as output. 
Relational  Algebra  works  on  the  whole  table  at 
once,  so  we  do  not  have  to  use  loops  etc  to  iterate 
over all the rows of data one by one.  

Example: σ age>17(student) 
This will fetch the tuples (rows) from table student,, 
for which age will be greater than 17. 

σage>17 and gender = 'Male' (student) 

This  will  return  tuples  (rows)  from  table  student 
with information of male students, of age more than 
17.   

BRANCH_NAME  LOAN_NO  AMOUNT 

Down town 

Redwood 

Perryride 

Downtown 

Mianus 

Roundhill 

Perryride 

L-17 

L-23 

L-15 

L-14 

L-13 

L-11 

L-16 

1000 

2000 

1500 

1500 

500 

900 

1300 

Input:  
σBRANCH_NAME="Perryride"(LOAN) 
Output: 

BRANCH _ NAME LOAN _ NO AMOUNT

Perryride

Perryride

−
L 15

−
L 16

1500

1300

2.   Project Operation (π) 
•   Project  operation  is  used  to  project  only  a  certain 

only a certain set of attributes of a relation. 

•   In simple words, if you want to see only the names 
all of the students in the student table, then you can 
use project operation. 
 Syntax of project Operator (π)–  
π 
column_nameN(table_name) 

column_name1, 

column_name2, 

______ 

(cid:1)  Basic/Fundamental Operations– 

1. Select (σ) 

2. Project (π) 

3. Union (∪) 
4. Set difference (–) 
5. Cartesian product (×) 
6. Rename (P) 

1.   Select  operation  (σ)–  This  is  used  to  fetch  rows 
(tuples) from table (relation) which satisfies a given 
condition.  

Example– 

πName,Age(student) 

  Above statement will show as only the Name and Age 

columns for all the rows of data in student table. 

3.   Union  Operation  (∪):  This  operation  is  used  to 
fetch  data  from  two  relation  (tables)  or  temporary 
relation (result of another operation). 

Syntax: A∪B 

π student (Regular class) ∪ πstudent (extraclass) 
4.   Set  difference  (–):  This  operation  is  used  to  find 
data  present  in  one  relation  and  not  present  in  the 
second relation. 

Database Management Systems  

57 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Syntax– 
  A–B where A and B are relations. 
Example–  If  we  want  to  find  name  of  student  who 
attend the regular class but not the extra class, then 
we can use the below operation. 

πstudent (Regular class) – πstudent (Extra class) 
5.   Cartesian  product  (×)–  This  is  used  to  combine 
data  from  different  relation  (tables)  into  one  and 
fetch data from the combined relation. 

Syntax–  
6.   Rename operation (P)–  

(A×B) 

•  This  operation  is  used  to  rename  the  output 
relation for any query operation which returns result 
like select, project etc. 

Syntax– P(Relation New, Relation old) 

the  rename  operation  is  used  to  rename  the  output 
relation. It is denoted by rho (ρ). 
JOIN in DBMS 
•   A JOIN  clause is  used to  combine rows  from  two or 
more tables, based on a related column between them. 

•   Join  in  DBMS  is  a  binary  operation  which  allows 
you  to  combine  Join  product  and  selection  in  one 
single statement. 

Types of SQL JOIN 

1. INNER JOIN 
2. LEFT JOIN 
3. RIGHT JOIN 
4. FULL JOIN 
Example–  EMPLOYEE 

EMP _ ID EMP _ Name

Angelina

Robert
Christain
Kristen

1

2
3
4

5

PROJECT– 

CITY
Chicago

Austin
Denver
Wash int on

SALARY AGE

200000

300000
100000
500000

200000

30

26
42
29

36

Russell

Losangels

PROJECT _ NO EMP _ ID DEPARTMENT

101
102

103

104

1
2

3

4

Testing
Development

Designing

Development

1.   INNER  JOIN–  In  SQL  INNER  JOIN  selects 
records that have  matching  values in both tables as 
long as the condition is satisfied. 

Syntax– 

SELECT tables1.column1, table1.column2 
FROM table1 INNER JOIN table2 

  ON 

table1.matching_column=table2.matching_columns 

Query– 

SELECT EMPLOYEE.EMP_NAME,  
 PROJECT.DEPARTMENT 
FROM EMPLOYEE INNER JOIN PROJECT 

  ON PROJECT.EMP_ID = EMPLOYEE_ID 
Output– 

EMP _ NAME DEPARTMENT

Angelina
Robert

Christian

Kristen

Testing
Development

Designing

Development

2.   LEFT  JOIN–  The  SQL  Left  JOIN  returns  all  the 
values from left table and the matching values from 
the right table. 
•  If  there  is  no  matching  join  value,  it  will  return 

NULL. 

Syntax– 

SELECT  table1.column1,  table1.column2  FROM 
table1 LEFT JOIN table2 

  ON 

table1.matching_column=table2.matching_column: 

QUERY– 

EMPLOYEE.EMP_NAME, 

SELECT 
PROJECT.DEPARTEMENT 
FROM EMPLOYTEE LEFT JOIN PROJECT 
  ON PROJECT.EMP_ID=EMPLOYEE.EMP_ID; 
Output– 

EMP _ NAME DEPARTMENT

Angelina

Robert
Christian

Kristen

Russell

Marry

Testing

Development
Designing

Development

NULL

NULL

3.   RIGHT  JOIN–  IN  SQL,  RIGHT  JOIN  returns  all 
the  values  from  the  values  from  the  rows  of  right 
and the  matched  values from  the left table. If there 
is no matching in both tables, it will return NULL. 

Database Management Systems  

58 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Syntax– 

SELECT table1. column1, table1.column2 
FROM table1 RIGHT JOIN table2 

  No 

table1.matching_column 

= 

table2.matching_column_, 
4. FULL JOIN– In SQL, FULL JOIN is the result 
of  a  combination  of  both  left  and  right  outer  join. 
Join  table  have  all  the  records  from  both  tables.  It 
puts NULL on the place of matches not found. 

Syntax– 

SELECT table1.column1, table1.column2 
FROM table1 FULL JOIN table2 

  ON 

table1.matching_column=table2.matching_column; 

SQL Basic Structure 
1.    Basic  structure  of  an  SQL  expression  consists  of 

select, from and where clauses. 
•  From clause corresponds to cartesian product lists 

relation to be used. 

•  Where clause corresponds to seclection predicate 

in relational algebra. 

  To  fetch  the  entire  table  or  all  the  fields  in  the 

table. 

•  SELECTFROM table_name; 

WHERE SQL Clause 

  WHERE  clause  s  used 

to  specify/apply  any 
condition while retrieving, updating or deleting data 
from  a  table.  This  clause  is  used  mostly  with 
SELECT, UPDATE and DELETE query. 
The basic syntax of the SELECT statement with the 
WHERE clause is as shown below– 
SELECT  column1,  column2,  columnN  FROM 
table_name;   

ID  NAME  AGE  ADDRESS  SALARY 

Ramesh  32 

Ahmadabad  2000.00 

1 

2 

3 

4 

5 

6 

Khilan 

25 

Kaushik  23 

Delhi 

Kota 

Chaitali  25 

Mumbai 

Hardik 

Komal  

21 

22 

24 

Bhopal 

MP 

Indore 

7  Mufty 

500.00 

2000.00 

6500.00 

8500.00 

4500.00 

1000.00 

SQL > SELECT ID, NAME, SALARY 

FROM CUSTOMERS 

  WHERE SALARY > 2000; 

Example– 
Consider the CUSTOMERS table having the  following 
records– 
The  following  code  is  an  example  which  would  fetch 
the ID, Name and salary fields from the CUSTOMERS 
table, where the salary is greater than 2000– 

This would produce the following result. 

ID  NAME  SALARY 

4 

5 

6 

Chaitali  6500.00 

Hardik 

8500.00 

Komal  

4500.00 

7  Mufty 

1000.00 

•  From Clause 
•  From  clause  can  be  used  to  specify  a  sub  query 

expression in SQL. 

•  Sub  queries  in  the  from  clause  are  supported  by 

most of the SQL implementation. 

Syntax– 

SELECT column1, column2 FROM 
(SELECT column_x as C1, column_y FROM table 
WHERE  PREDICATE_x)  as 
table2  WHERE 
PREDICATE; 

SET  Operations 
1. 
2. 
3.  
4. 

UNION 
UNION ALL 
INTERECT 
MINUS 

Functional Dependency 

Functional  dependency  (FD)  is  a  set  of  constraints 
between  two  attributes  in  a  relation  functional 
dependency says that if two tuples have same values 
for attributes  A1,  A2, ..... An then those two tuples 
must  have  to  have  same  values  for  attributes  B1, 
B2, ....... Bn. 
Functional  dependency  is  represented  by  an  arrow 
sign (→) that is, 

X → Y 

(cid:1)  Trivial– If 

 a  functional  dependency  (FD)  X→Y 
holds  where  Y  is  a  subset  of  X,  then  it  is  called  a 
trivial FD. Trivial FDs always hold. 

  Non-Trivial–  If  an  FD  X  →  Y  holds,  where  Y  is 
not a subset of x, then it is called a non-trivial FD. 
  Completely  non-trivial–  If  an  FD  X→Y  holds, 
where  X  intersect  Y  =  φ,  it  is  said  to  be  a 
completely non-trivial FD. 

(cid:1)  Armstrong's  Axioms–  If  F  is  a  set  of  functional 
dependencies then the closure of F, denoted as F+, is 
the  set  of  all  functional  dependencies  logically 
implied by F. 

Database Management Systems  

59 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
• Armstrong rules– 
1. Reflexive Rule 
2. Augmentation Rule 
3. Transitivity Rule 

Aggregate function in SQL 

SQL  aggregation  function  is  used  to  perform  the 
calculations on multiple rows of a single column of 
a table. 
• Aggregate functions 

1. count() 

2. sum() 

3. avg() 

4. min() 

5. max() 

Trigger– A trigger is a stored procedure in database 
which  automatically  invokes  whenever  a  special 
event in the database occurs. 

Syntax–  Create  trigger  [Trigger_name]  [before/after) 

{insert|update|delete}on [table_name] 

[for each row] 

[trigger_body] 

Normalization– Non loss decomposition and functional 
dependencies,  first,  second  and  third  normal  forms 
dependency preservation, Boyce/codd normal form. 
Decomposition–  The  process  of  breading  up  or 
dividing  a  single  relation  into  two  or  more  sub 
relations is called as decomposition of a relation. 

  Update anomalies–  If  data  items  are  scattered  and 
are  not  linked  to  each  other  properly,  then  it  could 
lead to strange situations. 

  Deletion  anomalies–  We  tried  to  delete  a  record, 
but  parts  of  it  was  left  undeleted  because  of 
unawareness, the data is also saved somewhere else. 
Insert  anomalies–  We  tried  to  insert  data  in  a 
record that does not exist at all. 

  Normalization  is  a  method  to  remove  all  these 
anomalies  and  bring  the  database  to  a  consistent 
state. 

First Normal Form 

 First  Normal  form  is  defined  in  the  definition  of 
relations (table) itself. 

Course

Content

Programming

Java,C

+ +

Web

HTML, PHP

  We  rearrange  the  relation  (table)  as  below  to 

convert it to first normal form. 

Course

Content

Programming
Programming

Web

Web

Java
+ +
C

HTML

PHP

Each attribute must contain only a single value from 
its pre-defined domain. 

Second Normal Form 

Second  normal  form,  we  need  to  understand  the 
following– 
Prime attribute– An attribute which is a part of the 
candidate key, is known as a prime attribute. 

  Non-prime  attribute–  An  attribute  which  is  not  a 
part  of  the  prime-key,  is  said  to  be  a  non-prime 
attribute. 
•  If we follow second normal form, then every non-
prime  attribute  should  be  fully  functionally 
dependent on prime key attribute. 

•  That is, if X→ A holds, then  there should not be 
any  proper  subject  Y  of  X,  for  which  Y-A  also 
holds true. 
Student_project 

Student- 

Stu_ID 

Stu_Name 

Proj_ID 

Project- 

Proj_ID  

Proj_Name  

Third Normal Form 

For a relation to be in third normal form, it must be 
in  second  normal  form  and  the  following  must 
satisfy. 

  No non-prime attribute is transitively dependent on 

prime key attribute. 
Student_Detail– 

Database Management Systems  

60 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Student_Detail– 

Zip codes– 

Boyce-Codd Normal form 

•  BCNF  is  an  extension  of  third  normal  form  on 
strict terms. 
• For any non-trivial functional dependency, X → A 
X, must be a super key. 
•  In  above  image  Stu_ID  is  the  super  key  in  the 
relation  student_Detail  and  zip  is  the  super  key  in 
the relation zip codes. 

Stu_ID → Stu_Name, Zip 

and  zip  →  city  (which  conforms  that  both  the 
relation are in BCNF). 

Fourth normal form (4NF) 
  A  relation  will  be  4NF  if  it  is  Boyce/codd  normal 

and has no multi valued dependency. 
for  a  dependency  A  →  B,  if  for  single  value  of  
multiple value of B exists, then the relation will be a 
multi-valued dependency. 

Fifth normal form (5NF) 
  A  relation  in  5NF  if  it  is  in  4NF  and  not  contains 
any join dependency and joining should be lossless. 
5NF  is  also  known  as  project-join  normal  form 
(PJ/NF). 

Transaction Management In DBMS– 

•  A transaction is set of logically related operation. 
•  Now  that  we  understand  what  is  transaction  we 
the  problems 

should  understand  what  are 
associated with it. 

•  To solve this problem, we have the following two 

operations. 

•  Commit– If all the operations in a transaction are 
those 

completed 
successfully 
changes to the database permanently. 

then  commit 

•  Rollback–  If  any 

then 
the  operations  fails 
the  changes  does  by  pervious 

rollback  all 
operations. 

States of transaction– Transaction can be implemented 
using SQL queries and sever. 

  Active state– 

•  The  active  state  is  the  first  state  of  every 
transaction.  In  this  state,  the  transaction  is  being 
executed. 

For  Example–  Insertion  or  deletion  or  updating  a 
record is done here. But all the records are still not 
saved to the database. 
Partially  committed–  In  the  partially  committed 
state,  a  transaction  executes  its  final  operation  but 
the data is still not saved to the database. 

  Committed–  A  transaction  is  said  to  be  in  a 
committed  state  if  it  executes  all  its  operations 
successfully. 
Failed  state–  If  any  of  the  checks  made  by  the 
database recovery  system  fails, then the transaction 
is said to be in the failed state.   

transaction 

  Aborted–  If  the  transaction  fails  in  the  middle  of 
the 
the 
then  before 
transaction,  all  the  executed  transaction  are  rolled 
back to its consistent state. 
Two operation– 
1. Re-start the transaction 
2. Kill the transaction 

executing 

Transaction property 

The  transaction  has  the  four  properties.  These  are 
used  to  maintain  consistency  in  a  database,  before 
and after the transaction. 
Property of transaction 
1. Atomicity 
2. Consistency 
3. Isolation 
4. Durability  

1.   Atomicity–  It  states  that  all  operation  of  the 
transaction  take  place  at  once  if  not  the  transaction 
is aborted. 

2.   Consistency– A transaction must after the database 
from one steady state to another steady state. This is 
the  responsibility  of  both  the  DBMS  and  the 
application developers to make certain consistency. 
executing 
independently of one another is the primary concept 
followed by isolation. 

3.  Isolation–  Transactions 

that 

are 

4.  Durability–  The  durability  property  is  used  to 
indicate  the  performance  of  the  database  consistent 
state. 
Implementation  of  Atomicity  and  durability– 
The recovery management component of a database 
system  can  support  atomicity  and  durability  by  a 
variety of schemes. 

Database Management Systems  

61 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Shadow copy– 
In the shadow copy scheme, a transaction that wants 
to update the database first creates a complete copy 
of the database. 
Figure  below  depicts  the  scheme,  showing  the 
database state before and after the update. 

(cid:1)  Schedule–  A  series  of  operation 

from  one 
transaction  to  another  transaction  is  known  as 
schedule. 

Serializability in DBMS 
schedules  may 
non-serial 

to 
Some 
inconsistency  of    the  database.  Serializability  is 
mainly of two types– 

lead 

  Conflict  serializability–  If  a  given  non-serial 
schedule can be converted into a serial schedule by 
swapping  its  non-conflicting  operations,  then  it  is 
called as a conflict serializable schedule. 

  Conflict  operations–  Two  operations  are  called  as 
conflicting operations if all the following conditions 
hold true for them. 
• Both the operation belong to different transaction. 
•  At  least  one  of  the  two  operations  is  a  write 
operations. 

Example– Consider the following schedule 

Transaction T1 Transaction T2

(
)
R1 A
)
(
W1 A
(
)
R1 B

(
R2 A

)

In this schedule, 

•   W1(A)  and  R2(A)  are  called  as  conflicting 

operations. 

•   This  is  because  all  the  above  conditions  hold  ture 

for them. 

  VIEW  Serializability–  View  serializability  is  a 
process  to  find  out  that  a  given  schedule  is  view 
serializable is not. 
Two  schedules  S1  and  S2  are  said  to  be  view 
equivalent if they satisfy the following conditions. 
1.  Initial  Read–  An  Initial  read  of  both  schedules 
must be the same suppose two schedule S1 and S2. 
IN  schedule  S1,  if  a  transaction  T1  is  reading  the 
data item  A, then in  S2, transaction T1 should also 
read A. 

T1

T2

T1

T2

Read A

(

)

Write A

(

)

Read A

(

)

Write A

(

)

Schedule S1

Schedule S2

2. Update Read– 

T1

T2

T3

T1

T2

T3

Write A

(

)

Write A

(

)

Read A

(

)

Write A

(

)

Write A

(

)

Read A

(

)

ScheduleS1

Schedule S2

3. Final write– 

T1

T2

T3

T1

T2

T3

Write A

(

)

Re ad A

(

)

Write A

(

)

Read A

(

)

Write A

(

)

Write A

(

)

Transaction Isolation Levels in DBMS 
 The SQL standard defines four isolation levels. 
1. Read uncommitted 
2. Read committed 

3. Repeatable Read 
4. Serializable 
Failure Classification– 
1. Transaction Failure 
2. System Crash 
3. Disk Failure 

1.  Transaction  failure–  Transaction  failure  occurs 
when  it  fails  to  execute  or  when  it  reaches  a  point 
from where it can't go any further. 
1. Logical error 

2. Syntax error 

2.   System  Crash–  System  failure  can  occur  due  to 
power failure or other Hardware or Software failure. 
Example- Operating system error 

Database Management Systems  

62 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.   Disk  Failure–  It  occurs  where  hand-disk  drives  or 

storage drives used to fail frequently. 

Problems with Concurrent Execution– In a database 
transaction,  the  two  main  operation  are  READ  and 
WRITE operations. 
(i) Lost Update Problem (W-W Conflict) 
(ii) Dirty Read Problems (W-R Conflict) 

(iii) Unrepeatable Read Problem (W-R Conflict) 

Lost  Update  Problem  (Write-Write  Conflict)–  Let's 

take the value of A is 100 

  CONCURRENCY  CONTROL–  Concurrency 
control  is  the  working  concept  that  is  required  for 
controlling  and  managing  the  concurrent  execution 
of database and thus avoiding the in consistencies in 
the database. 
Two-PHASE  LOCKING  (2PL)–  The  Two-Phase 
locking protocol divides the execution phase of the 
transaction into three parts. 

Time Transaction T Transaction T
2
)
(
−
A A 50

Read A

t
1

=

1

3

4

5

6

Read A

(
)
+
A A 50

=

Write A

(

)

Write A

(

)

2

t
t

t

t

t

•   At t1 times, T1 Transaction reads the value of A i.e. 

100. 

•   At  t2  Time,  T1  Transaction  deducts  the  value  of  A 

by 50. 

Dirty  Read  Problem  (W-R  Conflict)–  This  type  of 
problem  occurs  when  one  transaction  T1  update  a  data 
item of the database, and then that transaction falls due 
to  some  reason  but  its  updates  are  accessed  by  some 
other transaction. 

Example– Lets value A is 100. 

1

Time Transaction T Transaction T
2
(
)
Read A
+
A A 20
)
(
Write A

=

2

(
)
Read A
+
A A 30
)
(
Write A

=

Write B

(

)

Time Transaction T Transaction T
2
)

Read A

(

1

)

(
Read A
+
=
A A T30
(
)
Write A

Read A

(

)

3

t
1
t
t
t
t
t
t

4

5

6

7

2

t
1
t
t
t
t

3

4

5

  Unrepeatable Read Problem (R-W Conflict)– 

Example– Let take value A is 100 

There are two phases of 2PL– 
1. Growing phase 
Example– 

2. Shrinking phase 

T
1
−

0 LOCK S A

(

T
2

)

1
2 LOCK X B

−

(

3

−

4 UNLOCK A

(

LOCK S A

−

(

)

)

)

−

5
6 UNLOCK B

(

)

−
LOCK X C

(

)

7

8

9

UNLOCK A

UNLOCK C

(
(

)
)

−

−

The  following  way  shows  how  unlocking  and 
locking work with 2-PL. 
Transaction T1 
• Growing phase from step 1-3 

• Shrinking phase from step 5-7 

• Lock point at = 3 
Transaction T2 
• Growing phase from step 2-6 

• Shrinking phase from step 8-9 

• Lock point at 6 

(cid:1)  Strict two-phase locking (strict-2PL) 
(cid:1)  The first phase of strict-2PL is similar to 2PL. 
(cid:1)  Strict-2PL  protocol  does  not  have  shrinking  phase 

of lock release. 

Database Management Systems  

63 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  Basic  Time  stamp  ordering  protocol  works  as 

1. Database 2. Area 3. File 4. Record 

follows– 
1.Check 

the 

following  condition  whenever  a 

transaction Ti issues a Read (X) operation. 

•  If  W_Ts  (X)  >  Ts(Ti)  then  the  operation  is 

rejected. 

•  If  W_Ts(X)  <  =  Ts(Ti)  then  the  operation  is 

executed. 

2. Check 

the  following  condition  whenever  a 

transaction Ti issues a write (X) operation. 

•  If  Ts  (Ti)  <  R_Ts  (X)  then  the  operation  is 

  Recovery and Atomicity 

rejected. 

•  If Ts(Ti) < W_Ts(X) the operation is rejected and 
Ti  is  rolled  back  other  waise  the  operation  is 
executed. 

  Where, 

Ts(Ti) denotes the time tap of the transaction Ti. 
R_Ts(X)  denotes 
data_itemX. 

the  Read 

time_stamp  of 

  W_Ts(X)  denotes 
data_itemX.   

the  write 

time_stamp  of 

Validation  Based  Protocol–  Validation  phase  is  also 
known  as  optimistic  concurrency  control  technique  the 
transaction is executed in the following three phase. 

1. Read phase 
2. Validation phase 

3. Write phase 

THOMAS WRITE RULE– Thomas write rule provides 
the guarantee of serializability order for protocol. 
The Basic Thomas Write rules as follows. 

•  When  a  system  crashes,  it  may  have  several 
transaction  being  executed  and  various  file  opened 
for them to modify the data items. 

•  But  according  to  ACID  properties  of  DBMS 
atomicity  of  transaction  as  a  whole  must  be 
maintained,  that  is,  either  all  the  operations  are 
executed or none. 

Log-Based  Recovery–  The  log  is  a  sequence 
of  records.  Log  of  each  transaction  is  maintained  in 
some stable so that if any  failure occurs, then it can be 
recovered from there. 

There we two approach to modify the database 
1. Deferred database modification 

2. Immediate database modification 
Recovery with concurrent transactions 
Concurrency  control  means 

that  multiple 
transactions can be executed  at the same time and then 
the inter leaved logs occur. 

Recovery  with  concurrent  transactions  can  be 

•   If Ts(T) < R+Ts(X) then transaction T is aborted and 

done in the following four ways. 

rolled back and operation is rejected. 

• 

If  Ts(T)<W_Ts(X) 
W_item(X)  operation  of 
continue processing. 

then  don't 

execute 

the 
transaction  and 

the 

1. Interaction with concurrency control 
2. Transaction rollback 

3. Check point 
4. Restart recovery 

•  If  neither  condition  1  nor  condition  2  occurs,  then 
allowed to execute write operation by transaction Ti 
and set W_Ts(X) to Ts(T).  

MULTIPLE GRANULARITY 
  Granularity–  It  is  the  size  of  data  item  allowed  to 

lock. 

  Multiple  Granularity–  It  can  be  defined  as 
liearachically  breaking  up  the  database  into  blocks 
which can be locked. 

  Hence,  the  levels  of  the  tree  starting  from  the  top 

level are as follow. 

BUFFER  Management–  The  buffer  manager  is  the 
software  layer  that  is  responsible  for  bringing  pages 
from  physical  disk  to  main  memory  as  needed.  The 
buffer manages the available main memory by dividing 
the  main  memory  into  a  collection  of  pages,  which  we 
called  as  buffer  pool  the  main  memory  pages  in  the 
buffer pool are called frames. 
ARIES  Algorithm–  Algorithm  for  recovery  and 
isolation  exploiting  semantics  (ARIES)  is  based  on  the 
write  Ahead  Log  (WAL)  protocol.  Every  update 
operation  writes  a  log  record  which  is  one  of  the 
following– 

Database Management Systems  

64 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
1.   Undo-only  log  record–  Only  the  before  image  is 

logged. 

2.   Redo-only log record–Only the after image is logged. 
3.   Undo-redo  log  record–  Both  before  image  and 

after images are logged. 

The recovery process actually consists of 3 phases. 
2. Redo   3. Undo 
1. Analysis 
Remote Backup 

Remote backup provides a sense in case the primary 
location  where 
located  gets 
the  database 
destroyed.  Remote  backup  can  be  offline  or  real-
time or online. 

is 

File–  A  file 
is  named  collection  of  related 
information  that  is  recorded  on  secondary  storage 
such as magnetic disks, magnetic tables and optical 
disks. 

S. 
No. 

1. 

2. 

3. 

4. 

SQL 

No SQL 

RELATIONAL 
DATABASE 
MANAGEMENT 
SYSTEM 
(RDBMS) 

databases 
These 
have  fixed or static 
or 
predefined 
schema. 

These  data  bases 
are  not  suited  for 
hierarchical 
data 
storage. 

ACID 

Follows 
property 
Example– MySQL, 
Oracle,  MS-SQL 
Server etc. 

No-relational 
distributed 
system. 

or 
database 

They  have  dynamic 
schema. 

suited 

These  database 
best 
hierarchical 
storage. 

are 
for 
data 

CAP 

Follows 
(Consistency, 
availability,  partition 
tolerance) 
Example–  MongoDB, 
GraphQL, HBase, ect. 

NoSQL Database 
  We know that MongoDB is a NoSQL database, so it 
is very necessary to know about NoSQL database to 
understand MongoDB throughly. 

  NoSQL database is used to refer a non-SQL or non 

relational database. 
Advantages of NoSQL– 

1. It supports query language 
2. It provides fast performance 
3. It provides horizontal scalability 

MongoDB advantages over RDBMS–  MongoDB  is  a 
new  and  popularly  used  database  it  is  a  document 
based, non relational database provider. 
MongoDB Advantages 

•   MongoDB is schema less. 

•  There may be difference between number of fields, 
content and size of the document from one to other. 

•  Structure of a single object is clear in MongoDB. 

•  There are no complex joins in MongoDB. 

•  Distinctive features of MongoDB. 

Easy to use 
Light weight 
Extremely faster than RDBMS  
Where MongoDB should be used– 
• Big and complex data 

• Mobile and social infrastructure 

• Content management and delivery 

• User data management 

• Data hub 

MongoDB Datatypes 
Following is a list of usable data types in MongoDB.  

Data type  Description 

String 

Integer 

Boolean 

Double 

Arrays 

Object 

String  is  the  most  commonly  used 
data type. It is used to store data. 

Integer  is  used  to  store  the  numeric 
value.  It  can  be  32  bit  or  64  bit 
depending on the server you are using. 

This data type is used to store Boolean 
values. It just shows yes/no values. 

Double data type stores floating point 
values 

This data type is used to store a list or 
multiple values into a single key. 

Object data type is used for embedded 
documents. 

Null 

It is used to store null values. 

Database Management Systems  

65 

YCT 

  
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
    06.   THEORY OF COMPUTATION 

(cid:1)  Theory of Computation(TOC)- 

It  is  the  mathematical  study  of  computing  machine 
and their capabilities. 

OR 

It  is  the  study  of  automata  theory  and  formal 
languages. 

(cid:1)  Ambiguity problem–(undecidable). 

•  The general problems are two types known as- 

1.  Decidable problem 
2.  Undecidable problem 

•  To  estimate 

the  Nature  of  problem  some 
mathematical  tools  are  used  which  is  known  as 
Automata. 

     { } {a, b} {aa, ab, ba, bb}..........

= ∈ ∪

∪

Infinite

=
=

     Complete language

Finite Automata 
(cid:1)  Finite  automata  is  the  mathematical  model  which 
contains finite number of state and transition defined 
between the states. 

•  Automata  is  mathematical  model  in  which  are 
study practical situation of computer science. 
(cid:1)  Alphabet 'Σ'– Finite non-empty set of symbols. 

Example– {0, 1}, {a,b,c,d} 

(cid:1)  String– Finite sequence of symbols over the given alphabet 'Σ'. 

Example–    {0, 1} repetition allowed. 

n

{0, 1, 0, 1} 

Length →    

4  

{0, 1, 0, 1, 0, 1}   
6 

(cid:1)  Epsilon (∈) – Length will be zero. 
(cid:1)  Language – Any set of strings over the given alphabet. 

L1: set of all string of length 

{0,1}

L {0,1,10, 01........}

=
• The set can finite, infinite, empty. 
• Finite language : (strings are finite) 
• Infinite Language : (strings are Infinite) 
• Empty Language : L = {∈}, finite length 

L = {∈}→ Valid String 
L = {∈, 0, 1, 00, 11, 01, 10 ..........} 

↓ 

Complete Language = Σ* 

(cid:1)  Substring–  Consecutive sequence of symbols over 

Deterministic Finite Automata (DFA) 
(cid:1)  Finite  Automata  can  be  represented  by  following 

two methods. 
• Transition diagram 
• Transition table 

(cid:1)  DFA: It is finite  Automata in  which from each and 
every  state  on  every  input  symbol  exactly  one 
transition exist. 

(cid:1)  DFA is formally define as five tuple : 
Q = Finite Number of state 

   Input alphabet 

0q =  Initial state 
F = Final state 
δ = Transition function 

DFA  (Q,

,

(cid:1)  Transition Function → Q

0q ,  F, δ) 
×  
Q

the given string known as substring. 
Ex. Mode → 4 length 

Hence, 

Total Number of Substring =

N(N+1)
2

+  
1

(cid:1)  Power of Σ :  Σ = {a, b} 

1 

2 

3 

0 

* 

   Set of all string of length 1, = {a, b}  
   {aa, ab, ba, bb} 
   8 
   Set of all string of length zero = {∈} or  ∈  

0

1

2 ..........

{q0.q1}× (a, b) 
{q0.a} 
{q0.b} 
{q1.a} 
{q1.b} 

(cid:1)  Acceptance of DFA: By reading string from left to 
right  end  of  the  string  the  DFA  enter  into  secure 
final  state  than  the  given  string  accepted  otherwise 
rejected. 

Theory of Computation  

66 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
         
 
  
 
 
         
 
 
 
 
 
 
 
 
 
 
           
 
        
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
(cid:1)  The set of string accepted by given DFA is known as 
Language of the DFA, Hence Every DFA represents 
exactly one language. 

•  

(cid:1)  Empty Language accepted: 

In any DFA, if no final state exist, or final state are 
not  reachable  from  initial  state  than  the  language 
accepted by DFA is Empty Language. 

(cid:1)  In any DFA if initial state is also final state then '∈' 

is also accepted by DFA. 

|ω| ≤ n 
(n + 2) state 
(cid:1)  Minimal DFA:  

ω ∈ {a, b} 

|ω| mod 2 = 0 

L = {∈, aa, ab, ba, bb} aaaa, .....} 

(cid:1)  Dead  State:  If  any  non-final  state  having  self  loop 
on  input  symbol  than  that  state  is  known  as  dead 
state. 

(cid:1)  By reading any input, if automata in DFA and if we 
don't reach to final state then that input is rejected. 
(cid:1)  C-programming language = set of all valid program.  

|ω| mod 2 = 1 

|ω| mod 3 = 0 

Program void main ( ) 
            { 
                int a, b; 
            { 

≅ ω ≅

| 1mod 3

|

(cid:1)  A Finite Automata is said to accept a language if all 
the  strings  in  the  language  are  accepted  and  all  the 
string  are  rejected  which  are  not  presented  in  the 
language. 

(cid:1)  DFA (Minimal)–  
ω = {a, b}, 
|ω| ≤ 2 
L = {∈, a, b, aa, ab, ba, bb} 

• 

|ω| mod n = 0 
'n' length string 
3 → 3 
4 → 4 
. 
. 
n → n 

• Minimal DFA– ω ∈ {a, b}* 
na(ω) = 2 (exactly two a's) 

L = {aa, aba, baa, aab, ......} 

• na(ω) ≥ 2 (at least two a's) 

• na (ω) ≤ 2 (at most two a's) 

• ω ∈ {a, b}* 

na(ω) mod 2 = 0 
na(ω) ≅ 0 mod 2 

|ω| = n 
(n + 2) state,   

|ω| ≥ n 
(n + 1) state 

Theory of Computation  

67 

YCT 

 
 
       
 
                   
 
 
 
 
 
 
   
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
  
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
•  The  language  for  which  TM  is  possible  know  as 

REL. 

Note–  FA → Finite Automata 

PDA → Push Down Automata 
CFL → Context-Free Language 
CSL → Context Sensitive Language 
TM → Turing Machine 
REL → Recursively Enumerable Language 
LBA → Linear Bounded Automata 

Power Sequence = [TM > LBA > PDA > FA] 

(cid:1)  Expressive Power– 

•  Number  of  language  accepted  by  particular 
automata  know  as  expressive  power  of  that 
Automata. 

•  It  is  important  to  note  that  DFA  and  NFA  are  of 
same power because every NFA can be converted 
into  DFA  and  every  DFA  can  be  converted  into 
NFA. 

•  The  turning  machine  i.e.  TM  is  more  powerful 

than any other machine. 

(cid:1)  Minimization of DFA 

*∈ ∑   both 

Equivalent state- Two state q1 and q2 are equivalent 
)
∨ x
result  either 
final  state  or  non-final  state  otherwise  they  are  not 
equivalent.   

2q , x

1q , x

and 

δ

δ

(

(

)

(cid:1)  State Equivalence Algorithm– To detect equivalent 

state for two algorithm exist know as- 
• State equivalence algorithm 
• Marking algorithm 

(cid:1)  There  minimization  algorithm  application  for  only 
for DFA (Non-applicable for NFA and ∈-NFA) 
(cid:1)  After  apply  minimization  algorithm  for  any  DFA 
then the language accepted by DFA remains same. 
(cid:1)  Before  apply  minimization  algorithm  all  not 

reachable state one eliminated first. 

(cid:1)  Minimum Number of State of following– 

• ω ∈ {a, b}* 

na(ω) ≅ o mod 2 
and 
nb(ω) ≅ o mod 2 

L

∈


= 




, aa, bb, aabb





.......




abab

baba

bbbb

na(ω)  nb(ω) 
even 
even  
odd 
odd 

even 
odd 
odd 
even 

∈, aa, bb  
aab 
ab 
abb 
(cid:1)  Compliment  of  DFA–  By  interchanging  final  state 
into non-final state and non-final state, then  we can 
get the compliment of DFA. 

•  If 

language  accepted  by  DFA 
compliment of DFA accept "Σ* – 1". 
•  Compliment is applicable only for DFA. 

is 

'1' 

then 

Note–  We  cannot  get  the  compliment  of  NFA  and  e-

NFA. 

(cid:1)  Chomskey Hirarchy– 

•  Finite automata having one stack memory element 

know as push down automata. 

•  The  comparison  element  remember  the  stack  to 
in  push  down 

perform  validation  of  string 
automata. 

•  Hence  language  L2  is  accepted  by  push  down 

automata but not finite automata. 

•  To  accept  language  L3  finite  automata  phase  and 
push down automata phase hence turning machine 
is constructed. 

•  The  language  for  which  FA  is  possible  know  as 

Regular language. 

• The language for which PDA is possible know as 

CFL. 

• The Language for which LBA is possible know as 

CSL. 

Theory of Computation  

68 

YCT 

 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Construction of NFA 
1.   Construct  NFA  that  accept  all  string  of  a'b  and  b's 

where each string ending with abab. 

(cid:1)  Construct the Minimal DFA– 

L = {an bn/n, m ≥ 1} 
L = {ab, aabb, aaab, abb .......} 

2.   With aba or abb 

• Construct the minimal DFA for the language. 

L = {1, 2, 4 ...... 2n} 
all these number are in unary. 
L = {1, 11, 1111 ........} 
L = {12n/n>0} 

not possible 

•  

(cid:1)  NFA to DFA conversion– 

Subset  construction  algorithm 
algorithm) 
• Construct DFA equivalent to solving NFA. 

(Equivalence 

NFA: 

(cid:1)  ∈-closer–  ∈-closer  state  of  which  starting  by 
reading  only  ∈-reachable  state.  The  initial  state  of 
DFA is ∈-closer initial state of NFA.   

•  Construct  a  minimal  DFA  that  accept  all  the 
strings of 0's and 1's which contains. 
(i) 0 1 as substring 

L = {01, 010, 011, 101, 001 .....}  

(cid:1)  Properties of FA– 

1. Emptyness problem 
2. finiteness problem 
3. Equivalence problem 
4. Membership problem 

Non-Deterministric Finite Automata (NFA) 
(cid:1)  In  NFA  from  the  given  state  and  the  given  input 
signal  there  may  be  '0'  transition  or  '1'  transition  or 
more than '1' transition exist. 
• NFA is formally different (Q, Σ δ, q0, F) 

  Q → Finite no. of state 
Σ → Input alphabet 
q0 → Initial state 
F → Set of final state 
δ → Transition function 
• Minimization algorithm not applicable for NFA. 
• Complementation is not applicable for the NFA. 
•  In  NFA  for  valid  string  also  Non-final  paths  or 
transition may exist. 

1.   Emptyness  problem–  It  means,  checking  whether 

language accepted by the given FA is empty or not. 
Step-1  →  Eliminate  all  non-reachable  state  form 
DFA. 
(ii)  To  resultant  automata  at  least  one.  Final  item 
exist  and  we  accept  non-empty  language  other 
empty language. 

2.   Finiteness  problem–  It  means  checking  whether 
language accepted by given automata is finite or not. 

Theory of Computation  

69 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.   Equivalence  problem–  Checking  whether  given 

two automata accept same language. 

4.   Membership  problem– It  means checking  whether 

the Exist 'x' in the given automata or not. 

x, y, z. Σ = {a, b} 
I/P alphabet (Σ = {a, b}) 

Regular Expression 

Converstion

→ Finite Automata 

(RE ⇒ ∈-NFA) Thomson construction 

Regular 
Expression 

∈-NFA 

1.   φ 

2.   ∈ 

3.   a 

4.   r1.r2 

5.   r1 + r2 

  Basic R.E. 

 Basic R.E. 

 Basic R.E. 

Regular Expression 
•   The  simplest  way  of  represent  regular  languages 

know as regular expression. 

•   Regular  expression  can  be  constructed  by  using 
following '3' operand and input symbols as operands. 

6.   r1* 

*  → Kleene closer 
+  →  Union operator 
.  →  Concatenation operation 

(cid:1)  1. L = { } φ 

2. L = {∈} ∈  
3. L = {a} a 
4. L = {a, b} ab 
5. L = (a, b) a + b 
6. L = {∈, a, aa, aaa ......}a* 
7. L = {a, aa, aaa ......}a+ 

•   For  one  regular  language,  there,  may  be  possibility 
of  having  many  regular  expression  by  but  one 
regular  expression  represent  only  one  regular 
language only. 

Identities of Regular Expression 

7.   r1

+ 

8.   φ+ 

Construct NFA for RE– 

(a + b)* (aa + bb) (a + b)* 

1. R + φ = φ + R = R 
2. R.φ = φ.R = φ 
3. R.∈ = ∈.R = R 
4. R* = (R*)* = (R+)* = (R*)+  
5. RR* = R+ = R*R 
6. R+ + ∈ = R* 
7. a(ba)* = (ab)*a 
8. a + b = b + a 
9. ab ≠ ba 
10. (a+b)* ≠ (ab)* 
11. (a+b)* ≠ (a*b*) 
12. (a + b)* ≠ a* + b* 
13. (a + b)* = (a* + b*)* = (a* + b)* = (a + b*)* = 
(a*b*)* 
14. ∈* = ∈; ∈+ = ∈ 
15. φ* = ∈, φ+ = φ 
Theory of Computation  

70 

•   Mealy–  Mealy  is  mathematical  model  in  which 

output is associated with transition. 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
•   Moore–  Moore  is  mathematical  model  in  which 

output is associated with state. 

•   Construct Mealy Machine that contain all the string 
of a's and b's and produces one as output if last two 
symbol input are same otherwise produce. 

  Definition– (Q, Σ, q0, ∆, δ, λ ) 
Q → Infinite Number of states 

Σ → Input alphabet 

q0 → Initial state 
∆ → Output state 

δ → Transition function 

λ → Output function 

Mealy Machine ⇒ Q×Σ → ∆ 

Moore Machine ⇒ Q → ∆ 

•   Mealy  and  Moore  Machine  are  deterministic  in 
nature hence from each and every state input symbol 
exactly one transition exist. 

•   There is no final state in Mealy and Moore Machine 
because  they  are  not  acceptors,  they  are  output 
generators. 

•   Mealy  and  Moore  Machine  are  practical  use  in  Ckt 

design. 

•  Mealy  and  Moore  Machine  can  be  represented 

transition table or transition diagram. 

Mealy Machine 
•   Construct Mealy Machine that represents behaviour 

of 1's complement of binary number ckt. 

•   Construct  the  Mealy  Machine  that  represents  2's 
complement  of  binary  number  Ckt  behaviour. 
(Assume that we are reading the string from LSB to 
MSB and carry is discarded) 

(cid:1)  While  reading  the  string  from  LSB  initially  any 
number  of  zero  replace  them  by  zero  until  we  get 
first  '1'  replace  as  it  is  and  then  complement 
remaining things. 

•   Construct  the  Moore  Machine  that  takes  all  strings 
of  0's  and  1's  as  input  and  produces  A's  output  if 
input  is  ending  with  10  or  produces  B's  output  if 
input is ending with 11 otherwise C as output. 

•   Construct  the  Moore  Machine  that  takes  all  binary 
number if input and produces residue modulo  '3'  as 
output. 

•   Construct  the Moore Machine that takes all base  '3' 
as input and produces residue modulo 4 as output. 

Moore to Mealy Machine Conversion 
•  Construct  the  Equivalent  Mealy  Machine  to 
following Moore Machine 

Theory of Computation  

71 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
•   Mealy Machine– 

  Mealy Machine to Moore Machine Conversion– 

  Moore Machine– 

•   While  converting  from  Mealy  Machine  to  Moore 
Machine  number  of  state  of  Moore  M/C  may 
increases because there may be possibility of having 
more than one output at one state hence splitting of 
states happens. 

•   While  converting  from  Mealy  M/C  to  Moore  M/C 
Maximum  number  of  state  possible  in  Moore  M/C 
from the given 'n' state m-output symbol Mealy M/C 
is n*m. 

(v)   Palindrome  language  has  one  symbol  regular 
and  over  more  them  one  symbol  are  non-
regular. 

Pumping Lemma 

•   Pumping Lemma is the theorem using to prove non-

regular language as non-regular. 

•   Pumping  Lemma  uses  prove  by  contradiction 

strategies. 

•  

(cid:1)  Method steps– L = {an bn/n ≥ 1} non regular 

1. Assume L is regular 
2. L = FA = n state 

3. |z| ≥ n 

4. |z| 

     ↑ 
    u|v|w 
5. Loop string 

6. uv, w ∈ ∀ i > 0 

    u, v w ∉ L, non regular. 

Steps– 
To prove language 'L' is non-regular 
(i) Assume L is regular 
(ii)  If  'L'  is  regular  than  their  exist  finite  Automata 
for 'L' assume 'n' states on their. 
(iii)  Select  some  |z|  string  |z|  from  length  whose 
length is greater than or equal to n. 

• Divide |z| string in three parts (u, v, w) such length 
of v is |v| ≥ 1. 

• If L is regular for all ∀ i ≥ 1, 

u v, w ∈ L 

at least i value u v w ∉ L then L is non-regular. 

Regular Language Detection 

Closure properties of Regular Language 

(i)   Finite language is always regular, but all regular 

1. Union Operation– 

language need not be finite. 

(ii)  Finite  Automata  having  finite  memory,  hence 
the  language  which  requires  finite  comparison 
can be recognized by FA. 

(iii)  Finite Automata fails to accept language, which 

requires infinite memory. 

(iv)  Any 

infinite 

language  having  comparison 

between symbol is non-regular. 

L1 = Regular Language = FA1 
L2 = Regular Language = FA2 

Hence regular language are closed under union. 

Theory of Computation  

72 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2.   Sub-set Operation– The subset of regular language 
may or may not regular, hence regular language are 
not closed under subset operation. 
an bn ⊆ a* b* ⊆ (a + b)* 
Non-regular 

Regular   

3.   Concatenation– 

L1 = Regular Language = an = FA1 
L2 = Regular Language = bn = FA2 

Regular language are closed under concatenation. 
Note– Let 'L1' and 'L2' are two Regular Language F1 and 
F2  are  finite  Automata  for  L1  and  L2  is  always 
regular.  Hence  Regular  Language  are  closed  under 
concatenation. 

4.   Kleene Closure–  

L → Regular Language 

the FA exist 

5. 

 Positive Kleene closure– 

(i) Let 'L' be a Regular Language and 'F' be the finite 
Automata  for  'L'  then  the  Kleene  closure  of  it, 
always regular because FA exists as follows. 
(ii) Let  'L' is  Regular  Language F be the FA  for 'L' 
then the positive closure of it always regular because 
FA as follow. 

6.   Complementation– 

L - Regular Language 

Σ* – L ⇒ Regular 

Compliment of Regular Language is always regular 
because  can  construct  complemented  DFA  by 
interchanging  final  state  as  non-final  and  non-final 
state as final. 
7.   Intersection– 

L1 → Regular 
L2 → Regular 

L1 ∩ L2 = (

L
1

L∪

2

)

• Whenever union and complement one closed then 
intersection  is  also  closed.  Hence  finally  Regular 
Language are closed under intersection. 

8.  Reversal Operation– 

L = {an bm} ⇒ LR = {bm an} 

•  Reversal  of  Regular  Language  is  always  Regular 
because Regular Language are closed under reversal. 

•  Reversal  operation  on  regular  expression  applied 
as follows– 
1– (E + F)R = ER + FR (001 + 110)R ⇒ 100011 

9.   Init Operation– 

Init (L)– Init of language 'L' is set of all prefix of all 
string of the language. 

10.  Substitution operation– 
L = {an bm/n, m ≥ 1} 
S(L) = {0n1m/n, m ≥ 1} 

Substitution  (s)  is  a  mapping  from  Σ  →  ∆  where 

each  symbol  of    Σ  is  replaced  by  a  Regular 

Language over the  ∆. 

S(φ) = φ 

S(∈) = ∈ 

S(a) = a 

11.  Homomorphism  Operation–  Homomorphism  is  a 

special case of substitution where each symbol of Σ 

can be replaced by A single string for the ∆. 

1. H(φ) = φ 

2. H(∈) = ∈ 

3. H(a) = a 

4. H(a + b) = H(a) + H(b) 

Two DFA 

2DFA → (Q, Σ, δ, q0, F) 

δ : Q × E → Q × {L, R}  

• 2-DFA is a DFA which is capable to move Left as 

well as right side direction. 

Intersection is closed under Regular Language. 

• 2-DFA is formally defined as follows. 

Theory of Computation  

73 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  Acceptance  method– By reading the string starting 
from  left  if  the  2DFA  enter  into.  Final  state 
whenever M/C is halted. Then the string is accepted 
otherwise string is rejected. 
Equivalence classes– 
•  Equivalence  class  of  state  'q'  is  set  of  string  by 
which we can reach state 'q' from the initial state. 

•  The  number  of  equivalence  for  given  Regular 
Language  is  number  of  states  of  minimal  DFA 
exist for that language. 

GRAMMARS 
• Set of rules used for describe rules for the language. 

• Grammar is following determines as: 

N = Set of non-terminals [S, A, B] 
T = Set of terminals [a, b] 

P = Number of production S → ab/ba/c/∈ 
S = Starting symbol 

Example–  S → AB 

A → a 

B→ b 

Every grammar is formed α → β 

where β is replacement of 'α' 

(cid:1)  Derivation–  The  process  of  generating  string  from 

the given grammar know as derivation. 

•  The  derivation  can  be  either  left  most  derivation 
(LMD) or completely right most derivation (RMD). 

(cid:1)  LMD– It is process of derivation in which left most 
non-terminal is replaced by its right hand side part. 
(cid:1)  RMD–  It  is  process  of  derivation  in  which  right 
most  non-terminal  is  replaced  by  its  RHS  part  at 
every set. 

(cid:1)  Parse Tree or Derivation Tree–Tree representation 
of the derivation know as parse tree all heaf node of 
parse tree know as yield of the parse tree. 

(cid:1)  Sentential Form– 

•  Every step in the derivation is one sentential form 
sentential form may be collection of terminals and 
non-terminals. 

•  The derivation is LMD then sentential form is left 

sentential form. 

•  Every grammar represent one language. 
•  For  CFL 
grammar. 

their  exist  grammar  context  free 

•  For  CSL  their  exist  grammar  context  sensitive 

grammar. 

• All  grammar  is  of  the  form  of  α,  β,  α  should 

contain at least order. 

(cid:1)  Linear  Grammar–  In  any  grammar  their  exist 
exactly  one  non-terminal  on  LHS  and  almost  one 
non terminal (A) on RHS. 
•  The  linear  grammar  can  be  left  linear  or  Right 

grammar or middle linear. 

•  Regular  grammars  are  not  one  class  of  linear 
grammar  hence  all  regular  grammar  are  linear 
grammar  but  all  linear  grammar  need  not  be 
regular. 

(cid:1)  Regular Grammar– Grammar is called a type 3 or 
regular  grammar  if  all  its  production  are  type  3 
production. A production S →  ∧  is allowed in type 
3 grammar, but in this case S does not appear on the 
right-hand side of any production. 

S → bs/aA 
A → bA/aS/∈ 

Theory of Computation  

74 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Context Free Grammar 
(cid:1)  Context-free languages are applied in parser design. 
They  are  also  useful  for  describing  block  structures 
in  programming  languages.  It  is  easy  to  visualize 
derivations  in  context-free  languages  as  we  can 
represent derivations using tree structures. 

(cid:1)  The language  generate by context-free grammar are 

known as CFL. 

S → S1/S2 
S1 → AB 
A → aAb/ab 
B → CB/C 
SL → PQ 
P → aP/Q 
Q → bQC/bc 
Simplification of context free grammar– 
(i) Useless Variable 
(ii) Unit Production 
(iii) Null Production  

•  Checking  whether  the  given  CFG  is  Regular  or 
not, is undecidable. 

Ambiguity Problem 

A  terminal  string  ω  ∈  L  (G)  is  ambiguous  if  there 
exist  two  or  more  derivation  tree  for  ω  (or  these 
exist two or more left most derivation of ω). 

•   Elimination  of  useless  variable– 

It  means 
elimination of variable from the grammar which are 
not  deriving  any  string  and  also  eliminate  variable 
which are not required for derivation. 

•   Variable not reachable from S (Starting Symbol). 

(ii)  Unit  Production–  Any  production  of  the  form 
"A→B" known as unit production. 
(iii) Null Production (A→∈)– Any production like 
"A→∈" known as Null production. 

Unambiguous Grammar 

The grammar is said to be unambiguous for all string 
if the grammar exist only one parse tree or only one 
LMD  or  one  RMD  or  if  one  LMD  and  one  RMD 
ever exist but both produces the same parse tree. 
1.  a = b + c * d; 

S → id/E 

E → E + E/ E*E |id; 

E → E + E 

→ E + E * E 

→ id + E * E 

→ id + id*E 
→ id + id * E 

Inherently Ambiguous Grammar 

In  ambiguous  grammar  from  which  elimination  of 
ambiguity is not possible. 
inherently 
Example–The  following 
ambiguous  CFL  Means,  all  of  its  grammar  are 
ambiguous  and  elimination  of  ambiguity  is  not 
possible for each grammar. 

language 

is 

•  

(i)   Normal form of CFG means applying condition 

on RHS of the production. 

(ii)  To  normalize 
simplified. 

the  grammar, 

it  should  be 

(iii)  There  are  mainly  two  normal  forms  known  as 

Chomsky and Greibach normal form. 

  GNF Normal Form– A → av* 

(a) Convert into GNF? 

S → AB 
A → aA|bB|b 
B → b 

•   The  grammar 

is 

left  recursive  grammar, 

then 

eliminate the left recursion to convert into GNF. 
Decision Properties of CFG– 

(i) Emptyness
(ii) Finiteness
(iii) Membership







Decidable

(i)  Emptyness–  Checking  whether  CFG  generate 
empty language or not. 

Theory of Computation  

75 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Algorithm–  

•  PDA  is  only  one  type  only,  but  recognize  or  are 

(a) Eliminate  useless  variable 

from 

the  given 

two types, DPDA, NDPDA. 

grammar. 

Definition–  

(b) Starting symbol is also useless then that grammar 

(i)   There is only one type of PDA, that is language 

generates empty language otherwise non-empty. 

recognizer (No output generator). 

(ii) Finiteness problem– It means checking whether 

(ii)  Expressive  power  of  NPDA  is  more  than 

given CFG generates finite language or not. 

DPDA. 

Algorithm–  

(iii)  By default PDA means N-PDA. 

(a) Convert the given grammar into CNF grammar. 

(iv)  There  are  two  type  of  acceptance  methods  to 

(b) Construct CNF graph. 

accept a string in PDA, they are– 

(iii) Membership Problem or Parsing Algorithm– 

• Empty Stack Method 

(a)   Checking  whether  string  'x'  is  generated  from 

• Final State Method 

given CFG or not. 

(b)  Checking  whether  given  string  is  member  of 

given grammar or not, know as parsing. 

(c)   The algorithm which performs parsing, know as 

parsing algorithm or membership algorithm. 

Push Down Automata (PDA) 

PDA(Q, Σ, q0, F, δ, z0, ) 

Q → Finite number of state 

Σ → Input alphabet 

q0 → Initial state 

F → Set of final states 

z0 → Initial stack element 

 → Stack element 

δ → Transition function 

Q × Σ ∪ {∈} ×  → Q × * 

Example– 

L

=

{

n n

}
b a / n 1

≥

(a)  Empty  Stack  Method–  By  reading  the  string 

from  left  to  right,  end  of  the  string.  If  the  stack  is 

empty then the given string is accepted and irrelative 

about number of final state. 

(b)  Final  State  Method–  By  reading  the  starting 

from left to right, end of the string, the PDA enters 

into  final  state,  then  given  string  is  accepted  and 

irrelative about stack symbol. 
(cid:1)  Parsing and Push Down Automata 

(i)  Top-Down  Parsing–  We  present  certain 

techniques  for  top-down  parsing  which  can  be 

applied 

to  a  certain  subclass  of  context  free 

languages.  We  discuss  LL(1)  parsing,  LL(K) 

parsing,  Left  factoring  and  the  technique  to  remove 

left reversion. 

(ii)  Bottom  up  Parsing–  In  bottom-up  parsing  we 

have to reverse the productions to gets finally. This 

suggests  the  following  moves  for  a  PDA  acting  as 

bottom up parser. 
(a) δ(P,  ∧ , αT) = {(P, A)| there exists a production  

A → α}  

(b) 

δ

(

P,

)
σ ∧ =

,

{
(

P,

σ

}
)

for all

σ ∑  
in .

Using  (i)  we  replace  αT  on  the  basis  by  A  when 

A→α  is  a  production  the  input  symbol  σ  is  moved 

on to the stack using (ii) for acceptability we require 

some moves when the PDS has S or z0 on the top. 

Theory of Computation  

76 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Turing Machine Model 

Turing's Aim– 
Design a model that is- 
(i) simple (ii) Intuitive (iii) Generic 

(cid:1)  Recursive  Enumerable 

(RE) 

or  Type-0 
Language–  RE  language  or  type-0  language  are 
generated  by  type-0  grammars.  It  means  TM  can 
loop  for  ever  for  the  string  which  are  not  a  part  of 
the language. RE languages are also called as Turing 
recognizable languages. 

(cid:1)  Recursive  Language  (REC)–  REC  language  are 
also  called  as  Turing  decidable  languages  the 
relationship  between  RE  and  REC  language  can  be 
shown in figure.  

• The  Turing  Machine  can  be  thought  of  as  finite 
control  connected  to  a  R/W  (read/write)  head.  It 
has  one  tape  which  is  divided  into  a  number  of 
cells. 

• A Turing machine M is a 7-tuple, namely (Q, Σ, , 

δ, q0, b, F) 

1. Q is finite nonempty set of states. 

2.  is a finite nonempty set of tape symbols. 

3. b∈  is the blank 

4.  Σ  is  a  non-empty  set  of  input  symbols  and  is  a 
subset of  and b ∉ Σ, 

5. δ is transition function mapping (q, x) on to (q, y, 
D)  where  D  denotes  the  direction  of  movement  of 
R/W head; D=L or R according as the movement is 
to the left or right. 

6. q0 ∈ Q is the initial state. 
7. F ⊆ Q is the set of final states. 

Representation of Turing Machines 

(i) instantaneous descriptions using move-relations. 
(ii) transition table 
(iii) transition diagram 

Nondeterministic Turing Machines 

•  A  non-deterministic  Turing  machine  is  a  7-tuple 
(Q, Σ, , δ, q0, b, F) 
(i) Q is a finite nonempty set of states 

(ii)  is a finite nonempty set of tape symbols 

(iii) b∈  is called the blank symbol. 

(iv)  Σ  is  a  nonempty  subset  of  ,  called  the  set  of 

input symbols. 
(v) q0 is the initial state. 
(vi) F⊆ Q is the set of final states. 

(vii) δ is a partial function from Q ×  into the power 

set of Q ×  × {L, R}. 

Closure Properties of Recursive Languages 

•   Union– If L1 and if L2 are two recursive languages, 
their union L1 ∪ L2 will also be recursive because if 
TM halts for L1 and halts for L2, it will also halt for 
L1 ∪ L2. 

•   Concatenation–  If  L1  and  if  L2  are  two  recursive 
languages,  their  concatenation  L1,  L2  will  also  be 
recursive. 

•   Kleene  Closure–  If  L1  is  recursive,  its  Kleene 

closure L1* will also be recursive. 

•  

Intersection  and  complement–  If  L1  and  if  L2  are 
two  recursive  languages,  their  intersection  L1  ∩  L2 
will also be recursive. 

Linear Bounded Automata 

•   A  linear  bounded  Automata  is  a  multi-track  non-
deterministic  Turing  machine  with  a  tape  of  some 
bounded finite length. 

Length = function  
(length of the initial input string, constant C) 

A  linear  bounded  automata  can  be  defined  as  an  8-
tuple (Q, X, Σ, q0, ML, MR, δ, F) 
(i)   Q is a finite set of states 
(ii)   X is the tape alphabet 

(iii)   Σ is the input alphabet 
(iv)   q0 is the initial state 
(v)   ML is the left end marker 
(vi)   MR is the right end marker were MR ≠ ML 
(vii)  δ is a transition function which maps each pair 
(state,  tape  symbol)  to  (state,  tape  symbol, 
constant 'C') where C can be o or +1 or –1 

Theory of Computation  

77 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(viii) F is the set of final state 

•  A  decision  problem  is  decidable  if  there  exists  a 

A deterministic linear bounded automaton is always 
context  sensitive  and  the  linear  bounded  automaton 

with empty language is undecidable. 

(cid:1)  Context Sensitive Language 

decision  algorithm 

for 

it  otherwise 

it 

is 

undecidable. 

(cid:1)  Decidability properties of regular languages– 

(i) DFA membership–  

Instance : ADFAM = {Q,Σ, δ,q0, F} and string  ω ∈ 

Σ*. 

(ii) DFA emptiness– 

•  A  context  sensitive  grammar  is  an  unrestricted 

grammar in which all the productions are of form. 

ADFA m = {Q, Σ, δ, q0, F} 

(cid:1)  Undecidable problems– 

α → β 

  We will now discuss the notion of undecidability. 

  Where α, β ∈ (V∪T)* and |α| ≤ |β| 

where  α  and  β  are  strings  of  non-terminals  and 

terminals. 

•  Context-sensitive  grammars  are  more  powerful 

than  context  free  grammars  because  there  are 
some languages that can be described by CSG but 

not  by  context  free  grammars  and  CSL  are  less 
powerful than unrestricted grammar. 

A decider for the Language L 

•  All  computations  of  a  decider  TM  must  halt. 

Decidable language are often called also recursive 

language. 

•  A  language  is  Turing  recognizable  if  it  is 

• Context sensitive grammar has 4-tuples. 

recognized by a TM. 

G = {N, Σ, P, S} 

N = Set of non-terminal symbols 

Σ = Set of terminal symbols 

S = Start symbol of the production 

P = Finite set of production 

Theorem–  LTM  accept  is  undecidable  the  proof  (to 

be gone through in class) show that in fact the more 

restricted language. 

Lsel  accept  =    {<  M,  <  M  >>  M  is  a  TM}  is 

undecidable the crucial idea is diagonalization. 

All rules in p are of the form α, α2 → α1 βα2 

•  The  language  that  can  be  defined  by  context 

sensitive grammar is called CSL. 

(cid:1)  Complexity– 

The  classes  P  and  NP- We introduce the classes P 

Properties of CSL are–  

and NP of languages. 

•  Union,  intersection  and  concatenation  of  two 

•  A  Turing  Machine  M  is  said  to  be  of  time 

context sensitive languages is context sensitive. 

complexity T(n) if the following holds. Input w of 

•  Complement  of  a  context-sensitive  language  is 

length  n,  M  halts  after  making  at  most  T(n) 

context-sensitive. 
(cid:1)  DECIDABILITY 

•  A  decision  problem  is  a  function  that  associates 
with  each  input  instance  of  the  problem  a  truth 
value true or false. 

moves. 

•  A  language  L  is  in  class  P  if  there  Exists  come 

polynomial  T(n)  such  that  L  =  T(m)  for  some 

deterministic Tm m of  time complexity T(n).  

Theory of Computation  

78 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 07.  

COMPILER DESIGN 

Overview of Language Processing System 

(cid:1)  Loader/Linker–  It  converts  the  re-locatable  code 
into  absolute  code  and  tries  to  run  the  program 
resulting in a running program or an error message. 
Linker  loads  a  variety  of  object  files  into  a  single 
file  to  make  it    executable.  Then  loader  loads  it  in 
memory and executes it. 

Structure of the compiler Design 

(cid:1)  Compiler–  Compiler  is  a  translator  program  that 
in  (High  Level 
translates  a  program  written 
Language)  the  source  program  and  translate  it  into 
equivalent  in  (Machine  Level  Language)  the  target 
program. As an important part of a compiler is error 
showing to the programmer. 

(cid:1)  Assembler– Programmers found it difficult to write 
or read programs in machine language. They begin 
to  use  a  mnemonic  (symbols)  for  each  machine 
subsequently 
instruction,  which 
translate  into  machine  language.  Such  a  mnemonic 
machine  language  is  now  called  an  assembly 
language.  Programs  known  as  assembler  were 
written  to  automate  the  translation  of  assembly 
language in to machine language. 

they  would 

(cid:1)  Interpreter–  An  interpreter  converts  high  level 
language into low level machine language, just like 
a  compiler.  But  they  are  different  in  the  way  they 
read  the  input.  The  compiler  in  one  go  reads  the 
inputs, does the processing, and executes the source 
code  whereas  the  interpreter  does  the  same  line  by 
line.  A  compiler  scans  the  entire  program  and 
translates  it  as  a  whole  into  machine  code  whereas 
an  interpreter  translates  the  program  one  statement 
at  a  time.  Interpreted  programs  are  usually  slower 
with respect to compiled ones.   

LEXICAL ANALYSIS  

Lexical  analysis  is  the  first  phase  of  the  compiler 
also known as a scanner. It converts the  high  level 
input program into a sequence of Tokens. 

•   Lexical  analysis  can  be  implemented  with  the 

Deterministic Finite Automata (DFA). 

•   The output is a sequence of tokens that is sent to the 

parser for syntax analysis. 

•   Token– Token is a sequence of characters that can 
be  treated  as  a  single  logical  entity.  Typical  token 
are,  (1)  Identifiers  (2)  Keywords  (3)  Operators  (4) 
Special symbols (5) Constants. 

•   Pattern– A set of strings in the input for which the 
same token is produced as output. This set of strings 
is  described  by  a  rule  called  a  pattern  associated 
with the token. 

•   Lexeme–  A  lexeme  is  a  sequence  of  characters  in 
the  source  program  that  is  matched  by  the  pattern 
for a token. e.g- "float", "=", "273". 

(cid:1)  FLEX (Fast Lexical Analyzer Generator)– FLEX 
is  a  computer  program  for  generating  lexical 
analyzers written by Vern Paxson in C around 1987. 
It  is  used  together  with  Berkeley  Yacc  Parser 

Compiler Design  

79 

YCT 

 
 
 
  
 
 
 
 
a  is  an  FIRST(Yi)  and  ε  is  in  all  of  FIRST(Yi)....., 
FIRST(Yi–1); that is, Y1, ...., Yi–1 ⇒ *ε. 
If ε is in FIRST(Yj) for all j = 1,2, ....., k then add ε 
to  FIRST(X).  For 
in 
FIRST(Y1)  is  surely  in  FIRST(X).  If  Y1  does  not 
derive ε, then add nothing more to FIRST(X), but if 
Y1 ⇒*ε, then add FIRST(Y2) and so on. 

everything 

example, 

2.   FOLLOW(A)–  To  compute  FOLLOW(A)  for  all 
non-terminals  A,  apply  the  following  rules  until 
nothing can be added to any FOLLOW set. 
1. Place  $  in  FOLLOW(S),  where  S  is  the  start 

symbol and $ is input right end marker. 

2. If  there  is  a  production  A  ⇒  α  B  β,  then 
everything  in  FIRST(β)  except  ε  is  placed  in 
FOLLOW(B). 

3. If there is a production A → αB or a production 
then 

A→αBβ,  where  FIRST(β)  contains  ε, 
everything in FOLLOW(A) is in FOLLOW(B). 

LR Parsers 
•   In  LR(K),  L  stands  for  Left  to  right  scanning,  R 
stands  for  Right  most  derivation,  K  stands  for 
number of look ahead symbols. 

•   LR  parsers  are  table-driven,  much  like  the  non-
recursive  LL  parsers.  A  grammar  which  is  used  in 
construction  of  LR  parser  is  LR  grammar.  For  a 
grammar to be LR it is sufficient that a left-to-right 
shift-reduce  parser  be  able  to  recognize  handles  of 
right-sentential  forms  when  they  appear  on  the  top 
of the stack. 

•   The time complexity for such parsers is O(n3). 
•   LR parsers are faster than LL(1) parser. 
•   LR parsing is attractive because– 
  →   The most general non-backtracking shift reduce 

parser. 

  →   The class of grammars that can be passed using 
LR methods is a proper super set of predictive 
parsers, LL(1) grammars CLR(1) grammars. 

  →   LR parser can detect a syntactic error in the left 

to right scan of the input. 

The LR parsing algorithm– 
 •   It  consists  of  an  input,  an  output,  a  stack,  a  driver 
program  and  a  parsing  table  that  has  two  parts 
(action and go to). 

•   The driver/parser program is  same  for all these  LR 
parsers, only the parsing table changes from parser 
to another. 

generator  or  GNU  Bison  parser  generator.  FLEX 
and Bison both are more flexible than Lex and Yacc 
and  produces  faster  code.  Bison  produces  parser 
from  the  input  file  provided  by  the  users.  The 
function  yylex()  is  automatically  generated  by  the 
flex  when  it  is  provided  with  a  .l  file  and  this 
yylex()  function  is  expected  by  parser  to  call  to 
retrieve tokens from this token stream.  

  Note–  The  function  yylex()  is  the  main  flex 
function that runs the Rule section and extension (.l) 
is the extension used to save the programs. 

(cid:1)  Program  Structure–  In  the  input  file,  there  are  3 

sections. 

(i)   Definition Section– The definition section contains 
the  declaration  of  variables,  regular  definitions, 
manifest constants. In the definition section, text is 
enclosed  in  "%{%}"  brackets.  Anything  written  in 
this brackets is copied directly to the file lex.yy.c. 
(ii)  Rules  Section–  The  rules  section  contains  a  series 
of rules in the form; pattern action and pattern must 
be unintended and action begin on the same line in 
{}  brackets.  The  rule  section 
in 
"%%%%". 

is  enclosed 

(iii)  User  Code  Section–  This  section  contains  C 
statements  and  additional  functions.  We  can  also 
compile these functions separately and load with the 
lexical analyzer. 

Parsing 
A  program  that  performs  syntax  analysis  is  called  a 
parser.  A  syntax  analyzer  takes  tokens  as  input  and 
output  error  message  if  the  program  syntax  is  wrong. 
Parser  obtains  a  string  of  tokens  from  the  lexical 
analyzer  and  verifies  that  it  can  be  generated  by  the 
language  for  the  source  program.  The  parser  should 
report any syntax errors in an intelligible fashion. 

(cid:1)  Constructing  a  parsing  table–  To  construct  a 
parsing table, we have to learn about two functions: 
1. FIRST()  2. FOLLOW() 

1.   FIRST(X)– To compute FIRST(X) for all grammar 
symbols X, apply the following rules until no more 
terminals or ε can be added to any FIRST set.  
1. If X is a terminal, then FIRST(X) is {X}. 
2. If X → ε is a production, then add ε to FIRST(X). 
3.  If  X  is  non-terminal  and  X→  Y1Y2  ....  YK  is  a 
production, then place 'a' in FIRST(X) if for some i, 

Compiler Design  

80 

YCT 

 
  
 
 
 
 
 
 
 
 
 
 
 
Stack– To store the string of the form. 
S0 X1 S1 ..... XmSm where 
Sm : state 

  Xm: grammar symbol 

Each  state  symbol  summarizes  the  information 
contained in the stack below it. 
Parsing Table– Parsing table consists of two parts- 
(i) ACTION Part– 
Let,  

Sm → top of the stack 
ai → current symbol 

Then  action  [Sm,  ai]  which  can  have  one  of  four 
values. 
1. Shift S, where S is a state. 
2. Reduce by a grammar production A→B  
3. Accept 
4. Error 
(ii)  GO  TO  Part–  If  goto  (S,  A)  =  X  where 
S→state, 
A  →  non-terminal,  then  GOTO  maps 
state S and non-terminal A to state X. 

Configuration–  
(S0x1S, x2S2 ... SmSm, aiai + 1 .. an $) 
The next move of the parser is based on action [Sm, ai]. 
The configurations are as follows– 
1.   If action [Sm, ai] = Shift S 

(S0x1S1, x2S2 ... xmSm, aiai + 1 ... an $) 

2.   If action [Sm, ai] = reduce A → B then 

(S0x1S1 x2S2 ... xm–rSm–r, As aiai + 1 ... an $) 
where S = goto [Sm–r, A] 

3.   If action [Sm, ai] = accept, parsing is complete. 
4.   If  action  [Sm,  ai]  =  error,  it  calls  an  error  recovery 

routine. 

SLR parsing table construction 
1.   Construct the canonical collection of sets LR(0) items 

for G'. Where G' the augmented grammar for G. 

2.   Create the parsing action table as follows: 

(a)   If a is a terminal and [A→ α aβ] is in Ii, go to 
(Ii, a) = Ij then action (i, a) to shift j. Here 'a' must be 
a terminal. 
(b)   If  [A  →α]  is  in  Ii,  then  set  action  [i,  a]  to 
'reduce A → α' for all a in FOLLOW(A); 
(c)   If  [S'→S]  is  in  Ii  then  set  action  [i,  $]  to 
'accept'. 
3.  Create  the  parsing  go  to  table  for  all  non-
terminals A, if go to (Ii, A) = Ij then go to [i, A] = j. 
4. All entries not defined by steps 2 and 3 are made 
errors. 
5. Initial state of the parser contains S' → S.  
The  parsing  table  constructed  using  the  above 
algorithm is known as SLR(1) table for G. 

Note–Every  SLR(1)  grammar  is  unambiguous,  but  every 

unambiguous grammar is not a SLR grammar. 
Canonical LR Parsing (CLR) 
•  To  avoid  some  of  invalid  reductions,  the  states 
need to carry more information. 
• Extra information input into a state by including a 
terminal symbol as a second component of an item. 
• The general form of an item. 

[A → αβ, a] 

  Where A → αβ is a production. 

a is terminal/right end marker ($). We will call it as 
LR(1) item. 
'LR(1)  item  is  a  combination  of  LR(0)  items  along 
with  look  ahead  of  the  item.  Here  1  refers  to  look 
ahead of the item.' 
Construction of the sets of LR(1) items 

Function closure(I): 

Begin 
Repeat 
For each item [A→ α.B.β, a] in I, 
Each production B → γ in G', 
  And each terminal b in FIRST(βa) 
Such that [B→γ, b] is not in I do 

  Add [B → γ, b] to I; 

End; 

  Until no more items can be added to I; 
L. ALR Parsing Table 
•  The  tables  obtained  by  it  are  considerably  smaller 

than the canonical LR table. 
•   LALR stands for look ahead LR. 
•   The  number  of  states  in  SLR  and  LALR  parsing 

tables for a grammar G are equal. 

•   But  LALR  parsers  recognize  more  grammars  than 

SLR. 

•   YACC  creates  a  LALR  parser  for  the  given 

grammar. 

•   YACC stands for 'Yet another compiler compiler'. 
•  An  easy,  but  space-consuming  LALR 

table 

construction is explained below: 

1.  Construct  C = {I0, I1, ...., In}, the collection of sets 

of LR(1) items. 

2.  Find all sets having the common core; replace these 

sets by their union. 

3.   Let C' = {J0, J1, ....Jm} be the resulting sets of LR(1) 
items.  If  there  is  a  parsing  action  conflict  then  the 
grammar is not a LALR(1). 

4.  Let  K  be  the  union  of  all  sets  of  items  having  the 

same core. Then goto (J, X) = K. 
•  If  there  are  no  parsing  action  conflicts  then  the 
grammar is said to LALR(1) grammar. 
•  The  collection  of  items  constructed  is  called 
LALR(1) collection. 

(cid:1)  Comparison of parsing methods– 

Every LR(0) in SLR (1) but vice versa is not true. 

Compiler Design  

81 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  Syntax  Directed  Translation–  To  translate  a 
programming  language  construct,  a  compiler  may 
need to  know  the type of construct, the location of 
the  first instruction, and the  number of instructions 
generated etc so, we have to use the term 'attributes' 
associated with constructs. 

An  attribute  may 

type, 
number 
location, 
compatibility of variables used in a statement which 
cannot be represented by CFG alone. 

arguments,  memory 

represent 

of 

So, we need to have one more phase to 

do this, i.e., 'semantic analysis' phase. 

In  this  phase,  for  each  production  CFG,  we  will 
given some semantic rule. 

Syntax Directed Definition (SDD) 
 It  is  high  level  specification  for  translation.  They 
hide  the  implementation  details,  i.e.,  the  order  in 
which translation takes place. 

  Attributes + CFG + Semantic rules = SSD 
  A SDD is a generalization of a CFG in which each 
grammar  symbol  is  associated  with  a  set  of 
attributes.  There  are  two  types  of  set  of  attributes 
for a grammar symbol. 
1. Synthesized attributes 
2. Inherited attributes 
Each  production  rule  is  associated  with  a  set  of 
semantic  rules.  Semantic  rules  setup  dependencies 
between  attributes  which  can  be  represented  by  a 
graph 
dependency 
determines  the  evaluation  order  of  these  semantic 
rules.  Evaluation  of  a  semantic  rule  defines  the 
value of an attribute. But a semantic rule  may also 
have some side effects such as printing a value. 
(cid:1)  Attribute  grammar–  An  attribute  grammar  is  a 
syntax directed definition in which the functions in 
semantic rules 'cannot have side effects'.  

graph.  The 

dependency 

(cid:1)  Annotated  parse  tree–  A  parse  tree  showing  the 
values  of  attributes  at  each  node  is  called  an 
annotated parse tree. The process of computing the 
attribute values at the nodes is called annotating (or 
decorating) of the parse tree. 

In  a  SDD,  each  production  A  →  ∞  is 

associated with a set of semantic rules of the form: 

b = f(C1, C2, ......Cn) where 
f : A function 

b can be one of the following: 
b  is  a  'synthesized  attribute'  of  A  and  C1,  C2, 
...........Cn  are  attributes  of  the  grammar  symbols  in 
A → ∞ 
The  value  of  a  'synthesized  attribute'  at  a  node  is 
computed  from  the  value  of  attributes  at  the 
children of that node in the parse tree. 

(cid:1)  Synthesized Attribute– The value of a synthesized 
attribute  at  a  node  is  computed  from  the  value  of 
attributes at the children of that node in a parse tree. 
Consider the following grammar: 

L → En 
E → E1 + T   
E → T 
T → T1*F 
T → F 
F → (E) 
F → digit 
Let  us  consider  synthesized  attribute  value  with 
each  of  the  non-terminals  E,  T  and  F  Token  digit 
has  a  synthesized  attribute  lexical  supplied  by 
lexical analyzer. 

Production 

Semantic Rule 

print (E.val) 
E.val: = E1.val + T.val 
E.val: = T1.val 
T.val: = T1.val*F.val 
T.val: = F.val 
F.val: = E.val 
F.val: = digit.lexval 

L → En 
E → E1 + T 
E → T 
T → T1*F 
T → F 
F → (E) 
F → digit 
(cid:1)  Inherited  Attributes–  An  attribute  of  a  non-
terminal  on  the  right-hand  side  of  a  production  is 
called  an  inherited  attribute.  The  attribute  can  take 
value  either  from  its  parent  or  form  its  siblings 
(variables  in  the  LHS  or  RHS  of  the  production). 
For example, let's say A → BC is a production of a 
grammar  and  B's  attribute  is  dependent  on  A's 
attributes  or  C's  attributes  then  it  will  be  inherited 
attribute. 
Types  of  SDD's–  Syntax  Directed  Definitions 
to  specify  syntax  directed 
(SDD)  are  used 
translations. There are two types of SDD. 
1. S-attributed definitions 
2. L-attributed definitions 

S-attributed definitions– 
•   Only  synthesize  attributes  used  in  syntax  direct 

definition. 

•  S-attributed  grammars  interact  well  LR(K)  parsers 
since the evaluation of attributes is bottom-up. They 
do not permit dependency graphs with cycles. 

L-attributed definitions– 
•   Both inherited and synthesized attribute are used. 
•   L-attributed  grammar  support  the  evaluation  of 
attributes  associated  with  a  production  body, 
dependency-graph  edges  can  go  from  left  to  right 
only. 

•   Each  s-attributed  grammar  is  also  a  L-attributed 

grammar. 

•  L-attributed  grammars 

can  be 

incorporated 

conveniently in top down parsing. 

•   These  grammars  interact  will  with  LL(K)  parsers 

(both table driven and recursive descent). 

  A  syntax  directed  definition  is  L-attributed  if  each 
inherited attribute of Xj, 1 ≤ j ≤ n, on the right side 
of A→X1, X2 ..... Xn, depends only on– 

1.  The attributes of symbols X1, X2, .... Xj–1 to the left 

of Xj in the production. 

Compiler Design  

82 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2.  The inherited attributes of A. 

is  L-attributed, 
Every  S-attributed  definition 
because  the  above  two  rules  apply  only  to  the 
inherited attributes. 

Intermediate Code Generation 
In the analysis-synthesis model, the front end translates 
a  source  program  into  an  intermediate  representation 
(IR). From IR the back end generates target code. 

of 

are 

types 

different 

intermediate 

There 
representations– 
•   High level IR, i.e. AST (Abstract Syntax Tree). 
•   Medium level IR, i.e. Three address code. 
•  Low level IR, i.e. DAG (Directed Acyclic Graph) 
•  Postfix Notation (Reverse Polish Notation, RPN). 
Benefits of Intermediate Code Generation (ICG)–  
1.   We can obtain an optimized code. 
2.  Compilers can be created for the different machines 
by attaching different backend to existing front end 
of each machine. 

3.  Compilers  can  be  created  for  the  different  source 

languages. 

(cid:1)  Directed Acyclic Graphs (DAG) for expression– 
•  A DAG  for an expression identifies the common 
sub expressions in the given expression. 
•  A node N in a DAG has more than one parent if 
N represents a common sub expression. 
•  DAG  gives 
regarding 
evaluate the expressions. 

the  generation  of  efficient  code 

important  clues 
to 

the  compiler, 

(cid:1)  Three-Address Code– In three address codes, each 
statement  usually  contains  3  addresses,  2  for 
operands and 1 for the result. 
Example– x = y OP z 
• x, y, z are names constants or compiler generated 
temporaries. 
•  OP  stands  for  any  operator.  any  arithmetic 
operator or logical operator. 

(cid:1)  Types of three address statement– 

  Assignment–  
•  Binary assignment : x = y OP z store the result of 
y OP z to x. 
•  Unary  assignment  x  =  OP  y  store  the  result  of 
unary operation on y to x. 

  Copy– 

• Simple copy x = y store y to x. 
• Indexed copy x = y [i] store the contents of y[i] to 
x. 
• x[i] = y store y to (x + i)th address. 
  Address and pointer manipulation– 

x = & y  
x = * y 

*x = y  

store address of y to x 
store address of y to x 
store y to location pointed by x 

Jump– 
• Unconditional jump– goto L, jumps to L. 
• Conditional: 

if (x relop y) 
goto L1; 
else 
{ 
goto L2; 
} 

where relop is <, <=, >, >=, = or ≠ 

Procedure call– 

Param x1; 
Param x2; 
. 
. 
. 
Param xn; 

call procedure p with n parameters 

Call p, n, x; 
and store the result in x. 
return x 

Use x as result from procedure. 

(cid:1)  Implementation  of  three  Address  Statements– 
Three  address  statements  can  be  implemented  as 
records  with  fields  for 
the 
the  operator  and 
operands. There are 3 types of representations– 
1. Quadruples 
2. Triples 
3. Indirect triples 

1.   Quadruples– A quadruple has four fields: op, arg1, 

arg2, and result. 
•  Unary operators do not use arg2. 
•  Param use neither arg2 nor result. 
•  Jumps put the target label in result. 
•  The  contents  of  the  fields  are  pointers  to  the 
symbol table entries for the names represented by 
these fields. 

•  Easier to optimize and move code around. 
•  For  the  expression  x  =  y  *  –  z  +  y*  –  z,  the 

quadruple representation is– 

Arg2 

OP 
Uminus 
* 
Uminus 
* 
+ 
= 

(0) 
(1) 
(2) 
(3) 
(4) 
(5) 
 2.  Triples– Triples have three fields: OP, arg1, arg2. 

t3 
t4 

Result 
t1 
t2 
t3 
t4 
t5 
x 

Arg1 
z 
y 
z 
y 
t2 
t5 

t1 

•  Temporaries  are  not  used  and  instead  references 

to instructions are made. 

•  Triples are also known as two address code. 
•  Triples  takes  less  space  when  compared  with 

quadruples. 

•  Optimization by moving code around is difficult. 
representations  of 
triple 
•  The  DAG 
expressions are equivalent. 

and 

•  For the expression a = y* – z + y* – z the triple 

representation is– 

Compiler Design  

83 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
OP 
Uminus 
* 
Uminus 
* 
+ 
= 

(0) 
(1) 
(2) 
(3) 
(4) 
(5) 
3.   Indirect Triples– 

Arg1 
z 
y 
z 
y 
(1) 
a 

Arg2 

(0) 

(2) 
(3) 
(4) 

•  In  direct  triples,  pointers  to  triples  will  be  there 

instead of triples. 

• Optimization by moving code around is easy. 
•  Indirect  triples  takes  less  space  when  compared 

with quadruples. 

•  Both  indirect  triples  and  quadruples  are  almost 

equally efficient. 

•  High  Level  Intermediate  representation.  Example- 

Abstract Syntax Tree (AST) 

•  Medium-level 

representation. 
intermediate 
Example-Control flow graph of complex operations. 
•  Low-Level  Intermediate  representation.  Example- 

Quadruples, DAGs. 

•   Code for abstract stack machine, i.e. postfix code. 
2.   Target  Programs–  The  output  of 

the  code 
generator  is  the  target  program.  The  output  may 
take on a variety of forms– 
(i) Absolute machine language 
(ii) Relocatable machine language   
(iii) Assembly language 

3.  Memory  Management–  Mapping  names  in  the 
source  program  to  addresses  of  data  objects  in 
runtime  memory  is  done  by  the  front  end  and  the 
code generator. 
•  A  name  in  a  three  address  statement  refers  to  a 

• Indirect triple representation of 3-address code. 

symbol entry for the name. 

(0) 
(1) 
(2) 
(3) 
(4) 
(5) 

(14) 
(15) 
(16) 
(17) 
(18) 
(19) 

Statement 
(14) 
(15) 
(16) 
(17) 
(18) 
(19) 

OP 
Uminus 
* 
Uminus 
* 
+ 
= 

Arg1  Arg2 

(14) 

z 
y 
z 
(16) 
y 
(17) 
(15) 
(18) 
x 
Code Generation 

Code  generation  is  the  final  phase  of  the  compiler 
model. 

The requirement imposed on a code generator are– 
• Output code must be correct. 
• Output code must be of high quality. 
• Code generator should run efficiently. 
(cid:1)  Issues in the design of a code generator– 
1.  Input 

Intermediate 
the  code  generator– 
representation  with  symbol  table  will  be  the  input 
for the code generator. 

to 

•  Stack, heap, garbage collection is done here. 

4.   Instruction 

selection– 

Instruction 

selection 

depends on the factors like- 
• Uniformity 
• Completeness of the instruction 
• Instruction speed 
• Machine idioms 
• Choose set of instructions equivalent to intermediate 

representation code. 

• Minimize execution time used registers and code 

size. 

5.   Register allocation–  

•  Instructions with register operands are faster. So, 

keep frequently used values in registers. 

•  Some registers are reserved. 
Example–  SP,  PC  etc.  minimize  number  of  loads 
and stores. 
6. Evaluation order–  
•  The  order  of  evaluation  can  affect  the  efficiency 

of the target code. 

•  Some  orders  require  fever  registers  to  hold 

intermediate results. 

  Runtime storage management– To run a compiled 
program,  compiler  will  demand 
the  operating 
system  for  the  block  of  memory.  This  block  of 
memory  is  called  runtime  storage.  This  runtime 
storage is subdivided into the generated target code, 
Data  objects  and  information  which  keeps  track  of 
procedure activations. 
The  runtime  storage  contains  stack  and  the  heap. 
Stack  contains  activation  records  and  program 
counter, data object within this activation record are 
also stored in this stack with relevant information. 
  Activation  Record–  Information  needed  during  an 
execution  of  a  procedure  is  kept  in  a  block  of 
storage called an activation record. 
•  Storage for names local to the procedure appears 

in the activation record. 

•  Each  execution  of  a  procedure  is  refereed  as 

activation of the procedure. 

Compiler Design  

84 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
•  If  the  procedure  is  recursive,  several  of  its 

activation might be alive at a given time. 

•  Runtime storage is subdivided into 
1. Generated target code area 
2. Data objects area 
3. Stack 
4. Heap 
Code 
Static data 
Stack 

.......↓ 

.......↑ 

Heap 
•  Sizes  of  stack  and  heap  can  change  during 

program execution. 

For  code  generation  there  are  two  standard  storage 
allocations: 

1.   Static  allocation–  The  position  of  an  activation 

record in memory is fixed at compile time. 

2.   Stack  allocation–  A  new  activation  record  is 
pushed  on  to  the  stack  for  each  execution  of  the 
procedure. 

(cid:1)  Basic  Blocks–  Basic  blocks  are  sequence  of 
consecutive  statements  in  which  flow  of  control 
enters at the beginning and leaves at the end without 
a halt or branching. 
1. First determine the set of leaders. 
• First statement is leader 
• Any target of goto is a  leader. 
• Any statement that follows a goto is a leader. 
2.  For  each  leader  its  basic  block  consists  of  the 
leader and all statements up to next leader. 
(cid:1)  Initial node: Block with first statement is leader. 
(cid:1)  Once the basic blocks have been defined, a number 
of  transformations  can  be  applied  to  them  to 
improve the quality of code. 
1. Global : Data flow analysis. 
2. Local : Structure preserving transformations, 
    Algebraic transformations 

(cid:1)  Basic  Blocks  compute  a  set  of  expressions.  These 
expressions are the values of the names live on exit 
from the block. 

(cid:1)  Two basic blocks are equivalent it they compute the 

same set of expressions. 

(cid:1)  DAG Representation of Basic Blocks–  

•  DAGs are useful data structures for implementing 

transformations on basic blocks. 

•  Tells, how value computed by a statement is used 

in subsequent statements. 

•  It  is  a  good  way  of  determining  common  sub 

expressions. 

(cid:2) Leaves are labeled by unique identifiers, either 

variable names or constants. 

(cid:2) Interior  nodes  are  labeled  by  an  operator 

symbol. 

(cid:2) Nodes  are  also  optionally  given  as  a  sequence 

of identifiers for labels. 

Peephole Optimization 
•  Target  code  often  contains  redundant  instructions 

• 

and suboptimal constructs. 
Improving the performance of the target program by 
examining  a  short  sequence  of  target  instructions 
(peephole)  and  replacing  these  instructions  by  a 
shorter or faster sequence is peephole optimization. 
•   The  peephole  is  a  small,  moving  window  on  the 
target  program.  Some  well  known  peephole 
optimizations are– 
(i) Elimination of Redundant Loads and Stores– 
Example- 

(i) MOV R0, a 
(ii) MOV a, R0 

  We can delete instruction (ii), because the value of a 

is already in R0. 
(ii) Eliminating Unreachable Code– An unlabeled 
and 
instruction 
unconditional jump maybe removed. 

immediately 

following 

•   May be produced due to debugging code introduced 

during development. 

•   May  be  due  to  updates  in  programs  without 

control  optimizations–  The 

considering the whole program segment. 
(iii)  Flow  of 
unnecessary jumps can be eliminated. 
Jumps like: 
Jumps to jumps, 
Jumps to conditional jumps,  
Conditional jumps to jumps: 
Example– We can replace the jump sequence 
goto L1  
....... 
L1 : got L2 
By the sequence 

  Got L2 

L1: got L2 
.... 
It there are no jumps to L1 then it may be possible to 
eliminate the statement L1 : goto L2. 
(iv) Reduction in strength– 
•  x2 is cheaper to implement as x*x than as a call to 

exponentiation routine. 

x*23 ⇒ x << 3 

•  Replacement of multiplication by left shift. 
Example– 
•  Replace division by right shift. 
Example– x >> 2 (is x/22) 
(v) Use of machine Idioms– 
•  Auto  increment  and  auto  decrement  addressing 

•  A DAG for a basic block has following labels on 

modes can be used whenever possible. 

the nodes: 

Compiler Design  

Example– replace add # 1, R by INCR. 

85 

YCT 

 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   08.  

OPERATING SYSTEM 

Introduction 
Operating system acts as an interface between computer 
hardware  and  user.  It  manages  and  controls  all  the 
hardware and flow of data, instructions and information 
to  within  the  system.  The  operating  system  takes 
instructions from the user and directs it to CPU, which 
further passes the instructions to the hardware. 

(cid:1)  Operating system Services– 

Operating system is one of the core software programs 
that run on hardware and makes it usable. The user can 
interact with hardware so that they can send commands 
and  receive  output.  An  operating  system  provides  an 
interface between user and machine. This interface can 
be Graphical User Interface (GUI) in which users. Click 
on screen elements to interact with operating system or 
a  Command  Line  Interface  (CLI)  to  tell  the  operating 
system  to  do  things,  it  also  manages  the  computers 
resource  such  as  CPU,  memory,  disk  drives  and 
printers. It provides services for application software. 

Types of Operating System 

Process concept 
(cid:2)   Text Section– A process is more than the program 
code, which is sometimes known as the text section. 
It  also  includes  the  current  activity,  as  represented 
by the value of the program counter. 

(cid:2)   Stack–  The  stack  contains  temporary  data,  such  as 
function  parameters,  returns  addresses,  and  local 
variables. 

(cid:2)   Data Section– Contains the global variable. 
(cid:2)   Heap–  Dynamically  allocated  memory  to  process 

during its run time. 

(cid:1)  Process state 

(cid:1) 

Function of an Operating System–   

• New– The process is being created. 
• Running– Instructions are being executed. 
•  Waiting–  The  process  is  waiting  for  some  event 

to occur. 

• Ready– The process is waiting to be assigned to a 

processor. 

• Terminated– The process has finished execution. 

Operating System  

86 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  Process  Control  Block  (PCB)–  Process  in  an 
operating  system  is  represented  by  a  data  structure 
called  Process  Control  Block  (PCB)  also  called  a 
task control block. 

•   Pointer– It is a stack pointer which is required to be 
saved  when  the  process  is  switched  from  one  state 
to  another  to  retain  the  current  position  of  the 
process. 

•   Process  State–  The  state  may  be  new,  ready, 

running, waiting, halted and so on. 

•   Process  Number–  Every  process  is  assigned  with 
unique ID known as process ID or PID which stores 
the process identifier. 

•   Program  Counter–  The  counter  indicates  the 
address  of  the  next  instruction  to  be  executed  for 
this process. 

•   Registers–  These  are  the  CPU  registers  which 
includes:  accumulator,  base,  registers  and  general 
purpose registers. 

•   Memory  Limits–  This 

the 
information  about  memory  management  system 
used  by  operating  system.  This  may  include  the 
page tables, segment tables etc. 

contains 

field 

•   Open Files List– This information includes the list 

of files opened for a process. 
Threads 

Thread is a single sequence stream within a process. 
Threads  have  same  properties  as  of  the  process  so 
they  are  called  as  light  weight  processes.  Threads 
are executed one after another but gives the illusion 
as if they are executing in parallel. Each thread has 
different states. 

Sr. 
No. 

Similarity  between 
and 
Threads 
Processes 

Difference  between 
and 
Threads 
Processes 

are 

Threads 
not 
independent  of  one 
another  but  processes 
are independent. 

Unlike  processes,  all 
threads  can  access 
every  address  in  the 
task. 

Threads  are  designed 
to  assist  each  other, 
processes may or may 
not do it. 

1.  Only  one  thread  or 
process  is  active  at  a 
time. 

2.  Within  a  processes, 
execute 

both 
sequentially. 

3. 

4. 

can 

Both 
children. 

create 

thread  or 
is  blocked, 
thread  or 

If  one 
process 
another 
process can run. 

Parameters 

Implemented 
by 

Recognize 

Context 
switch time 

Hardware 
support 

Blocking 
operation 

Types of Threads 
1. User  Level 
Thread 
(ULT) 

2.  Kernel 
Level 
Thread 
(KLT) 

threads 

User 
are 
implemented 
by users. 

threads 

Kernel 
are 
implemented 
by 
system. 

operating 

Operating 
system  doesn't 
recognize  user 
level threads. 

threads 
recognize 
operating 

Kernel 
are 
by 
system. 

Context  switch 
time is less. 

Context  switch 
time is more. 

Context  switch 
no 
requires 
hardware 
support. 

user 
thread 

If  one 
level 
performs 
blocking 
operation  then 
entire  process 
will 
be 
blocked. 

Hardware 
support 
needed. 

is 

If  one  Kernel 
thread  perform 
blocking 
operation 
another 
can 
execution. 

then 
thread 
continue 

Operating System  

87 

YCT 

 
 
 
 
 
 
 
 
Creation  and 
Management 

Operating 
system 

Thread 
management 

User 
level 
threads  can  be 
created 
and 
managed  move 
quickly. 

Any  operating 
system 
can 
support 
user-
level threads. 

The 
thread 
library contains 
for 
the  code 
thread  creation 
message 
passing,  thread 
scheduling data 
transfer 
and 
thread 
destroying. 

level 
take 
to 
and 

time 

Kernel 
threads 
more 
create 
manage. 

level 
are 

Kernel 
threads 
operating 
system-
specific. 

It 

The  application 
code  does  not 
thread 
contain 
management 
code. 
is 
merely  an  API 
the  Kernel 
to 
mode. 
The 
windows 
operating 
system  makes 
use 
this 
of 
feature. 

Example 

Example-  Java 
thread,  POSIX 
threads. 

Example– 
Window 
Solaris. 

Advantages 

•  User 

threads 
simple 
quick 
create.  

level 
are 
and 
to 

•  Can  run  on 

any 
operating 
system. 

•  In  user  level 

threads, 
switching 
between 
threads  does 
not 
need 
Kernel  mode 
privileges. 

• Scheduling  of 

multiple 
that 
threads 
belong 
to 
same  process 
different 
on 
is 
processors 
in 
possible 
Kernel 
level 
threads. 

• Multi 

threading  can 
there  for 
be 
Kernel 
routines. 

• When 

a 
thread  at  the 
Kernel 
level 
is  halted,  the 
Kernel 
can 
schedule 
another 
thread  for  the 
same process. 

Disadvantages 

•  Multi  thread 
applications 
on user-level 
threads 
cannot 
benefit  from 
multi 
processing. 
•  If  a  single 
user-level 
thread 
performs 
blocking 
operation, 
the 
process 
halted. 

entire 
is 

a 

•  Transferring 

control 
within 
a 
process  from 
one  thread  to 
another 
necessitates  a 
mode  switch 
to 
Kernel 
mode. 
•  Kernel 

level 
threads  takes 
more  time  to 
and 
create 
manage  than 
user 
level 
threads. 

(cid:1)  Multi-threading Models–   
Many-to-One 
Model 

One-to-One 
Model 

Many-to-Many 
Model 

In  this  model, 
have 
we 
multiple 
user 
threads 
mapped  to  one 
Kernel  thread. 
When  a  user 
thread  makes  a 
blocking 
call 
system 
entire  process 
blocks.  As  we 
have  only  one 
Kernel 
thread 
and  only  one 
user thread can 
access  Kernel 
at  a  time,  so 
multiple 
threads  are  not 
able 
access 
multiprocessor 
same 
at 
time. 

the 

In  this  model, 
one 
to 
one 
relationship 
between 
and 
Kernel 
thread. 
user 
Multiple thread 
can 
on 
run 
multiple 
processor. 
Problem  with 
this  model 
is 
that  creating  a 
thread 
user 
the 
requires 
corresponding 
Kernel 
thread. 
As  each  user 
is 
thread 
connected 
to 
different. 
Kernel,  if  any 
thread 
user 
makes 
a 
blocking 
system call, the 
user 
other 
threads  would 
not be blocked. 

this  model, 
have 
user 

In 
we 
multiple 
threads 
multiplex 
to 
same  or  lesser 
of 
number 
Kernel 
level 
threads. 
of 
Number 
level 
Kernel 
threads 
are 
specific  to  the 
machine, 
of 
advantage 
this  model  is  if 
a  user  thread  is 
blocked  we  can 
schedule  others 
to 
user 
thread 
Kernel 
other 
thread. 
Thus, 
system  does  not 
block 
a 
particular thread 
is  blocked.  It  is 
the  best  multi-
threading 
model. 

if 

Operating System  

88 

YCT 

 
  
 
 
fork() in C 

that  makes 

Fork()  system  call  is  used  for  creating  a  new 
process,  which  is  called  child  process,  which  is 
called process, which runs con-currently with the 
process 
the  fork()  call  (parent 
process).  After  a  new  child  process  is  created, 
both  processes  will  execute  the  next  instruction 
following the fork() system call. A child process 
uses  the  same  program  counter,  same  CPU 
registers, same open files which use in the parent 
process. 

()

 Note–  
1.  fork()  is  threading  based  function,  to  get  the  correct 

output run the program on a local system. 

2. Total number of processes = 2n, where n is number of 

fork() system calls. 

Process Scheduling 

 The  process  scheduling  is  the  activity  of  the 
process manager that handles the removal of the 
running process  from the  CPU and the  selection 
of  another  process  on  the  basis  of  a  particular 
strategy. 
a 
is 
multiprogramming  operating 
systems.  Such 
operating  systems  allow  more  than  one  process 
to  be  loaded  into  the  executable  memory  at  a 
time  and  the  loaded  process  shares  the  CPU 
using time multiplexing. 

essential  part  of 

an 

It 

Types of Process Scheduler 

term 

Long 
scheduler 

short 
scheduler 

term 

It  is  a  job 
scheduler. 

a  CPU 

is 
It 
scheduler. 

Speed  is  fastest 
among other two. 

is 
than 
term 

Speed 
lesser 
short 
scheduler. 

Medium  term 
scheduler 

It  is  a  process 
swapping 
scheduler. 

is 

Speed 
in 
between  both 
short  and  long 
term 
scheduler. 

It controls the 
of 
degree 
multi-
programming. 
It  is  almost 
or 
absent 
minimal 
in 
time  sharing 
system. 
It 
processes 
from 
pool 
and 
loads 
into 
them 
memory  for 
execution. 

selects 

It  provides  lesser 
over 
control 
degree 
of 
multiprogramming 
It is also minimal 
time  sharing 
in 
system. 

It  reduces  the 
of 
degree 
multi-
programming. 
It  is  a  part  of 
sharing 
Time 
systems. 

those 
It  selects 
processes  which 
are 
to 
ready 
execute. 

re-
can 
It 
the 
introduce 
into 
process 
memory 
and 
execution  can 
be continued. 

Categories of scheduling 

Preemptive scheduling 

A  processor  can  be 
to  execute 
preempted 
the  different  processes 
in  the  middle  of  any 
current 
process 
execution. 
CPU  utilization  is  more 
efficient  compared 
to 
non-preemptive 
scheduling. 
scheduling 
Preemptive 
is 
The 
prioritized. 
highest  priority  process 
is 
is  a  process 
currently utilized. 

that 

be 
Starvation  may 
the 
to 
caused,  due 
insertion 
priority 
of 
process in the queue. 

It 
is  quite 
flexible 
critical 
the 
because 
processes are allowed to 
access  CPU  as 
they 
arrive  in  to  the  ready 
queue,  no  matter  what 
process 
executing 
is 
currently. 
Examples of preemptive 
scheduling  are  Round 
Robin 
Shortest 
and 
Remaining Time First. 

Non-Preemptive 
scheduling 

the 

Once 
processor 
starts  its  execution,  it 
must  finish 
it  before 
executing  the  other.  It 
can't  be  paused  in  the 
Middle.  
CPU  utilization  is  less 
efficient  compared 
to 
preemptive scheduling. 

When any process enters 
the  state  of  running,  the 
state  of  that  process  is 
never  deleted  from  the 
scheduler 
it 
finishes its job. 
Starvation 
can  occur 
when  a  process  with 
large 
time 
burst 
occupies the system. 

until 

It  is  rigid  as  even  if  a 
critical  process  enters 
the 
the 
ready  queue 
process  running  CPU  is 
not disturbed. 

Examples 
of 
non-
scheduling 
preemptive 
are  First  Come  First 
Serve  and  Shortest  Job 
First. 

Operating System  

89 

YCT 

 
 
 
 
 
Scheduling Algorithms 

First-Come, First-Served (FCFS) Scheduling– 

•  In this scheduling algorithm, jobs are executed 

on a first come, first serve basis. 

•  It  is  both  preemptive  and  non-preemptive 

scheduling algorithm. 

•  Easy to understand and implement. 

•  Its implementation is based on FIFO queue. 

•  Poor  in  performance  as  average  wait  time  is 

(cid:1) 

high. 

Process Waiting Time

P
0
P
1
P
2
P
3

5
5 0
− =
8 1 7
− =
14 2 12
− =
22 3 19
− =

Average Waiting Time = (5 + 7 + 12 +19 )/4  

             = 10.75 

Round-Robin Scheduling– 
•  Round  Robin 

is 

the  preemptive  process 

scheduling algorithm. 

•  Each process is provided a fix time to execute, 

Process Arrival Time Execute Time Service Time

it is called a time quantum. 

P
0
P
1
P
2
P
3

0
1
2
3

Gantt Chart– 

5
3
8
9

5
8
16
25

P
0

P
1

P
2

P
3

0

5

8

16

25

Waiting Time  = Service Time – Arrival Time 

•  Once  a  process  is  executed  for  a  given  time 
period,  it  is  preempted  and  other  process 
executes for a given time period. 

•  Context  switching  is  used  to  save  states  of 

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

Process Waiting Time

P
0
P
1
P
2
P
3

(cid:1)(cid:1)
5 0 5
− =
8 1 7
− =
16 2 14
− =
22
25 3
− =

Average Waiting Time = (5 + 7 + 14 + 22)/4 = 12 

(cid:1) 

Shortest-Job-First (SJF) Scheduling– 

•  This  algorithm  scheduling  depends  on  the 
length of next CPU burst of process, rather than 
its total length. Process with the minimum burst 
time at an instance executes first. 

•  It  is  very  efficient  in  minimizing  the  waiting 
time and is easy to implement in Batch system. 

•  It  cannot  be  implemented  if  the  required  CPU 

time is not known in advance. 

Process Arrival Time Execute Time Service Time

P
0
P
1
P
2
P
3

0
1
2
3

5
3
8
6

5
8
14
22

P
0

P
1

P
2

P
3

0

5

8

14

22

 Waiting Time  = Service Time – Arrival Time 

P0 
P1 
P2 
P3 
P4 

0 

1 

2 

3 

5 

4 

5 

3 

2 

6 

12 

17 

9 

11 

20 

12 

16 

7 

8 

15 

Ready Queue  

P0 ; P1 ; P2 ; P3 ; P4 ; P1; P5 
Gantt chart 

P0 

P1 

P2 

P3 

P0 

P4 

P1 

P4 

    0        3         6        9       11       12      15      17    20 
Average Waiting Time = (12 + 16 + 7 + 8+15)/5 = 11.6 
Synchronization 

on 

perform  write 

read  and 
the 

some 
Some  processes  perform 
processes 
file 
simultaneously.  This  lead  to  data  inconsistency 
as data is being read as well as modified by many 
processes at the same time. To prevent such data 
inconsistency 
is 
required.  All  process  that  want  to  perform  read 
operation  can  do  the  reading  simultaneously  but 
process  that  needs  to  perform  write  operation 
should do it one at a time. The process that exist 
at the same time are called concurrent processes. 

synchronization 

process 

Operating System  

90 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
(cid:1) 

(cid:1) 

•  Processes  are  categorized  as  one  of  the 
following two types– 
1.   Independent process– The execution of one 
process does not affect the execution of other 
processes. 

2.   Cooperative  process–  A  process  that  can 
affect  or  be  affected  by  other  processes 
executing in the system. 

Process  synchronization  problem  arises  in  the 
case  of  cooperative  process  also  because 
resources are shared in cooperative process.  

Race  Conditions–  Process  that  are  working 
together  share  some  common  storage  (main 
memory, file etc.) that each process can read and 
write.  When  two  or  more  processes  are  reading 
or  writing  some  shared  data  and  the  final  result 
depends  on  who  runs  precisely  when,  are  called 
race  conditions.  Several  processes  access  and 
process  the  manipulations  over  the  same  data 
concurrently  then  the  outcome  depends  on  the 
particular  order  in  which  the  access  takes  place. 
A  race  condition  is  a  situation  that  may  occur 
inside a critical section.  
The  Critical-Section  Problem–  Consider  a 
system consisting of n processes {P0, P1, ......, Pn–
1}. Each process has a segment of code, called a 
critical  section,  in  which  the  process  may  be 
changing  common  variables,  updating  a  table, 
writing  a  file,  and  so  on.  The  critical  section 
problem is to design a protocol that the processes 
can use to cooperate. Each process  must request 
permission to enter its critical section. 
The section of code implementing this request is 
the  entry  section.  The  critical  section  may  be 
followed by an exit section. The remaining code 
is  the  remainder  section.  The  entry  section  and 
exit  section  are  enclosed  in  boxes  to  highlight 
these  important  segments  of  code.  The  general 
structure  of  a  typical  process  Pi  is  shown 
following– 

do { 

 entry section 

critical section 

 exit section 

remainder section 

 } while (true); 

A  solution  to  the  critical-section  problem  must 
satisfy the following three requirements: 
1.   Mutual exclusion– If process Pi is executing 
in its critical section, then no other processes 
can be executing in their critical sections. 
2.   Process–  If  no  process  is  executing  in  its 
critical  section  and  some  processes  wish  to 
enter  their  critical  sections,  then  only  those 
processes  that  are  not  executing  in  their 
remainder 
in 
deciding  which  will  enter  its  critical  section 
next,  and  this  selection  cannot  be  postponed 
indefinitely. 

can  participate 

sections 

3.   Bounded  waiting–  There  exists  a  bound,  or 
limit,  on  the  number  of  times  that  other 
processes  are  allowed  to  enter  their  critical 
sections after a process has made a request to 
enter  its  critical  section  and  before  that 
request is granted. 

(cid:1)  Mutex locks– The hardware solutions presented 
are  after  difficult  for  ordinary  programmers  to 
access, particularly on multi-processor machines, 
and particularly because they are often platform, 
dependent.  Therefore  most  systems  after  a 
software  API equivalent called  mutex  locks (the 
term mutex is short for mutual exclusion).  
We use the mutex lock to protect critical regions 
and  thus  prevent  race  conditions.  That  is,  a 
process  must  acquire  the  lock  before  entering  a 
critical  section,  it  releases  the  lock  and  the 
release() function releases the lock. 

  do { 

acquire lock 

critical section 

release lock 

remainder section 

} while (true); 

is 

the 

A  mutex  lock  has  a  Boolean  variable  available 
whose  value  indicates  if  the  lock  is  available  or 
not.  It  the  lock  is  available,  a  call  to  acquire() 
succeeds,  and 
then  considered 
lock 
unavailable.  A  process  that  attempts  to  acquire 
an  unavailable  lock  is  blocked  until  the  lock  is 
released.  Calls  to  either  acquire()  or  release() 
must  be  performed  atomically.  Thus,  mutex 
locks  are  often  implemented  using  one  of  the 
hardware mechanisms described.  

Operating System  

91 

YCT 

 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
  
 
  
 
 
Acquire: 

acquire() { 

Release: 

release() { 

Producer: 
  do{ 

while(!available) 

;  /*busy wait*/ 
available = false;; 
} 

available = true; 
} 

(cid:1) 

Semaphores– A semaphore is simply an integer 

variable  that  is  shared  between  threads.  This 

variable  is  used  to  solve  the  critical  section 

problem  and  to  achieve  process  synchronization 

in the multiprocessing environment.  

A  semaphore  S  is  an  integer  variable  that,  apart 

from initialization, is accessed only through two 

standard  atomic  operations:  wait()  and  signal(). 

The  wait()  operation  was  originally  termed  P; 

signal()  was 

originally 

called  V.  All 

modifications 

to 

the 

integer  value  of 

the 

semaphore  in  the  wait()  and  signal()  operations 

must be executed indivisibly. 

Wait: 

  wait(S){ 

Signal: 

signal(S) { 

while (S < = 0) 

;   //busy wait 

S++; 

} 

S--; 

} 

....... 
/*produce an item in next-produced*/ 
..... 

  wait(empty); 
  wait(mutex); 
...... 

/*add next-produced to the buffer*/ 

...... 

signal(mutex); 
signal(full); 
  }while(true); 

Consumer: 
  do{ 

  wait(full); 
  wait(mutex); 

...... 
/*remove an item buffer to next-consumed*/ 
...... 

signal(mutex); 
signal(empty); 

...... 

/*consume the item in next-consumed*/ 

...... 
}while(true); 

We  can  interpret  this  code  as  the  producers 

(cid:1) 

The  Bounded-Buffer  Problem–  This 

is  a 

producing full buffers for the consumer or as the 

generalization of the producer-consumer problem 

consumer  producing  empty  buffers  for 

the 

wherein access is controlled to a shared group of 

producer. 

buffers  of  a  limited  size.  In  this  problem,,  the 

producer  and  consumer  processes  share  the 

following data structures: 

int n; 

semaphore mutex = 1; 

semaphore empty = n; 

semaphore full = 0; 

We  assume  that  the  pool  consists  of  n  buffers, 

each  capable  of  holding  one  item.  The  mutex 

semaphore  provides  mutual  exclusion 

for 

accesses  to  the  buffer  pool  and  is  initialized  to 

the value1. The empty and full semaphores count 

the  number  of  empty  and  full  buffers.  The 

semaphore empty is initialized to the value n; the 

semaphore full is initialized to the value 0. 

Deadlocks 

  Deadlock  is  a  situation  where  a  set  of  processes 
are  blocked  because  each  process  is  holding  a 
resource  and  waiting 
resource 
acquired by some other process. 
(cid:1)    Necessary Conditions of Deadlock- 

for  another 

1.  Mutual exclusion- At least one resource must 
be  held  in  a  non-sharable  mode,  that  is,  only 
one  process at a time can use the resource. If 
another  process  requests  that  resource,  the 
requesting  process  must  be  delayed  until  the 
resource has been released. 

2.  Hold and Wait- A process must be holding at 
least  one  resource  and  waiting  to  acquire 
additional  resources  that  are  currently  being 
held by other processes. 

Operating System  

92 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.  No  preemption-  Resources 

cannot  be 

As a result, the assignment edge is deleted. 

preempted;  that  is,  a  resource  can  be  released 

only voluntarily by the process holding it, after 

that process has completed its task. 

4.  Circular wait- A set {P0, P1, ... Pn} of waiting 
processes must exist such that P0 is waiting for 
a  resource  held  by  P1.  P1  is  waiting  for  a 
resource  held  by  P2,  ...  Pn-1  is  waiting  for  a 
resource  held  by  Pn  and  Pn  is  waiting  for  a 
resource held by P0. 

(cid:1)  Resource-Allocation Graph (RAG)– Deadlocks 
can  be  described  more  precisely  in  terms  of  a 

directed graph called a system resource-allocation 

graph.  This  graph  consists  of  a  set  of  vertices  V 

and  a  set  of  edges  E.  The  set  of  vertices  V  is 

partitioned into two different types of nodes: P = 

{P1, P2, ....Pn}, the set consisting of all the active 
processes in the system and  R = { R1, R2 ......Rm 
},  the  set  consisting  of  all  resource  types  in  the 

system. 

(cid:1)  Request Edges– A set of directed edge from Pi to 
Rj,  indicating  that  process  Pi  has  requested  Rj(Pi 

→Rj) and is currently waiting for that resource to 
become available. 

(cid:1)  Assignment Edges– A set of directed edge from 
Rj  to  Pi  indicating  that  resources  Rj  has  been 
allocated  to  process  Pi(Rj  →Pi)  and  that  Pi  is 
currently holding resource Rj. 

When  process  Pi  requests  an  instance  of  resource 

type  Rj,  a  request  edge  is  inserted  in  the  resource-

allocation graph. When this request can be fulfilled, 

the  request  edge  is  instantaneously  transformed  to 

an  assignment  edge.  When  the  process  no  longer 

needs access to the resource, it releases the resource. 

(cid:1)  Banker's  Algorithm–  The  resource-allocation-
graph  algorithm  is  not  application  to  a  resource-
allocation  system  with  multiple  instances  of  each 
resource  type.  The  deadlock-avoidance  algorithm 
that we describe next is applicable to such a system 
but  is  less  efficient  than  the  resource-allocation 
graph  scheme.  This  algorithm  is  commonly  known 
as the banker's algorithm. 

  We  need  the  following  data  structures,  where  n  is 
the number of processes in the system and m is the 
number of resource types: 

•   Available–  A  vector  of  length  m  indicates  the 
number  of  available  resources  of  each  type.  If 
available[j]  equals  k,  then  k  instances  of  resource 
type Rj are available. 

•   Max–  An  n  ×  m  matrix  defines  the  maximum 
demand of each process. If Max[i][j] equals k, then 
process  Pi  may  request  at  most  k  instances  of 
resource type Rj. 

•   Allocation-  An  n×m  matrix  defines  the  number  of 
resources  of  each  type  currently  allocated  to  each 
process. If allocation [i][j] equals k, then process Pi is 
currently allocated k instances of resource type Rj.   
•   Need–  An  n×m  matrix  indicates  the  remaining 
resource  need  of  each  process.  If  need  [i][j]  equals 
k,  then  process  Pi  may  need  k  more  instances  of 
resource type Rj to complete its task. 
  Need[i][j] = Max [i][j] – Allocation [i][j] 
  We  can  treat  each  row  in  the  matrices  Allocation 
and Need as vectors and refer to them as Allocationi 
and  Needi.  The  vector  Allocationi  specifics  the 
resources  currently  allocated  to  process  Pi;  the 
vector  Needi  specifies  the  additional  resources  that 
process Pi may still request to complete its task. 

Operating System  

93 

YCT 

 
 
 
 
 
 
 
 
(cid:1)  Banker's algorithm consists of safety algorithm and 

resource request algorithm. 

Safety  Algorithm–  The  algorithm  for  finding  out 
whether  or  not  a  system  is  in  a  safe  state.  This 
algorithm can be described as follows: 

1. Let work and finish be vectors of length m and n, 
respectively.  Initialize  work  =  Available  and 
Finish [i] = false for i = 0,1, ...., n – 1. 

2. Find an index i such that both 

  a. Finish [i] = = false 

  b. Needi ≤ work 
  If no such i exists, go to step 4. 

3.   Work = Work + Allocation; 

  Finish [i] = true 

  Go to step 2. 

4. If Finish [i] = = true for all i, then the system is in 

a safe state. 

This  algorithm  may  require  an  order  of  m×n2 
operations to determine whether a state is safe. 
(cid:1)  Resource-Request  Algorithm–  We  describe  the 
algorithm  for  determining  whether  requests  can  be 
safely granted. 
Let  requesti  be  the  request  vector  for  process  Pi.  If 
Requesti [j] = = k, then process Pi wants k instances 
of resource type Rj. When a request for resources is 
made by process Pi, 
1. 

If  Requesti  ≤  Needi,  go  to  step  2,  otherwise, 
raise  an  error  condition,  since  the  process  has 
exceeded its maximum claim. 

2. 

If  Requesti  ≤  Available,  go 
to  step  3. 
Otherwise, Pi must wait, since the resources are 
not available. 

3.   Have  the  system  pretend  to  have  allocated  the 
requested resources to process Pi by modifying 
the state as follows: 
Available = Available – Requesti ; 
Allocationi = Allocationi + Requesti ; 
Needi = Needi – Requesti ; 

If the resulting resource-allocation state is safe, the 
transaction is completed, and process Pi is allocated 
its  resources.  However,  if  the  new  state  is  unsafe, 
then Pi must wait for Requesti and the old resource-
allocated state is restored. 

(cid:1)  Recovery  from  Deadlock–  When  a  detection 
algorithm determines that a deadlock exists, several 
alternatives  are  available.  One  possibility  is  to 

inform  the  operator  that  a  deadlock  has  occurred 
and  to  let  the  operator  deal  with  the  deadlock 
manually.  Another  possibility  is  to  let  the  system 
recover from the deadlock automatically. There are 
two options for breaking a deadlock. One is simply 
to abort one or more processes to break the circular 
wait.  The  other  is  to  preempt  some  resources  from 
one or more of the deadlocked processes. 
(i)  Process  Termination–  To  eliminate  deadlocks 
by aborting a process, we  use one of two  methods. 
In  both  methods,  the  system  reclaims  all  resources 
allocated to the terminated processes. 

•  Abort all deadlocked processes. 

resources  preemption,  we 

•  Abort  one  process  at  a  time  until  the  deadlock 
cycle is eliminated. 
(ii)  Resource  Preemption–  To  eliminate  deadlock 
using 
successively 
preempt  some  resources  from  processes  and  give 
these resources to other processes until the deadlock 
cycle is broken. 
If  preemption  is  required  to  deal  with  deadlocks, 
then three issues need to be addressed: 
1. Selecting a victim 
2. Rollback 
3. Starvation 

Memory-Management Strategies 
(cid:2)   Swapping– Swapping is a process of removing the 
currently  running  program  from  memory  (called 
swap out) and bringing in another program in to the 
memory  (called  swap  in).  Swapping  makes  it 
possible  for  the  total  physical  address  space  of  all 
processes to exceed the real physical memory of the 
of 
system, 
multiprogramming in a system. 

increasing 

degree 

thus 

the 

  A  program  can  be  swapped  out  under  following 

conditions– 
(i)   If its time quantum has expired. 
(ii)  If higher priority process has arrived. 
(iii)  If using preemptive SJF scheduling algorithm 
(iv)  If a program has completed its execution. 

  Note–A  process  with  pending  I/O  should  never  be 

swapped out.  
Swapping  requires  backing  store  which  could  be 
fast  disk.  It  should  be  large  enough  to  accomodate 
copies  of  all  memory  images  for  all  users.  The 
context-switch  time  in  such  a  swapping  system  is 
fairly high. 

Operating System  

94 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  Memory Allocation– One of the simplest methods 
for  allocating  contiguous  memory  is  to  divide  all 
available memory into equal sized partitions, and to 
assign  each  process  to  their  own  partition.  This 
restricts both the number of simultaneous processes 
and  the  maximum  size  of  each  process  and  is  no 
longer used. An alternate approach is to keep a list 
of unused (free) memory blocks (holes) and to find 
a hole of a suitable size whenever a process needs to 
be  loaded  into  memory.  There  are  many  different 
strategies for finding the 'best' allocation of memory 
to  processes,  including  the  three  most  commonly 
discussed: 

1.   First  fit:  Allocate  the  first  hole  that  is  big 
enough.  Searching  can  start  either  at  the 
beginning of the  set of  holes  or at the location 
where  the  previous  first-fit  search  ended.  We 
can  stop  searching  as  soon  as  we  find  a  free 
holes that is large enough. 

2.   Best  fit–  Allocate  the  smallest  hole  that  is  big 
enough.  We  must  search  the  entire  list,  unless 
the  list  is  ordered  by  size.  This  strategy 
produces the smallest leftover hole. 

3.   Worst fit– Allocate the largest hole. Again, we 
must search the entire list, unless it is sorted by 
size. This strategy produces the largest leftover 
hole,  which  may  be  more  useful  than  the 
smaller leftover hole from a best-fit approach. 

Simulations  have  shown  that  both  first  fit  and  best 
fit  are  better  than  worst  fit  in  terms  of  decreasing 
time and storage utilization. Neither first fit nor best 
fit is clearly better than the other in terms of storage 
utilization, but first fit is generally faster. 

(cid:1)  Fragmentation–  Fragmentation  is  an  unwanted 
problem  in  the  operating  system  in  which  the 
processes  are  loaded  and  unloaded  from  memory 
and  free  memory  space  is  fragmented.  Processes 
can't  be  assigned  to  memory  blocks  due  to  their 
small size, and the memory blocks stay unused. It is 
also  necessary  to  understand  that  as  programs  are 
loaded and deleted from memory, they generate free 
space or a hole in the memory. These small blocks 
cannot  be  allotted  to  new  arriving  processes, 
resulting in inefficient memory use. 

(cid:1)  Segmentation– A process is divided in to segments. 
The chunks that a program is divided into which are 

not  necessarily  all  of  the  same  sized  are  called 
segments. Segmentation gives the user's view of the 
process which paging does not give. Here the user's 
view is mapped to physical memory. 

Important Points– 

•  

In  the  segmentation,  Logical  Address  space 
will be divided in to various segments. 

•   To  achieve  user's  view  of  memory  allocation, 

the segmentation will be implemented. 

•   The  paging  does  not  follow  user's  view  of 

memory allocation. 

•   Segments of Logical Address space will vary in 

the size. 

s  =  Number  of  bits  required  to  represent  segments 
of logical address space. 

OR 
segment number 

d  =  Number  of  bits  required  to  represent  segment 
size. 

OR 
segment offset 

• Number of entries in the segment table is same as 
number of segments in the logical address space. 

•  The  variable  size  segments  are  brought  from 
logical address space to physical address space so it 
is similarly behaving like variable partition scheme. 
Hence, the segmentation still suffers from 'External 
fragmentation'. 

(cid:1)  Paging– The basic method for implementing paging 
involves breaking physical memory into fixed sized 
blocks  called  frames  and  breaking  logical  memory 
into  blocks  of  the  same  size  called  pages.  When  a 
process is to be executed, its  pages are loaded into 
any available memory frames from their source (file 
system  or  the  backing  store).  The  backing  store  is 
divided  into  fixed-sized  blocks  that  are  the  same 
size  as  the  memory  frames  or  clusters  of  multiple 
frames. 

Operating System  

95 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  To  avoid,  the  overhead  of  bringing  large  size 
segment into memory, the segmented paging will be 
implemented. 

(cid:1)  In the segment paging, paging will be applied on the 

segment. 

(cid:1)  Instead  of  bringing,  the  entire  segments  into  the 
memory,  pages  of  segment  will  be  brought  into 
memory. 

(cid:1)  Number  of  entries  in  page  table  of  segment  = 

Number of pages on segment. 

(cid:1)  Page size of segment is same as frame size of PAS 

(Physical address space). 

(cid:1)  Virtual-Memory  Management–  Virtual  memory 
gives  an  illusion  to  the  programmers  that  the 
programs of larger size than actual physical memory 
can be executed. 

Virtual  memory 

is 

implemented  by  using 

Demand paging. 

(cid:1)  Demand Paging– The process of loading the page 
into  memory  on  demand  (Whenever  page  fault 
occurs) is known as demand paging. 

Step  3.  Operating  system  will  search  for  the 
required page in the logical address space. 
Step  4.  The  required  page  is  brought  from  logical 
address  space  (LAS)  to  physical  address  space 
(PAS).  But  the  problem  in  the  PAS,  all  the  frames 
are  occupied  by  some  other  pages,  so  we  need  to 
replace  the  page,  so  for  that  reason  we  need  page 
replacement algorithm. 
Step 5. So after replacement, the page table will be 
updated accordingly. 
Step  6.  The  signal  will  be  sent  to  the  CPU  to 
continue the program execution and it will place the 
process back into the ready state. 

(cid:1)  The CPU will access the required page in the main 
memory and continue the program execution. 
(cid:1)  The  page  fault  service  time  include  the  time  to 

perform all the above six steps.  

(cid:1)  Page fault service time = s  
  main memory access time = m 

page fault rate = p 
then  the  formula  for  EMAT(Effective  Memory 
Access Time) 

EMAT = p(s) + m 

EMAT = p*(s) + (1 – p)*m 

"s>>m"   

Page Replacement Algorithms 

(i) FIFO Page Replacement– In this algorithm, the 
operating  system  keeps  track  of  all  pages  in  the 
memory in a queue, the oldest page is in the front of 
the queue, when a page needs to be replaced page in 
the front of the queue is selected for removal. 
Reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 
2, 0, 1, 7, 0, 1 
(Reference  means  page  number  referred  by  the 
process in the logical address) 
The number of frames allocated to the process will 
be decided by instruction set architecture. 

  Assume, Number of Frame = 4 

(cid:1)  Virtual  memory  concept  is  implement  in  order  to 

increase the degree of multiprogramming.  
Step 1. The CPU is trying to refer some page in the 
memory  but  the  page  is  currently  not  available  in 
the main memory (that is called page fault). 
Step 2. The program execution  will be  stopped, so 
the  signal  will  sent 
the  operating  system 
to 
regarding the page fault. 

Operating System  

96 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  Belady's  Anomaly–  By  increasing  number  of 

  Reference string: 

frames  to  the  process,  the  number  of  page  faults 

should  decrease  but  instead  they  are  increasing 

case  of  FIFO,  this  problem  is  called  as  Belady's 

anomaly. 

(ii) Optimal Page Replacement– In the event of 

page fault, the page is replaced which is not used 

  Reference string: 

for longest duration of time in future. Use of this 

page replacement algorithm guarantees the lowest 

possible  page  fault  rate  for  a  fixed  number  of 

frames.  

Reference string: 

(cid:1)  Thrashing– Thrashing is a condition or a situation 
when the  system is spending  a  major portion of its 
time  serving 
the  actual 
processing done is very negligible. 

the  page  faults,  but 

  Note– If we confused about which one used (if they 

are not given in future reference string), then follow 

the FIFO order. 

  Reference string: 

the 

degree 

further 

If  we 
of 
increase 
multiprogramming,  then  the  CPU  utilization  will 
drastically  fall  down  and  the  system  will  spend 
more  time  only  in  the  page  replacement  and  the 
time taken to complete the execution of the process 
will increased. This situation in the system is called 
as Thrashing. 

(iii) LRU Page Replacement– In the event of page 

fault, replace the page which is least recently used. 

This  approach  is  the  Least  Recently  Used  (LRU) 

algorithm. 

  Cause of Thrashing– 

1. High degree of multiprogramming 
2. Lack of frames 

  Recovery of Thrashing– 

1. Do not allow the system to go into thrashing and 
instruct  long  term  scheduler,  not  to  bring  the 
process in to the main memory after the point of 'λ'. 
2. If  the  system  is  already  present  in  the  thrashing 
then  instruct  the  Midterm  scheduler  to  suspend 
some  of  the  processes  so  that  we  can  recover  the 
system from Thrashing. 

Operating System  

97 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
File System 
  A  file  is  a  named  collection  of  related  information 
that  is  recorded  on  secondary  storage.  A  file  is  the 
smallest allotment of logical secondary storage; that 
is,  data  cannot  be  written  to  secondary  storage 
unless  they  are  within  a  file.  Commonly,  files 
represent  programs  and  data.  Data  files  may  be 
numeric,  alphabetic,  alphanumeric,  or  binary.  Files 
may  be  free  form,  such  as  text  files,  or  maybe 
formatted rigidly. 

(cid:1)  File  Attributes–  A  files  attributes  vary  from  one 
operating system to another but typically consist of 
these: 
• Name 
• Identifier 
• Type  
• Location  
• Size  
• Protection 
• Time, date and user identification 

  All the attributes of the file is called as file context. 

File context will be saved in the FCB (File Control 
Block). 

(cid:1)  File Operations– A file is an abstract data type. In 

the file is having various operations: 
• Creating a file 
• Reading a file 

• Truncating a file 
• Repositioning within a file 
• Appeding a file  
• Rename 
• Print 
• Paste 
• Send 
File Types– 

(cid:1) 
File type 

Executable 

Usual 
Extension 
exe, 
bin 

com, 

Object 

obj, O 

Source code 

C, CC, java, 
perl, asm 

batch 

bat, sh 

• Writing a file 
• Opening a file 
• Modify 
• Deleting a file 
• Save 
• Redo 
• Copy 
• Cut 
• Undo 

Function 

ready-to-run 
machine language 
program 

complied,  machine 
language, 
not 
linked 

source 
various language 

code 

in 

commands  to  the 
command 
interpreter 

Markup 

Word 
processor 

Library 

Print or view 

xml,  html, 
tex 

textual 
documents 

data, 

xml, 
docx 

rtf, 

various 
word-
processor formats 

lib,  a,  so, 
dill 

libraries 
routines 
for 
programmers 

of 
for 

gif, pdf, jpg  ASCII  or  binary 
file  in  a  format  for 
printing or viewing 

Archive 

rar, zip, tar 

related 
files 
grouped  into  one 
sometimes 
file, 
for 
compressed, 
archiving 
or 
storage 

Multimedia 

mpeg,  mov, 
mp3,  mp4, 
avi 

binary 
file 
containing audio or 
A/v information 

(cid:1)  Access Methods– 

• Sequential Access (Record by Record) 
• Direct Access (Jump to particular Record) 

(cid:1)  Directory Structure– The directory can be viewed 
as a symbol table that translates file names into their 
directory entries. If we take such a view, we see that 
the directory itself can be organized in many ways. 
The organization must allows us to insert entries, to 
delete entries, to search for a named entry and to list 
all the entries in the directory. 
1.  Single  Level  Directory–  The  simplest  directory 
structure  is  the  single  level  directory.  All  files  are 
contained  in  the  same  directory,  which  is  easy  to 
support  and  understand.  The  two  files  cannot  have 
the same name. 

2. Two Level Directory– In the two level directory 
structure, each user has his own User File Directory 
(UFD). The UFDs have similar structures, but each 
lists only the files of a single user. When a user job 
starts  or  a  user  logs  in,  the  system's  Master  File 
Directory (MFD) is searched. The MFD is indexed 
by  user  name  or  a  count  number  and  each  each 
entry points to the UFD for that user. 

Operating System  

98 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
                                                                                                                            
 
 
 
 
 
 
3.  Tree  structured  Directories–  The  natural 

generalization is to extend the directory structure to 

a tree of arbitrary height. This generalization allows 

users  to  create  their  own  subdirectories  and  to 

organize  their  files  accordingly.  A  tree  is  the  most 

common  directory  structure.  The  tree  has  a  root 

directory and every file in the system has a  unique 

path name. 

4. Acyclic Graph Directories– An acyclic graph a 

graph  with  no  cycles,  allows  directories  to  share 

subdirectories  and 

files.  The 

same 

file  or 

subdirectory  may  be  in  two  different  directories. 

The acyclic  graph is a natural generalization of the 

tree-structured directory scheme. 

(cid:1) 

Disk Space Allocation Methods– 

1. Contiguous Allocation- 

File 

abc.doc 
xyz.doc 

Directory 
Starting Disk Block 
Address (DBA) 

2 
9 

Size 

4 
5 

•  

In  the  contiguous  allocation,  whenever  the  file 
is  created  then  disk  block  will  be  allocated  in 
the contiguous manner. 

•  

•   Every file will be associated with starting DBA 
and size of file with respect to Disk Block. 
If we want to increase file 'xyz.doc' then block 
14 (Next Block) is should be free, but it is not 
true  always,  so  that  increasing  the  file  size  is 
not possible always. 

•   Even  Though,  it  is  suffering  from  external 

fragmentation. 

•   Last  block  of  file  may  not  be  full  always,  so, 
that the internal fragmentation may exist in the 
last disk block of the file. 
It  supports  both  sequential  and  random  access 
of the file. 

•  

Linked 

Allocation 

Random Access : Random Access Possible by 
'Random Access = Starting DBA + Offset'  
2. 
(Non-Contiguous 
Allocation)–  Linked  allocation  solves  all  problems 
of  contiguous  with  linked  allocation,  each  file  is  a 
linked  list  of  disk  blocks,  the  disk  blocks  may  be 
scattered  anywhere  on  the  disk.  The  directory 
contains a pointer to the first and last blocks of the 
file. Each block contains a pointer to the next block. 

File 

abc.doc 
xyz.doc 

Starting 

(DBA) 

2 
9 

Directory 

Ending (DBA) 

1 
10 

Operating System  

99 

YCT 

 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
addresses  of  the  file,  so  it  is  pointing  to  another 
block so it is behaving like indexed allocation. 
•  If the file is very-very small, it is  waste of using 
entire  one  disk  block  just  to  store  the  disk  block 
addresses. 

•  To avoid these problem, we go for unix-i node. 
4. UNIX I-Node Implementation– An extension of 
indexed allocation  

Increasing the file size is always possible if the 

•  In  the  linked  allocation,  whenever  the  file  is 
created,  the  disk  space  will  be  allocated  in  a  non-
contiguous manner. 
•  
free disk block is available. 
•   There is no external fragmentation. 
• In the last block, it may be full or may not be. The 
internal  fragmentation  may  exist  in  the  last  disk 
block of the file. 
• There is a overhead of maintaining the pointers in 
every block. 
•  If  the  pointer  of  any  disk  lost,  the  file  will  be 
truncate. 
•  
It supports only sequential access of the file. 
•   So  to  avoid  overhead  of  maintaining  the 
pointer, we go for indexed allocation. 
3. Indexed Allocation–  

Directory 

Index node 

4 

File 

abc.do
c 

•  In index allocation, every file is associated with a 

its own index node. 

•  The  index  node  contains  all  the  disk  block 

address of the file. 

•  If  the  file  is  very-very  large  then  one  disk  block 
may  not  be  sufficient  to  store  all  the  disk  block 

•  UNIX follows I-Node  way of allocation in order 

to allocate the disk space to the file. 

•  Every file is associated with its own I-Node. 
•  All are disk block only, some contain disk block 

and some contain addresses of disk block. 

•  Single  indirect  means  one  level  contain  address 

and next level contains data block. 

•  Double indirect means two level address and then 

next level data block. 

•    Whenever the file is created, then depending on 
the  size  of  the  file,  it  will  be  stored  in  only  one 
place  either  direct  DBA  or  single  indirect  or 
double indirect and so on. 

•  Depending  on  the  size  of  the  file,  file  will  be 
stored only in one particular place, may be in the 
direct  DBA's  or  may  be  in  the  single  indirect  or 
double indirect and so on. 

•  Reference  count  =  Reference  count  contains  the 

total number of link to DB'S. 

DBsize
DBA

=

Number of Disk Block Address 's

one disk block can contain

(cid:1)  Disk Free-Space Management– 

1. Bit Vector– The free-space list is implemented as 
a bit map or bit vector. Each block is represented by 
1 bit. If the block is free, the bit is 1; if the block is 
allocated, the bit is 0. 

Operating System  

100 

YCT 

  
 
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
The  main  advantage  of  this  approach  is  its  relative 
simplicity and its efficiency in finding the first free 
block or n consecutive free blocks on the disk. One 
technique for finding the first free block on a system 
that  uses  a  bit-vector  to  allocate  disk  space  is  to 
sequentially check each  word in the bit  map to see 
whether  that  value  is  not  0,  since  a  0-valued  word 
contains only 0 bits and represents a set of allocated 
blocks. The first non-0 word is scanned for the first 
1  bit,  which  is  the  location  of  the  first  free  block. 
The calculation of the block number is– 

number of bits
per word





×

(





−
number of 0 value words

)

+

off set of first1bit.

2.  Linked  List–  In  this  approach,  the  free  disk 
blocks are linked together i.e. a free block contains 
a pointer to the  next  free block. The block  number 
of  the  very  first  disk  block  is  stored  at  a  separate 
location on disk and is also Cached in memory. 

In  above  figure,  the  free  space  list  head  points  to 
Block 4 which points to Block 5, the next free block 
and so on. The last free block would contain a null 
pointer  indicating  the  end  of  free  list.  A  drawback 
of this method is the I/O required for free space list 
traversal. 
3.  Grouping–  This  approach  stores  the  address  of 
the free blocks in the first free block. The first free 
block stores the address of some, say n free blocks. 
Out  of  these  n  blocks,  the  first  n-1  blocks  are 
actually free and the last block contains the address 
of next free n blocks. 
4.  Counting–  This  approach  stores  the  address  of 
the  first  free  disk  block  and  a  number  n  of  free 
contiguous disk blocks that follow the first block. 
Every entry in the list would contain– 
(i) Address of first disk block 
(ii) A number n 

DISK Structure 
  Modern magnetic disk drives are addressed as large 
one-dimensional arrays of logical blocks, where the 
logical  block  is  the  smallest  unit  of  transfer.  The 
size of a logical block is usually 512 bytes, although 
some  disks  can  be  low-level  formatted  to  have  a 
different  logical  blocks  size,  such  as  1024  bytes. 

The  one-dimensional  array  of  logical  blocks  is  
mapped  on  to  the  sectors  of  the  disk  sequentially. 
Sector  0(zero)  is  the  first  of    the  first  track  on  the 
outermost cylinder. The mapping proceeds in order  
through  that  tracks,  then  through  the  rest  of  the 
tracks  in  that  cylinder  and  then  through  the  rest  of 
the cylinders from outer most to inner most. 

• Seek Time– Seek time is the time taken to locate 
the disk arm to a specified track where the data is to 
be read or write. 
•  Rotational  Latency–  Rotational  latency  is  the 
time  taken  by  the  desired  sector  of  disk  to  rotate 
into  a  position  so  that  it  can  access  the  read/write 
heads. 
•  Transfer  Time–  Transfer  time  is  the  time  to 
transfer the data. It depends on the rotating speed of 
the disk and number of bytes to be transferred. 
• Disk Access Time–  

  Disk  Access  Time  =  Seek  Time  +  Rotational 

Latency + Transfer Time. 

DISK Scheduling Algorithms 

The  goal  of  disk  scheduling  algorithms  is  to 
minimize the average seek time of the disk. 
1.  FCFS  Scheduling–  A  disk  queue  with  requests 
for I/O to blocks on cylinders .... 

98, 183, 37, 122, 14, 124, 65, 67 

Total  track  movement  made  by  read/write  header 
(seek time) = (98 – 53) + (183 – 98) + (183 – 37) + 
(122 – 37) + (122 – 14) + (124 – 14) + (124 – 65) + 
(67 – 65)  
= 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 
= 640 

Operating System  

101 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2.  SSTF  (Shortest  Seek  Time  First)  Scheduling– 
The  SSTF  algorithm  selects  the  request  with  the 
least  (minimum)  seek  time  from  the  current  head 
position. 
queue = 98, 183, 37, 122, 14, 124, 65, 67   

the  other  end,  however, 

the  other,  servicing  requests  along  the  way.  When 
it 
the  head  reaches 
immediately  returns  to  the  beginning  of  the  disk 
without  servicing  any  requests  on  the  return  trip. 
The  C-SCAN  scheduling  algorithm  essentially 
treats  the  cylinders  as  a  circular  list  that  wraps 
around from the final cylinder to the first one. 
queue = 98, 183, 37, 122, 14, 124, 65, 67 

Seek time = (65 – 53) + (67 – 65) + (67 – 37) + (37 
– 14) + (98 – 14) + (122 – 98) + (124 – 122) + (183 
– 124) 
= 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 
= 236 
3.  SCAN  Scheduling–  In  the  scan  algorithm,  the 
disk  arm  starts  at  one  end  of  the  disk  and  moves 
toward  the  other  end,  servicing  requests  as  it 
reaches each cylinder, until it gets to the other end 
of  the  disk.  At  the  other  end,  the  direction  of  head 
movement is reversed and servicing continues. The 
head  continuously  scans  back  and  forth  across  the 
disk. The SCAN algorithm is sometimes called the 
elevator algorithm. 
queue = 98, 183, 37, 122, 14, 124, 65, 67 

Seek  time  =  (65  –  53)  +  (67  –  65)  +  (98  –  67)  + 
(122  –  98)  +  (124  –  122)  +  (183  –  124)  +  (199  – 
183) + (199 – 0) + (14 – 0) + (37 – 14) 
= 12 + 2 + 31 + 24 + 2 + 59 + 16 + 199 + 14 + 23 
= 382 
5. LOOK Scheduling– In this algorithm, it will go 
till only the last request (not 199) and come back to 
satisfy the remaining request. 
queue = 98, 183, 37, 122, 14, 124, 65, 67 

  Right– It  will  first satisfy all the right-side request 
and  go  till  the  end  and  come  back  to  satisfy  the 
remaining left. 
Left– First satisfy all left side and go till the '0' and 
satisfy the remaining. 
Seek  time  =  (65  –  53)  +  (67  –  65)  +  (98  –  67)  + 
(122  –  98)  +  (124  –  122)  +  (183  –  124)  +  (199  – 
183) + (199 – 37) + (37 – 14) 
= 12 + 2 + 31 + 24 + 2 + 59 + 16 + 162 + 23 
= 331 
4.  C-SCAN  (Circular  SCAN)  Scheduling–  C-
SCAN moves the head from one end of the disk to 

Seek  time  =  (65  –  53)  +  (67  –  65)  +  (98  –  67)  + 
(122 – 98) + (124 – 122) + (183 – 124) + (183 – 37) 
+ (37 – 14) 
= 12 + 2 + 31 + 24 + 2 + 59 + 146 + 23 
= 299 
6. C-LOOK (Circular LOOK) Scheduling– In C-
LOOK,  it  will  go  in  the  right  direction  and  go  till 
the  last  request  and  directly  jump  to  first  request 
(14)  left  most  and  request  and  then  satisfy  the 
remaining request. 

queue = 98, 183, 37, 122, 14, 124, 65, 67 

Operating System  

102 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
  RAID-2  –  This  configuration  uses  striping  across 
disks,  with  some  disks  storing  error  checking  and 
correcting  (ECC)  information.  RAID  2  also  uses  a 
dedicated  Hamming  code  parity,  a  linear  form  of 
ECC. RAID 2 has no advantage over RAID3 and is 
no longer used. 

  RAID-3  –  This 

technique  uses  striping  and 
dedicates  one  drive  to  storing  parity  information. 
The  embedded  ECC  information  is  used  to  detect 
errors. Data recovery is accomplished by calculating 
the  exclusive  information  recorded  on  the  other 
drives.  Because  an  I/O  operation  addresses  all  the 
drives at the same time. RAID 3 cannot overlap I/O. 
For  this  reason,  RAID  3  is  best  for  single  user 
systems with long record applications. 

  RAID-4  –  This  level  uses  large  stripes,  which 
means  a  user  can  read  records  from  any  signle 
drive.  Overlapped  I/O  can  then  be  used  for  read 
operations. Because all write operations are required 
to  update  the  parity  drive,  no  I/O  overlapping  is 
possible. 

  RAID-5 – This level is based on parity block level 
striping.  The  parity  information  is  striped  across 
each  drive,  enabling  the  array  to  function,  even  if 
one  drive  were  to  fail.  The  array's  architecture 
enables  read  and  write  operations  to  span  multiple 
drives.  This  results  in  performance  better  than  that 
of a single drive, but not as high as a RAID-0 array. 
RAID-5 requires at least three disks, but it is often 
recommended 
least  five  disks  for 
performance reasons. 

to  use  at 

  RAID-6– This technique  is  similar to  RAID-5, but 
it includes a second parity scheme distributed across 
the drives in the array. The use of additional parity 
enables  the  array  to  continue  functioning  even  if 
two  disks  fail  simultaneously.  However,  this  extra 
protection  comes  at  a  cost.  RAID  6  arrays  often 
have slower write performance than RAID 5 arrays. 

Seek time = (65 – 53) + (67 – 65) + (98 – 67) + 
(122 – 98) + (124 – 122) + (183 – 124) + (183 – 
14) + (37 – 14) 
= 12 + 2 + 31 + 24 + 2 + 59 + 169 + 23 
= 332 

RAID  Structure–  RAID  (Redundant  Arrays  of 
Independent  Disks)  is  a  technique  which  makes 
use of a combination of multiple disks instead of 
using  a  single  disk  for  increased  performance, 
data redundancy or both. 

(cid:1) 

(cid:1)  RAID Levels– RAID combines several independent 
and  relatively  small  disks  into  single  storage  of  a 
large size. The disks included in the array are called 
array  members.  The  disks  can  combine  into  the 
array in different  ways,  which are known as RAID 
levels. We describe the various levels here– 

  RAID-0 

(Stripping)–  This  configuration  has 
striping but no redundancy of data. It offers the best 
performances  but 
fault 
tolerance. 

is  does  not  provide 

  RAID-1 

(Mirroring)–  Also  known  as  disk 
mirroring, this configuration consists of at least two 
drives that duplicate the storage of data. There is no 
striping. Read performance is improved, since either 
time.  Write 
disk  can  be  read  at 
performance is the same as for single disk storage. 

the  same 

Operating System  

103 

YCT 

 
 
 
 
  
 
 
 
 
 
 
 
   09. 

COMPUTER NETWORK 

Data Communication 

Data  communication  is  the  exchange  of  data 
between  device  or  human  by  local  or  remote 
using transmission medium. 
Components– There are five mainly components 
of a data communication system. 

Data Flow 

Data  flow  is  the  communication  between  two 
devices.  It  can  be  simplex  half  duplex  and  full 
duplex. 

Simplex–  It  is  an  unidirectional  communication 
or one way start. Key boards traditional monitor 
and radios are example of simplex devices. 

It 

is 

two  or  bidirectional 
Half-duplex– 
communication.  In  half-duplex  each  station  can 
both  transmit  and  receive  but  not  at  same  time. 
Walkie-Takies  is  the  example  of  half  duplex 
system. 

It 

is 

two  or  bidirectional 
Full  duplex– 
communication  in  full  duplex  both  stations  can 
simultaneously.  This 
transmit  and 
separate 
physically 
sharing 
transmission  path  to  avoid  collision  telephone 
line is the example of full duplex.  

receive 
two 

contain 

Networks 

 A  computer  network  is  a  group  of  computers 
that  enables  one 
connected 
computer  to  communicate  with  other  computers 
and share their resources, applications and data. 

to  each  other 

1. Message 
2. Sender 
3. Receiver 
4. Transmission Medium 
5. Set of rules (protocol) 

Message 

Sender 

Receiver 

Transmission 
medium 

Protocol 

It  is  the  information  or  data  to  be 
communicated. Message can be in 
the  form  of  text,  number,  picture, 
audio, video and multimedia etc. 

It  is  the  device  which  capable  of 
sending  data  over  network.  It  can 
be  a  computer,  telephone,  laptop, 
Mobile video camera and so on. 

It is the device (destination) where 
finally  message  send  by  source 
and received by receiver. It can be 
computer  workstation,  telephone, 
television etc. 

It  is  physical  path  by  which  data 
travels  from  sender  to  receiver.  It 
is  act  as  bridge  between  sender 
and receiver.  
Example–  Twisted  pair  cable, 
coaxial cable fiber optic cable and 
radio waves. 

It is a set of rules that govern data, 
data communications. It represents 
an agreement between the devices 
without  protocol  you  can  connect 
but not communicate. 

Computer Network  

104 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Performance 

Network Criteria 

time 

It can be measured in many ways, 
including 
and 
transit 
response time . Transit time is the 
amount  of  time  required  for  a 
message to travel from one device 
to another.  
Response 
between 
response. 
The  nature  of  a  network  depends 
on a number of factors, including 
the type transmission medium, the 
number of user the capabilities of 
the  connected  hardware  and  the 
efficiency of the software. 

the  elapsed 
a 
and 

is 
inquiry 

time 
an 

Reliability 

Security 

Network  reliability  is  measured 
by  the  frequency  of  failure.  The 
time  is  takes  a  link  to  recover 
from a failure. 

Network  security  issues  include 
protecting data from unauthorized 
access,  protecting  data  loss  and 
implementing 
and 
procedures  for  recovery  from  dot 
losses. 

policies 

Physical Structure 

Types  of  connection–  There  are  two  possible 
types of connection. 
(a)  Point-to-point  connection–  This  connection 
provides  a  dedicated  link  between  two  devices. 
For  example  Television  and  remote  control, 
computer connected by telephone line. 

(b)  Multipoint–  In  this  connection  more  than 
two specific devices share a single link. 

Two types of multipoint connection– 
(i)  Spatial  sharing–  In  this  sharing  several 
computer can share the link simultaneously. 
(ii) Time sharing– In this, user must take turn. 

Physical Topology 

 In  physical  topology,  a  network  is  formed  by 
physically  connecting  two  or  more  devices  with 
two or more links. 

Communication using OSI Model 

OSI (Open Source Interconnection) Model  

virtual 

Functions 
•  Networks 
terminal 
• Mail services 
• Directory services 

Protocols 

Central Devices 

SMTP, HTTP, FTP, 
POP3, 
SNMP, 
Telnet. 

– 

Layer 

Application 

Application 
Layer 
(Layer 7) 

for 

These 
application 
produce the data which 
has  to  be  transferred 
over  the  network.  This 
layer  also  serves  as  a 
window 
the 
application  services  to 
access the network and 
for 
the 
displaying 
received information to 
the user. 
Example- 
browsers, 
Skype, Messenger etc. 

Computer Network  

105 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
MPEG,  XDR,  SSL, 
TLS, MIME 

– 

• Translation ASCII to 

EBCDIC 
•  Encryption/ 
  Decryption 
•  Compression 

Net  BIOS,  SAP 
PPTP, 
ADSP, 
RTCP, PAP,RPCP 

Gateway 
Servers  

phone, 

TCP, 
UDP, 
SPX 

Firewall, Gateway  

•  Session 

establishment, 
maintenance 
termination 
•  Synchronization 
•  Dialog controller 
•  Segmentation 
reassembly 

and 

and 

•  Services 

addressing 

•  Message 

point 

acknowledgement 

•  Routing  
•  Logical Addressing 
•  Subnet 
control. 

traffic 

IPv6, 

IPv4, 
IPSEC, MPLS 

ICMP, 

Router  
Brouters 

• Framing  
• Physical addressing 
• Error control  
• Flow control  
• Access control  

PPP,  ARP  Frame, 
Relay,  ATM,  Fiber 
Cable etc.  

Switch  
Bridge 
Access point 

Presentation 
Layer 
(Layer 6) 

Session layer  
(Layer 5) 

Transport 
Layer 
(Layer 4) 

Network Layer 
(Layer 3) 

Data Link 
Layer (Layer 
2) 

layer 

It  is  also  called  the 
Translation  Layer.  the 
the 
data 
from 
is 
application 
extracted 
and 
manipulated  as  per  the 
to 
required 
transmit 
the 
network. 

format 
over 

here 

This layer is responsible 
for  the  establishment  of 
connection  maintenance 
sessions, 
of 
authentication  and  also 
ensures security. 

for 

data 

located 

in 
layer 
to 
It 

the 
The 
is 
transport 
as 
referred 
segments. 
is 
responsible for the end 
to  end  delivery  of  the 
complete message. The 
layer  also 
transport 
the 
provides 
of 
acknowledgement 
the 
successful  data 
transmission  and  re-
transmits the data if an 
error is found. 
It  works 
the 
transmission  of  data 
from  one  host  to  the 
in 
other 
different  networks.  It 
takes  care  of 
also 
packet 
the 
sender  and  receiver's 
IP addresses are placed 
in  the  header  by  the 
network layer 
It is responsible for the 
node-to-node  delivery 
of  the  message.  The 
main  function  of  this 
layer  is  to  make  sure 
data  transfer  is  error 
free  from  one  node  to 
the 
another, 
physical 
it 
collects  the  packets  to 
from frames, which are 
then  transmitted  over 
the network.  

over 
layer, 

routing. 

Computer Network  

106 

YCT 

 
• Bit  synchronization 
• Bit rate control 
• Physical topologies 
• Transmission mode       

RJ-45  100  Base  Tx, 
ISDN. 

Hub,  NIC,  Cable, 
Modem,  wireless  
Repeaters  

Physical Layer 
(Layer 1) 

It 
is  responsible  for 
transmitting  individual 
bits  from  one  node  to 
next.  When 
the 
this 
receiving  data, 
layer will get the signal 
received and convert it 
into 0s and 1s and send 
them  to  the  data  link 
layer.  Which  will  put 
the 
back 
frame 
together 

Basis 

Topology 

Bus 

Star 

Ring 

Tree 

Mesh 

Hybrid 

Architecture  A 

network 
in 
topology 
there 
which 
is  a  single 
line  (the  bus) 
to  which  all 
are 
nodes 
connected 
and  the  node 
connect  only 
to this bus. 

hybrid 
The 
the 
topology 
is 
of 
combination 
multiple 
topologies,  used 
for  constructing  a 
large 
single 
topology. 

network 
in 

A 
topology 
which 
peripheral 
node 
are 
connected  to 
central  node 
(such  as  a 
hub, 
switch 
or router) 

Tree  topology 
is the variation 
star 
of 
topology.  This 
topology has a 
hierarchical 
flow  of  data. 
tree 
In 
topology 
all 
the  computers 
are  connected 
the 
like 
branches 
of 
tree.    

In 
ring 
topology  each 
is 
node 
to 
connected 
other 
two 
devices, 
one 
each  on  either 
side, 
the  
nodes 
connected 
each 
with 
other 
thus 
forms  a  ring 
the  link  in  a 
ring 
topology 
is 
unidirectional. 

In 
this 
networking 
topology, 
each 
communicat
ing  device 
is connected  
with  every 
other  device 
the 
in 
network.  In 
to 
order 
connect 
n 
nodes. 
Mesh 
topology 
require  
n(n-1)/2 
communicat
ion links 

Computer Network  

107 

YCT 

 
 
 
 
 
 
 
 
Advantages 

Disadvantage
s 

•  Usually 
requires 
less 
cabling 
•  The  failure 
one 

of 
computer 
does 
effect 
other 
computers 
in 
the 
network 
•  The  failure 
the 

not 
the 

in 

of 
backbone 
cable 
results 
the 
breakdown 
entire 
of 
network 

Delay/ 
Response 
time 

•  It 

is 
difficult  to 
reconstruct 
in  case  of 
faults 

Slow 
response 
time  because 
of 
one 
computer 
transmit  at  a 
time 

Common 
Cable 

Coaxial 
cable, twisted 
pair, fiber 

•  Message 
delivery 
is  more 
reliable. 
•  Network 
congestio
n 
is 
minimum 
to 
due 
large 
number 
of links. 

•  It  is  very 
expensive 
to 
implemen
t. 

•  It  is  very 
difficult 
to 
configure 
and 
install. 

Manages 
high 
amounts  of 
traffic 
because 
multiple 
devices  can 
transmit 
data 
simultaneou
sly 

All  king  of 
cable 
that 
can  be  used 
with  LAN 
and WAN. 

•  It 

is  more 
effective    as  it 
uses  multiple 
topologies 

• It is contains the 
and 
best 
efficient  feature 
of 
the 
combined 
topology 
which 
constructed.  

form 
is 

it 

•  It  is  relatively 
more  complex 
than  the  other 
topology 

•  It  is  difficult  to 
and 

install 
configure. 

Worst 
time. 

response 

Cabling  depends 
on  the  types  of 
networks,  twisted 
pair, coaxial fiber. 

• 

Supported 
most 

by 
hardware 
and 
software 
•  Date 

is 
receive a by 
all 
the 
nodes 
efficiently 
because  of 
point-to-
point link.  

the 
node 
the 

•  When 
root 
fails, 
whole 
network 
crashes. 
•  It is difficult 

to 
configure. 

• 

• 

Allows 
easy  error 
detection 
and 
correction 
Star 
topology is 
easy 
to 
install. 

•  Each  node 
has an equal 
access 
to 
other  nodes 
in 
the 
network 
•  Addition  of 
node 
new 
not 
does 
degrade  the 
performanc
e 
of 
network 

the 

•  The 

hub 

•  It 

is 

failure 
leads 
to 
the  overall 
network 
crash. 
•  Requires 
more 
amount  of 
cable 
for 
connecting 
the nodes. 

ring 

relatively 
expensive to 
construct 
the 
topology. 
•  The  failure 
of  one  node 
in  the  ring 
topology 
the 
affects 
other  nodes 
in the ring. 

to 
Data  has 
make  a  lot  of 
stops 

Slowly 
because 
more traffic. 

of 

Good 
response 
time, 
depends  on 
lot of stops 

Twisted  pair 
requires  more 
cables 
than 
other 
topologies 

Overall  length 
each 
of 
segment 
is 
limited  by  the 
cabling 
of 
used  (Coaxial. 
Twisted  pair-
Fiber) 

•  Coaxial 
cable 
twisted 
pair fiber 
•  No  more 
100 

the 

than 
meters 
from 
computer 
to 
the 
connection 
device 

Computer Network  

108 

YCT 

Congestion  

One 

Compared 

Information 

A 

A 

few  of 

Often  used  across 

control 

computer at a 

bus  topology 

goes 

in  one 

transmission 

congestion 

long 

distances, 

time 

sends 

it  gives  for 

direction 

from 

any 

direct  from 

information 

information. 

much  better 

around 

the 

station 

source 

to 

transfer 

Information 

performance 

ring 

and 

propagates 

destination 

happen 

on 

can 

in 

goes 

along 

signals  don't 

passes 

along 

throughout  the 

except 

the 

different 

ways, 

the  cable  and 

necessarily 

the ring until it 

medium 

and 

station  with 

depending  on  the 

the  computer 

get 

reaches 

the 

can 

be 

less 

other topologies. 

accesses 

the 

transmitted 

correct 

received by all 

connection 

information 

to 

all 

the 

computer,  no 

other stations. 

off the cable 

work stations 

buffering 

at 

repeater. 

Reliability 

If 

the 

In  hub  fails 

If 

the  cable 

In  case  of  any 

A failure of 

Extremely 

rare 

common 

then 

the 

fails  or  any 

node 

failure, 

one device 

reliability 

cable 

fails, 

whole system 

computer 

other 

does not 

then 

the 

will 

crash 

shuts 

down, 

hierarchical 

cause a break 

whole system 

down. 

then the whole 

network 

are 

in the 

will 

crash 

down. 

system  will 

not affected 

network or 

crash down. 

transmission 

of data. 

Complexity 

Easy 

to 

Average 

Complexity 

Move 

Installation 

the 

most 

connect 

or 

complexity 

because 

of 

complex 

is  complex 

complicated one 

remove 

each  device 

simple  to  data 

because 

of 

in 

mesh 

nodes 

in  a 

connects 

to 

to devices. 

tree 

is 

topology,  as 

network 

without 

central 

device  with 

affecting  any 

only  one  link 

other node. 

only. 

combination  a 

each node is 

star 

network 

connected 

topology and a 

to 

more 

bus topology. 

than 

one 

node.  

Security 

Any 

Security 

data 

travels 

The  data  pass 

The 

data 

The 

worst 

computer 

depends  on 

from 

one 

over 

more 

pass 

over 

security 

that 

is 

central 

device  to  the 

than one node 

more 

than 

connected  to 

device 

next  until  they 

one node 

bus  topology 

security. 

reach 

their 

destination. 

network  will 

be able to see 

all 

the  data 

transmissions 

on 

all 

the 

other 

computers 

Computer Network  

109 

YCT 

is 

and 

TCP/IP Model 
control 
for  Transmission 
stands 
TCP/IP 
Protocol/Internet 
suite 
Protocol 
communication  Protocols  used  to  interconnect 
network  devices  on  the  internet.  TCP/IP  is  also 
used  as  a  communication  Protocol  in  a  private 
computer  network.  The  TCP/IP  model  is  a 
concise version of the OSI model. 
Logical connections between layers of 
the TCP/IP Protocol. 

is          

layer 

1.  Physical  Layer-  This 
the  data  and 
for  generating 
responsible 
requesting  connections.  It  acts  on  behalf  of  the 
sender  and  the  Network    access  layer  on  the 
behalf of the receiver. 
2. Transport Layer- This layer monitors  end to 
end path selection of the packets. It also provides 
service  to  two  application  layer.  Transmission 
control  Protocol  (TCP)  and  User  datagram 
Protocol  (UDP)  are  transport  layer  protocol  at 
this level. 
1. TCP      2. UDP 
3.  Internet  Layer-  This  layer  is  responsible 
for  sending  packets  different  networks. 
The main protocols residing at this layer 
are as follows. 

4. Data link Layer- It is the closest to the network 
hardware. It provides service to Internet layer. 
5. Application Layer- This layer is analogous to 
the  transport  layer  at  the  OSI  model.  It  is 
responsible  for  end  to  end  communication  and 
error free delivery of data. 

TCP/IP model Vs OSI Model 

OSI 

OSI represent open 
system Interconnection 

OSI is a generic 
independent Protocol in 
standard. It is acting as 
an interaction gateway 
the network and the 
final  user. 

The OSI model 
represents defines 
administration, interface 
and connections. It 
describes clearly which 
layer provides services. 

The protocols of the 
OSI model are better 
unseen and can be 
appropriate protocol 
quickly. 

It provides both 
connection and 
connectionless oriented 
transmission in the 
network layer however 
only connection 
oriented transmission in 
the transport layer. 

TCP/IP 
TCP/ IP model represents 
the Transmission Control 
Protocol/ Internet 
Protocol. 

TCP/IP model depends on 
standard protocols about 
which the computer 
network has created. It is 
a connection protocol that 
assigns the network of 
hosts over the internet. 

It does not mention the 
services, interfaces, and 
protocols. 

.The TCP/IP model 
protocols are not hidden, 
and we can't fit a new 
protocol stack in it. 

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

Local Area Network– LAN is usually privately 
owned  and  connects  a  few  hosts  within  a  single 
building , office or campus. 
Each host in a LAN has a identifier, an address, 
that uniquely defines the host in the LAN. 
Packets sent by one host to another host contain 
the  addresses  of  both  the  source  host  and  the 
destination host. 

Computer Network  

110 

YCT 

 
 
 
  
        
 
      
 
   
 
 
 
 
 
 
 
          
 
 
 
 
 
 
 
Most  LANs  use  a  smart  connecting  switches 
which is able to recognize the destination address 
of the packet to all other hosts.  

Metropolitan Area Network 

It  is  larger  than  LAN  but  smaller  than  WAN. 
This  is  the  type  of  computer  network  that 
connects 
  over  a  geographical 
distance  through  a  shared  communication  path 
over a city, town or metropolitan area.  

  computers 

College

Government 
building

MAN

Office

Residential 
Area

Wide Area Network 

WAN  has  a  wide  geographical  extension,  it 
in  different  geographical 
means  spreading 
location. WAN inter connects connecting devices 
such  as  switches,  routers  or  modem.  WAN  is 
normally  built  and  operated  by  communications 
companies  and  leased  by  the  organization  using 
it.  
Example of WAN– 
Point-to-Point  WAN–  This  network  connects 
two 
a 
transmission media. 

communicating 

through 

device 

Switch  WAN–  It  is  a  combination  of  several 
point-to-point  WANs  that  are  connected  by 
switches. 

The Internet 

 Internet  is  two  or  more  networks  that  can 
transmit data with each other. 

Back 
bones 

Backbones  are  large  networks  owned 
by  some  communication  companies 
Verizon, AT & T, sprint etc. 

Peering 
Point 

Network 
Provider 

Customer 
Network 

ISP 

Peering  points  are  complex  switching 
system that connects backbones. 

It  is  a  smaller  networks  that  use  the 
services  of  the  backbones  for  a  free.  It 
connected  to  backbones  and  sometime 
to other provider networks. 

The customer networks are networks at 
the  edge  of  the  internet  that  is  use  the 
internet. 
services  provided  by 
Customer  network  pay  a  fee  to  the 
provider  network 
the 
services. 

receive 

the 

to 

is 

service 

providers 

Internet 
a 
combination of backbones and provider 
networks. 
The  backbones  are  after  referred  to  as 
international ISPs. 
Provider networks are often referred to 
as national or regional ISPs. 

Computer Network  

111 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
1.  

Accessing the Internet 

Accessing Internet 
1. Using Telephone Networks  
2. Using Cable Networks  
3. Using Wireless Networks  
Using Telephone Networks– 
i. Dial up service 
ii. DSL service  
i.  Dial-up  Service–  In  this  connection  the 
services  connect  to  the  internet  through  a  phone 
line  connection.  Dial-up  service  established 
between  two  or  more  communication  devices  in 
it  uses  Public  Switched  Telephone 
which 
Network  (PSTN)  for  connect  to  the  internet.  Its 
data transfer rate is up to 56 kbps. 

ii.  Digital  Subscriber  Line 
(DSL)–  DSL 
technology  is the  most promising  for supporting 
high-speed  digital  communication  over 
the 
existing  telephone.  This  technology  is  a  set  of 
technologies,  each  differing  in  the  first  letter 
(ADSV,  VDSL,  HDSL  and  SDSL).  The  set  is 
often  referred  to  as  xDSL,  where  x  can  be 
replaced by A, V, H, S. ADSL, provides a wider 
frequency range for downstream transfers, which 
offers several time faster downstream speeds. An 
ADSL 
connection  may  offer  20  Mbps 
downstream and 1.5 Mbps upstream. 

2. 

to 

Cable  Networks–  Cable  TV  network  ware 
originally  created  to  provide  access  to  TV 
programs,  but  later  cable  networks  became 
popular  among  people  who  just  wanted  a  better 
signal.  In  addition,  cable  networks  enabled 
access 
stations  via 
remote  broadcast 
microwave connections. 
Now  cable  TV  found  a  good  market  in  internet 
access provision. 
Types of cable TV Networks are as follows– 
1. Traditionally Cable Networks 
2. Hybrid Fiber-Coaxial Network 

1.   Traditionally  Cable  Networks  was  called 
Community  Antenna  Television  (CATV)  in 
1940s. 

2.   Hybrid  Fiber-Coaxial  Network  (HFC)  This 
network  user  a  combination  of  fiber  and 
coaxial cable. 

SONET 
•  Synchronous  Optical  Network 

a 
communication protocol. It is used to transmit a 
large amount of data using optical fiber. 

is 

•  By  SONET,  multiple  digital  data  streams 
transferred  at  the  same  time  over  the  optical 
fiber.  

SONET Network Elements 

STS 
Multiplexer 

•  Its  converts  electrical  signal 

to optical signal. 

•  STS  performs  multiplexing 

STS 
De-
multiplexer 

Regenerator 

Multiplexer 

of signals. 

•  It 

performs 
multiplexing. 

signal 

de-

•  It  converts  optical  signal  to 

electrical signal. 

It  is  a  repeater  that  takes  an 
optical signal and strengthens it. 

This device allows to remove a 
signal  or  add  signals  coming 
into 
from  different  sources 
given path. 

Computer Network  

112 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1) 

SONET  Layers–  SONET 
functional layers 

includes 

four 

Path 
Layer 

•  Path  layer  functionalities  are  provided 

by STS Mux/Demux. 

signal 

(cid:1)  Microwaves–  Microwaves  are  ratio  waves  that 
transmission. 
provide  a  high-speed 
Microwaves  are  a  line  of    sight  transmission. 
Microwaves  have  a  frequency  range  between  
1GHz-300  GHz.  Microwave  unidirectional 
antennas send out signal in one direction. 
(cid:1)  Millimeter wave– Millimeter wave is a band of 
electromagnetic spectrum that can be used proud 
range  of  product  and  services.  It  is  high-speed 
point  to  point  wireless  local  area  networks 
(WLANs)  and  broadband  access  range  30  GHz 
to 300 GHz.  

•  Path 

layer 

is  responsible  for 

the 
movements  of  signals  from  its  optical 
destination. 

(cid:1) 

(cid:1) 

Line 
Layer 

•  The  line  layer  is  in  charge  of  signal 

movement across a physical line. 

•  STS  Mux/Demux  and  Add/Drop  mux 

provides its functions. 

Section 
Layer 

•  It  layer  responsible  for  the  movement 

of signal across a physical section. 

• It layer functions are provided by each 

network device. 

Photonic 
Layer 

•  It  layer  relates  to  the  OSI  models 

physical layer. 

•  This  includes  physical  specifications 

for the optical fiber channel. 

Wireless Transmission Radio 

Wireless  transmission  is  a  format  of  unguided 
media.  Wireless  communication  involves  no 
physical  link  established  between  two  or  more 
devices  communicating  wirelessly.  A  little  part 
of  electromagnetic  spectrum  can  be  used  for 
wireless transmission. 
Radio  Transmission–  Wireless  communication 
is  the  transmission  of  voice  and  data  without 
cable or wire. Radio waves can have wavelength 
from  1mm  to  100,000  km  and  have  frequency 
range  from  3Hz  (Extremely  low  frequency)  to 
300 GHz (extremely high frequency).  
Infrared–  Infrared 
is  used  for  short-range 
communication like TV remotes, Mobile phones, 
Personal  computers  etc.  The  frequency  range  of 
infrared rays 300 GHz to 400 THz. 
Radio  waves–  Radio  waves  can  travel  large 
distances  as  well  as  penetrate  any  wall  (uni-
directional). The requirement of radio waves are 
antennas,  sending  antennas  when  are  transmit 
message other is receiving range 3 KHz-1 GHz. 

(cid:1) 

(cid:1) 

(cid:1) 

Lightwave Transmission 

Light  wave  transmission  is  used  for  wireless 
lasers  communication.  It  is  a  relatively  low  cost 
way  to  connect  two  building  LAN.  Laser  light 
also  diffuses  easily 
in  poor  atmospheric 
condition likes rain, fog and so on.  
Telephone  Local  Loop–  Local  loop  is  the 
portion  of  the  telephone  system  that  connects 
home  or  office.  Local  loop  wiring  is  used 
Unshielded  Twisted  Pair  (UTP)  cabling  to  the 
transmission method distance from the telco is co 
to subscriber's customer premises 5 kilometers. 

Trunks–  Trunks  are  used  to form  networks  and 
to  interconnect  LANs  (Local  Area  Networks)  to 
form  WAN  (Wide  Area  Network)  or  VLAN 
(Virtual LAN). Trunk network is built up locally 
or  through  the  internet.  It  is  a  point  to  point 
connection  between  two  points  on  a  different 
networks.  

Multiplexing 

Multiplexing  is  a  set  of  technique  used  to 
combine and send the multiple data over a single 
medium. Multiplexing is a many to one combine 
a  single  stream.  There  are  a  three  multiplexing 
technique such as– 
Frequency  Division  Multiplexing  (FDM),  Wave 
length  Division  Multiplexing  (WDM),  Time 
Division Multiplexing (TDM). 

Computer Network  

113 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
FDM– FDM is an analog multiplexing technique 
that combines analog signals. 
WDM–WDM 
analog  multiplexing 
technique  to  combine  optical  signals.  WDM  is 
used the high data rate capability of a fiber optic 
cable. 

an 

is 

(cid:1) 

(cid:1) 

(cid:1) 

TDM–  TDM  is  a  digital  process  that  allow  a 
several  connection  to  share  high  bandwidth  of  a 
link. 

ISDN–  Narrowband 

Narrowband 
ISDN 
integrated  services  digital  network  is  called  the 
N-ISDN.  Narrowband  integrated  services  digital 
network  an  attempt  to  digitize  the  analog  voice 
information.  N-ISDN  is  users  64  kbps  circuit 
switching.  
integrated 
ISDN–  Broadband 
Broadband 
services  digital  network  digital  networking 
services  and  provides  digital 
transmission 
telephone wires as well as over other media. The 
broadband  ISDN  speed  is  around  2  MBPS  to  1 
GBPS  and  the  transmission  is  related  to  ATM. 
The  broadband  ISDN  communication  is  usually 
made using the fiber optic cables. 

ATM– A synchronous Transfer Mode (ATM) is 
a  switched  wide  area  network  based  cell  relay 
protocol  designed  by  ATM  forum  and  adopted 
by  (ITU-T).  International  Telecommunication 
Union-Telecommunication  Standard  Section 
(ITU-T)  efficient  for  call  relay  transmits  all 
information such as video or voice. 

(cid:1)  High  Speed  LANs–  The  IEEE  802.3  to  802.6 
LAN  is  data  transfer  rates  in  the  range  of  10 
Mbps  to  16  Mbps  served.  The  high  speed  LAN 
that  is  emerged  broadly  categorized  into  three 
types  on  taken  passing,  successors  of  Ethernet 
and  switching  technology.  High  speed  LANs 
with  data  transfer  rate  of  100  Mbps  to  more. 
There are varieties of Fast Ethernet such as 100- 
Base-Tx, 100-Base-Fx and 100-Base-Tu etc.  

(cid:1) 

radio 

Cellular  Radio–  Cellular  radio  is  a  form  of 
broadcast 
used  widely  mobile 
communication  specifically  wireless  modems 
and  cell  phones.  A  cell  phone  to  access  web, 
send  and  receive  e-mail.  A  cell  phone  is  a 
telephone devices that uses high frequency radio 
waves 
transmit  voice  and  digital  data 
to 
messages.  

Communications Satellite 

A  communication  satellite  is  a  space  station 
receives  microwave  signal  earth  based  station 
amplifies  a  signal.  Transmission  from  an  earth 
is  an  uplink. 
to  a  satellite 
based  station 
Transmission  from  a  satellite  to  an  earth-based 
station 
three 
communication satellite such a as Geo Stationary 
Earth  Orbit  (CEO),  Low-Earth-Orbit  (CEO)  and 
Medium-Earth-Orbit (MEO). 

link.  There  are 

is  a  down 

orbit  Geosynchronous 

(cid:1)  Geosynchronous  Earth  Orbit/Geo-stationary 
Earth  Orbit–  Geosynchronous  orbit  is  the 
Geostationary 
orbit 
include  O'  to  earth's  equatorial  plane  (that  is 
directly  above 
the  equator).  Line-of-sight 
propagation is sending and receiving antennas be 
locked into each other location. A satellite moves 
faster or slower than the Earth's rotation is useful 
only for short periods. 
LEO 
(LEO) 
Satellites–  Low-Earth-Orbit 
satellite polar orbits. The altitude is between 500 
and 2000 km with a rotation period of 90 to 120 
min. The satellite is a speed  of 20,000 to 25000 
km/h.  Low-Earth-Orbit  satellites  orbits  are 
commonly  used  for  communication  military 
imaging 
reconnaissance, 
application. 

spying  and  other 

(cid:1) 

Switching 

switching 

large  networks, 

technology 
In 
determines  the  best  path  for  data  transmission, 
from the sender to the receiver. 
Switching 
to  connect 
techniques  are  used 
switching techniques are used to connect systems 
to perform auto-one communications. 

Switching and TCP/IP  Layers– There are four 
switching at TCP/IP layer. 

Computer Network  

114 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Switching  at  Physical  Layer–  Physical  layer 
can  have  only  circuit  switching.  There  are  no 
packets exchanged at the physical layer. Physical 
layer  allow  signal  to  travel  in  one  path  or 
another. 

Switching at Data Link Layer– Data link layer 
is  packet  switching.  Packets  means  frames  or 
cells. Packet switching at the data link layer done 
using virtual circuit approach. 

Switching at Network Layer– Network Layer is 
packet  switching.  Network  layer  can  be  used 
virtual circuit approach or datagram approach.  

3.  Teardown  Phase–  When  one  of  the  parties 
needs  to  disconnect,  a  signal  is  sent  to  each 
switch to release the resources. 

Packet-Switched Network 
In a computer  network, communication between 
two ends is done in blocks of data called packets, 
this  allows  us  to  make  switches  work  for  both 
storages  and  forwarding  because  a  packet  is  an 
independent entity that can be stared an later can 
be sent in. 

is 

switching. 

a  message 

Switching  at  Application  Layer–  Application 
layer 
The 
communication  at  application  layer  occurs  by 
that 
exchanging  messages.  We  can 
communication using email is a kind of message 
switched communication. 

say 

Circuit Switched Networks 

 A  circuit  network  is  made  of  a  set  of  switches 
connected by physical links in which each link is 
divided in to n channels. ISDN is an example of 
circuit switched network. 

The  actual  communication  in  a  circuit  switch 
network  requires  three  phases  are  connection 
setup, data transfer and connection teardown. 

1.  Setup  Phase–  Setup  phase  two  parties  (or 
multiple  parties 
in  a  conference  call)  can 
communicate  a  dedicated  circuit  needs  to  be 
established.  The  end  systems  are  normally 
connected 
the 
switches. 

through  dedicated 

lines 

to 

There are two type of packet switched network. 
(i) Datagram networks 
(ii) Virtual Circuit Networks 
Datagram  networks–  Datagram  networks  are 
referred  to  as  connection  less  networks.  There 
are no setup or teardown phases. Each packet is 
treated  the  same  by  a  switch  regardless  of  its 
source or destination. 
tables  are 
i.  Routing  tables–  The  routing 
periodically.  The 
and 
dynamic 
destination  addresses  and 
the  corresponding 
forwarding  output  ports  are  recorded  in  the 
tables. 
ii. Destination address– The destination address 
is  the  header  of  the  packet  in  a  data  gram 
network  remains  the  same  during  the  entire 
journey of the packet. 
•  ATM  (Asynchronous  Transfer  Mode) 
fundamental packet switching. 

updated 

is 

Virtual-Circuit Networks 

2.  Data  Transfer  Phase–  After 
the 
establishment  of  the  dedicated  circuit  (channels) 
the two parties can transfer data. 

Computer Network  

115 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A  virtual-circuit-switched  network 

is  across 

Broadcast  address–  Broadcasting  one  to  all 

between  a  circuit-switched  network  and  a  data 

communication. Example FF:FF:FF:FF:FF:FF 

gram  network. There are some characteristics of 

(cid:1) 

a virtual circuit switched network such as 

Redundancy–  The  control  concept  in  detecting 

or correcting error is redundancy. Redundant bits 

i.   There  are  setup  and  teardown  phases  in 

are  added  by  the  sender  and  removed  by  the 

addition to the data transfer phase. 

receiver.  It  is  allows  the  receiver  to  detect  or 

ii.   Resource  can  be  allocated  in  setup  phase 

circuit switched network or on demand as in 

a datagram network. 

correct corrupted bits. 
• An error-detecting code can detect only the type 
of errors for which it is designed other of errors 

iii.  A  virtual  circuit  network 

is  normally 

may remain undetected. 

implemented in data link layer. While circuit 

switched  network  is  implemented  physical 

•  A  single-bit  error  is  the  same  for  us  as  a  burst 
error  called  error  correction.  The  number  of 

layer  and  datagram  network  in  the  network 

error  and  the  size  of  message  are  important 

layer. 

factors. We can divide coding schemes into two 

Addressing–  Virtual-circuit  network  two  types 

broad categories block coding and convolution 

addressing are involved such as global and local 

coding. 

(virtual-circuit identifier) 

(cid:1) 

Important factor of (ARP) Protocols  
•  Address  Resolution  Protocol  (APR)  is  used  to 
get  MAC  address  of  a  node  by  providing  IP 

addresses. 

•  ARP  is  used  to  find  the  MAC  addresses  that 

corresponds to an IP address. 

•  The  ARP  protocol  is  one  of  the  auxiliary 
protocol  defined  in  the  network  layer.  It  maps 

an  IP  address  to  a  logical  link  address.  ARP 

accepts  IP  address  from  the  IP  protocol  maps 

the  address  to  the  corresponding  link  layer 

address and pass to the data link layer. 

•  The  data  link  layer  is  responsible  to  creation 
and  delivery  of  a  frame  to  another  node.  It  is 

responsible  for  packetizing  (framing),  flow 

control  and  error  control,  congestion  control 

along the link. 

•  Link  layer  protocols  three  types  of  addresses 
such  as  unicast,  Multicast  and  broadcast. 

Unicast–  Address  Unicasting  one-to-one 

• Minimum hamming distance for error detection 
is  set  of  code  words.  The  minimum  hamming 

distance 

is  a  smallest  hamming  distance 

between all possible pairs of code words. 

•  Minimum  distance  for  linear  block  codes  are 
number  of  non-zero  valid  code  word  with  the 

smallest number. 

•  Parity  check  code  error  detection  is  a  linear 

block code. 

•  Error  detection  technique  is  based  on  a  binary 
division Cyclic Redundancy Check (CRC).  
•  Cyclic  Redundancy  check  is  a  subset  of  cyclic 
code  (CRC)  is  used  in  network  such  as  LAN, 

WAN.  It  is  used  to  binary  division  error 

detection technique. 

•  Checksum  is  an  error  detecting  technique 
applied to a message of any  length. Checksum 

technique  is  used  at  the  network  and  transport 

layer rather than the data-link layer. 

•  Data  link  control  (DLC)  is  connectionless  or 
connection  oriented.  DLC  is  a  net  way  and 

communication.  A 

frame  unicast  address 

transport layer protocol. 

destination  is  destined  only  one  entity  in  the 

link.  Example  A3:34:54:11:92:F1 

It 

is 

separated by colons. 

•  Data  Link  Control  (DLC)  is  procedure  for 
communication  between  two  adjacent  nodes 

such as node to node communication. Data link 

Multicast  address–  Multicast  address  one-to-

control 

function 

include  control 

function 

many communication. Example A2:34:45:11:92:F1 

include framing and flow error control. 

Computer Network  

116 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1) 

TDM–  Time  Division  Multiplexing  is  requires 
the  transmitter  and  receiver  to  be  synchronized 
periodically. 

Description 

detection 

CSMA/CD  CSMA/CD is reduce the possibility of 
collision  but  it  is  not  eliminate  it. 
Carrier  Sense  Multiple  Access  with 
collision 
CSMA/CD 
transmission  and  collision  detection 
are  continuous  processes.  We  do  not 
sent the entire frame and then look for 
the  collision.  CSMA/CD  as  the  media 
access  method Ethernet  LAN as token 
passing, Token Ring, Token Bus. 

CSMA/CA  Carrier  Sense  Multiple  Access  with 
collision  (CSMA/CA)  is  a  wireless 
network. Collision are avoided through 
the  use  of  CSMA/CA  three  strategies 
such  as  Inter  frame  space,  contention 
window, acknowledgements.  

IEEEI 802 Standard for LANs (MAC) 

LLC-Logical Link Control  MAC:  Media  Access 

Data-link layer  Ethernet 

MAC 

Control 

Token  Ring 
MAC 

Physical layer 

Ethernet 
Physical 
Layer 

Token  Ring 
Physical 
Layer 

Token 
Bus 
MAC 

Token 
Bus 
Physical 
Layer 

Transmission media OSI or TCP/IP suite 
Transmission media IEEE standard 
• IEEE 802.16 standard for Wi-Max technology. 

HUB 

A  hub  is  a  device  that  operates  only  in  the 
physical layer. A repeater is a multiport device is 
called hub. A hub or a repeater is a physical layer 
device. Type of Hub-  Active  Hub, Passive Hub, 
Intelligent Hub. 

Connection 
less  Protocol–  Connectionless 
protocol  frames  are  sent  from  one  node  to  next 
without  any  relationship  between  the  frames. 
Frames are not numbered and there is no sense of 
ordering. 

Connection  Oriented  Protocol–  Connection-
oriented  protocol 
logical  connection 
is  a 
established  between 
two  nodes.  Connection 
oriented  protocol  some  point-to-point  protocol. 
Same  wireless  LAN, 
some  WAN. 
Connection  oriented  protocol  are  rare  in  wired 
LAN. 

and 

Protocol  Description 

PPP 

HDLC 

Point-to-point  protocol  provide 
the 
services of physical layer. But to control 
and  manage  the  transfer  of  data  link 
layers.  PPP  does  not  provide  any  flow 
control.  Error  control  is  also  limited  to 
error  detection.  PPP  uses  a  character 
oriented frame. It is a link layer protocol 
such as link control protocol.  

bit 

oriented 

protocol 

High level Data Link Control (HDLC) is 
a 
for 
communication  over  point-to-point  and 
multipoint link. HDLC is a three types of 
(I-frame), 
frames, 
supervisory 
and 
unnumbered frames (u-frames). 

information 
frame 

frame 
(s-frames) 

(cid:1) 

Media  Access  Control  is  a  sub-layer  in  the  data 
link layer. 

ALOHA–  Aloha  is  random  access  method.  It 
was  designed  for  a  radio  (wireless)  LAN,  but  it 
can be used on any stared medium. The original 
ALOHA  protocol  is  called  pure  ALOHA.  Pure 
ALOHA is vulnerable time a station send frame. 
Slotted  ALOHA  was  invented  to  improve  the 
efficiency of pure ALOHA. 

Computer Network  

117 

YCT 

 
 
 
 
 
 
 
 
 
Routers 

7  of  OSI  model.  TLS  is    sometimes  called  SSL 

A  router  is  a  three  layer  device  operates  in  the 

(Secure Socket Layer).  

physical layer. Data-link layer, network layer. A 

router  is  an  internetworking  devices.  A  router 
change the link-layer addresses in a packet. 

10 Gigabit 
LAN

Gigabit LAN

Switch

Gigabit LAN
Switch

Fragmentation 

Fragmentation  is  a  process  divided  packets  into 
smaller  pieces  (fragments)  so  that  resulting 

pieces  can  travel  across  link  smaller  Maximum 

Transaction  Unit  (MTU)  that  original  packed 
size. The network layer fragmentation data when 

the  maximum  size  of  a  data  gram  exceeds  the 
maximum  size  of  data  that  can    retained  in  a 

frame.  There  are  three  type  of  fragmentation. 
External  fragmentation,  Internal  fragmentation, 
Data fragmentation.  

......

......

Firewalls 

System

System System

System

Firewalls  provide  protection  against  outside 

(cid:1) 

Dynamic  Host 

configuration 

Protocol 

(DHCP)– DHCP is an application layer program 

using  the  client  server  helps  TCP/IP  at  the 

network  layer.  DHCP  to  assign  permanent  IP 

address is the host and router. 

Bridge 

A  bridge  operates  data  link  layer.  A  bridge  is  a 

repeater add on functionality filtering by reading 

the MAC address source and destination. Bridge 

is used inter connecting two LAN working same 
protocols. 

Gateway 

Gateways are protocol converters and operate at 

cyber  attackers  by  shielding  your  computer  or 
network from  malicious or unnecessary  network 

traffic.  There is a two types of firewall. 

i.  Packet-Filter 
firewall–  A  packet-filter 
firewall  is  a  router  that  uses  a  filtering  table  to 

decide packet must be discard (not forward). It is 
based on network layer and transport layer. 

ii.  Proxy  Firewall–  A  proxy  firewall  is  a 

network  security  system  that  protect  network 
resource by  filtering  messages at the application 
layer. 
Routing  → Routing Algorithms 
i.   Distance-vector  Routing–  DVR  is  used  to 
find the least cost (shortest distance) between 

a  source  node  (using  the  Bell  man-ford 
Equation). 

any network layer. Gateways are generally more 

ii.   Link state routing is select the best least-cost 

complex  than  switch  or  routers.  A  gateway  is 
also called protocol converter. 

Tunneling 

Tunneling  is  used  in  virtual  private  networks 

(VPNs).  It  can  also  setup  efficient  and  source 

connections  between  networks,  enable 

the 

unsupported  network  protocol.  A  VPN  is  a 

secure,  encrypted  connection  over  the  public 

shared  network.  VPN  is  a  Transport  Layer 

Security (TLS) protocol operate layer 6 and layer 

route to transfer the data packets between the 

sender/source and receiver/destination. 

iii.   Path-Vector-Routing  is  not  actually  used  in 

an internet and is mostly designed to route a 

packet between ISP. Example BGP is a path 
vector routing protocol.   

Congestion Control 

Congestion  control  a  number  of  packets  send  to 

the  network  is  greater  than  the  capacity  of  the 

network.  It  can  handle  the  number  of  packets  a 
network.   

Computer Network  

118 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Cryptography 

of 

technique 

securing 
Cryptography 
is 
to  achieve 
information  and  communication 
message 
integrity  and  confidentiality  and 
exception.  The  cryptographic  parameter  client 
and server a 48 byte master secret is created from 
the  pre-master  secret  by  applying  two  hash 
function (SHA-1 and MDS). 

Asymmetric  key cryptography is a  use to public 
key and private key. 

Electronic Email 

to  exchange 
Electronic  mail  allows  users 
messages.  When  the  request  arrives  the  server 
provides  the  service.  Electronic  mail  is  an  on 
way transaction. 

Public key 

Email-Architecture 

Public key cryptography is used for email traffic, 
such  as  with  the  standard  encryption  method 
S/MIME,  for  digital  signatures  as  well  as  for 
cryptographic  protocol  such  as  SSL/TLS,  SSH 
and HTTPS. 

Secret key 

Secret key cryptography is also called symmetric 
cryptography  because  the  same  key  is  used  to 
both  encryption  and  decryption  the  data.  Secret 
key crypto graphic include Advanced Encryption 
Standard 
(AES).  Triple  Data  Encryption 
Standard (3DES) and Rivest Cipher 4 (RC4).   

Domain Name System 

DNS  is  a  host  name  for  IP  address  translation 
service.  It  is  application  layer  protocol  for 
message  exchange  between    clients  and  servers. 
DNS  is  a  distributed  data  base  internet  service 
that translate domain name to IP address. TCP/IP 
protocol use the IP address.   

Electronic Email Security 

Email  security  is  the  process  of  ensuring  the 
availability,  integrity  and  authenticity  of  email 
communication  by  protecting  against  the  risk  of 
email threats.  

Name Server 

Name  server  are  work  as  a  directory  that 
translates domain names in to IP addresses. 

Protocol 

SMTP 

Description 

standard 

Simple  Mail  Transfer  Protocol  is  an 
communication 
internet 
protocol 
mail 
transmission  message  transfer  agents 
use  SMTP  to  send  and  receive  mail 
messages. 

electronic 

for 

POP3 

Post  Office  Protocol  Version  3  (POP3) 
provides access to an inbox stored in an 
email server. It executes the  down load 
and delete operation for messages. 

MIME  Multipurpose  Internet  Mail  Extensions 
allows  an  e-mail  message  a  non-ASCII 
file  such  as  a  video  image  or  a  sound 
and  it  provide  mechanism  transfer  non 
text characters to text characters. 

IMAP4 

is  an  application 

Internet Message Mail Access Protocol, 
layer 
version  4 
protocol 
that  operates  for  receiving 
emails  from  mail  server.  Users  have 
remote access to all the contexts. 

Symmetric Key Cipher 

Domain Name System Resource Records 

 A  symmetric  key  cipher  uses  the  same  key  for 
both  encryption  and  decryption.  A  key  can  be 
used for bidirectional communication. 

Asymmetric  key  cryptography 
is  based  on 
applying  mathematical  function  to  the  number. 

Resource  records  are  used  to  store  data  domain 
names  and  IP  addresses.  Each  resource  record 
specifies information about particular object. The 
server  uses  these  records  to  answers  queries  for 
hosts in its zone. 

Computer Network  

119 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 10.  

PROGRAMMING IN 
C and C++ 

(cid:1) 

A token is the smallest element of a program that 
is meaningful in the compiler. 

(cid:1) 

(cid:1) 

functions, 

Identifier refers to name given to entities such as 
variables, 
structures,  array  etc. 
Identifiers must be unique.   
Keywords  is  reserved  word.  It  can't  use  as  a 
variable name and constant name. 

auto 

const 

default 

float 

int 

short 

struct 

unsigned 
(cid:1) 

break 

double 

do 

for 

long 

signed 

switch 

void 

case 

else 

enum 

goto 

register 

sizeof 

typedef 

volatile 

char 

continue 

extern 

if 

return 

static 

union 

while 

Constant is a name given to the variable. It can't 
altered  or  changed  during  execution  once 
defined. 
String  is  a  sequence  of  characters  terminated 
with a null character '\0' strings are defined as an 
array of characters. Example– 
Char str[] = "YCT" 

Index 0

1

2

Str

Y C T

Operators  are  used  to perform  the  operations  on 
variables and value. 

(cid:1) 

(cid:1) 

Arithmetic Operators 
Arithmetic  operators  are  used 
mathematical operations. 

Operators  Meaning of Operators 

to  perform 

+ 

– 

* 

/ 

% 

++ 

– – 

Addition, Adds two values 

Subtraction,  Subtracts  one  value 
from another 

Multiplication,  Multiplies 
values 

two 

Division,  Divides  one  value  by 
another 

Remainder after division 

Increment,  increase  the  value  of  a 
variable by 1 

Decrement, Decreases the value of a 
variable by 1 

Relational Operators 

Relational  Operators  are  used  to  checks  the 
relationship between two operands. 

Operators  Meaning of Operator 

= = 

! = 

> 

< 

> = 

< = 

Equal to 

Not equal 

Greater than 

Less than 

Greater than or equal to 

Less than or equal to 

Logical Operators 

 Logical  operators  are  used  to  determine  the  logic 
between variable or values and return either 0 or 1. 

Operators  Operators Meaning 

&& 

|| 

! 

Logical and, Returns true if the both 
statements are true. 

Logical  or,  Returns  true  if  the  one 
of the statements is true. 

Logical  Not,  Reverse  the  result, 
returns false if the result is true. 

Programming in C & C++ 

120 

YCT 

 
 
 
 
 
 
 
 
 
 
 
% 

^ 

& 

* 

( 

) 

– 

+ 

' 

. 

: 

; 

Percent 
sign 

Caret 

Ampersand 

Asterisk 

Left 
parenthesis 

right 
parenthesis 

Underscore 

Plus sign 

Comma 

Period 

Colon 

Semicolon 

` 

- 

= 

< 

> 

? 

{ 

} 

[ 

] 

" 

Apostrophe 

Minus sign 

Equal 

Opening  angle 
bracket 

closing 
bracket 

angle 

Question mark 

Left brace 

Right brace 

Left bracket 

Right bracket 

Quotation mark 

(cid:1) 

Data  types  in  C–  There  are  several  different 
ways  to  store  data  in  C  and  they  are  all  unique 
that 
from  each  other.  The 
information can be stored as are called data type. 

types  of  data 

Bitwise Operators 

 Bitwise  operators  are  used  to  perform  bit  level 
operations. 

Operators  Meaning of Operators 

& 

| 

^ 

<< 

>> 

~ 

Bitwise AND 

Bitwise OR 

Bitwise XOR (Exclusive OR) 

Left Shift 

Right Shift 

Bitwise complement 

Assignment Operators 

Assignment  operators  are  used  to  assign  values 
to variables. 

Operators  Meaning of Operators 

= 

* = 

/ = 

% = 

+ = 

– = 

<< = 

>> = 

& = 

^ = 

| = 

Simple Assignment 

Multiplication Assignment 

Division Assignment 

Remainder Assignment 

Addition Assignment 

Subtraction Assignment 

Left Shift Assignment 

Right Shift Assignment 

Bitwise AND Assignment 

Bitwise exclusive OR Assignment 

Bitwise inclusive OR Assignment 

Control Structure: LOOPS– A loop is used to 
repeat  a  block  of  code  until  the  specified 
condition is met. 

Other Operators 

Operators  Meaning of Operators 

Sizeof() 

To  return  the  actual  sizeof  any 
given variable 

(cid:1) 

& 

* 

? : 

–> 

, 

To return the address of any given 
variable 

Pointer to a variable 

Conditional  expression  or  ternary 
operator 

Member selection operator 

Comma  operators  linked  related 
expression together. 

Special Characters 

Special symbols have some special meaning and 
they can't be used for other purposes. 

Symbol  Meaning 

Symbol  Meaning 

~ 

# 

$ 

Tilde 

Pound sign 

Dollar sign 

/ 

| 

\ 

Slash 

vertical bar 

back slash 

For Loop 
Syntax: 

for(init statement; testexpression; updatestatement) 

{ 

//body of loop 
} 

Programming in C & C++ 

121 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1)  How for loop works: 

Syntax– 

for(init;condition;increment){ 
  for(init;condition;increment){ 
//statement of inside loop 
} 
//statement of outer loop 
} 

Flow-Chart of Nested for Loop 

(cid:1) 

/* Calculation of simple interest for 3 sets p, n 
and r */ 
main(){ 

int p, n, count; 
float r, si; 
for (count = 1; count < =3; count 
= count + 1) 

printf("Enter values of p, n and r"); 
scanf("%d %d %f", &p, &n, &r); 
si = p * n * r/100; 
printf("simple interest = Rs. %f\n", si); 

{ 

} 

} 

Flow-Chart of Program 

Consider the program given below. 
main(){ 
  int r, c, sum; 
  for (r = 1; r<= 3; r++){ 

for(c = 1; c< = 2; c++){ 

sum = r + c; 

printf("r  =  %d  c=%dsum  =  %d\n",  r,  c, 

sum); 

} 
} 

  } 

While Loop– The while loop, loops through a block 

of code as long as a specified condition is true. 

Nested  for  Loop–  A  for  loop  inside  another  for 

loops is called nested for loop. 

Programming in C & C++ 

122 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
Syntax– 

While(condition){ 
//statement of  
body 

} 

Selection Statements 

1. If statement 
Syntax– 

if(condition) 

{ 

statement execute if 

statement is true 

} 
Flow-Chart of if statement 

(cid:1) 

Understand  operation  of  the  while  loop  by 
chart– 

Do/While  Loop–  This  loop  will  execute  the 
code block once, before checking if the condition 
is true, then it will repeat the loop as long as the 
condition is true. 

Syntax– 

  do { 

//block to be executed 

} 
while (condition); 

2. If-else statement– 
Syntax– 

if(condition){ 

//execute block if condition true 

  }else{ 

//execute if condition false 

  } 

Flow-Chart of if-else 

3. Nested if– 
Syntax– 

if(condition 1) 
  { 
  //execute if condition 1 true 
  if(condition 2){ 
  //execute if condition 2 true 
  } else{ execute if condition 2 

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

1. Break Statement Syntax– 

  //specific condition 

  break; 

Flow-Chart of break statement 

4. If-else ladder– 

Syntax– 

if(test expression){  

  //statement 

  } else if { 

2. Continue statement 

Syntax– 

Continue; 

Flow-Chart of continue 

//statement 

} 

else if{//statement 

} 

. 

. 

. 

else{//statement 

} 

Flow-Chart of Ladder if -else 

Array and Strings 

(cid:1) 

Arrays– Array are used to store multiple values 

in a single variable, instead of declaring separate 
variables for each values. 

(cid:1) 

Access the element of an Array– 

Jump Statements 

It is used to interrupt the flow of the program or 
escape a particular section of the program. 

Programming in C & C++ 

124 

YCT 

 
 
 
 
 
 
   
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Example– 

return 0; 

int main(){ 
  int myFirstIndex[] = {25, 40, 70, 150}; 
  printf("%d", myFirstIndex[0]); 
  return 0; 
} 

output = 25 
(cid:1) 

Array in Loop– 

Example– 

int main() 

{ 

int arr [] = {5, 10, 15, 17, 20}; 
int i = 0; 
while (i < 5) 
{ 

printf("%d", arr[i]); 
i++; 

} 
return 0; 

} 
Output = 5 10 15 17 20 
(cid:1)  Multidimensional Arrays– 

A multidimensional array is an array of arrays. 

Syntax– 

data_type array_name[size1][size2].....[sizeN]; 

Example– 

} 
Output:  2 
3 
4 
5 
6 
8 

(cid:1) 

Strings–  Strings 
text/characters. 

are 

used 

for 

storing 

'\0'

C[0] C[1] C[2]

a

b

\0

Example– 

  int main(){ 

char greetings[] = "Hello YCT"; 
printf("%s", greetings); 
return 0; 
} 

Output = Hello YCT 

Memory Address 

 The memory address is the location of where the 
variable  is  stored  on  the  computers.  Memory 
address is in hexadecimal form. 

Column 0 Column1 Column 2

Pointers 

3

6

4

8

Pointers are used to store the address of variables 
or memory location. 

Syntax– 

datatype  *var_name; 

Declare a pointer variable must be a * before its name. 

How to pointer works 

Row 0

Row1

2

5

int main(){ 

int matrix[2][3] = {{2,3,4}, 

{5,6,,8}}; 
int i,j; 
for (i=0; i<2; i++){ 

for(j=0; j<3; j++){ 
printf("%d\n", matrix 

[i][j]); 

} 

} 

Programming in C & C++ 

125 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Example– 

  main(){ 

int a; 
pirntf("%d", &a); //print address of a 
return0; 
} 
Output = 0x7ffe59c7a1e4 
Note–  Output  can  be  assigned  different  address  in 

different runs. 

Example– 

int main(){ 

int* PC, C; 
  C = 32; 
printf(" Address of C:%d\n", & c); 
printf("value of C:%d\n\n", C); 
PC = & C; 
printf("Address of pointer PC:%d\n"PC); 
printf("Content of pointer PC:%d\n\n", *PC); 

  C = 11; 

printf("Address of pointer PC:%d\n", PC); 
printf("content of pointer PC:%d\n\n", * PC); 

*PC = 2; 

printf("Address of C:%d\n", &C); 
printf("value of C: %d\n\n", C); 

return 0; 

} 

Output– 

Address of C : 0x7ffd485f65ec 
value of C: 32 
Address of pointer PC: 0x7ffd485f65ec 
Content of pointer PC: 32 
Address of pointer PC: 0x7ffd485f65ec 
Content of pointer PC: 11 
Address of C: 0x7ffd485f65ec 
Value of C: 2 

Functions 

(cid:1) 

Functions– A function is a block of code which 
only runs when it is called. 

Syntax– 

void myFunct(){ 
//code to be executed(definition) 
} 

//declaration 

(cid:1) 

Standard Library Functions– Library functions 
are used to defined in header files. 

Some Header Files 

conio.h 

stdio.h 

It  is  type  of  console  output/input  header 
file. 

It is a standard type of output/input header 
file. 

time.h 

The function that are time related 

math.h 

errno.h 

print() 

function 

The 
operations. 

are 

related 

to  math 

The  function  are  related  to  error  handling 
functions. 

The function send formatted output on the 
screen. This function defined in the stdio.n 
header file. 

Ctype.h  Character type functions 

assert.h 
(cid:1) 

Program assertion functions 

User  defined  function–  Working  flow  of  user 
defined function 
#include<stdio.h> 
  void functionName(){ 

  function  names  are  identifiers  and  should  be 
unique. 

User Defined Function 

1. No arguments and no return value 

2. No arguments and a return value 

3. Arguments and return value 

4. Arguments and with return value 

1. No Arguments and no return value– 
Syntax– 

void function_name(){ 
//no return value 
return; 

} 

2. No arguments and a return value– 
Syntax– 

return_type function_name() 

{ 
//execute program 
return value; 

} 

Programming in C & C++ 

126 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3. Arguments and No return value– 
Syntax–  

void function_name(type1 argument1,  

type2 argument2,.....typeN argumentN) 
{ 

//execute program 
return; 

} 

return n+ sum(n – 1); 

else 

return n; 

} 

Output– Enter a positive integer:6 

sum = 21 

Structure 

4. Arguments and with return value– 
Syntax– 

return_type 
type2 arguments2___typeN arguementN) 

function_name(type1  arguments1, 

 A  structure  or  struct  is  a  collection  of  variables 

(different types) under a single name.  

Structure using the struct keyword and 

declare each of its members inside curly braces. 

{ 

//execute program 

  return value; 
} 

Recursion 

 A  function  that  calls  itself  is  known  as  a 
recursive  function  and  technique  is  known  as  a 
recursion.  This  technique  provides  a  way  to 
break  complicated  problems  down  into  simple 
problems which are easier to solve. 

Working of Recursion 

Syntax–  

struct structureName { 

  datatype member1; 

  datatype member2; 

  ....... 

  }; 

Example– 

(.) Symbol Access the structure members. 

Example– 

struct myStructure{ 

  int myNum; 

  char myLetter; 

}; 

  int main(){ 

struct my StructureS1; 

  S1.myNum = 13; 

  S1.myLetter = 'B'; 

  printf("my number:%d\n",S1.myNum); 

  printf("my letter:%c\n",S1.myLetter); 

return 0; 

} 

Output– 

my number: 13 

my letter : B 

Sum of Natural Numbers– 

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
int sum(int n){ 
if (n! = 0) 

Programming in C & C++ 

127 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
   
 
 
   
 
 
   
 
 
   
 
 
   
 
 
 
   
 
 
 
 
   
 
 
 
   
 
 
 
 
   
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Keyword typedef 

Output– 

We  use  the  typedef  keyword  to  create  an  alias 
name for data types. 
Example– 
#include <stdio.h> 
#include <string.h> 
  typedef struct person{ 

(cid:1) 

Imaginary Part : 9 
Real Part : 5.25 
Integer: 6 

Structure  and  Pointers–  Pointer  to  structure 
members are accessed using arrow (→) operator. 
#include<stdio.h> 
  struct Point{ 

char name[50]; 
int dtdNo; 
float salary; 

} person; 
int main(){ 

person p1; 
strcpy(p1.name, "Rahul"); 
p1. dtdNo=1010; 
p1.salary = 9000; 

printf("Name; %s\n", p1.name); 
printf(" department No: %d\n",p1.dtdNo); 
printf("salary:%.2f", p1.salary); 

return0; 

} 

Output– 

Name: Rahul 
Department No. 1010 
Salary: 9000 

(cid:1) 

Nested Structure– Nested struct within a struct. 
# include <stdio.h> 
  struct complex { 
int img; 
float real; 
}; 
struct number { 

struct complex comp; 
int integer; 

} num1; 
int main(){ 

num1.comp.img = 9; 
num1.comp.real = 5.25; 
num1.integer = 6; 
printf("Imaginary Part; 

%d\n", num1.comp.img); 
printf("Real Part:%2f\n", 
num1.comp. real); 
printf("Integer:%d", num1.integer); 
return 0; 

} 

int a, b; 

}; 
int main(){ 
struct Point p1 = {1, 2}; 
struct Point *p2 = &p1; 
printf("%d%d", p2 →a, p2→ b); 

return 0; 

} 
1, 2  

Output: 
(cid:1) 

Structure  and  functions–  Structures  can  be 
passed  as  function  arguments  like  all  other  data 
types.  We  can  pass  individual  members  of  a 
structure, and entire structure. 

Example– 

#include <stdio.h> 
  struct student { 

char name[40]; 
int age; 
float salary; 

}; 
void display(struct students); 

int main(){ 

struct students S1; 
printf("Enter name:"); 
scanf("%[^\n]%*c", S1.name); 
printf("Enter age: "); 
scanf("%d", &S1.age); 
printf("Enter salary: "); 
scanf("%f", &S1.salary); 
display(S1); 
  return 0; 
  } 
  void display(struct students) 
  { 
  printf("\n Displaying information\n"); 
  printf("Name:%s", s.name); 
  printf("\n Age: %d", s.age); 
  printf("\n salary: %f",s.salary); 
} 

Programming in C & C++ 

128 

YCT 

 
 
 
 
 
 
 
   
 
   
 
   
 
 
 
   
 
   
 
   
 
   
 
 
 
 
   
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Output– 

Enter name: Rahul 
Enter age: 29 
Enter salary: 9000 
Displaying information 
Name : Rahul 
Age : 29 
Salary : 9000 

Unions 

Union  is  a  user  defined  data  type  in  C,  which 
stores  a  collection  of  different  kinds  of  the  data, 
just  like  a  structure.  The  keyword  union  is  used 
to declare the union in C. 

(cid:1) 

of 

structures 

An  Array 
function 
arguments–  An  array  is  a  collection  of  similar 
data  types.  A  group  of  structures  of  the  exact 
definition is known as an array of structures. 

as 

Example– 

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
Output– 

Name: Rahul 
Section: A 
Percentage: 90.5 
Name: Pramod 
Section: B 
Percentage: 85.5 
Name: Vibhav 
Section: C 
Percentage: 98.5 

Syntax– 

Union UnionName 
  { 

//member definitions 

  }; 
Example– 

#include <stdio.h> 
#include <string.h> 
union course{ 

char website [50]; 
char subject [50]; 
int price; 

}; 
void main() { 

union course c; 
strcpy(c.website,"yct.com"); 
printf("website: %s\n", c.website); 
strcpy(c.subject,  "The  c  programming 

of Language"); 

printf("Book Author: %s\n", c.subject); 
c.price = 100; 
printf("Book Price: %d\n", c.price); 

} 

Output– 

(cid:1) 

Website: yct.com 
Book Author: the c programming language  
Book Price : 100 

Pointers  to  Unions–  We  can  have  pointers  to 
unions  and  can  access  members  using  the  arrow 
operator (→). 
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
printf("%d %c", p2 → a, p2 → b) 
return 0; 

} 

Output–50  

OOPs Concepts 

(cid:1)  Object Oriented Programming System– 

(cid:1) 

object  take  up  space  in  memory  and  have  as 
associated  address  like  a  record  in  Pascal  or 
structure or union in C. 
Encapsulation–  Keeping  the  data  and  function 
into a single unit like a capsule. 
Consider a real life example of encapsulation in a 
company, 
like 
accounts  section,  finance  section,  sales  section 
etc. The finance section  handles all the  financial 
transaction  and  keeps  records  of  all  the  data 
related to finance. 
Abstraction– It is a process  of hiding irrelevant 
details from the user. 

there  are  different  sections 

Example– 

  #include <iostream> 

using namespace std.; 

class implement abstraction { 

Class–  A  class  can  be  considered  a  container 
containing data variables and functions. 
Human Being as a class– 

private: 

int a, b;  

public; 

void set (int x, int y){ 

a = x; 

b = y; 

} 

void display(){ 

cout << "a=" <<a<<endl 

cout << "b=" <<b<<endl 

} 

}; 

int main(){ 

implement abstraction obj; 

obj.set(10, 20); 

obj.display(); 
return θ; 

} 

Output– 

a = 10 

 b = 20 

(cid:1) 

Inheritance–  Inheriting  features  from  a  base 
class into a derived class. 
  The  class  which  inherits/takes  the  features  in 
known  as  the  derived  class  and  the  class  whose 
features if inherited is called the base class. 

(cid:1)  Object–  Objects  are  the  instances  of  the  class. 
When a class is defined, no memory is allocated 
but when it is instantiated memory is allocated. 
  Class person{ 

char name [30]; 
int id; 

public: 

void getdetails(){} 

}; 

int main(){ 
person p1;//p1 is a boject. 
} 

Programming in C & C++ 

130 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Example– 

Example of Function Overloading– 

#include <iostream> 

using namespace std; 

class Yct{ 

public: 

void fun(int x){ 

  cout <<"value of X is" 

<<x << endl; 

  } 

void fun(double x) { 

  cout <<"value of x is" 

  << x << endl; 

} 

void fun(int x, int y){ 

  cout<<" value of x and y is" 

  << x <<", " <<y << endl; 

  } 

}; 

int main(){ 

  Yct obj1; 

  obj1.fun(5); 

  obj1.fun(5.52); 

  obj1.fun(55, 50); 

return 0; 

  } 

Output– 

value of x is 5 

value of x is 5.52 

value x is and y is 55, 50. 

Example– 

#include <iosterm> 

using namespace std; 

class Yct{ 

public: 

  Yct(){ 

cout<<"Yct can give a writer" 

  <<endl; 

} 

}; 

class Yct computer{ 

public: 

  Yctcomputer(){ 

  cout<<"department of 

computer"<<endl; 

} 

}; 

class Man: public Yct, public 

  Yctcomputer{}; 

int main(){ 

  Man b1; 

return 0; 

} 

Output–  Yct can give a writer 

Department of computer 

(cid:1) 

Polymorphism–  Redefining  the  way  something 
works  either  by  changing 
the  method  of 
performing  it  or  changing  the  parts  using  which 
it is done. 

Programming in C & C++ 

131 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1) 

(cid:1) 

In  unary  operator  function  no  arguments  should 
be passed. It works only with one class objects. 
In  binary  operator  overloading  function  there 
should become argument to be passed. 

(cid:1) 

friend  operator 

The  operator  overloading  function  must  precede 
with friend keyword and declare a function class 
scope, 
two 
function 
parameter 
in  a  binary  operator  varies  are 
parameter in a unary operator. 
Example Operator Overloading–  
#include <iostream> 

takes 

using namespace std; 
class count{ 

private: 

int value; 

public: 

count(): value(10){} 
void operator ++(){ 
++value; 
} 

void display(){ 

cout<<"count:"<<value 
<<endl; 

} 
}; 
int main(){ 

count count1; 

++count1; 

count1.display(); 
return0; 

} 
Output–  count:11 
(cid:1) 

Constructor and Destruction– A constructor is 
a special member function with exact same name 
as the class name. 
  The  constructor  name  is  the  same  as  the  class 
Name  because,  compiler  uses  this  character  to 
differentiate constructors from the other member 
function of the class. 
  A constructor must not declare a return type or 
void  because  it  is  automatically  called  and 
generally used for initializing values. 

(cid:1) 

Default  Constructor–  A  constructor  with  no 
arguments called default constructor. 

Syntax– 

  Class CLASS_NAME 

{ _____ 
  public: 
  CLASS_NAME() 

  { ____ 
  } 

// other member functions 

  }; 

(cid:1) 

Para-meterized  Constructor– 
contains 
parameters  in  the  constructor  definition  and 
declaration. 

It 

Syntax– 

  class class_Name 
  { 

public: 

Class_Name(datatype variable) 

{ ____ 
} 

}; 

Example– 

#include <iostream> 
using namespace std; 
class Rectangle{ 

private: 

double length; 
double breadth; 

public: 

Rectangle(double l,double b){ 

length = l; 
breadth = b; 
} 

double calculateArea() { 

return length * breadth; 

} 

}; 
int main(){ 

Rectangle obj1(10, 5); 
Rectangle obj2(13, 8) 
cout<<"Area of Rectangle1:" 
<<obj1.calculateArea(); 
cout<<"Area of Rectangle2:" 
<<obj2.calculateArea(); 
return 0; 

} 

Programming in C & C++ 

132 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(cid:1) 

(cid:1) 

Copy  Constructor–  A  copy  constructor  is  a 
member  function  that  initialize  an  object  using 
another object of the same class. 

Constructor  Overloading–  Overloading 
in 
constructor  are  the  constructors  with  the  same 
name and different parameters. 

Example– 

# include<iostream> 
using namespace std; 
int count = 0; 
class Test{ 

public: 

Example– 

#include<iostream> 
using namespace std; 
class constructor{ 

public: 

float area; 
  constructor(){ 

area = (); 
} 

  constructor(int a, int b){ 

area = a*b; 
} 

void display(){ 
cout<<"Area:"<<area<<endl; 
} 
}; 
int main(){ 

constructor obj; 
constructor obj2(22, 40); 
obj.display(); 
obj2.display(); 
return; 

} 

Output–  Area: 0 

Area: 880 

(cid:1) 

Destructors–  Destructors  are  usually  used  to 
deallocate  memory  and  do  other  cleanup  for  a 
class  object  and  its  class  members  when  the 
object is destroyed. 
A destructor is a member function with the same 
name as its class prefixed by a ~(tilde). 
  Class x{ 

public: 
//constructor for class x 
x(): 
//Destructor for class x 
~(); 
}; 

Destructor takes no arguments and has no return 
type. Its address can't be taken. 

Test(){ 
  count++; 
  cout<<"\n No. of object created: 

\t"<<count; 

  } 
  ~Test(){ 

cout<<"\n  No  object  destroyed

:\t"<<count; 
--count; 

  } 
}; 
main(){ 

Test t, t1 
return 0; 

Output– 

No. of object created: 1 
No. of object created: 2 
No. of object destroyed: 2 
No. of object destroyed: 1 

Templates 

Templates are primarily implemented for crafting 
a  family  of  classes  or  functions  having  similar 
features. 

(cid:1) 

Functions  templates–  A  functions  template 
defines a family of functions. 

Syntax–  

  template<parameter_list> 

function_declaration 

  export template <parameter_list> 

function_declaration 
The general form of a function template is. 

Syntax–  

template<class type> ret_type 
func_name(parameter list) 
  { 

//body of function 

  } 

Programming in C & C++ 

133 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
   
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
   
 
 
 
 
 
 
 
 
Example– 

# include<iostream.h> 
#include<conio.h> 
template<class swap> 
  void swapp(swap & i, swap & j){ 

swap t; 
t = i; 
i = j; 
j = t; 

} 
int main(){ 
int e, f; 
char g, r; 
float x, y; 
cout<<"\n please insert 2 integer values" 
cin>>e>>f; 

swapp(e, f); 

cout<<"\n Integer values after swapping" 
cout<<e<<"\t"<<f<<"\n\n"; 
cout"\n please insert2 character 
values:";cin>>g>>r; 

swapp(g, r); 
cout<<"\n character values after 
swapping:"; 
cout<<g<<"\t"<<r<<"\n\n"; 
cout<<"\n please insert 2 Float 
values:"; cin>>x>>y; 
swapp(x, y); 
cout  <<"\n  the  resultant  float  values  after 

swapping:"; 

cout <<x<<",\t" <<y<<"\n\n"; 
} 

Output– 

Please insert 2 Integer values: 10 15 
Integer values after swapping: 15 10 
Please inert 2 character values: A B 
Character values after swapping : B A 
Please inert 2 Float values: 2.2 4.4 
The 

resultant 
4.4 2.2 

float  values  after  swapping:

(cid:1) 

Class  Template–  A  class  template  defines  a 
family of classes. 

Syntax– 

template class name<argument-list>; 
extern template class name<argument-list>; 

Example– 

#include <iostream> 
using namespace std; 
const size = 3; 

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

} 

T operator*(vector & y){ 

T sum = 0; 

for (int i=0; i <size; i++) 

sum + = this →v[i] *y.v[i]; 

return sum; 

} 

}; 

int main(){ 

int x[3] = {1, 2, 3}; 

int y[3] = {4, 5, 6}; 

vector <int> v1; 

vector <int> v2; 

v1 = x; 

v2 = y1 

int R = v1*v2; 

cout<<"R="<<R<<"\n"; 

return 0; 

} 

Output– 

R = 32 

Function Template with multiple 
Parameters 

Function  template  use  more  than  one  generic 
data  type  in  the  template  statement,  using  a 
comma (,) separated list. 

Syntax– 

template<class T1, Class T2, _____> 
  returntype  functionname  (arguments  of  types 
T1, T2, ____){ 
  ≡ body of function 
} 

Programming in C & C++ 

134 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Overloading of template function 

A template function may be overloaded either by 
template  functions  or  ordinary  functions  of  its 
name. 

Example– 

#include <iostream> 

#include <string> 

  using namespace std; 

  template <class T> 

  void display (T x){ 

cout<<"Template display:"<<x<<"\n"; 

} 

void display(int x){ 

cout <<"Explicit display:"<<x<<"\n"; 

} 

int main(){ 

display(1000); 

display(10.25); 

display('C'); 

return 0; 

} 

Output– 

Explicit display: 1000 

Template display: 10.25 

Template display: C 

Exception handling 

is  a  mechanism 
that 
 Exception  handling 
that  detects  and  handles 
separates  code 
exceptional  circumstances  from  the  rest  of  your 
program.  Exception  basically  built  upon  three 
keyword, namely, try, throw and catch. 
Try– The keyword try is used to preface a block 
of  statements  which  may  generate  exception. 
You use a function try block to indicate that you 
want  to  detect  exception  in  the  entire  body  of  a 
function. 

try block syntax–   

Function try block syntax– 

Catch block syntax– You can declare a handler 
to  catch  many  types  of  exceptions.  The  objects 
that  a  function  can  catch  are  declared  in  the 
parentheses following the catch keyword. 

Syntax– 

(cid:1) 

expressions–  You  use 

Throw 
throw 
expression  to  indicate  that  your  program  has 
encountered an exception. 

a 

Syntax–  

the  type  of  assignment_expression  can't  be  an 
incomplete type, abstract class type, or a pointer 
to  an  incomplete  type  other  than  the  following 
types. 
  void* 
  const void * 
  volatile void * 
  const volatile void * 
The  catch  block  that  catches  an  exception  must 
immediately follow the try block that throws the 
exception. The general form of these two blocks 
are 

------- 
------- 
try { 

------ 
throw exception; 
------ 
------ 

//block of statements 
which detects and  
throws an exception 

} 
Catch (type arg) { 

----- //block of statements that 
----- //handles the exception 

} 
----- 
-----  

Example– 

#include <iostream> 

using namespace std; 

void divide(int x, int y, int z){ 

Programming in C & C++ 

135 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  cout<<"\n we are inside the function\n"; 
  if((x–y)!=0){ 

int R = z/(x–y); 
cout<<"Result+"<<R<<"\n"; 
}else{ 

throw(x–y); 
} 

  } 
  int main(){ 

try{ 

cout<<"we are inside the try 

block\"; 

divide(10, 20, 30); 
divide(10, 10, 20); 

} catch (int i){ 

cout<<" Caught the exception\n"; 

return 0; 

} 

Output–   We are inside the try block  
We are inside the function  
Result = –3 
We are inside the function  
caught the exception. 

Multiple Catch Statements 

 It  is  possible  that  a  program  segment  has  more 
than one condition to throw an exception. In such 
cases,  we  can  associate  more  than  one  catch 
statement with a try (much like the conditions in 
a switch statement). 

Syntax– 

try{ try block} 
Catch(type1 arg){ 

//Catch block1 

} 
Catch(type2 arg){ 

//Catch block2 

} 

_____ 
____ 
Catch(typeN arg){ 

//Catch blockN 

} 

Example– 

#include <iostream> 
using namesapce std; 
void test(int x){ 

try{ 

if(x= =1) throw x; 

else 

if(x = = 0) throw x; 

else 

if(x = = –1) throw 1.0; 

cout <<"End of try-block\n"; 

} 

catch(char c){ 

cout<<"Caught a character\n"; 

} 

catch(int m){ 

cout<<"Caught an integer\n"' 

} 

catch(double d){ 

cout<<"Caught a double\n"; 

} 

cout<<"end of try_Catch system\n\n"; 

} 

int main(){ 

cout<<"Testing Multiple Catches\n"; 

cout <<"x= = 1\n"; 

test(1); 

cout<<" x = = 0\n"; 

test(0); 

cout<<"x= = –1\n"; 

test (–1); 

cout<<"x = = 2\n"; 

test(2); 

return 0; 

} 

Output– 

Testing Multiple Catches 

x = = 1  

Caught an integer 

End of try_catch system 

x = = 0 

Caught a character 

End of try catch system 

x = = –1 

Caught a double 

End of try_catch system 

x = = 2 

End of try black 

End of try catch system 

Programming in C & C++ 

136 

YCT 

 
 
 
 
 
 
 
 
 
   
 
   
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
Re-throwing an exception 

 A handler may decide to re-throw the exception 
caught  without  processing  it.  In  such  situations, 
we  may  simply  invoke  throw  without  any 
arguments as show below throw; 

Example– 

# include <iostream> 
using namespace std; 
void divide(double x, double y){ 
  cout<<"inside function\n"; 
  try{ 

if(y = = 0.0) 

throw y; 

else 

cout<<"Division="<<x/y<<"\n"; 

} 
Catch(double){ 

cout<<"Caught 

double 

inside 

function\n"; 

throw; 

} 
cout<<"End of function\n\n"; 
} 
int main(){ 

cout<<"Inside main\n"; 
try 
{ 
divide(10.5, 2.0); 
divide(20.0, 0.0); 
} 
Catch (double){ 
cout<<"Caught double inside  
main\n"; 
} 
cout<<"End of main\n"; 
return 0; 
} 

Output– 

Inside main 
Inside function 
Division = 5.25 

End of function 
Inside function 
Caught double inside function 
Caught double inside main 
End of main 

Instantiation 

The  creation  of  a  new  instance  of  the  class  is 
called instantiation. Memory is allocated for that 
object and the class construction runs. 

There  are  three  different  ways  of 

instantiation an object through constructors. 

that  are 

transferred  between 

Steam–  In  C++  stream  refers  to  the  stream  of 
characters 
the 
program  thread  and  I/O.  Stream  classes  in  C++ 
are  used  to  input  and  output  operations  on  files 
and I/O devices. 
Stream Classes– The C++ I/O system contains a 
hierarchy  of  classes  that  are  used  to  define 
various streams to deal with both the console and 
disk files. 

Stream classes for console I/O operations. 

As  seen  the  above  iOS  is  the  base  class  for 
istream  and  ostream  which  are  in  turn  base 
classes for iostream. 

Unformatted I/O Operations 

Overloaded  operators  >>  and  <<  :-  We  have 
used the objects cin and cout  (pre defined in the 
iostream file) for the input and output of data of 
various types. 

Cin>>variable1>> variable2>>....>variableN 

This  is  the  general  format  for  reading  data  from 
the keyword. 

Cout<<item1<<item2<<.......<<itemN 

This is the general format for displaying data on 
the screen. 
get()  and  put()  function–  The  classes  istream 
and  ostream  define  two  member  functions  get() 

Programming in C & C++ 

137 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
and  put()  respectively  to  handle  the  single 
character input/output operations. 

Example– 

#include <iostream> 
using namespace std; 
int main(){ 

get(char*)  version  assigns  the  input  character  to 
its argument. 

get(void) version returns the input character. 

Example– 

#include <iostram>  

using namespace std; 

int main(){ 

int count = 0; 

char c; 

cout<<"Input Text\n"; 

cin.get(c); 

while(c! = '\n'){ 

cout.put(c); 

count++; 

cin.get(c); 

  } 

  cout<<"\nNumber of character = 

" <<count <<"\n"; 

  return 0; 

} 

Input text 

object oriented programming 

Output– 

object oriented programming 

Number of characters = 27 

(cid:1) 

the  newline  character 

When  we type a line of input, the text is sent to 
the  program  as  soon  as  we  press  the  RETURN 
key. The program, reads are characters at a time 
using  the  statement  cin.get(c);  and  displays  it 
using  the  statement  cout.pute(c);.  The  process  is 
terminated  when 
is 
encountered. 
getline() and write() function– We can read and 
display  a  line  of  text  more  efficiently  using  the 
line  oriented  input/output  function  getline()  and 
write(). The getline() function reads a whole line 
of  text  that  ends  with  a  newline  character.  This 
function can be invoked by using the object cin. 

cin.getline(line, size); 

int size = 20; 
char city[20]; 
cout<<"Enter City Name:\n"; 
cin>>city; 
cout<<"City name;" <<city<<"\n\n"; 
cout<<Enter city name again;\n"; 
cin.getline(city, size); 
cout<<"City name now:"<<city<<"\n\n"; 
cout<<"Enter another city name:\n"; 
cin.getline(city, size); 
cout<<"New city name:"<<city<<"\n\n"; 

return 0; 

} 

Output– 

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
• iOS class functions and flags 
• Manipulators 
• User defined output functions 

Programming in C & C++ 

138 

YCT 

  
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Functions 

Task 

width() 

precision() 

fill() 

setf() 

To  specify  the  required  field 
size  for  displaying  an  output 
value 

To specify the number of digits 
to  be  displayed  after 
the 
decimal point of a float value 

To  specify  a  character  that  is 
used  to  fill  the  unused  portion 
of a field 

To  specify  format  flags  that 
can  control  the  form  of  output 
display 

Unsetf() 

To clear the flags specified 

} 

ostream & form (ostream & output){ 

  output.setf(ios:: showpos); 

  output.setf(iso:: showpoint); 

  output.fill('*'); 

  output.precision(2); 

  output.<<setiosflags(ios::fixed) 

<<setw(10); 

return output; 

} 

int main(){ 

cout<<currency << form << 7864.5; 

return 0; 

} 

Manipulators 

Manipulators 

Equivalent ios function 

Output–  Rs**+ 7864.50 
(cid:1) 

Console program file interaction flow– 

setw() 

width() 

setprecision() 

precision() 

setfill() 

setiosflags() 

fill() 

setf() 

resetiosflags() 

unsetf() 

(cid:1) 

The addition to these functions supported by the 
C++ library. 

Designing  Our  Own  Manipulators–  We  can 
design  our  own  manipulators  for  certain  special 
purpose. 

  ostream & manipulator(ostream & output) 

{ 

____ 

____ 

____ 

return output; 
} 

Example– 

#include <iostream> 

#include <iomanip> 

using namespace std; 

//user defined manipulators 

ostream & currency (ostream & output){ 

  output <<"Rs"; 

return output; 

Classes for file stream operations 

The  I/O  system  of  C++  contains  a  set  of  classes 
that define the file handling methods. 

Class 

filebuf 

fstreambase 

Contents 

Its purpose is to set the file buffers 
read  and  write.  Contains 
to 
openprot  constant  used 
the 
open()  of  file  stream  classes.  Also 
contain  close()  and  open()  as 
members. 

in 

Provides operations common to the 
file  stream.  Serves  as  a  base  for 
fstream,  ifstream  and  of  stream 
class.  Contains  open()  and  close() 
functions. 

Programming in C & C++ 

139 

YCT 

 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
ifstream 

ofstream 

fstream 

Provides 
operations. 
input 
Contains  open()  with  default  input 
mode.  Inherits  the  functions  get(), 
getline(), read() seekg() and tellg() 
functions from istream. 

Provides 
operations. 
output 
Constains  open()  with  default 
output  mode. 
put(), 
and  wrtie(), 
seekp(), 
function from ostream. 

Inherits 

tellp() 

and 

Provides  support  for  simultaneous 
operations. 
output 
input 
Contains  open()  with  default  input 
made.  Inherits  all  the  functions 
from  istream  and  ostream  classes 
through iostream. 

Opening and Closing a file 

The first method is useful when we use only one 
file  in  the  stream.  The  second  method  is  used 
when we want to manage multiple files using one 
stream. 

(cid:1)  Opening files using constructor 

We  know  that  a  constructor  is  used  to  initialize 
an object while it is being created. 

Create  a  file  stream  object  to  manage 
the stream using the appropriate class. That is to 
say,  the  class  ofstream  is  used  to  create  the 
output stream and the class ifstream to create the 
input stream. 

Initialize 

the  file  object  with 

the 

desired filename. 

ofstream outfile("results");//output only 
ifstream infile("data");//input only 

Example– 

#include <iostream.h> 

#include <rstream.h> 

int main(){ 

  ofstream outf("item"); 

  cout<<"Enter item name:"; 

  char name[30]; 

  cin>>name; 

  outf>> name; 

  outf<<name<<"\n"; 

  cout<<Enter item cost:"; 

  float cost; 

  cin>>cost; 

  outf<<cost<<"\n"; 

  outf.close(); 

  ifstream inf("item"); 

  inf>>name; 

  inf>>cost; 

  cout<<"\n"; 

  cout<<"item name": <<name<<"\n"; 

  cout<<"item cost:" <<cost<<"\n"; 

  inf.close(); 

  return 0; 

} 

Output– 

Enter item name: CD-ROM 

Enter item cost: 350 

Item name : CD-ROM 

Item cost : 350 

(cid:1)  Opening  files  using  open()–  The  function 
open() can be used to open multiple files that use 
the same stream object. 

Example– 

#include <iostream.h> 

#include <fstream.h> 

  int main(){ 

ofstream fout; 

fout.open("Country"); 

fout<<"United States of America\n"; 

fout<<"United Kindom\n"; 

fout<<"south Korea\n"; 

fout.close(); 

fout.open("Capital"); 

fout<<"Washinton\n"; 

fout<<London\n"; 

fout<<"Seoul\n"; 

fout.close(); 

Const int N = 80; 

Programming in C & C++ 

140 

YCT 

 
 
  
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Char line [N]; 

ifstream fin; 

fin.open("Country"); 

cout<<"contents of country file\n"; 

while(fin){ 

fin.getline(line, N); 

cout<<line; 

} 

fin.close(); 

fin.open("capital"); 

cout<<"\n  contents  of  capital  file\n";

while(fin){ 

fin.getline(line, N); 

cout<<line; 

} 

fin.close(); 

return 0; 

} 

Output– 

Contents of Country file 

United States of America 

United Kingdom 

South Korea 

Contents of capital file 

  Washington 

London 

Seoul  

Then,  the  location  of  a  desired  object,  say  the 

mth object, may be obtained as follows. 

int location = m* object_length 

The  location  gives  the  byte  number  of  the  first 

byte of the mth object. We can set the file pointer 

to  reach  this  byte  with  the  help  of  seekg()  or 
seekp(). 

(cid:1) 

Error Handling During file operations– A file 

which we are attempting to open for reading does 

not exist. 
•  The  file  name  used  for  a  new  file  may  already 

exist. 

•  We  may  attempt  an  invalid  operation  such  as 

reading past the end of file.  

•  There  may  not  be  any  space  in  the  disk  for 

storing  more  data.  We  may  use  an  invalid  file 

name. 

•  we  may  attempt  to  perform  an  operation  when 

the file is not opened for that purpose. 

Error Handling functions 

Function 

Return value and meaning 

eof() 

Return true (non-zero value)  if end of 

file 

is  encountered  while  reading 

otherwise return false (zero) 

fail() 

Returns  true  when  an  input  or  output 

operation has failed 

Updating a file Random Access 

bad() 

Returns true if an invalid operations is 

Updating  is a routine task  in  the  maintenance of 

any data file. The updating would include one or 

more of the following tasks. 
 • Displaying the contents of a file 
 • Modifying an existing item 
 • Adding a new item 
 • Deleting an existing item. 

This  can  be  easily  implemented  if  the  file 

contains  a  collection  of  items/objects  of  lengths. 

In  such  cases,  the  size  of  each  object.  Can  be 

obtained using the statement. 

int object_length=sizeof(object); 

attempted  or  any  unrecoverable  error 

has  occurred.  If  it  is  false,  it  may  be 

possible  to  recover  from  any  other 

error reported and continue operation. 

good() 

Return  true  if  no  error  has  occurred. 

This  means,  all  the  above  functions 

are false. For instance, if file.good() is 

true,  all  is  well  with  the  stream  file 

and  we  can  proceed  to  perform  I/O 

operation  when  it  returns  false,  no 

further operations can be carried out. 

Programming in C & C++ 

141 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
   
 
 
 
 
 
 
 
 
   11.  

WEB TECHNOLOGY 

HTML 

HTML  is  the  standard  markup  language  for 
creating web pages. HTML stands for Hypertext 
Markup Language and describes the structure of 
a  web  page.  HTML  elements  tell  the  browser 
how to display the content. 

<!DOCTYPE  html>  –  Declaration  defines  that  this 

document is HTML5 document. 

<html>  –  Element  is  the  root  element  of  an  HTML 

page. 

<head> – Element contains meta information about the 

HTML page. 

<title>  –  Element  specifies  a  title  for  the  HTML  page 
(which  is  shown  in  the  browser's  title  bar  or  in 
the pages tab) 

<body> – Element  defines the documents body and is a 
container  for  all  the  visible  contents  such  as 
headings,  paragraph,  images,  hyperlinks,  tables, 
lists etc. 

HTML Page Structure 

Version of HTML 

Years  Version 

1991 

1995 

First Versions of HTML 

HTML 2.0 

1997  W3C Recommendation 3.2 

1999  W3C Recommendation 4.01 

2000  W3C Recommendation XHTML 1.0 

2008  WHATWG HTML5 first Public Draft 

2012  WHATWG HTML5 Living standard 

2014 

 W3C Recommendation HTML5 

2016  W3C Recommendation HTML5.1 
2017  W3C  Recommendation  HTML5.1  2nd 

Edition 

2017  W3C Recommendation HTML5.2 

HTML tag and Element 

HTML  element  defined  by  a  start  tag  some 
content and an end tag like. 

HTML Tag and Attributes 

HTML  attributes  provide  additional  information 
about  elements.  Attributes  are  always  specified 
in  the  start  tag  and  attributes  usually  come  in 
name/value pairs like, name = "value". 

Example–  The  <a>  tag  defines  a  hyperlink.  the 
href attributes specifies the URL of the page the 
link goes to. 

<a href = "http://www.yct.com"> 

visit YCT</a > 

Some Important Tags 

Description 

Defines a comment 

Tag 

<!......> 

<!DOCTYPE>  Defines the document type 

<a> 

<abbr> 

<address> 

<area> 

<article> 

<aside> 

Defines a hyperlink 

Abbreviation or an acronym 

Defines  contact  information  for 
the author/owner of a document 

Area inside an image map 

Defines an article 

Defines  content  aside  from  the 
page content 

<audio> 

Embedded sound content 

Web Technology 

 142 

YCT 

 
 
 
 
 
 
 
<b> 

<base> 

bold the text 

<frame> 

Defines a window in a frameset 

The  base  URL/target 

for  all 

<frameset> 

Defines a set of frames 

relative URLs in a document 

<h1> or <h6> 

Defines HTML headings. 

<blockquote> 

A  section  that  is  quoted  from 

<head> 

Contains  metadata/Information 

<body> 

<br> 

<button> 

<canvas> 

<code> 

<col> 

another source 

Documents of body 

Single line break  

A clickable button 

for the document. 

<header> 

A  header  for  a  document  or 

section. 

<i> 

Defines  a  part  of  text  in  an 

Used to draw graphics, on the fly 

via scripting (usually javascript) 

A piece of computer code 

Specifies  column  properties  for 

each column within a <colgroup> 

<img> 

<input> 

<label> 

alternate voice or mood. 

Defines an image. 

An input control. 

Defines  a  label  for  an  <input> 

element. 

element 

<legend> 

A  caption 

for  a  <fieldset> 

<colgroup> 

A  group  of  one  or  more  columns 

in a table for formatting 

<data> 

Adds 

a  machine 

readable 

translation of a given content. 

<datalist> 

A  list  of  predefined  options  for 

input controls 

<dd> 

Description/value  of  a  term  in  a 

description list 

<li> 

<link> 

<map> 

<mark> 

<meta> 

element. 

A list item. 

Defines the relationship between a 

document 

and 

an 

external 

resource. 

Defines an image map. 

marked/highlighted text 

metadata 

about 

an  HTML 

<details> 

Defines additional details that the 

document. 

user can view or hide. 

<meter> 

Defines  a  scalar  measurement 

<dialog> 

A dialog box or window. 

within a known range. 

<div> 

<dl> 

<dt> 

A section in a document 

<nav> 

Defines Navigation links. 

Defines a description list 

<object> 

Defines  a  container 

for  an 

Defines 

a 

term/name 

in 

a 

external application. 

description list 

<ol> 

Defines an ordered list. 

<embed> 

A  container 

for  an  external 

<optgroup> 

Defines a group of related options 

application. 

in a drop-down list. 

<fieldset> 

Groups  related  elements 

in  a 

form. 

<option> 

<output> 

An option in a dropdown list. 

The result of calculation. 

<figcaption> 

Defines  a  caption  for  a  <figure> 

<picture> 

Defines  a  container  for  multiple 

element 

image resources. 

<figure> 

specifies self contained 

<script> 

Defines a client-side script. 

<font> 

Defines  font,  color  and  size  for 

<section> 

A section in a document. 

text 

<footer> 

<form> 

A footer for a document or section 

HTML form for user input 

<small> 

<source> 

Defines smaller text. 

Defines  multiple  media  resources 

for media elements. 

Web Technology 

 143 

YCT 

<span> 

<style> 

A section in a document. 

Example– 

Defines  style  information  for  a 
document. 

<sub> 

Subscripted text. 

<summary> 

Defines  a  visible  heading  for  a 
<details> element. 

<sup> 

<svg> 

<table> 

<tbody> 

Defines superscripted text. 

A container for SVG graphics. 

Defines a table. 

Groups  the  body  content  in  a 
table. 

<td> 

Defines a cell in a table. 

<textarea> 

A multiple input control. 

<time> 

<track> 

<var> 

<video> 

<wbr> 

a specific time 

text 

Defines 
element (<video> and <audio>) 

tracks  for  media 

Defines a variable. 

Defines embedded video content. 

A possible line-break. 

Absolute URLs and Relative URLs 
A full web address are using an absolute URL in 
the href attribute. 

Example–  

<a href="https://www.google.com/">Google</a> 

A  local  link  (a  link  to  a  page  within  the  same 
website) 
is  specified  with  a  relative  URL 
(without the "https://www"), 

Example– 

<a href="html_page.php">HTML File 

</a> 

Link to an Email Address 

Use  mailto:  inside  the  href  attribute  to  create  a 
link  that  opens  the  user's  email  program  (to  let 
them send a new email.) 

Example– 

<a href="mailto:yct@gmail.com"> 

Send Mail </a> 

HTML Image– The HTML <img> tag is used to 
embed an image in a web page. The <img> tag is 
empty,  it  contains  attributes  only  and  does  not 
have a closing tag <img> tag has two attributes 
src– Specifies the path to the image 
alt– Specifies an alternate text for the image. 

<img src="imageName" alt="AltName"> 

HTML  Favicon–  A  favicon  is  a  small  image 
displayed  next  to  the  page  title  in  the  browser 
tab. To add a favicon to your website, either save 
your favicon image to the root directory of your 
web server, or create a folder. 

  Add favicon 

<link 
href="favicon path"> 

rel=-"icon" 

List 

type="image/icon" 

A  list  is  a  record  of  short  pieces  of  related 
information  or  used  to  display  the  data  or  any 
information  on  web  pages  in  the  ordered  or 
unordered form. 

Unordered List 

An  unordered  list  starts  with  the  <ul>  tag.  Each 
list item starts with the <li> tag list items will be 
marked with bullets by default. 

Unordered  list  marker–  Use  the  CSS  property 
list_style_type,  define  the  style  of  the  list  item 
marker. 

  disc– item marker to a bullet 

  circle– item marker to a circle 

  square– list item marker to a square 

  none– the list items will not be marker 

Example– 

<ul style="list-style-type: square;"> 

  </ul>  

<li> Rahul </li> 

<li> Raj </li> 

Ordered list 

An ordered list starts with the <ol> tag. Each list 
item  starts  with  the  <li>  tag.  The  list  by  default 
marked will numbers. 

ordered list used to type attributes type 

defines the list item marker. 
  type = "1" ⇒ by default 
  type = "A" ⇒ Item numbered with upper case 

Web Technology 

 144 

YCT 

 
 
 
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
 
 
 
 
   
 
 
  type = "a" ⇒ Item numbered with lowercase 

type = "I" ⇒ Item numbered with upper roman 

numbers 

type = "i" ⇒ Item numbered with lower roman 

numbers 

Example– 

  <ol type = "1, A , a, I, or i"> 

  <li> Rahul </li> 

  <li> Raj </li> 

  </ol> 

List Tags– 
  <ul> ⇒ Defines unordered list 
  <ol> ⇒ Defines ordered list 
  <li> ⇒ A list item 
  <dl> ⇒ Description list 
  <dd> ⇒ The term in a description list 
Head Element 

The  <head>  HTML  element  contains  machine 
readable 
the 
document. 

(metadata)  about 

information 

like  <title>,  <style>,  <meta>,  <link>,  <script> 
and <base> 

<meta>  element–  The  <meta>  element 
is 
typically  used  to  specify  the  character  set,  page 
description,  keywords,  author  of  the  document 
and viewport settings. 

Example– 

The character set used– 

<meta charset = "UTF-8"> 

Keywords for search engines– 

<meta  name  =  "keywords"  content  =  "HTML, 
CSS, Javascript"> 

A description of your web page– 

<meta  name  =  "description"  content  ="  Free 
online PDF"> 

The author of page– 

<meta name = "author" content ="YCT"> 

Refresh document every 30 seconds– 

<meta http_equiv = "refresh" content="30"> 

Setting  the  viewport  to  make  your  website  look 
good on all devices. 

<meta  name  =  "viewport"  content  =  width  = 
device-width, initial-scale =1.0"> 

Semantic Elements 

Semantic  elements  have  meaningful  names 
which  tells  about  type  of  content  like  header, 
footer, table, .....etc. 
Semantic  Elements– 
<aside>, 
<details>,  <figcaption>,  <figure>,  <footer>, 
<header>,  <main>,  <mark>,  <nav>,  <section>, 
<summary>, <time>. 

<article>, 

Non-semantic Elements 

Non-semantic categories as their names don't tell 
anything  about  what  kind  of  content  is  present 
inside  them  <div>  and  <span>  is  non-semantic 
elements. 

Form 

HTML form on a web page allows a user to enter 
data that is sent to a server for processing. 
  <form>  element  is  a  container  for  different 
types  of  input  elements  such  as:  text  fields, 
checkboxes, radio buttons, submit buttons etc. 

Form Attributes–  
Action- The action attributes define the action to 
be performed when the form is submitted. 

that 

the  response 

Target-  The  target  attribute  specifies  where  to 
is  received  after 
display 
submitting the form. 
target  value  ⇒  _blank,  _self,  _parent,  top, 
framename. 
Method–  The  method  attributes  specifies  the 
HTTP  method  to  be  used  when  submitting  the 
form data. 

method = "get" 

method = "post" 

Get  method  is  mainly  used  at  the  client  side  to 
send a request to a specified server to get contain 
data or resources. It is send to limited data. 

Post  method  sent  to  the  server  is  stored  in  the 
request body of the HTTP request. 

Web Technology 

 145 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
 
 
Multimedia 

Web Storage 

Multimedia  comes  in  many  different  formats.  It 

can be almost anything you can hear or see, like, 

images,  music,  sound,  video,  records,  films, 
animations and more. 

Common Video Formats 

Web  storage  can  store  data  locally  within  the 
users browser. 

Format 

MPEG 

AVI 

WMV 

QuickTime 

Realvideo 

Flash 

ogg 

WebM 

File 

.mpg 

.mpeg 

.avi 

.WMV 

.mov 

.rm 

.ram 

.swf 

.flv 

.ogg 

.webm 

MPEG-4 or MP4 

.mp4 

Note–  Only  MP4,  WebM  and  Ogg  Video  are 

supported by the HTML standard. 

Common  Audio  Formats–  MP3  is  the  best 

format for compressed recorded music. The term 

MP3  has  become  synonymous  with  digital 

music.  

Format 

MIDI 

RealAudio 

WMA 

AAC 

WAV 

Ogg 

MP3 

File 

.mid 

.midi 

.rm 

.ram 

.wma 

.aac 

.wav 

.ogg 

.mp3 

Note–  Only  MP3,  WAV  and  Ogg  audio  are 

supported by the html standard. 

LocalStorage–  Stores  data  with  no  expiration 
date and gets cleared only through JavaScript or 
clearing the browser cache/locally stored data. 

SessionStorage–  Stores  data  only  for  a  session 
meaning that the data is stored until the browser 
(or  tab)  is  closed.  Storage  limit  is  larger  than  a 
cookie (at most 5 MB). 

Web  Worker–  Web  workers  are  multithreaded 
object which is used to execute JavaScript in the 
background without affecting the performance of 
the application or webpage. 

Server Sent Events (SSE) 

A  server  sent  events  is  when  a  web  page 
automatically  gets  updates  from  a  server  via  an 
HTTP connection. This is a one way connection. 

The event source object is used to receive server 
sent event notification. 

Events 

onopen 

Description 

When a connection to the server is 
opened. 

onmessage 

When a message is received. 

onerror 

When an error occurs. 

DHTML 

DHTML stands for Dynamic HTML, it is totally 
different  from  HTML.  DHTML  is  based  on  the 
properties  of  the  HTML,  JavaScript,  CSS  and 
DOM which helps in making dynamic content. 

is  used 

to  create 

DHTML 
interactive  and 
animated  web  pages  that  are  generated  in  real 
time,  also  known  as  dynamic  web  pages  so  that 
when such a page is accessed the code. 

HTML–  HTML  stands  for  Hyper  Text  Markup 
Language and it is a client side markup language. 
It is used to build the block of web pages. 

JavaScript–  It  is  client  side  scripting  language 
that  enables  you  to  create  dynamically  updating 

Web Technology 

 146 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
content, control multimedia, animate images and 
pretty much everything else.  
CSS–  CSS  is  a  language  of  style  rules  that  we 
use  to  apply  styling  to  our  HTML  content,  for 
example setting background colors and fonts and 
laying out our content in multiple columns. 

DOM–  DOM  is  known  as  a  Document  Object 
Model which act as the weakest links in it. 
XML 

XML stands for Extensible Markup Language. It 
was  designed  to  store  and  transport  data.  It  is 
called  extensible  because  it  allows  the  author  of 
the document to defines the markup elements by 
their own.  

Advantages of XML– 
•  XML  support  Unicode,  all  most  all  the  human 
be 

language 

written 

can 

readable 
communicated using XML. 

•  It  can  be  used  to  render  data  structure  i.e 

records and lists and trees. 

• XML needs another software application called 
parser.  An  XML  document  is  very  strict  while 
maintaining a standard. 

• XML is used both on and offline for storing and 

processing data. 

•  XML  allows  validation  of  the  document  using 
XSD  or  schematron.  These  are  types  of  the 
schema for validating XML documents. 
Difference Between XML and HTML 

XML  was  designed  to  carry  data  with  focus  on 
what data is.  

HTML  was  designed  to  display  data  with  focus 
on how data looks. 

XML  tags  are  not  predefined  like  HTML  tags 
are. 

In XML all elements must have a closing tag. 
XML tags are case sensitive. 
XML  Declaration–  XML  declaration  is  not  a 
tag.  It  is  used  for  the  transmission  of  the  meta 
data of a document. 

Syntax– 

<?xml version = "1.0" encoding = "UTF-8"?> 

This  line  represents  the  XML  prolog  or  XML 
declaration.  The  XML  prolog  is  optional.  It  if 
exists, it must come first in the document. 

The  version  =  "1.0"  is  the  version  of  the  XML 
currently used. 

The  encoding  =  "UTF-8"  specifies  the  character 
encoding used while writing an XML document. 

XML Valid and Well Formed– XML document 
must be well formed. Document must conform to 
all  XML  syntax  rules.  Document  conform  to 
semantic rules, which are usually set in an XML 
schema or a DTDC (document type definition). 

Example– 

<?xml version = "1.0" encoding = "UTF-8"?> 

  <message> 

<warning> 

Hello Rahul 

</warning> 

  </message> 

XMLHttpRequest Object 

The  XMLHttpRequest  object  can  be  used  to 
request data from a web server. 
•  Update a web page without reloading the page. 
•  Request  data  from  a  server  after  the  page  has 

loaded. 

• Received data  from a  server after the page  has 

loaded. 

•  Send data to a server in the background. 
XMLHttpRequest Properties 
Indicate 

the 

status  of 

readyState– 
connection. 

the 

Status– It contains the http response code string 
from server. 

StatusText–  It  contains  the  http  response  string 
from  the  server.responseText.  It  contains  the 
response in text format from the server. 

responseXML–  It  contains  the  response  XML 
from server. 

getAllResponseHeaders– 
headers name as string. 

It 

returns  all 

the 

OverrideMimeType– It is used to set the mime 
type which is used to treat the response data type 
to be treated as text or XML type. 

stands 

for  Document  Type 
DTD–  DTD 
Definition.  DTD  defines  the  structure  and  the 
legal  elements  and  attributes  of  an  XML 
document. 

Web Technology 

 147 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Schema– XML schema describes the structure of 
an XML document. XML document with correct 
syntax is called "Well Formed". 

ECMAScript 
(2017) 

JavaScript 
is  a  programming 

language 

that 
JavaScript 
execute  on  the  browser.  It  turns  static  HTML 
web  pages 
interactive  web  pages  by 
dynamically  updating  content,  validating  form 
data  controlling  multimedia  animate  images  and 
almost everything else on the web pages. 

into 

Versions  of  JavaScript–  In  the  years  1996,  a 
standards  organization  called  ECMA  (European 
Computer 
Association). 
International  carved  out  standard  specifications 
called ECMA script (ES). 

Manufacture 

ECMAScript Editions 

Version 

Official Name 

Description 

ES1 

ES2 

ES3 

ES4 

ES5 

ECMAScript1 
(1997) 

ECMAScript2 
(1998) 

ECMAScript3 
(1999) 

First edition 

Editorial changes 

Added regular 
expressions added 
try/Catch Added 
Switch Added do-
while 

ECMAScript4  

Never released 

ECMAScript5 
(2009) 

Added string, 
padding, 
object.entries(), 
object values() 
added async 
functions and shared 
memory, Allows 
trailing commas for 
function parameters. 

Added rest/spread 
properties, 
asynchronous 
iteraction, and 
promise.finally(), 
ReqExp 

String.trimstar() 
string.trimEnd() 
Array.flat(), 
object.fromEntries 
optional catch 
binding 

The Nullish 
Coalescring 
operator(??) 

ECMAScript 
(2018) 

ECMAScript 
(2019) 

ECMAScript 
(2020) 

Variable 

Variables are containers for storing data (storing 
data values.) 

Added "strict mode", 
JSOn support, 
string.trim(), 
Array.isArray() and 
Added Array 
iteration methods 
Allows trailing 
commas for object 
literals. 

Added let and const, 
default parameter 
values and Added 
Array.find(), 
Array.findIndex() 

Added exponential 
operator (**), 
Array.includes() 

Undefined

ES6 

ECMAScript 
(2015) 

ECMAScript 
(2016) 

Web Technology 

 148 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
BigInt–  JavaScript  BigInt  variables  are  used  to 
store  big  integer  values  that  are  too  big  to  be 
represented by a normal JavaScript number. 

Undefined–  A  variable  without  a  value  has  the 
value undefined. The type is also undefined. 

Null–  The  null  value  represents  the  intentional 
absence of any object value. It is treated as false 
for Boolean operations. 

 Regular Expression– A regular expression is a 
sequence  of  characters  that  forms  a  search 
pattern.  Regular  expressions  are  often  used  with 
the two string methods search() and replace(). 

The 

search()  method 

an 
expressions to search for a match and returns the 
position of the match. 

uses 

The 

replace()  method 

returns  a 

modified string where the pattern is replaced. 

Regular  Expression  Modifiers–  Modifiers  can 
be  used  to  perform  case  insensitive  more  global 
searches. 

Modifier  Description 

i 

g 

Perform case insensitive matching 

Perform  a  global  match(find  all 
matches rather than  stopping  after 
the first match) 

m 

Perform multiline matching. 

This Keyword 

The  this  keyword  refers  to  an    object.  Which 
object depends on how this is being invoked.  

Note–  This  is  not  a  variable.  It  is  keyword  you  can't 

change the value of this. 

Example–  

<html> 

<body> 

<p id="demo"></p> 

<script> 

const person = { 

firstName: "Rahul", 

lastName: "Kumar", 

id: 1001, 

fullName: function() { 

return this.firstName +" " + 

this.lastName; 

} 

}; 

document.getElementById("demo"). 

innerHTML = person.fullName(); 

Output– 

</script> 

</body> 

</html> 

Rahul Kumar 

Arrow Function 

Arrow function allow us to write shorter function 
syntax. 

let myFunction = (a, b) ⇒ a*b; 

Example– 

<html> 

<body> 

  <p id="demo"></p> 

<script> 

let hello = " "; 
hello = ( ) ⇒ { 
return "Hello World"; 

} 

document.getElementById("demo").innerHTML
= hello(); 

</script> 

</body> 

</html> 

Modules 

files  modules  are 

Modules  allow  you  to  break  up  your  code  into 
separate 
from 
external files with the import statement. And also 
rely on type = "module" in the <script> tag. 

imported 

Example– 

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

 
 
 
 
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
   
 
   
 
   
 
   
 
   
 
 
   
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Servlet Architecture– 

Execution of Servlets– 

1. The clients send the request to the web server. 

2. The web server receives the request. 

3. The  web  server  passes  the  request  to  the 

corresponding servlet. 

4. Servlet  process  the  request  and  generates  the 

response in the form of output. 

5. The servlet sends the response back to the web 

server. 

6. The web server sends the response back to the 
client  and  the  client  browser  displays  it  on  the 
screen. 

Applets 

An  Applet  is  a  java  program  that  can  be 
embedded into a web page. It runs inside the web 
browser  and  works  at  client  side.  An  Applet  is 
embedded in HTML page using the APPLET or 
OBJECT tag and hosted on a web server. Applet 
are used to make the website more dynamic and 
entertaining. 

Lifecycle of Applet 

When  an  Applet  begins,  the  following  methods 
are called in this sequence. 

1. init() 

2. start() 

3. paint() 

 150 

YCT 

Syntax– 

1. Export variable_name = value; 

2. Variable_name = value; 

 export {variable_name} 

Java 

corporation. 

Java  was  developed  by  James  Gosling  at 
SunMicro system in the year 1995, later acquired 
It 
simple 
by  oracle 
is 
programming 
is  an  object 
language.  Java 
oriented programming language  with its runtime 
environment.  It  is  combination  of  features  of  C 
and C++ with some essential additional concepts. 

a 

Servlets 

Servlet is a server side java program module that 

handles  client  requests  and 

implements 

the 

servlet  interface.  Servlets  can  respond  to  any 

type  of  request  and  they  are  commonly  used  to 

extend  the  application  hosted  by  web  servers. 

Servlet  is  a  web  component  that  is  deployed  on 

the server to create a dynamic page. 

Properties  of  servlets  are  as  follows–  Servlets 

work  on  the  server  side.  Servlets  are  capable  of 

handling  complex  requests  obtained    from  the 

web server. 

Web Technology 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
When  an  Applet  is  terminated  the  following 

sequence of method calls takes place. 

1. stop() 

2. destroy() 

init()– The init() method is the first method to be 

called.  This  is  where  you  should  initialize 

variables. This method is called only once during 

the run time of your Applet. 

start()– The start() method is called after init(). It 

is also called to restart an Applet after it has been 

stopped. 

paint()– The paint() method is used to paint the 

Applet. It provides graphics class object that can 

be used for drawing oval, rectangle, arc etc. 

stop()– The stop() method is called when a web 

browser  leaves  the  HTML  document  containing 

the applet, when it goes to another page. 

destroy()– The  destroy()  method  is  called  when 

the  environment  determines  that  your  Applet 

needs to the removed completely from memory. 

Python Programming 

Python is a general purpose, dynamic, high-level, 
and interpreted programming language.  
It  supports  an  Object  Oriented  programming 
approach to develop applications and   
It  is  used  in  web  development,  data  science, 
creating software prototypes, and so on. 
Fortunately  for  beginners,  Python  has  simple 
easy-to-use  syntax  and  this  makes  Python  an 
to  program  for 
excellent 
beginners. 

language 

learn 

to 

History of Python 

Python  was  created  by  Guido  van  Rossum,  and 
first released on February 20, 1991. 
The  name  of  the  Python  programming  language 
comes from an old BBC television comedy sketch 
series called Monty Python’s Flying Circus. 
Keywords in Python programming 
In  Python,  keywords  are  case  sensitive  and  they 
are  reserved  words.  That  means  we  cannot  use 
keywords as a variable or function. 
Keywords  are  used  to  define  the  syntax  and 
structure of the Python language. 
Following are some keywords available in Python 
programming language. 

There  are  two  standard  ways  to  run  an 

False  await 

Applet– 

1. Executing the Applet within a java compatible 

web browser. 

2. Using an Applet viewer.  

1.  Using  java  enabled  web  browser–  To 

execute  an  Applet  in  a  web  browser  we  have  to 

write  a  short  HTML  text  file  that  contains  a  tag 

that  loads  the  Applet.  We  can  use  APPLET  or 

OBJECT tag for this purpose. 

  <applet  code  =  "HelloWorld"  width  =  200 

height = 60> 

</applet> 

pass 
raise 
return 

else 
except 
finally 
for 
from 
global 
if 

import 
in 
is 
lambda 
nonlocal 
not 
or 

 None break 
True  class 
continue 
and 
as 
def 
assert  del 
async  elif 
try 
Note:- All the keywords except True, False and None are 
in lowercase and they must be written as they are. 

while 
with 
yield 

Python Identifiers 

An  identifier  is  a  name  given  to  entities  such  as 
class, functions, variables, etc. 
 It helps to differentiate one entity from another. 

Rules for Defining Identifiers 
1. An identifier cannot start with a digit. 

2.  Using  Applet  Viewer–  This  is  a  easiest  way 

For example-  

to  run  Applet.  To  execute  HelloWorld  with  an 

Applet viewer, you may also execute the HTML 

file shown earlier. 

a1( valid declaration) 
But 1a is not a valid declaration. 
2. Keywords cannot be used as identifiers. 

For example-  

If  the  preceding  HTML  file  is  saved  with 

assert = 1 

HelloWorld  html,  then  the  following  command 

line will run HelloWorld. 

appletviewer RunHelloworld.html 

3.  Special  symbols  such  as    !,  @,  #,  $,  %  etc. 
cannot be used as an identifier. 

For example-  

b$ = 3 

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

  a = 10 

print("Value of N_new:",N_new) 

print("datatype of N_new:",type(N_new)) 

After running the above code we get output as :- 

datatype of N_int: <class 'int'> 

datatype of N_float: <class 'float'> 

Value of N_new: 10.5 

datatype of N_new: <class 'float'> 

                     x = "welcome to  yct" 

Explicit Type Conversion 

                    print(a) 

                    print(x) 

Output–  

10 

                welcome to yct 

Data Type in Python 

Every  value  in  Python  has  a  data  type.  Since 
everything  is  an  object  in  Python  programming, 
data  types  are  actually  classes  and  variables  are 
instances (object) of these classes. 

Following diagram demonstrates the various types 
of data types in python programming language. 

In explicit type conversion, users convert the data 

type of an object to required data type and for that 

we  use  the  predefined  functions  such  as    int(), 

float(),  str(),  etc 

to  perform  explicit 

type 

conversion. 

Syntax– 

<required_datatype>(expression) 

For example– To add string and integer data types using 

explicit type conversion. 

a = 50 

b = “100” 

result1 = a + b 

b = int(b) 

result2 = a + b 

print(result2) 

Type Conversion in Python– 

The  process  of  converting  the  value  of  one  data 
type  such as (integer, string, float, etc.) to another 
data type is known as  type conversion. There are  
two types of type conversion. 

Implicit Type Conversion 

In Implicit type conversion, Python automatically 
converts one data type to another data type.  

For example– 

Converting integer to float- 

N_int = 5 

N_float = 5.5 

N_new = N_int + N_float 

print("datatype of N_int:",type(N_int)) 

print("datatype of N_float:",type(N_float)) 

Output– 

Traceback (most recent call last): 

File “”, line 1, in 

TypeError:  unsupported  operand  type(s)  for  +: 

‘int’ and ‘str’ 

150 

In the above example, variable a is of the number 

data type and variable b is of the string data type. 

When  we  try  to  add  these  two  integers  and  store 

the value in a variable named result1, a TypeError 

occurs  as  displayed  in  the  output.  So,  in  order  to 

perform  this  operation,  we  have  to  use  explicit 

type  casting.  As  we  can  see  in  the  above  code 

block,  we  have  converted  the  variable  b  into  int 

type and then added variables a and b. The sum is 

stored  in  the  variable  named  result2,  and  when 

printed it displays 150 as output, as we can see in 

the output block. 

Web Technology 

 152 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Python Namespace 

For example– 

A namespace is a collection of names and python 
implements namespaces as dictionaries. 
A namespace allows us to have unique names for 
each object  If we don’t know, this is just a quick 
reminder to tell us that strings, lists, functions, etc. 
everything in python is an object. 

In  other  words,  we  can  say  that  the  role  of  a 
namespace is like a surname. 

Namespaces are of basically three types:- 
1. Built-in Namespace– It  includes functions and 
exception names that are built-in in Python. 

2.  Global  Namespace–  It  includes  names  from 
the modules that are imported in the project. It is 
created  when  we  include  the  module  and  it  lasts 
until the script ends. 
3.  Local  Namespace–  It  is  created  when  the 
function is called and the scope ends when the value 
is returned. 

if...else Statement in python 

If statement 

Syntax–  

if test exp: 

 statement(s) 

if...else Statement 

Syntax– 
if test exp: 

  Body of if 

else: 

    Body of else 

if...elif...else 

Syntax– 
if test exp: 

    Body of if 

elif test exp: 

    Body of elif 

else:  

    Body of else 

Loop in Python Programming 

For loop– A for loop is used for iterating over a 
sequence (that is either a list, a tuple, a dictionary, 
, or a string). 

fruits = ["mango", "banana", "orange"] 

for x in fruits: 

  print(x) 

Output– 

mango 

               banana 

               orange 

While Loop– With the  help of while loop we can 

execute a set of statements as long as a condition 
is true. 

Syntax– 

while test_expression: 

 body of while 

For example– 

i = 1 

  while i < 5: 

  print(i) 

  i += 1 

Output– 

1 

2 

3 

4 

Break Statement in Python 

With the  help of break statement we can stop the 

loop even if the while condition is true. 

For example-   Exit the loop when i is 4. 

i = 1 

  while i < 8: 

  print(i) 

  if (i == 4): 

    break 

  i += 1 

Output– 

1 

2 

3 

4 

Pass Statement in Python 

In  Python  programming,  the  pass  statement  is  a 

null statement. It is generally used as placeholder. 

Syntax– 

pass 

 153 

YCT 

Syntax–  

             for val in sequence: 

                 loop body 
Web Technology 

 
 
 
 
 
 
 
 
 
 
 
 
                
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
                
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Errors and Exceptions in Python 
Syntax  Errors–    when  error  caused  by  not 

Example– 

tuple = ("Rahul", "Yct", "Raj") 

print(tuple) 

following  the  proper    syntax  of  the  language  is 

Output– ("Rahul", "Yct", "Raj") 

called syntax error or parsing error. 

Exceptions–  when  errors    occurring  at  runtime 

(after  passing 

the  syntax 

test)  are  called 

exceptions or logical errors. 

List 

List  are  used  to  store  multiple  items  in  a  single 

variable. List are created using square brackets. 

List  items  are  ordered,  changeable  and  allow 

duplicate values. And list first item has index [0] 

and second item has index [1]. 

Example– list = ["Rahul", "Raj", "Kumar"] 

print(list) 

Output– ['Rahul', 'Raj', 'Kumar'] 

List Methods 

Method 

count() 

Tuple Methods 

Description 

Return  the  number  of  times  a 

specified value occurs in a tuple 

index() 

Searches  the  tuple  for  a  specified 

value  and  returns  the  position  of 

where it was found 

Set–  Sets  are  used  to  multiple  items  in  a  single 
variable  and  it  is  collection  which  is  unordered, 
unchangeable and unintexed sets are written with 
curly brackets. Sets can't allow duplicate value. 

Example– 

theset = {"Rahul", "Kumar", "Raj" "Rahul") 

Method 

Description 

Output– 

append() 

Adds an element at the end of the 

print(theset) 
("Kumar", "Raj", " Rahul") 

Set Methods 

list 

Method 

Description 

clear() 

Removes all the element from the 

list 

copy() 

count() 

Returns a copy of the list 

Returns  the  numbers  of  element 

with the specified value 

add() 

clear() 

copy() 

Adds an element to the set 

Remove  all  the  elements 

from the set 

Returns a copy of the set 

index() 

Returns  the  index  of  the  first 

difference() 

Returns a set containing the 

element with the specified value 

difference  between  two  or 

more sets 

insert() 

Adds  an  element  at  the  specified 

position 

pop() 

Removes 

the  element  at 

the 

specified 

differecne_update() 

Remove  the  items  in  this 

set that are also included in 

another, specified set 

remove() 

Removes 

the 

item  with 

the 

pop() 

Removes  an  element  from 

specified value 

the set 

reverse() 

Reverses the order of the list 

remove() 

Remove 

the 

specified 

sort() 

Sorts the list 

element 

Tuple– Tuples are used to store multiple items in 

union() 

Return a set containing the 

a single variable. A tuple is a collection which is 

ordered and unchangeable and tuples are written 

with round brackets. Tuple items are indexed the 

first item has index [0] and second index[1]. 

union of sets 

update() 

Update  the  set  with  the 

union of this set and others 

Web Technology 

 154 

YCT 

 
 
 
 
 
 
   
 
 
 
   
 
 
 
   
Dictionary–  Dictionaries  are  used  to  store  data 

value in  key  value pairs. It is  written  with curly 

brackets.  A  dictionary  is  a  collection  which  is 

ordered, changeable and is not allow duplicates. 

Array 

An  array  is  a  special  variable  which  can  hold 

more than one value at a time. In order to create 

Python  arrays.  You  will  first  have  to  import  the 

Example– 

thedict={"brand": "Ford",  

  "Model":" Mustang",  

  "year": 1954 

  } 

print(thedict) 

Output–  {'brand':  'Ford',  'Mode':  'Mustang',  'year'  " 

1954} 

Dictionary Method 

Method 

Description 

array module. 

Array Import 

Using  import  array  at  the  top  of  the 

file.  You  would  then  go  to  create  an 

array using array.array(). 

Instead of having to type array.array() 

all the time, use import array as arr at 

the top of the file or arr.array(). 

Use 

from  array 

import*  with* 

importing 

all 

the 

functionalities 

clear() 

copy() 

get() 

items() 

keys() 

pop() 

Removes  all  the  elements 

from the dictionary 

Returns  a  copy  of 

the 

dictionary 

Returns  the  value  of  the 

specified key 

Returns a list containing a 

tuple  for  each  key  value 

pair 

available. 

Example–  

import array as arr 

numbers = arr.array('i', [10, 15, 20]) 

print(numbers) 

Output– 

array('i',[10, 15, 20]) 

Methods of array 

Returns  a  list  containing 

Method 

Description 

the dictionary's keys 

append() 

Adds an element at the end of the list. 

Removes the element with 

clear() 

Removes all the elements from the list. 

the specified key 

copy() 

Returns a copy of the list. 

popitem() 

Removes  the  last  inserted 

count() 

Returns the number of element with the 

key value pairs 

specified value. 

update() 

Updates 

the  dictionary 

with 

the  specified  key-

value pairs 

values 

Returns  a  list  of  all  the 

values in the dictionary 

setdefault() 

Returns  the  value  of  the 

specified  key.  If  the  key 

does  not  exist,  insert  the 

key  with 

the  specified 

index() 

Returns  the  index  of  the  first  element 

with the specified value. 

insert() 

Adds  an  element  at 

the  specified 

position. 

pop() 

Removes  the  element  of  the  specified 

position. 

remove() 

Removes 

the 

first 

item  with 

the 

specified position. 

value 

reverse() 

Reverses the order of the list. 

Web Technology 

 155 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Module 

RegEx in Python 

A module to be the same as a code library. A file 

A  regular  expression  is  a  sequence  of  characters 

containing a set of  function  you  want to include 

that  defines  a  search  pattern.  A  pattern  defined 

in your application. A file with the file extension 

using  RegEx    can  be  used  to  match  against  a 

.py.  

How to use Module and Variable– The module 

we  just  created  by  using  the  import  statement. 

Module  create  variables  of  all  types  (arrays, 

dictionaries, objects). 

Example– 

file name mymodule.py  

  company={ 

"Name": "Yct", 

"Model": 1993, 

"City": "Prayagraj" 

} 

string. 

Iterators in Python– 

An  iterator  is  an  object  that  implements  the 

iterator  protocol.  In  other  words,  an  iterator  is  an 

object that implements the following methods: 

__iter__ - It returns the iterator object  itself. 

__next__ - It returns the next element. 

 Generators in Python– 

Python  generators  are  a  simple  way  of  creating 

iterators. 

A  generator  is  a  special  type  of  function  which 

does  not  return  a  single  value,  instead,  it  returns 

an iterator object with a sequence of values. 

In  a  generator  function,  a  yield  statement  is  used 

So,  import  the  module  named  my  module  and 

rather than a return statement.  

access the company. 

import mymodule 

x= mymodule.company["model"] 

print(x) 

Output– 1993 

File Handling in python 

Python  has  a  number  of  functions  for  creating, 

reading,  updating,  and  deleting  files.  The  key 

function  for  working  with  files  in  Python  is  the 

open()  function.  The  open()  function  takes  two 

Exception Handling in Python 

When  exceptions  occur,  the  Python  interpreter 

stops  the  current  process  and  passes  it  to  the 

calling process until it is handled. If not handled, 

the  program  will  crash.  These  exceptions  can  be 

handled using the try statement. 

parameters; filename, and mode. 

                 f = open(filename, mode) 

There are four different modes for opening a file:- 

"r" - Read - Opens a file for reading 

"a" - Append - Opens a file for appending  

"w" - Write - Opens a file for writing 

"x" - Create - Creates the specified file 

Web Technology 

 156 

YCT 

 
 
 
 
 
 
 
   
 
   
 
   
 
   
 
 
 
   
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   12.     SOFTWARE ENGINEERING 

Software Development Life Cycle 
(SDLC) 

delivery life cycle since this is the part where the 

team  estimates 

the  cost  and  defines 

the 

SDLC  is  a  process  followed  for  a  software 

requirements of the new software. 

project,  within  a  software  organization.  It 

Stage 2 

consists  of  a  detailed  plan  describing  how  to 

Analysis–Analyzing  maximum 

information 

develop,  transit,  replace,  maintain  and  alter  or 

from  the  client  requirements  for  the  software, 

enhance particular software. 

the 

team  has 

to  discuss  each  details  and 

SDLC defines a methodology for improving the 

specification  of  the  product  with  the  customer 

quality of software and the overall development 

and  then  analyze  the  requirements  keeping  the 

process. 

design code of the software in mind. 

Graphical representation of the various stages 

Stage 3 

or steps of a typical SDLC: 

Designing–  In  this  stage,  Developers  will  first 

(cid:1) 

(cid:1)  

outline  the  details  for  the  overall  application  as 

input and software architecture of the end user. 

Designing helps the overall system architecture. 

It serves as input for the next phase of the model 

such as user interface, system interface, network, 

and network requirements and database. 

 In  designing  phase,  there  are  two  kinds  of 

design documents:- 

The  SDLC  is  a  structured  process  that  enables 

the production of high-quality, low-cost software 

in  the  shortest  production  time.  The  goal  of  the 

SDLC is to produce superior software that meets 

and  exceeds  all  customer  expectations  and 

demands, 

by 

the 

following 

of 

above 

stages/steps:- 

Stage 1 

Planning–  Project  planning  is  all  about  "What 

do  we  want?"  It  is  vital  role  in  the  software 

Stage 4 
Building  or  Developing–  In  this  stage,  the 

actual  development  starts  and  the  product  is 

built. If the design is performed in a detailed and 

organized  manner,  code  generation  can  be 

accomplished  without  much  hassle.  Hence, 

programming  code  is  generated  as  per  DDS 

during this stage. 

Software Engineering  

157 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Stage 5 

Coding or Implementation– Coding starts once 

the  developer  gets  the  design  document.  The 

software design is translated into source code. It 

means  translating  the  design  to  a  computer-

legible  language.  File  conversion,  user  training, 

and new changes to the system are belong to this 

stage/phase. 

Stage 6 

Testing–  Testing  is  done  by  testing  team  to 

verify that the functionality of entire application 

works  according  to  the  customer  requirements. 

By  finding  some  bugs/defects,  the  team  fixes 

them  and  sends  back  for  a  re-test.  This  process 

continues  until  the  software  is  bug-free,  stable 

Waterfall  Model–  It  is  linear  and  straight-

and  working according  to the business  needs of 

that system. 

Stage 7 

Deployment  or 

Installation–  Product 

is 

deployed  in  the  production  environment  or  first 

UAT  (User  Acceptance  Testing)  depending  on 

the  customer  expectation,  then  based  on  the 

feedback given by the project manager, the final 

software is released and checked for deployment 

issues if any. 

Stage 8 

Maintenance–  If  any 

issue  comes  up 

in 

forward  and  requires  development  teams  to 
finish one phase of the project completely before 

moving on the next.  

Hence,  the  outcome  of  one  phase  acts  as  input 
for the next phase. This model is not suitable for 

accommodating projects. 

Example– 

Requirements

Specification

Design

Evaluation

Testing

Iterative Model– This model focuses or stresses 
on  repetition  and  repeat  testing.  Developers 

create  a  version  rapidly  for  relatively  less  cost, 
then  test  and  improve  it  through  successive 

deployment  phase  and  needs  to  be  fixed  or  any 

enhancement,  it  is  taken  care  by  the  developers 

versions. 
Example– 

by  using  following  three  activities,  because 

maintenance  phase  of  SDLC  is  most  effected 

during costly faults is introducing: 

Software Engineering  

158 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
 
 
Spiral Model– Spiral model starts with analysis. 

Example– 

This  model 

is  flexible  compared 

to  other 

methodologies.  Projects  pass  through  four  main 

phases again and again in a metaphorically spiral 

motion.  It  is  a  risk-driven  process  model.  It 

resembles  in  its  emphasis  on  repetition  and 

project  risk  factor 

is  considered  which 

is 

inefficient 

for  smaller  projects.  Until 

the 

software retires, it will continue. 

Example–  

Spiral model has four phases:- 

         Agile  Model–  It  is  a  group  of  Iterative  and 

incremental model. In this model, any product is 

broken  into  small  incremental  builds  as  this 

model focuses more on flexibility rather than on 

requirement while developing any product. New 

features can be added easily in this model. 

Agile  does  not  rush  the  team  to  deploy  the 

product  to  customers  but  to  perform  testing  at 

the end of each sprint. 

V-Model–  This  model 

is  also  known  as 

verification and validation  model. In this model, 

verification  and  validation  goes  hand-in-hand 

i.e.  development  and  testing  goes  parallel  as  it 

includes  tests  at  each  stage  of  development.  V-

model joins by coding phase.  

Example– 

Example– 

Prototype Model–  In  this  model,  the  prototype 

is  developed  prior  to  the  actual  software.  This 

model  has  limited  functional  capabilities  and 

inefficient  performance  when  compared  to  the 

actual  software.  It  gets  the  valuable  feedback 

from  the  customer.  Feedbacks  are  implemented 

and  the  prototype  is  again  reviewed  by  the 

customer for any change. 

Software Engineering  

159 

YCT 

 
        
 
 
 
 
 
 
 
 
 
 
                   
 
         Big  Bang  Model–  This  model  is  used  for 

Money  and  efforts  are  put  together  as  the  input 

smaller  projects  and  experimental  life  cycle 

and output come as a developed software which 

designed  to  inform  other  projects  within  same 

might  be  or  might  not  be  the  same  as  the 

company. 

requirements of customer, in this model. 

Software Metrics: Software Project 

Management 

Software  Metrics-  It  is  standard  measurement 

for  the  estimation  of  quality,  progress,  health 

and testing of software characteristics which are 

This  model  is  flexible  because  it  doesn't  follow 

any  rigorous  procedures  or  processes.  It  starts 

measurable  or  countable  and  quantifiable.  It 

with  little  planning  and  moves  to  the  coding 

includes  measuring 

software  performance, 

stage  because  it  does  not  have  requirements  of 

planning  work  items,  productivity  and  many 

much scheduling and planning. 

other uses. 

Classification of software Metrics 

Software Engineering  

160 

YCT 

 
 
       
 
 
 
 
 
M

C

by gathering

.

In order to
p

.

Software Engineering  

161 

YCT 

 
 
 
If anyone wants to get the percentage of the test cases, the following formula can be useful;- 

Sr. No. 

Percentage (%) of 

Formula 

Formula for Test metrics 

1. 

2. 

3. 

4. 

5. 

6. 

7. 

8. 

9. 

Test cases executed 

Test case effectiveness 

Passed test cases 

Failed test cases 

Blocked test cases 

Fixed defects 

Rework effort ratio 

Accepted defects 

Defects deferred 

No. of test cases executed

Total no. of test cases

×

100

No. of detected defects

No. of running test cases

×

100

Total no. of test run

Total no. of test executed

×

100

Total no. of failed test cases 

Total no. of test executed

×

100

Total no. of blocked tests

Total no. of test executed

×

100

Total no. of  flaues fixed

No.of defects reported

×

100

Actualrework efforts

Totalactualefforts

×

100

Defects accepted

Total defects

×

100

Deferred defects for future use

Total defects reported

×

100

Let's take an Example to Calculate Test Metrices 

Sr. No. 

Testing Metrics 

Data retrieved while developing 
test cases 

1. 

2. 

3. 

4. 

5. 

6. 

7. 

8. 

9. 

10. 

11. 

12 

No. of requirements 

No. of test cases 

Total no. of test cases 

Total no. of test cases executed 

No. of passed test cases 

No. of failed test cases 

No. of blocked test cases 

No. of unexecuted test cases 

Total no. of defected test cases 

Accepted defects 

Defects deferred for future use 

Fixed defects 

5 

40 

200 

164 

100 

60 

4 

36 

20 

15 

5 

12 

Software Engineering 

162 

YCT 

 
 
 
 
 
  
 
 
 
 
Solution for the above example is written below:- 

Software Project Management (SPM) 

Project- A project is a collection of tasks as inputs and 

outputs  needed  to  achieve  a  particular  goal  while  a 

software  project  is  the  complete  procedure  of  software 

Software  Project  Management-  It  is  a  proper  way  of 

planning,  leading,  execution,  supervision  and  control  of 

software  project.  It  is  also  a  discipline  and  skill  for 

organizing  and  managing  software  projects.  It 

is 

necessary  to  incorporate  user  requirements  along  with 

development. 

budget and time constraints. 

Software Engineering 

163 

YCT 

 
 
 
 
 
Software Engineering 

164 

YCT 

 
 
 
 
 
 
Software 

following them any organization can protect the integrity 
of the software.  
Needs/Requirements 
Project 
of 
Management–  For  any  software  organization  while 
staying  within the customers  budget and completing  the 
product  on  time,  delivering  a  high-quality  product  is  an 
essential part. time, cost and quality are the triple factors 
of  many  factors  including  both  internal  and  external 
which may impact the other two. 

The  above  list  of  focus  areas  that  can  tackle  the  broad 
upsides  of  the  software  project  management  and  by 

Down sides of Software Project Management 

If  one  wants  to  engage  software  project  management 

technique  to  put  in  place,  these  initiatives  can  be  costly 

and  time  consuming.  One  could  need  instruction  since 

one's  team  will  also  be  utilizing  them.  A  project  may 

need  help  of  professional  or  subject  experts  depend  on 
situation. 
It is multi-step difficult procedure tending to complicate 

things excessively which may lead to provide confusion 

among team. Project having a larger scope especially if it 

doesn't have a dedicated team. 

A project manager is a person who 

makes  both 

large  and 

small 

projects  and  all  types  of  decisions 

and  is  responsible  for  planning, 

designing,  monitoring,  controlling, 

executing and closure of a project. 

For  the  software  project  management,  when  we  hire 

individuals, new hires join our company with or without 

having  company's  culture  then  they  can  be  kept  at 

workforce as small as possible. Resulting that the cost of 

Role of a Project Manager 
1.   As  a  leader  –  What  the  team  is  expected  is  leaded 
and guided by a project manager by providing them 
direction to make them understandable. 

communication tends to soar. 

Sometimes.  project  managers  provide  little  or  no  space 

for creativity. To initiate rigid standard, the team leaders 

either put  much focus on  management or put strict time 

on  staff,  or  encourage  creativity.  That  is  why  an 

organization  can  build  and  ship  code  quickly  else  it 

opens up new doors to achieve more objectives. 

2.   As  a  medium  –  A  project  manager  may  be  a 
if  he 
medium  between  his  clients  and 
coordinates 
related 
transfers 
information  from  clients  to  his  team  and  reports  to 
the senior management. 

team 
all 

them 

and 

3.   As a team motivator – To encourage team member 
to  work  properly  for  the  successful  completion  of 
the project. 

Software Engineering 

165 

YCT 

 
 
         
 
 
 
 
 
 
4.   As a team organizer – To organize teams to deliver 

4.   Managing Project Risk – The  following risks in a 

on  an  outcome  such  as  functions,  structure  and 

project  consist  of  all  activities  like  monitoring, 

communications etc. 

analyzing, preparing and identification of the plan:- 

5.   As  a  mentor  –  A  team  must  have  an  attachment 

(cid:1)  The  experienced  team  (staff)  leaves  the  project  and 

guided  by  a  mentor  to  his  team  at  each  step  to 

the new team joins it. 

provide a recommendation in the right direction. 

(cid:1)  Changes 

in 

organization, 

requirements, 

technologies, environment, business competition and 

misinterpreting needs. 

5.   Managing  Scheduling  –  It  refers  to  roadmap  with 

specified  order  within  time  slot  allotted  to  each 

activity.  It  defines  various  tasks,  milestones  and 

arrangement by keeping many factors in mind. 

(cid:1)   It is necessary to find out multiple tasks, break down 

them 

into  smaller,  and  manageable  modules, 

estimate time frame for each task, calculate the total 

time from start to finish, etc. 

6.   Managing  Project  Communication  –  Effective 

communication  from  planning  to  closure  in  the 

1.   Planning  and  Tracking  Project  –  Planning  and 

success of a project, it plays a vital role and bridges 

tracking projects are multiple processes or tasks that 

gap between clients, team members, organizations as 

are executed before the construction of the software 

well  as  other  project  creator  or  developer  by 

product starts, by managing project resource. 

following  many  steps 

like  planning,  sharing, 

2.   Managing Scope – Scope management avoids price 

feedback and closure. 

and time overrun and clearly defines what would do 

7.   Managing Configuration – It controls the changes 

and what would not. 

in  software 

like  need,  design,  functions  and 

3.   Managing Estimation – It figures out the size (line 

development 

of 

the 

project.  Configuration 

of code), efforts, cost as well as time. 

management is needed because several people work 

(cid:1)   The line of code depends on the users or their needs. 

on  software,  help  to  build  coordination  between 

(cid:1)   By  the  help  of  efforts,  a  developer  can  quickly 

suppliers,  run  on  multiple  systems,  change  in  need, 

estimate  how  big  team  are  needed  to  inform  the 

budget,  schedule,  etc.  by  performing  many  tasks 

software. 

including  identification,  base-line,  change  control, 

(cid:1)   The  time  can  be  easily  determined  when  size  and 

status accounting, audits and reviews. 

efforts are estimated. 

         Baseline  defines  completeness  of  a  phase,  change 

(cid:1)   Cost 

includes 

size, 

quality, 

hardware, 

control ensures all changes made to software system 

communication,  training,  licenses,  tools  and  skilled 

by  using  many  steps  like  identification,  validation, 

manpower. 

analysis, control, execution and close request. 

Software Engineering 

166 

YCT 

 
 
There are two broadly recognized techniques:- 

Project Estimation Techniques 

Decomposition Technique 

Empirical Estimation Technique 

It  Assumes  the  software  as  a  product  of  various 

It  uses  derived  formula  to  make  estimation  based  on  LOC 

compositions. It has two main model. 

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

Difference between COCOMO-1 and COCOMO-2 

COCOMO-1 

COCOMO-2 

It provides estimates of effort and schedule. 

It  provides  the  estimates  that  represent  one  standard 

deviation. 

It  is  useful  for  waterfall  model  of  SDLC  (Software 

It is useful in non-sequential, rapid development. 

Development Life Cycle). 

It is based on linear reuse formula. 

It is based on non-linear reuse formula. 

Effort  exponent  is  determined  by  3  development 

Effort exponent is determined by 5 scale factors. 

models. 

Size  of  software  stated  in  terms  of  lines  of  code 

Size  of  software  stated  in  terms  of  object  points  (OPs), 

(LOC). 

Function Points (FPs) and Line of Code (LOC). 

Software Engineering 

167 

YCT 

 
 
 
COCOMO Model in Brief –  
(cid:1)  Cost estimation model developed by Boehm in 1981. 
(cid:1)  Regression model based on LOC (no of Lines of Code) 
(cid:1)   Predicts the effort (E) and schedule (D) of product based on size of software. 
(cid:1)  A  cocomo  model  addresses  the  area  of  application  composition  model,  early  design  state  model  and  Post 

architecture model. 

Based on size 

(i)  Organic            1. Basic COCOMO Model 

Example- Data processing, Inventory management system etc. 

(ii)  Semi-Detached  2. Intermediate model 
Example- OS, DBMS, etc. 

(iii) Embedded        3. Detailed or Complete Model 
Example- ATM, Air Traffic Control, etc. 

Intermediate  model  is  an  expansion  of  basic  cocomo  model  while  complete  cocomo  model  is  an  expansion  of 

intermediate cocomo model. 

Basic model 
E=a1(KLOC) a2 P.M 

KLOC model 

(2-50) Organic 

(1) 

D=b1 (E)b2  M 

(50-300) Semi-detached 

Productivity=

KLOC

E

(>300) Embedded 

Where E=effort, D=development time. 

a1 

2.4 

3.0 

3.6 

a2 

1.05 

b1 

2.5 

b2 

0.38 

1.12 

2.5 

0.35 

1.2 

2.5 

0.32 

Intermediate model 

E=a1(KLOC)a2 * EAF 
(Effort Adjust Factor) 

D=b1Eb2 

(2) 

Model 

(Attribute) 

15 Cost Drivers 

Product 

RELY, DATA, CPLX (Complexity) 

Project 

System 

MODP, TOOL, SCED 

TIME, STOR, VIRAT, TURN 

Personnel 

ACAP, AEXP, PCAP, VEXP, LEXP 

Software Engineering 

168 

YCT 

 
 
 
 
 
 
 
 
 
 
 
Example–  1=> 

Solution- The  most appropriate  mode  for 200 KLOC is 

       Suppose  a  project  was  estimated  to  be  400  KLOC. 

semi-detached mode. 

Calculate the effort and development time for each of the 

 Hence, E=3.0(200)1.12=1133.12 PM 

three models i.e., organic, semi-detached and embedded. 

             D=2.5(1133.12)0.35=29.3 PM 

Average staff size (ss) = 

E
D

Persons.

1133.12

         =

29.3

=

38.67 Persons.

Productivity

=

KLOC

E

200

1133.12

=

=

0.1765 KLOC / PM

               Productivity = 176 LOC/PM 

The  following  figure  shows  a  plot  of  estimated  effort 

versus product size. 

Solution- 

(i) 

 Organic mode, 

E=a1*(KLOC)a2  PM 

E=2.4 *(400)1.05=1295.31 PM 

D=b1(E)b2.M 

D=2.5*(1295.31)0.38=38.07 PM 

(ii)  Semi-detached mode, 

E=3.0*(400)1.12=2462.79 PM 

D=2.5*(2462.79)0.35=38.45 PM 

(iii) Embedded mode, 

E=3.6*(400)1.20=4772.81 PM 

D=2.5*(4772.8)0.32=38 Pm 

Example– 2=> 

A  project  size  of  200  KLOC  is  be  developed.  The 

team  has  average  experience  on  similar  type  of  project. 

The  Project  schedule  is  not  very  tight.  Calculate  the 

effort,  development 

time,  average  staff  size  and 

productivity of the project. 

Software Engineering 

169 

YCT 

 
 
 
 
 
 
 
            
 
 
PUTNAM Model in Brief 

Putnam Stated that Rayleigh-Norden curve that can be 
used to relate the number of delivered lines of code to the 
effort and the time needed to develop the product. 
The Putnam expression is 

L=CkK1/3td

4/3 

Ck = Constant  

    2 poor software dev. environment 
    8 good  
    11 excellent  

or K=

3

4

3
K / C td  
k
or K=C/td4 

For the same product size, c=L3/Ck3 is a constant 

or 

K
K

1

2

=

4
t d

/ 4
t d  
1

2

or 

4

∝

K 1/ t d
d1/ t∝

or  Cost   

Where K=total effort expended in PM 

            L=Product size in KLOC 

            td=time expended (development time) 

(cid:1)  According  to  the  Putnam,  project  effort  is  inversely 
proportional  to  the  fourth  power  of  the  development 
time. E = K/(TD**4) 
This formula predicts zero effort for infinite development 
time. 

Gantt Chart 
       It shows the project schedule with respect to time period which was devised by Henry Gantt in 1917. It is also 
known as a horizontal bar chart which represents activities and time schedule for the project. 

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

End 

Week1 

Week3 

Week6  

Week7 

Week10 

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

Time Estimates (in weeks) 

       Pert  stands  for  Project  Evaluation  and  Review 

Technique. Its  main objective is the analysis through its 

three  time  values  associated  with  each  activity.  These 

Activity 

Preceding 
Activity 

Optimistic 
time  
(to) 

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

Most 
likely 
time 
(tm) 
4 

12 

9 

15 

7.5 

9 

3.5 

Pessimistic 
time  
(tp) 

12 

26 

10 

20 

11 

9 

7 

A 

B 

C 

D 

E 

F 

G 

None 

None 

A 

A 

A 

B, C 

D 

2 

10 

8 

10 

7 

9 

3 

5 

5 

5 

E, F, G 

H 
(i)  Determine the critical path. 
(ii)  Draw the pert network 
(iii) Prepare the activity schedule 
(iv) What  is  the  probability  that  the  project  will  be 
finished  within  the  time  limit  if  a  30  week 
deadline is imposed? 

Solution– The shortest time and variance of each activity 
is  computed  by  the  following  formula  for  the  given 
network data-  

te = 

to

+

+
4tm tp

6

and

σ

=

−
(tp to)

2

36

Variance (σ)=> It is the variance of activity given by the 

following formula:- 

2
σ =

[

−
(tp to) / 6

2

]

=

2

−
(tp to)
36

Example– 

       The  following  characteristics  have  eight  activities 

(A, B, C, D, E, F, G and H) of a small project:- 

teof A

=

teof B

=

teof C

=

teof D

=

teof E

=

teof F

=

+ × +
2 4 4 12

6

=

30

6

=

5

10 4 12 26

+ ×

+

6

+ × +
8 4 9 10

6

=

10 4 15 20

+ ×

+

6

7 4 7.5 11

+ ×

+

=

84

6

=

14

54

6

=

=

9

90

6

=

15

=

48

6

=

8

6

+ × +
9 4 9 9

6

=

54

6

=

9

Software Engineering 

171 

YCT 

 
 
 
 
 
  
 
 
 
(cid:1)   The  critical  path  of  the  project  is  1-2-3-4-5-6, 

critical  activity being A ,D ,G and H. 

(cid:1)   The expected project is the sum of duration of each 

critical activity =5+15+4+5=29 weeks. 

   Variance of project= 

25

9

+

25

9

+

4

9

+ =  
6

0

       Software design is a process or mechanism in which, 
using  a  set  of  primitive  components  and  subject  to 
constraints,  any  agent  can  create  a  specification  of  a 
software  artifact  to  fulfill  goals  and  can  transform  user 
requirements  into  some  suitable  form  to  help  the 
programmers  in  coding  and  implementation.  Software 
design  usually  involves  problem  solving  and  solution 
planning.  It  has  above  many  design  mainly 
the 
following:- 

teof G

=

teof H

=

3 4 3.5 7

+ ×

+

6

+ × +
5 4 5 5

6

=

24

6

=

4

=

30

6

=

5

σ

of A

=

σ

of B

=

2

−
(12 2)
36
−
(26 10)
36

=

2

=

100
36
256
36

25
9
64
9

=

=

σ

of C

=

σ

of D

=

σ

of E

=

σ

of F

=

σ

of G

=

σ

of H

=

2

2

−
(10 8)
36
−
(20 10)
36
−
(11 7)
36
−
(9 9)
36
−
(7 3)
36
−
(5 5)
36

=

2

2

=

=

2

4
36

=

1
9
100
36

=

=

25
9

=

16
36

=

4
9

=

0
36
16
36
0
36

=

0

=

4
9

=

0

Activity 

σ 

Earliest Time 

Latest 
Time 

Start  Finish  Start  Finish 

A 

B 

C 

D 

E 

F 

G 

H 

25/9 

64/9 

1/9 

25/9 

4/9 

0 

4/9 

0 

0 

0 

5 

5 

5 

14 

20 

24 

5 

14 

14 

20 

13 

23 

24 

29 

0 

1 

6 

5 

16 

15 

20 

24 

5 

15 

15 

20 

24 

24 

24 

29 

Correctness-  As  per  the  need  of  the  user,  software 
design should be correct. 
Completeness-  The  design  should  be  complete  like 
modules, external interfaces and data structures.  
Flexibility-  As  per  the  need,  it  should  be  flexible  to 
modify or alter. 
Efficiency- All resources should be used by the program 
with efficient. 
Consistency- The consistency should be maintain in the 
design. 
Maintainability-  The  design  should  be  so  simple  in 
order  that  it  can  be  easily  maintainable  by  other 
designers. 

Software Engineering 

172 

YCT 

 
 
 
         
 
        
 
 
 
 
 
Software Design Levels / Metrics 

       There are many software design levels of  which we 
can divide into three main categories. These are;- 

Architectural  Design-  This  first  level  design  is  highest 
summarize  edition  of  the  system  that  determines  the 

software or application as a method with more elements 
interactive with each where the designers obtain the idea 

or thought of a suggested domain or province. It chooses 

the overall structure and ignores the internal details. 
High-Level Design- This second level design represents 
multiple components and cooperation with each. It is an 

identification of modular arrangement, different modules 
and  relationship  among  them.  This  design  also  defines 

the interface among each  module. High Level Design is 
also  known  as  preliminary  design  like  a  tree  diagram 

called the structure chart.  
Detailed Design- This third level design determines the 
logical  structure,  data  structure  and  algorithms  of  the 

different  modules  in  comparison  to  previous  module 

designs  and  implementations.  The  accomplishment  part 
which will be finally seen by the system, dealt with this 

detailed design.    

Function Oriented Design 
      How  the  module  should  be  interconnected  and 
the  system  based  on  SRS  (Software 
needed  for 

Requirement  Specification)  are  focused  by  the  function 
oriented design. In this approach or method, the design is 

decomposed  into  a  set  of  interacting  units  which  have 

clearly defined by the following categories:- 

Object Oriented Design 

Objects-  It  inherits  a  class's  attributes  and  operations 
involved  in  solution  design.  For  an  instance,  banks, 

company, person and users are considered as objects. 

Classes- These are generic descriptions of objects which 

are  class  instances  that  define  all  the  properties  and 

methods.  A  Class  encapsulates  the  data  and  procedural 

abstractions  described  by  attributes.  A  super  class  is 

generally a set of classes from where both attributes and 

operations can be inherited by a sub class. 

Messages-  Massages consist of the integrity of the goal 

object that is the name of requested operation and action 

needed  to.  complete  the  function.  All  objects  are 

communicated by massage passing. 

Abstraction-  Abstraction  handles  the  complexity  in 

object  oriented  design.  It  is  also  the  removal  of  the 

unnecessary and amplification of the essentials. 

Encapsulation-  Encapsulation 

is  also  known  as 

information  hiding  concept  or  concealing.  The  data  and 

operations are tied to a single unit. It not only bundles or 

groups a vital information of an object together but also 

restricts  access  to  the  operation,  method  and  data  from 

the out access to the operation, method and data from the 

outsider world. 

Inheritance-  To be staked hierarchically, OOD permits 

similar  classes,  where  lower  or  sub  classes  can  be 

implemented,  imported,  reused  variables  and  functions 

from 

their 

immediate  super  classes.  This  OOD's  

characteristics  is  called  an  inheritance  because  it  makes 

its easier to define and create a specific and generalized 

classes respectively. 

Polymorphism-  Polymorphism provides a program the 

ability  to  redefine  techniques  for  derived  classes.  It 

        Object  Oriented  Design  (OOD)  is  the  process  in 

permits  a  specific  routine  to  uses  different  types  of 

which  the  system  is  viewed  as  a  group  of  entities  or 
objects.  This  process  permits  the  creation  of  a  software 

variables at different times. Polymorphism is a  feature / 

technique or mechanism where similar tasks or functions 

solution  based  on  object  notion.  Each  object  handles  its 

performed depending.   

state data among them, and responsible for its own data. 
In other words, every object belongs to a class. 

upon  how  the  service  is  invoked,  then  the  respective 

portion of code gets executed. 

Software Engineering 

173 

YCT 

 
 
 
 
 
 
 
 
User Interface Design 

       The user interface is the frontend application view or 

the  visual  part  of  an  application  or  operation  system 

through  which  any  user  interacts  with  a  computer  or 

software  in  order  to  use  software.  How  commands  are 

given  to  computer  or  software  and  how  data  are 

displayed  on  the  screen  are  determined  by  interface 

design which is mainly of two types:-  

Text Based User Interface or Command 

Line Interface 

(cid:1)  By  using  coding  standards,  our  code  will  be  easily 
understandable, easy debugging, error-free according 

to needs. 

The coding standards are the  guidelines or rules how  to 

write 

the  code  so 

that  overall  coding  becomes 

understandable. 
(cid:1) The programmer should use- 

→ Less global variable 

→ Exception handling mechanism 

→  Naming  convention  for  global  and  local 

variable or constant. 

        It provides a command prompt, where the user types 

→ Comments for better understanding. 

the  predefined  commands  in  their  syntaxed  order.  The 

predefined  commands  are  needed  to  be  remembered  by 

the  users.  It  is  also  known  as  Command  User  Interface 

(CUI). 

→ Maximum 1 to 20 line of code in a phase. 

→ Very clever or easy code. 

→ Different identifier for multiple purpose. 

→  Name  of  variable  and  method  not  in  short 

  Graphical User Interface 

form. 

       It  provides  the  simple  interactive  interface  to  the 

users  to  interact  with  the  system.  Using  GUI,  users 

interpret  the  software    because  GUI  can  be  a  group  or 

combination of both hardware and software. 

Coding and Testing 

Coding- 

        Coding  is  the  process  or  phase  which  is  used  to 

transform  a  system's  design  into  a  computer  language 

format. This phase is concerned with the specification of 

software translating design into the  source code. Source 

code  writing  is  necessary  done  by  the  coders  or 

programmers who are independent people. 

        To develop a dynamic and reliable software, coding 

is an essential part of software. 
(cid:1)  By using coding, we can transform a system's design 

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

in  the  developed  software  or  existing  software.  In  other 

words, find software errors and verify that application or 

system  is  fit  for  use  or  not.  Preventing  bugs  reducing 

development  costs  and  improving  performance  are  the 

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

        In  this  testing,  the  tester  does  not  have  the 

into a programming language. 

knowledge of the coding. In this  testing,  we only check 

(cid:1) Programmer should implement a well defined coding 

the  functionality  of  the  software  that  is  input  is  passing 

known as coding standard. 

correctly and related output is producing or not. 

Software Engineering 

174 

YCT 

 
 
 
 
 
 
White Box Testing or Structured Testing- 
      In  this  testing,  the  tester  has  the  knowledge  of 
coking  and 
internal  structure  of  existing  software 
whether the internal structure is correct or not. 

Types of Testing 

        Besides  above  two  types  of  testing  there  are  many 
different types of software tests, these are- 
1.  Unit Testing- 

This  test  is  used  to  check  the  independent  and 
individual unit or  module of  software.  A unit is the 
smallest testable component of software. 

2.  Integration Testing- 

This  test  integrates  all  the  modules  one  by  one  and 
checks 
issues  (Whether  one 
module is compatible with another or not). 

the  compatibility 

3.  System Testing- 

In this testing, a coder puts the software in different 
environment  and  checks  whether  the  software  is 
compatible with new environment or not. 

4.  Stress Testing- 

In  this  testing,  the  tester  checks  how  the  system 
behaves  with  heavy  load  it  means  the  capability  of 
software  how  much  loaded  software  can  handle 
before it fails. 

5.  Performance Testing- 

It checks the speed and effectiveness of the software 
to  make  sure  that  it  generates  the  result  within  the 
specified time or real life load systems. Performance 
means  how  the  software  performs  under  different 
workloads. 

6.  Usability Testing- 

It validates how well a customer can use a system or 
web application  to complete  a task. In other  words, 
the coder checks the GUI part created by developer 
whether  GUI  part  or  design  of  software  is  user 
friendly or not. 
7.  Unit Testing- 

It  is  done  by  the  customer  to  verify  and  check  the 
delivered  product  or  whole  system  works  as 
intended or customer acceptation. 

8.  Alpha Testing- 

In  this  testing,  the  developer  feeds  the  input  and 

measures  the  output  because  this  testing  is  the  last 

testing  done  by  the  developer  side  just  before  the 

delivery of the product. 

Software Engineering 

9.  Beta Testing- 

In this testing, customer checks the functionality and 

features  of  the  software  and  provide  suggestions  to 

the  developer 

team  whether 

the  software 

is 

providing good results or not. 

10.  Functional Testing- 

It  checks  the  functions  by  emulating  business 

scenario  based  on  functional  needs.  To  verify  these 

functions, Black box testing is used in common way. 

11.  Verification Testing- 

It checks the product whether it is being built by the 

coder in correct way or not. 

12.  Validation Testing- 

It  checks  the  built  product  whether  it  is  completing 

customer's requirements or not. 

13.  Big Bang Testing- 

In  this  testing  methodology  all  components  or 

modules  of  a  system  are  combined  together  and 

tested as a whole. This testing is of two types- 

Top Down Integration- In this approach, firstly the 

higher  level  modules  are  integrated  then  secondly, 

the  lower  level  modules  are  integrated.  This  testing 

is also known as trickle-down approach. 

Bottom Up Integration- In this approach, firstly the 

lower  level  modules  are  integrated  then  the  higher 

level  modules  are  integrated.  This  testing  is  also 

known as bubble-up approach. 

Software Quality and Reliability 

Software Quality–"A quality product does exactly what 

the users want it to do." 

The software products have the several quality factors-  

A  quality  can  be  measured  a  number  of  ways,  two  of 

them give excellent insights into the product's stability- 
1.  Between  testing  and  actual  delivery,  the  number  of 
errors and defects are discovered in the system. 
2.  The  amount  of  time  or  the  Mean  Time  to  Defect 
(MTTD) are discovered prior to and after delivery to 

the customer between bugs or errors. 

175 

YCT 

 
 
 
 
 
 
 
 
Having  fewer  errors,  bugs,  defects,  a  higher  MTTD  is 

associated generally with better overall quality. 

The  software  quality  assurance  is  an  umbrella 

activity  for  checking  the  quality  of  software 

whether the software we are making is quality full 

or not. 

Software Reliability 

Reliability Testing or Software Testing 
(cid:1)  Reliability  tests  are  designed  to  measure  the  ability 

of  system  to  remain  operation  for  long  period  of 

time. 

(cid:1)   It  is  typically  expressed  in  terms  of  Mean  Time  to 

Failure (MTTF). 

(cid:1)   The average of all time intervals between successive 

       It  is  a  probability  of  failure-free  software  operation 

failure is called the MTTF. 

(cid:1)  After  a  failure  is  observed,  the  developers  analyze 
that  consumes 
the  defects  or  bugs 

and 

fix 

sometimes, it is called the Repair Time. 
Types of Reliability Testing 

for  a  specified  period  of 

time  within  particular 

environment.  It  is  a  dynamic  system  characteristics  or 

execution event. 

The failure of software depends on two factors- 
1.  No. of faults being evaluated in software. 
2.  Operational profile of execution of the software. 
Types of Time 

1.  Execution  Time-  The  actual  CPU  time  that  the 

software takes during its execution. 

2.  Calendar Time- Normal or regular time that we use 

on a daily basis. 

3.  Clock  Time-  Actual  time  that  is  elapsed  while  the 

software  is  executing.  This  time  also  includes  the 

time  that  the  software  spends  while  waiting  in  the 

system. 

Software Failure Mechanism 

Software 

failure  may  due 

to  bugs,  ambiguities, 

        Above three Reliability Testing are the main testing 

to  test  software  functionalities  but  there  are  many  more 

oversights or misinterpretation. 

The software failure are classified as- 

1.  Transient  Failure-  It  occurs  only  with  particular 

inputs. 

sub testing- 

4.

 Stress 
Testing

2.  Permanent Failure- It appears on all inputs. 

3.  Recoverable  Failure-  It  can  be  recovered  by  the    

system without operator's help. 

4.  Unrecoverable  Failure-  It  can  be  recovered  by  the 

system with operator's help only. 

5.  Non-corruption Failure- This failure doesn't corrupt 

system's data or state. 

6.  Corrupting  Failure-  This  failure  damages 

the 

5.

Endurance
  Testing

6.

 Spike 
Testing

⇒  It involves subjecting the system 
      to high levels of usage to identify 
      performance that can cause the
      system to fail.

⇒  It involves running the system 
      continuously for an extended 
      period of time to identify issues 
      such as memory leaks.
⇒  It involves subjecting to system 
      to sudden, unexpected increases 
      in load or usage to identify 
      performance, that can cause system
      to fail.

system's data or state. 

Software Engineering 

176 

YCT 

 
 
 
 
 
There are three main categories of reliability testing- 

2.  Measurement 

It is a technique by which measurement of reliability 

1. Modeling 
(cid:1)  Predictive  Modeling-  It  is  a  statistical  technique 

testing is performed by using following methods- 
(cid:1)  Mean  Time  Between  Failure  (MTBF)-  It  measures 

using machine learning and data mining. It is used to 

the reliability testing in terms of  mean time between 

predict and forecast future outcomes. It reduces time, 

failure. 

effort and costs in forecasting. 

(cid:1)  Estimation Modeling- It is a technique which is used 
to  find  out  the  cost  estimates  to  develop  and  test 
software algorithm, equations, etc. 

(cid:1)  Mean  Time  to  Failure  (MTTF)-  It  is  the  time 

between two consecutive failures. 

(cid:1)  Mean  Time  to  Repair  (MTTR)-  It  is  known  as  the 

time taken to fix the failure. 

Measure of Reliability Testing 

Sr. No. 

Metric Analysis 

1. 

2. 

3. 

4. 

5. 

6. 

Mean Time to Failure (MTTF) 

Mean Time to Repair 

(MTTR) 

Mean Time Between 

Failure (MTBF) 

Occurrence Rate of Failure 

Probability of Failure 

Availability 

Methods 

Total time

Number of units tested

Total timefor maintenance

Totalrepairs

Mean Time to Failure (MTTF)

+

Mean Time to Repair (MTTR )

1

Mean Time to Failure(MTTF)

Number of Failures

Totalcasesconsidered

Mean Timeof Failure(MTTF)

Mean TimeBetween Failure(MTBF)

Example-  Find  out  the  calculation  of  Mean  Time  to 
Failure (MTTF), where the total time and the number of 

unit tested are needed.  

(cid:1)  It  helps  the  system  upgrade  process  to  be  straight-

forwarded. 

(cid:1)  Greater productivity is given by system efficiency and 

Solution-If  the  values  are  as  below,  the  Mean  Time  to 
Failure (MTTF) is calculated as:- 

higher performance. 

MTTF

=

Totaltime

Number of units tested

=

100

40

=

2.5

Advantage of Software Reliability 

(cid:1)  It is used for data preservation. 
(cid:1)  It helps to avoid software failure 

Clean Room Approach 

       This approach was first proposed by Mills, Dyer and 
Linger during the 1980s. 

       In  software  engineering,  clean  room  is  an  approach 

to produce quality software. It follows a set of principles 
and  practices  for  gathering  needs,  designing,  testing, 

coding, managing, etc which improves the quality of the 

Software Engineering 

177 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
product  and  increases  productivity  by  consisting  the 

correctness  specification  that  starts  with  the 

following four key processes- 

1.  Management-  It  consists  of  project  mission, 
resources,  risk,  schedule,  training,  analysis, 

configuration, etc. 

2.  Specification-  It  consists  of  function,  analysis, 
by 

incremental 

planning 

needs, 

usage, 

considering the first process of each increment. 

highest level testing or box structure and moves 

forwards  to  the  design  detail  and  then  moves 

forwards  to  the  design  detail  and  then  to  the 

code.  By  applying  a  set  of 

''Correctness 

Questions", its first level occurs or takes place. 

If  these  do  not  signify  or  demonstrate,  the 

specification  correctness,  more  formal  and 

3.  Development- 

it  consists  of  correctness, 

mathematical methods are used. 

reengineering,  verification,  incremental  design, 

etc.  by  considering  the  second  process  of  each 

increment. 

4.  Certification-  It  consists  of  test  planning, 
certification 

modeling, 

statistical 

training, 

process, etc. by considering the final process of 

each increment. 

There  are  some  tasks  which  occur  in  clean  room 

approach- 

1.  Increment Planning-  

•    It  adopts  the  incremental  strategy,  which  is 

developed. 

•  It  creates  each  increment's  functionality, 

project size, and clean room schedule. 

•  According  to  the  plan,  each  increment  is 

integrated and certified in proper time which 

is needed to be care taken. 

2.  Requirement  Gathering-  A  more  detailed 
description  of  the  customer  level  need  is  done 

and  developed  by  using 

the 

traditional 

techniques like analysis, design, coding, testing, 

and debugging. 

3.  Box  Structure  Specification-  To  describe  the 
functional  specification,  box  structure  is  used. 

The  behavior,  data  and  procedure  in  each 

increment are separated and isolated by the box 

6.  Code 

Generation, 

Inspection 

and 

Verification- The box structure specification is 

represented  in  a  particular  language  which  is 

translated  into  the  appropriate  programming 

language  by  using  technical  reviews  for  the 

semantic  conformance  of  box  structure  and 

code.  At 

last,  correctness  verification 

is 

conducted for the source code. 

7.  Statistical  Test  Planning-  The  clean  room 
is  organized,  analyzed,  conducted, 

activity 

planned,  designed 

the  projected  usage  of 

software  in  parallel  specification,  verification 

and code generation. 

8.  Statistical  Use  Testing-  Designing  a  finite 
number  of  test  cases  is  always  necessary 

because  exhaustive 

testing  of  software 

is 

impossible.  Use  statistical  technique  to  execute 

a set of tests derived from a statistical sample of 

possible  execution  by  all  users  from  a  targeted 

population. 

9.  Certification- The increments are certified and 
ready  for  integration,  once  the  verification, 

inspection,  all  errors  and  usage  testing  have 

been correctly completed. 

Box Structure in Clean Room Process 

Model 

structure. 

In  clean  room  engineering,  box  structure  is  a 

4.  Formal  Design-  By  using  black  box  structure 
approach, the clean room design is a natural and 

modeling  approach.  A  box  is  like  a  container  that 

contains  the  details  of  system  or  aspects.  By  using  the 

seamless extension of specification that is called 

following  three  types  of  boxes  that  are  independent  to 

as  clear  boxes  and  state  boxes  that  is  also 

deliver 

the 

required 

information 

in 

each  box 

known as component level design. 

specification- 

5.  Correctness  Specification-  The  clean  room 
team  conducts  the  exact  series  of  rigorous 

1.  Black  Box-  It  identifies  the  system's  behaviour  to 

respond specific events. 

Software Engineering 

178 

YCT 

 
 
2.  State Box- It identifies the operation or sate data that 

are  similar  to  the  objects  by  representing  the  history 

of the black box. 

3.  Clear Box-It identifies the transition function used by 

state  box.  The  procedural  design  for  the  state  box  is 

included by the clear box.  

Benefits of Clean Room Approach 

       Clean  Room  approach  delivers  high  quality 

products,  reduces  developing  cost  and  overall  project 

time, saves resources, and increases productivity. 

Software Reengineering 

Booch Method 

       Booch  method  is  widely  used  on  object-oriented 

It  is  an  activity  that  improves  one's  understanding  of 

analysis  and  design  process.  This  method  was  authored 

software  or  prepares  or  improves  the  software  itself  for 

by  Grady  Booch  when  he  was  working  for  Rational 

increased maintainability, reusability, evalvability. 

Software.  This  method  consists  of  the  following  five 

activities in its macro process:- 

 Analysis,  Design,  Conceptualization,  Evolution, 

Maintenance . 

Macro  process- This process consists of the above five 

activities,  in  which  the  conceptualization  takes  into 

account  the  perspective  of  the  customer,  while  the 

        Software  reengineering  is  a  process  of  software 

analysis develops a model by defining classes, attributes, 

development or examination and alteration of a system to 

inheritance,  method,  etc.  The  design  develops  an 

reconstitute in a new form. It also changes a "bad" design 

architecture.  Evolution  relates  the  implementation,  and 

into  a  "good"  design.  This  process  encompasses  a 

the maintenance maintains the delivery of the product by 

combination  of  sub  processes  like  inventory  analysis, 

adding new requirements and eliminating bugs. 

reverse  engineering,  restructuring,  re-documentation, 

forward engineering code and data restructuring, etc. 

By variety of reasons, re-engineering can be done– 

⇒ It adds new features. 

⇒ It substitutes high casts. 

⇒ It improves maintainability. 

⇒ It adds new regulations and compliance. 

⇒ It boosts up productivity. 

⇒ It improves opportunity. 

⇒ It reduces risks. 

⇒ It saves and optimizes time. 

The Unified Modeling Language (UML) supersedes 
the notation aspect of the Booch method from 
which UML features the graphical elements form 
the Object-Modeling Technique (OMT). 

Micro  Process-  This  process  is  a  description  of  day  to 

day  activities.  Each  macro  process  has  its  own  micro 

process  which  consists  of  the  following  phases  that  are 

identified by Micro Process:- 

Classes, 

objects, 

object 

semantics, 

related 

to 

programming,  object 

relationship,  object 

interface, 

abstraction and implementation. 

Software Engineering 

179 

YCT 

 
 
 
 
 
 
 
 
 
Example-  Lets  illustrate  a  Booch  diagram  related  to  a 

BankAccount 

(Super  class)  having 

two  attributes 

SavingAccount  and  CheckingAccount  that  inherit  the 

super class:- 

Advantage of Booch method- 

Jacobson Method 

Jacobson method is  used to plan, design and implement 

object-oriented  software  which  covers  the  entire  life 

cycle  and  stress  traceability  between  different  phases 

both backward and forward. It is also known as Object-

Oriented Software Engineering (OOSE). This  method is 

broken down into five models or parts:- 

Requirements,  Analysis,  Design,  Implementation,  and 

Testing  model.  Jacobson  method  is  also  called  Object-

Oriented  Business  Engineering  (OOBE).  The  visual, 

      This  method  consists  of  many  diagrams  as  class, 

textual  and  structural  methods  were  formulated  by  Ivar 

object, state transition, module, process and interaction. 

Disadvantage of Booch method- 

       This  method  doesn't  use  all  symbols  and  diagrams 

while it defines a lot of symbols for almost every design 

decision. 

Jacobson in 1986. 

Use cases- 

(cid:1)  It needs the scenario for understanding system. 

(cid:1)  No  clear  flow  of  events  with  non-formal  text  is 

Rumbaugh Method 

needed. 

          It 

is  an  approach  very 

friendly  and  easy 

(cid:1) With a clear flow of events to follow, text is easy to 

methodology  used 

to  develop  manageable  object- 

read. 

oriented  because  it  is  the  closet  to  the  traditional 

approach.  Rumbaugh  method  is  also  known  as  OMT 

(cid:1) Formal style using pseudo code. 

(Object Modeling Technique) used in the real  world  for 

(cid:1) It governs interaction between the various actors. 

designing  and  modeling  of  software.  OMT  includes  the 

four stages (analysis, designing system, designing object 

and implementation).  

(cid:1) How and when the use case begins and ends. 

(cid:1) How and when of data storage and usage ends. 

         Additionally,  OMT  is  always  broken  down  into 

(cid:1)  How  the  constraints  of  the  problem  domain  are 

three  different  parts  or  models  (object,  dynamic, 

handled. 

functional). These three models are similar to traditional 

system. 

Example-  Lets  illustrate  a  Jacobson  method  ordering 

Example- Lets illustrate a Rumbaugh diagram related to 

kiosk  system,  which  relies  on  the  customer  for  order 

a  Bank-Account  having 

the 

transaction  between 

same as the receipt relies on the kiosk for order:- 

customer and Bank Account:- 

Software Engineering 

180 

YCT 

 
 
 
 
 
   13.  

CLOUD COMPUTING 

Introduction – 
Cloud  computing  is  on-demand  access  via  the  internet 

which contains a significant pool of resources including 
software, 
servers, 

analytics, 

database, 

storage, 

(cid:1) Store, backup and recover data. 
(cid:1) Stream audio and videos. 
(cid:1) Deliver software on demand from one place to 

another. 

networking and intelligence over the cloud (internet).  

(cid:1) Analyze, test and built applications. 

Cloud based storage makes your data possible 
to save them to a remote database rather than 
keeping/storing  them  on  a  hard  drive  or  local 
storage device. 

If  any  user  uses  an  online  service  to  send  emails, 
to  music,  send 
documents,  watch  movies, 

listen 

pictures,  play  games  then  these  all  are  made  possible 

behind the scene by cloud computing. It generally used 
to  store,  backup  and  recover  data.  By  using  the 

following you can - 

(cid:2) 

Cloud  computing  provides  more  options  for 

people  and  business  as  cost  savings,  increase 
productivity,  speed  and  efficiency,  performance 

and security that are benefits for users. 

Example  of  cloud  computing  -  Google  Drive, 
One Drive, Box or Dropbox, etc. 

Features of Cloud 

There are many cloud features– 

Automation 

& 

Archestration 

Performance 

Monitoring 

Cost 

Governance 

Management 

& 

Security 

Migration/Images 

configuration 

management 

Applications, 

computations 

Instance and 

billing 

storage, networks 

management 

compliance 

Risk, Audits 

service and 
resource 

governance 

Encryption mobile 

or endpoint 

security 

Types of Cloud Computing 

Private  Cloud  -  A  private  cloud  is  the  service  and 

Public  Cloud  -  This  service  is  sold  on-demand  by  the 

minute or hour through long-term commitments because 

a third-party CSP (Cloud Service Provider) provides the 

infrastructure that are maintained on a private network, 

service  over  the  internet.  In  this  cloud,  all  hardware, 

because it refers resources that can be physically located 

software,  servers,  storage  and  other  infrastructure  are 

on  the  company's  or  organization's  on-site  data  center. 

owned and managed by the CSP. 

Rarely, even some organizations pay third-party service 

Hybrid  Cloud  -  A  hybrid  cloud  is  the  combination  of 

to be built and hosted by private cloud. 

public  cloud  and  private  cloud  services.  It  is  used  to 

Cloud Computing 

181 

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
store/share  applications  and  data  to  both  physical 

Disadvantage of Cloud Computing 

storage  and  cloud  storage.  It  provides  company's 

business greater flexibility and deployment. 

(cid:1) 

(cid:1) 

(cid:1) 

(cid:1) 

(cid:1) 

(cid:1) 

Advantage of Cloud Computing 

Cloud  based  software  promises  to  reduce  IT 
complexity and costs. 

It offers companies from all fields to use software 

from any device via a native app or a browser. 

It provides a number of benefits that is why users 
can  carry  their  files  to  other  devices  remotely  or 

seamless manner. 

By  using  Dropbox  and  Google  Drive,  users  can 
check, send emails on any computer and can store 

files. 

It makes possible for users to backup, share, store 
their files, music and photos. 

It can provide security to users' files, documents, 

in the event of a hard drive crash. 

(cid:1) 

There are naturally risks with all the efficiencies, 
speed, 
that  come  with  cloud 
computing. 

innovations 

(cid:1)  When  security  comes  to  a  sensitive  medical 
records, it has always been a great concern. 

(cid:1) 

(cid:1)   Encryption protects the vital information. 
(cid:1) 

All the files, documents and data disappear when 
the encryption key is lost. 
The company's servers may fall victim to natural 
disasters,  internal  errors  (bugs),  and  even  power 
outages maintained by cloud computing. 
Types of Cloud Services (IaaS, PaaS, SaaS) 

There  are  four  broad  categories  that  are  fallen 
into  by  most  cloud  computing  services;  they 
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

Runtime 

Data 

Runtime 

Data 

Runtime 

Data 

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

Storage 

Servers 

Storage 

Servers 

Storage 

Servers 

Storage 

Networking 

Networking 

Networking 

Networking 

You manage 

Other manages 

1.  IaaS (Infrastructure as a Service)-  

Apart  from  the  above  resources,  the  IaaS  also 

It  is  a  computing  infrastructure  managed  over 

offers-  

internet.  IaaS  is  also  called  HaaS  (Hardware  as  a 

Service).  It  helps  users  to  avoid  the  cost  and 
complexity  of  purchasing  and  managing  physical 

servers.  Users  have  an  allocated  storage  capacity 
and  can  start,  stop,  access  and  configure  the 

Virtual  Machine  (VM)  and  storage  as  required. 

(cid:1) Virtual machine disk storage 
(cid:1) Load balancers  
(cid:1) Virtual local area networks (VLANs) 
(cid:1) IP addresses 
(cid:1) Software bundles 
Example-  Google  Compute  Engine  (GCE), 

Cloud Computing 

Microsoft Azure, Linode, DigitalOcean, Amazon 
YCT 

182 

 
 
 
 
 
 
 
 
 
Web  Services  (AWS),  Racksapace,  Cisco  Meta 

cloud. 

Characteristics of IaaS- 

■ Resources are available as a service. 

■Services are highly scalable, dynamic, flexible. 

■ GUI and API based access. 

■ Automated administrative tasks. 

2.  

PaaS (Platform as a Service)- 

Below are the several SaaS applications- 
(cid:1) Help desk applications 
(cid:1) Billing and invoicing system 
(cid:1) Human Resource (HR) solutions 
(cid:1)  Customer  Relationship  Management  (CRM) 
applications 

Characteristics of SaaS- 

■  Updation  are  applied  automatically  so  users 
are  not  responsible  for  hardware  and  software 

 It  is  a  created  platform  for  the  programmers 

updates. 

to develop, test, run and manage the applications, 

so  that  users  can  access  these  tools  over  the 
internet  using  APIs,  web  portals  or  gateway 

software.  PaaS  offers  runtime  environment  for 
applications  to  be  developed.  It  has  a  feature  of 

point-and-click  tool  that  enables  non-developers 
to create web applications.    

Example-  Windows  Azure,  Heroku,  Force.com, 

Google  App  Engine,  Apache  Stratos,  AWS 

Elastic  Beanstalk,  Magento  Commerce  Cloud 
and OpenShift, etc. 

Characteristics of PaaS- 

■ Integrates with web services and databases. 

■  Accessible  to  various  users  via  the  same 

development application. 

■ Supports multiple languages and frameworks. 

■ Provides an ability to Auto-scale. 

■  Builds  on  virtualization  technology,  so  that 
resources  can  easily  be  scaled  up  or  down  as 

per the company's needs. 

3.      SaaS (Software as a Service)-  

It is a web service by which users can access the 
applications  with the  help of  internet connection 
and web browser on their phone, tablet or PC. It 

is  also  called  'on-demand  software'  in  which  the 
applications  are  hosted  by  a  cloud  service 

provider. 

Example-ZenDesk, 
Slack,  Google  Apps, 
BigCommerce,  SalesForce,  Dropbox,  Cisco 

WebEx, and GoToMeeting, etc. 

■ Managed from a central location. 

■ Hosted on a remote server. 

■ Accessible over the internet.  

■ The services are purchased on the pay-as-per- 
use basis. 

Virtualization-  

It is a creation or technique of a virtual (rather 
than  actual)  version  of  something  such  as  a 

server,  a  desktop,  a  storage  device  (RAM),  an 
operating  system  or  network  resources  which 

allow  to  share  a  single  physical  instance. 

Creating  a  virtual  machine  over  existing 
operating  system  and  hardware  is  known  as 

Hardware virtualization. The machine on which 
the virtual machine is going to create is called a 

Host Machine. 

Types of Virtualization- 
1.  Hardware virtualization 
2.  Operation system virtualization 
3.  Server virtualization 
4.  Storage virtualization 

Cloud Computing 

183 

YCT 

 
 
 
 
 
 
Cloud Services Requirements 

Cloud and Dynamic Infrastructure 

Cloud Service Management 

delivered to the  users. These  deployment  models 

The 

cloud 

service  management 

system  offers 

standardization,  support  desk,  operational  control, 
monitoring,  and  consistent  service  delivery  needed  for 

are- 

1.  Public  clouds-  In  this  model,  a  business  rents 

the  capability  and  pays  for  what  is  used  on-

private, public, and hybrid cloud platforms by using the 

demand. 

following –  

1.  Simplify user interaction with IT 

Service  catalog  enables  standards  and  speeds  up 

the delivery. 

2.  Enable policies to lower the cost 

Automated  provison  &  decommission  speed  up 
delivery and assets respectively. 

3.  Enhance system administrator Efficiency 

Migration from various management isolates full-

fledged service. 

Cloud Deployment Models 

Using  cloud  deployment  models,  business 
processes,  application,  data  and  any  type  of  IT 

Advantages-  Minimal  investment,  No  setup 

cost,  Infrastructure  management  is  not  required, 

No maintenance, Dynamic scalability required. 

Disadvantages- Less secure, Low customization. 

2.  Private  clouds-  In 

this  model,  a  business 

essentially  turns  its  IT  environment  into  a  cloud 

and uses it to deliver services to their users. 

Advantages-  Better  control,  Data  Security  and 

Privacy, Support Legacy System, Customization. 

Disadvantages- Less scalable, more costly. 

3.  Hybrid  Clouds-  Hybrid 

clouds 

combine 

resource  can  be  provided  as  a  service  and 

elements  of  public  and  private  clouds.  By  using 

Cloud Computing 

184 

YCT 

 
 
 
 
 
 
 
 
this  model,  you  may  host  the  app  in  a  safe 

standardized 

Service-Oriented  Architecture 

environment. 

(SOA)  assets,  that  can  be  broadly  deployed  into 

Advantages-  Flexibility  and  control,  cost, 

new  and  existing  accounts  and  is  a  lower-cost 

security. 

model. 

Disadvantages-  Difficult  to  manage,  slow  data 

7.  Dynamic  Private  Clouds-  It  allows  client 

transmission. 

workloads to dynamically migrate to and from the 

4.  Community 

or 

Commodity 

Clouds- 

compute cloud as required. 

Community  clouds  are  managed  by  groups  of 

8.  Multi  Clouds-  It  combines  the  resources  of 

people,  communities  and  agencies  especially 

public and private clouds as the name implies. It 

government 

to  have 

the  common 

interests 

is similar to the hybrid cloud deployment model. 

working on the same mission. 

Instead of merging public and private clouds, this 

Advantages-  Cost  effective,  security,  shared 

cloud  uses  many  public  clouds  to  improve  the 

resources, collaboration and data sharing. 

reliability of the services. 

Disadvantages-  Limited  scalability,  Rigid  in 

Advantages- Reduced Latency, High availability 

customization. 

of service. 

5.  Shared  Private  Clouds-  This 

is  a  shared 

Disadvantages- Complex, security, issue. 

compute  capacity  with  variable  usage-based 

pricing to business units that are based on service 

Cloud Infrastructure 

offerings,  accounts,  datacenters.  To  take  over  or 

It is the  need of the  hour to reduce the risks and 

buy 

infrastructure  made  available 

through 

cost  associated  with  business,  it  is  becoming  at 

account consolidations, it needs on internal profit. 
6.  Dedicated  Private  Clouds-  It  has  IT  service 

the  same  time  vital  to  increase  the  agility  and 

quality  of  the  IT  infrastructure  by  consisting  of 

catalog with dynamic provisioning. It depends on 

the following:- 

Cloud Computing 

185 

YCT 

 
 
 
Types of Hypervisor 
1.  Type 1 Hypervisor- It is also called bare-metal or 

A grid computing network consists of three types 

of  machine  names-  Control  node,  Provider,  and 

native. It is a layer of software installed directly on 

User  and  layers  names-  Lower  layer,  Middle 

top  of  a  physical  server.  It  is  mainly  found  in 

layer and Upper layer. 

enterprise environment. 

 A  grid  computing  works  like  the  following 

Pros 

Cons 

Example 

figure. 

Control node is also known as server. 

Provider is also known as grid node. 

VM (Virtual 

Machine) 

Mobility 

Security 

Resource over 

allocation 

Limited 

VMware, 

functionality 

vSphere with 

Complicated 

ESX/ESXi, 

Management 

Oracle VM, 

Microsoft 

Price 

Hyper-V, Lynx 

Secure 

2.  Type  2  Hypervisor-  It  is  also  called  hosted 

hypervisor  which  is  installed  and  run  inside  the 

physical  host  machine's  operating  system.  It  is 

found  in  environments  with  a  small  number  of 

Cons 

Example 

processed parallel. For example. 

For the efficient execution, grid computing breaks down 

each  task  into  small  fragments  and  each  fragment  is 

servers. 

Pros 

Easy to manage 

       Convenient for 

testing 

Allows access 

to additional 

productivity 

tools 

Less flexible 

resource 

management 

Performance 

Security 

Oracle VM 

VirtualBox, 

VMware 

Workstation  

Pro/ VMware 

Fusion 

GRID COMPUTING 

To accomplish a joint task, a grid is made up of a 

number  of  resources  and  layers  or  distributed 

architecture  of  various  computers  connected  by 

      A = (4 × 7) + (3 × 8) + (2 × 9) 

Step 1:     A = 28 + (3 × 8) + (2 × 9) 

Step 2:     A = 28 + 24 + (2 × 9) 

Step 3:     A = 28 + 24 + 18 

Step 4:     A = 70 

Advantages of Grid Computing- 
(cid:2)   All machines with various operating systems can 

use a single grid computing network. 

(cid:2)   Across different physical locations, the tasks can 
be  done  or  processed  parallel  while  users  don't 

have to pay money for them. 

Servers  are  not  needed  because 

it 

is  not 

centralized. 

Disadvantages of Grid Computing 

For  some  applications,  licensing  may  make  it 

(cid:2) 

(cid:2)  

restrictive. 

networks. On a network, all machines collaborate 

(cid:2)  Many  groups  are 

reluctant  with 

sharing 

under  a  common  protocol  because  all  tasks  are 

resources. 

difficult for a single machine to handle. 

Cloud Computing 

(cid:2)  

186 

The grid software is still in the involution stage.

YCT 

 
 
 
 
 
 
 
 
 
 
 
 
  
Key Components of Grid Computing 

Computational  

Collaborative 

Manuscript 

Modular 

Data Grid 

Types of Grid Computing 

     Grid  computing  is  important  for  several 
reasons  as  efficiency,  cost,  and  flexibility  in  the 

financial  services,  gaming,  engineering  and 
entertainments. 

Cluster Computing 

(cid:2)   A  cluster  is  a  type  of  parallel  or  distributed 
processing system, which consists of a collection 

of interconnected stand–alone computer  working 
together  as  a  single,  integrated  computing,  A 

cluster generally refers to two or more computers 
(nodes) connected together. 

(cid:2) 

Cluster  computing  is  important  to  resolve  the 

demand  and  process  services  in  a  faster  way.  It 
ensures  the  computational  power  to  be  always 

available.  It  gives  a  single  strategy  as  it  is 
inexpensive, unconventional to the large server. 

Applications of Cluster Computing 

■ Weather forecasting     

■ Flight simulation 

■ Earthquake simulation 

■ Image rendering 

■ Petroleum exploration  

■ Various e-commerce applications 

Advantages of Cluster Computing- 
(cid:1) Cost effectiveness      
(cid:1) Processing speed 
(cid:1) Improved flexibility   
(cid:1) High performance 
(cid:1) Easy to manage            
(cid:1) Expandability 

(cid:1) Scalability  
(cid:1) Availability 

Disadvantages of cluster Computing- 

(cid:1)  High  cost  due  to  its  high  hardware  and  its 
design. 
(cid:1) Problem in finding bugs or faults. 
(cid:1) More space is needed to manage and monitor 
the infrastructure may increase. 

Types of Cluster Computing 

1.  High availability (HA) Clusters- It is used 
to  face  failure  issues.  It  is  also  called 

failover  cluster.  In  this  cluster,  services  and 

applications  may  be  made  available 

to 

different nodes if a node declines. 

2.  Load-balancing  Clusters-  It  allocates  all 
the  incoming  traffic  or  request  resources 

among  several  nodes  that  run  the  equal 

machines  and  programs  having  similar 

content.  In  this  cluster,  services  or  requests 

are  distributed  amongst  all  the  nodes  if  a 

node declines. 

3.  High  Performance  (HP)  Cluster-  It  is 
designed  to  take  benefit  of  the  parallel 

processing  of  all  nodes.  It  utilizes  super 

computers 

to 

resolve 

computational 

problems. 

4.  High  Availability  +  Load  Balancing-  The 
combined  performance  of  high-availability 

and load balancing clusters provides an ideal 

solution.  This  cluster  is  generally  used  for 

FTP server, web, news and e-mail. 

Cloud Computing 

187 

YCT 

 
 
 
 
 
 
 
 
 
 
 
        
Classification of Cluster 

1.  Open Cluster- This type of cluster causes 
enhanced security concerns and needed by 

every  node  accessed  through  the  web  or 
internet. 

2.  Close  Cluster- 

It 

is 

good 

for 

computational  tasks  and  needs  fewer  IP 
addresses.  This  type  of  cluster  provides 

increased  protection  to  the  nodes  that  are 
hidden behind the gateway node. 

Cluster Computing Architecture 

(cid:2)  It is a group of  workstations  or computers 
interconnections. 
connected  via  speed 
These  workstations  work  together  as  a 

single, 
integrated  computing  resources, 
that  are  designed  with  arrays.  A  node 

input 

having 
functions, 
memory, an operating system, works either 

and  output 

with a single or a multiprocessor. 

(cid:2)  Two  or  more  nodes  are  generally 

connected to a single line. 

(cid:2)  Every 

node  might 

be 

connected 

individually through a LAN network. 

Types of Clustering 

1.  Hierarchical  Clustering-  Hierarchical  clustering 
has  a  bottom  up  approach  if  it  uses  a  tree-like 

structure in agglomerative clustering. 

It  begins  with  each  element  as  a  separate 

successively more massive clusters:-  

     Hierarchical clustering has also a top-down approach 
if it uses top-down tree like structure. It begins with the 

whole set and proceed to divide it into success cluster. 

Cloud Computing 

188 

YCT 

 
  
 
 
        
 
 
2.  Partitioning Clustering- This clustering is divided 
into two  sub-types,  first one is K-means clustering 

and second one is Fuzzy C-means. 

DBSCAN- In image processing,  machine learning, 

data-mining  and  other  fields  are  widely  used  by 

DBSCAN. DBSCAN is a data clustering algorithm 

based  on  density.  It  is  widely  used  with  the 

increasing  size  of  clusters.  It  is  also  used  for 

applying  new  data  partitioning  and  merging 

method, by using KD tree Get neighbours query. 

OPTICS- It is similar to DBSCAN. It is useful for 

The  objects  are  divided 

into  many  clusters 

identifying clusters of different densities. It is also a 

mentioned  by 

the  number 

'K' 

in  K-means 

clustering. It is divided into two clusters C1 and C2 
but both have the similar characteristics. 

      While  in  Fuzzy  C-means  clustering,  objects 
have  the  similar  characteristics  but  a  single  object 

cannot belong to two different clusters because it is 
very similar to K-means.  

Example- 

(i)   A cricket game having runs scored by the player 

and wickets taken by the players. 

(ii)  Academic performance 

(iii) Diagnostic systems  

(iv) Wireless sensor networks 

(v)  Search engines 

How does K-Means Clustering work? 

K-Means 
flowchart:- 

clustering  works 

like 

following 

data clustering algorithm based on density. OPTICS 

extracts  the  clustering  structure.  This  algorithm 

builds  a  density  representation  by  creating  core 

distance and reach-ability distance. 

STING-  It  is  a  statistical  information  grid-based 

approach  which  follows  a  hierarchical  approach  to 

divide the spatial area into rectangular cells similar 

to  a  quadtree.  This  approach  separates  the  high 

level cells into multiple smaller cells which can be 

simply computed and stored. 

CLIQUE-  It 

is  a  grid  based  density  based 

technique or algorithm. In grid based algorithm, the 

CLIQUE  divides  the  space  of  distance  into  a  grid 

structure,  while  in  density  based  algorithm,  a 

cluster is a maximal set of connected dense units in 

a  subspace.  With  respect  to  the  value  of  records, 

this algorithm is very scalable. 

Advantages of CLIQUE- DBSCAN, K-Means and 

Farthest  First  are  outperforms  in  accuracy  and 

execution  time  by  CLIQUE  algorithm.  It  is  one  of 

the simplest methods which is able to find clusters 

and any number of clusters. 

Disadvantage  of  CLIQUE-  The  estimation  will 

take  place  and  correct  clusters  will  not  be  able  to 

find if the size of the cell is unsuitable for a set of 

high values. 

Cloud Computing 

189 

YCT 

 
 
 
                   
 
                   
 
 
                                                                                                                            
Beowulf Cluster 

The  hadoop  consists  of  the  following  mainly  four 

It  is  a  multi-computer  architecture  consisting  of 

multiple client nodes and a single server connected 

through  internet. The word "Beowulf" is originated 

components: 

1.  MapReduce-  It  is  like  a  data-structure  or  an 

algorithm.  MapReduce 

performs 

the 

from an old English poem having the same name. A 

distributed  processing  in  parallel  in  a  hadoop 

group of identical and commodity grade computers 

cluster to  work so fast. It has only two phases 

is called Beowulf cluster. This cluster differs  from 

namely Map and Reduce that are utilized. Any 

others  in  its  behaviour  of  working  on  many 

big data are inputted, they go through Map and 

operating systems- 

(cid:3) Kerrighed                 

(cid:3) MOSIX 

(cid:3) DragonFly BSD     

(cid:3) Rocks Cluster Distribution 

        (cid:3) PelicanHPC              

  (cid:3) Cluster knoppix 

Reduce  phases  until  they  got  executed  in 

output  form.  Map  function  breaks  the  data 

blocks (big data input) into tuples which works 

as  input  to  Reduce  function.  Then  the  Reduce 

function combines the tuples  into set of tuples 

and performs summation and sorting type jobs. 

Finally  they  are  sent  to  the  output  terminal  in 

A  Beowulf 

cluster 

have 

the 

following 

the output format. 

characteristics- 

(cid:3) A private network with dedicated processors, and 

easy replication for multiple vendors.  

(cid:3)  It  is  a  free  and  open  source  software  scalable 

with Input-Output and no custom components. 

It  is  an  Apache  open  source  framework.  It  is  

written  in  java  that  allows  distributed  execution 

using 

programming  models.  The 

hadoop's 

Map 

function 

does  many 

tasks 

as 

environment  provides  distributed  storage  and 

RecordReader,  Combiner,  Partitionar,  etc  and 

computation  across  computer  clusters.  By  the  help 

Reduce  function  also  does  many  tasks  as 

of two major layers, it is designed to scale up from 

a  single  server  to  thousands  of  servers.  Its  two 

layers are – 

(i)  Computation/processing layer (MapReduce) 

(ii)  Storage layer (HDFS) 

The  main  purpose  of  hadoop  is,  it  utilizes  a  large 

cluster  of  commodity  hardware  to  keep  and  store 

shuffle  and  sort,  Reduce  and  Produce  output 

format. 

2.  HDFS-  HDFS  stands  for  Hadoop  Distributed 

File System. It works on commodity hardware 

and  utilizes  storage  permission.  It  is  used  to 

store  data  in  large  chunk  of  blocks  to  the 

big 

size  data  by  working  on  MapReduce 

following two nodes- 

programming  algorithm.  For  example-  Yahoo, 

(a)  NameNode  (Master)-  It  is  used  to  guide 

Facebook,  eBay,  Netflix  are  using  hadoop  in  their 

the Datanode (slaves) because it works as a 

organization to deal with big data. 

master in Hadoop cluster. 

Cloud Computing 

190 

YCT 

 
 
 
 
 
 
 
(b)  DataNode  (Slaves)- It  is used  to  utilize  or 

store the data in Hadoop cluster because it 

works as a Datanode. 

3.  YARN- 

It 

is  a 

framework  on  which 

MapReduce  works.  YARN  works 

two 

Oozie 

It  is  a  Java  web  application  used  to  schedule 

hadoop 

jobs.  Multiple 

jobs  are  combined 

sequentially  into  one  logical  unit  of  tasks  by 

oozie. For Hadoop, oozie is a workflow scheduler 

operations-  Job  Scheduling  and  Resource 

that  permits  users  to  create  Directed  Acyclic 

Management.  Job  scheduler  divides  a  big  task 

Graphs of workflow. 

into  small  jobs  and  Resource  management 

manages  all  the  resources  that  are  made 

available  for  running  Hadoop  cluster.  YARN 

performs its tasks by using many features- 

Oozie consists of two parts:- 
(a)  Workflow  engine-  It  is  responsible  to  run 

and  store  workflows  of  Hadoop  jobs  as 

MapReduce,  Hive  and  Pig.  If  workflow 

as  Multi-  Tenacy,  Scalability,  Compatibility 

engine  specify  a  sequence  of  actions  to 

and cluster Utility. 

4.  Hadoop  Common-  It 

is  also  known  as        

execute, then workflow job has to wait. 
(b)  Coordinator  engine-  Based  on  predefined 

common  utility  used  by  HDFS,  MapReduce 

schedules  and  data  availability,  coordinator 

and YARN. Hadoop common utilities are Java 

engine runs workflow jobs. 

files  or  Java  library  or  Java  script  needed  for 

other  components.  It  solves  the  hardware 

failure if it occurs in hadoop framework. 

Advantages of Hodoop 

(cid:2)    Hadoop  has  an  ability  to  store  large  amount  of 

data. 

(cid:2)   Hadoop 

has 

high 

flexibility 

and 

high 

computational power. 

(cid:2)    Hadoop's tasks are independent i.e. open source. 

(cid:2)    

It has linear scaling. 

Disadvantage of Hadoop 

Oozie  can  manage  the  lifecycle  of  the  jobs  and 

timely  execution  of  thousands  of  workflows. 

Anyone 

can 

easily 

start, 

stop, 

suspend 

(cid:2)    Hadoop is not more effective for small data. 

(terminate)  and  re-run  the  jobs  as  oozie  is  very 

(cid:2)   Hadoop  has  hard  cluster  management  and 

much flexible and it has command line interface 

stability issues. 

(cid:2)    Hadoop concerns the security. 

as well as client API. 

Mahout 

(cid:2)   Hadoop  has  complexity,  latency,  limited  support 

The  name  mahout  came  from  Apache  Hadoop 

for  real  time  processing  and  limited  support  for 

which  uses  an  elephant's  logo.  A  Mahout  is  one 

structured data. 

who  drives  an  elephant.  It  is  an  open  source 

(cid:2)    Hadoop has data security, limited support for Ad-

project  also.  Many  popular  machine  learning 

hoc queries, for graph and machine learning. 

techniques 

such 

as 

classification, 

Cloud Computing 

191 

YCT 

 
   
 
recommendation and clustering are implemented 

by  Mahout.  Developers  are  enabled  to  use 

optimized  algorithm  by  highly  scalable  machine 

Low Touch 

It is also an on-boarding model or method that is 

learning liabrary that is called Mahout. 

largely self serve in  nature.  Low touch  model is 

opposite of a high touch model. It simply doesn't 

have  man  power  or  the  resources  to  provide  a 

high  tough  experience  to  each  customer  so  it  is 

attractive to new, and small companies. 

Benefits  of  low  touch-  Low  touch  model  takes 

very little time out of customer access team's that 

is one of the biggest benefits. 

Characteristics of low touch-  

(cid:1)  Little  to  no  human  interruption  during  on- 

boarding. 

High Touch 

It is hands-on for customers who require a lot of 

interaction 

and 

less 

reliance  on  digital 

engagement with any company. It is used to boil 

down  to  how  frequently  the  customer  can  be 

contacted. 

In other words, to support the customers through 

(cid:1)  To  deliver  value  on  automation  tools,  heavy 

the  pre-  and  post-sale  phases,  a  high  touch 

emphasis is occur. 

model,  a  human  first  method  is  used.  It  is  often 

(cid:1)  Executing  task  and  accomplishing  goals  can 

used  when  a  customer  needs  direct  guidance  to 

quickly be started by customers. 

High, Low, No-Touch Partner Program 

Segmentation 

navigate  a  complex  process.  It  includes  in-

person-meeting, webinars, video chat, demos and 

phone calls, etc. 

Benefits  of  high  touch-  The  main  benefits  of  a 

high  touch  method  are  that  customers  feel  like 

they  are 

receiving 

special  attention  and 

customers  can  tap  into  as  much  support  as  they 

require. 

Characteristics of high touch  

When  high-value  reoccurs,  it  is  said  High  touch 

(cid:1)  Little  to  no  human  interruption  during  on-

customer  service.  On  the  other  hand,  when 

boarding. 

company  uses  automation  to  digitally  engage 

(cid:1)  To  deliver  value  on  automation  tools,  heavy 

with  customers,  it  is  called  low  touch  customer 

emphasis is occur. 

service  while  neither  high-value  reoccurs  nor 

(cid:1)  Executing  task  and  accomplishing  goals  can 

company  uses  automation  to  digitally  engage,  it 

quickly be started by customers. 

is called no-touch customer service. 

Cloud Computing 

192 

YCT 

 
 
 
