class Robot:
    def __init__(self,name,color,weight) :
        self.name = name;
        self.color = color;
        self.weight = weight
    
    def introduce_self(self):
        print("My name is " + self.name);

# r1 = Robot();
# r1.name  = 'Tom';
# r1.color = 'Blue';
# r1.weight = 30;

# r2 = Robot();
# r2.name = 'jerry';
# r2.color = 'red';
# r2.weight = 2;

# r1.introduce_self();
# r2.introduce_self()

r1 = Robot("Tom","Blue",30);
r2 = Robot("jerry","Red",2);

r1.introduce_self();
r2.introduce_self();
