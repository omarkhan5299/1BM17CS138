class CallDetail:
    def __init__(self,c,r,d,t):
        self.caller = c
        self.reciever = r
        self.type = t
        self.duration = d
        
    def print_details(self):
        print("Caller:",self.caller,"Reciever:",self.reciever,"Type:",self.type,"Duration:",self.duration)
        


class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        list_of_call_objects=[]
        
        for el in list_of_call_string:
            l1=el.split(',')
            self.list_of_call_objects.append(CallDetail(l1[0],l1[1],l1[2],l1[3]))

        
        for ob in self.list_of_call_objects:
            ob.print_details()
             
            
            
        




call1='9999000001,93330000011,23,STD'
call2='9999000002,93330000022,54,Local'
call3='9999000003,93330000033,6,ISD'
list_of_call_string=[]
list_of_call_string=[call1,call2,call3]
obj=Util()
obj.parse_customer(list_of_call_string)


