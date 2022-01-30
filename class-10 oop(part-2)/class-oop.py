class Robot:
    def __init__(self,name,color,weight) :
        self.name = name;
        self.color = color;
        self.weight = weight;

    def instance_self(self):
        print("My name is"+ self.name)

r1 = Robot(name='Tom', color='red', weight=30);
r2 = Robot(name='jerry', color='blue', weight=20);

class Person:
    def __init__(self,n,p,i) :
        self.name = n
        self.personality = p
        self.is_setting = i

    def sit_down(self):
        self.is_setting = True
    def stand_up(self):
        self.is_setting = False

p1 = Person("Alice","aggresive",False)
p2 = Person("becky","talkative",True)

p1.robot_woned = r2
p2.robot_woned = r1

p1.robot_woned.instance_self()


        