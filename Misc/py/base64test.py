import base64
table='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def encode_2(raw):
    result=[0]*((int((len(raw)-1)/3)+1)*4)
    rest=len(raw)%3
    ct=0;
    for index,byte in enumerate(raw):
        	if(index%3==0):
        	val=byte&0xff
        	# print(val)
    	else:
        	val <<=8
        	# print(val)
        	val|=byte&0xff

        if(index%3==2):

            for x in range(4):

            	result[ct * 4 + 3 - x] = table[val & 0x3f]
            	val>>=6
        	ct+=1;
            val=0;
    else:
    	if(rest==1):
        	val<<=16
        if(rest==2):
        	val<<=8
    	if(rest!=0):
        	for x in range(4):
            	if x < 3 - rest:
                    result[ct * 4 + (3 - x)] = '='
                    val >>= 6
                else:
                	result[ct * 4 + (3 - x)] = table[val & 0x3F]
            	val >>= 6
	return "".join(result)

table='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
raw='asdasdasdasda'
print(encode_2(raw.encode()))
print(base64.b64encode(raw.encode()))