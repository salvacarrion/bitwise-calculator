# Bitwise math

How does a electronic circuit perform arithmetic operations using just ones and zeros?  
By using the Arithmetic Logic Unit (ALU) of the processor, which in the end makes use of
the logic (through the logic gates) to perform simple but powerful operations.

In order to better understand its basics, I've written a few arithmetic operators using 
just bitwise logic operators and loops.

## Examples

```
Values: **************************************
a = 15 = 1111
b = 3 = 0011

Operations: **********************************
[Addition] Half Adder: 15 + 3 = 0001 0010 = 18

[Subtraction] Half Subtractor: 15 - 3 = 1100 = 12

[Multiplication]: 15 x 3 = 0010 1101 = 45

[Division]: 15 ÷ 3 = 0101 = 5

[Power]: 15^3 = 1101 0010 1111 = 3375

[Sqrt]: sqrt(25) = 0101 = 5

is 15 odd? True
is 3 odd? True
```
