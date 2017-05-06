For this lab, I am given the option to store numbers in a "database" at an index of my choice.
With the restriction that I can't store at indexes where i%3==0 is true.


Using the store mechanism I am able to overwrite anywhere further in memory. Including the return address at index 109.

To make the shellcode for this, I wrote a python script that took assembly commands, assembled them, and stored them in 7 byte chunks (padded with NOPS). I used the final byte to write a EAX-=0 instruction which used the following 4 unwritable bytes as the 0.
