class myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"value is {self._value}")

    @ property
    def ten_value(self):
        return 10*self._value
        
obj= myclass(10)
print(obj.ten_value)
obj.show()



class myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"value is {self._value}")

    @ property
    def ten_value(self):
        return 10*self._value #adding 10*show
    
    @ten_value.setter
    def ten_value(self,new_value):#change ten_value
        self._value=new_value/10  #change value of show
        
obj= myclass(10)
obj.ten_value=67  #new value
print(obj.ten_value) #67.0
obj.show() #6.7



