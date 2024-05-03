flag =0

def prifix(x):
    for i in range(l):
                
        if x[0:1]=="ca":
           flag=1
           return x[i]
    
x=["cat","car","fear","center"]
l=len(x)
print(prifix(x),x)