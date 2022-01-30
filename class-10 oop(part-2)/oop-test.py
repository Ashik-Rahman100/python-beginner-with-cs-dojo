class Robot:
    def __init__(self,name,color,weight) :
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"'my name is {self.name}" )


r1 = Robot("Tom", "Blue", 20)
r2 = Robot("Jerry", "Red", 2)

# print(r1,"\n",r2)

class Person:
    def __init__(self,n,p,s) :
        self.name = n
        self.personality = p
        self.isSetting = s

    def sit_down(self):
        self.isSetting = True

    def sit_up(self):
        self.isSetting = False

p1 = Person("Alice","Agreesive",False)
p2 = Person("Bicky","Talkative",True)

p1.robot_woned = r2
p2.robot_woned = r1

robot =  p1.robot_woned.introduce_self()





        