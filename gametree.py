
class nodes:
    def __init__(self,value):
        self.value=value
        self.nexts=None
        self.childs=None
    

    def report(self):
        stack=[]
        ttrue=True
        back=self
        
        while ttrue:
            
            if back!=None:
                
                print("    "*len(stack)+back.value)
                if back.childs!=None:
                    stack=stack+[back]
                    back=back.childs
                else:
                    if back.nexts!=None:
                        back=back.nexts
                    else:
                        if len(stack)>0:
                            back=stack.pop()
                            back=back.nexts
                        else:
                            ttrue=False
                            
            else:
                ttrue=False
            
           
def loads(files):
    tree=nodes("start")
    
    stack=[tree]
    
    f1=open(files,"r")
    content=f1.read()
    f1.close()
    contents=content.split("\n")
    tabs=0
    mon=False
    for n in contents:
         
         if n.strip()=="":
             return tree
         ttrue=True
         count=0
         while ttrue:
             if n[count]!=" ":
                 ttrue=False
             else:
                 count+=1
         if count>len(stack):
             nodex=nodes(n.strip())
             stack[len(stack)-1].childs=nodex
             stack=stack+[nodex]
         elif count==len(stack):
             if count==len(stack):
                 nodex=nodes(n.strip())
                 stack[len(stack)-1].nexts=nodex
                 stack[len(stack)-1]=nodex
         elif count<len(stack):
                 ttrue=True
                 nodex=None
                 while ttrue:
                     if count<len(stack):
                         
                         nodex=stack.pop()  
                     else:
                         ttrue=False
                 
                 nodex=nodes(n.strip())
                 stack[len(stack)-1].nexts=nodex
                 stack[len(stack)-1]=nodex
    return tree


tree=loads("map.txt")
print(":")
tree.report()
def levels(stacks,currents):
    print("0.exit")
   
    if len(stacks)>0:
        print("1.back to father:"+stacks[len(stacks)-1].value)
    if currents.nexts!=None:
        print("2.next :"+currents.nexts.value)
    if currents.childs!=None:
        print("3.child :"+currents.childs.value)
    
    i=int(input("? "))
    return i
current=tree
stacks=[]
stacks=stacks+[tree]
y=0
ttrue=True
while ttrue:
    print(stacks[len(stacks)-1].value)
    a=levels(stacks,current)
    if a==0:
        ttrue=False
    elif a==1 and len(stacks)>0:
        current=stacks.pop()
    elif a==2 and current.nexts!=None:
        current=current.nexts
    elif a==3 and current.childs!=None:
        stacks=stacks+[current] 
        current=current.childs
        
    else:
        print("out of board")
    
    if 0==0:
        print("path:",end="")
        for n in stacks:
            print("\\"+n.value, end="")
        print("\ncurrent:"+current.value)


