# Consider the problem of searching for a pattern in a given string. Design a ‘C’ program to locate
# the pattern using Horspool’s algorithm. Give the trace of this algorithm.

# Horspool-python.txt

text='JIM_SAW_ME_IN_BARBER_SHOP'
pattern='BARBER'
table=[]
n=len(text);
m=len(pattern)
def shift_table():
    
    for i in range(128):
        table.append(m)
    for i in range(len(pattern)-1):
        table[ord(pattern[i])-ord('0')]=m-1-i;
    print(".......Shift Table Ready...........\n", table)
def horspool():
    i=m-1;
    while i<=n-1:
        k=0
        while(k<=m-1 and pattern[m-1-k]==text[i-k]):
            k+=1
        if k==m:
            return i-m+1
        else:
            i=i+table[ord(text[i])-ord('0')]
    return -1;

shift_table()
res=horspool()
if res==-1:
    print(" \n pattern not found \n")
else:
    print(" \n pattern found at pos=",res)




# OUTPUT:
# .......Shift Table Ready...........
#  [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4, 2, 6, 6, 1, 6, 6, 
#   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
#   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
#   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
#   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
#   6, 6, 6, 6, 6, 6, 6, 6]
 
#  pattern found at pos= 14
