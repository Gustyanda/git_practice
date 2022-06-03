#----- build up class
class point:
    def __init__(self,x,y): #(build in function class using init)
        self.x = x
        self.y = y

p = point(3.0,4.0) #(as a variable, which def by self)
print(p.x) 
print(p.y)
print(str(p.x) + ',' + str(p.y)) #(convert int as output str using one output print)


#----- function inside class
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def data(self): #(build up function recall self in class)
        print(p.x)
        print(str(p.x)+','+str(p.y)) #(print function call inside function)

p = point(3.0,4.0) #(as variable create outside)
p.data()


#----- build up boolean
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def data(self):
        print((p1.x != p2.x) and (p1.y == p2.y)) #(as target boolean output function)
    
p1 = point(3.0,4.0) #(variable)
p2 = point(2.0,4.0) #(variable)
p1.data() #(output)
p2.data() #(output)


#----- build up string
class person:
    def __init__(subject,name,age):
        subject.name = name
        subject.age = age

    def data(var):
        print(('my name is '+ var.name) + (' and my age is ' + str(var.age)))

x = person('Azharry',30)
x.data()


#----- build up mathematics
class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def data(t1,t2):
        print(t1.hour + t2.hour)

t1 = time(5,30,25)
t2 = time(6,10,30)
time.data(t1,t2)



#----- build update data variable
class Rocket:
    def __init__(self, altitude):
        self.altitude = altitude
    
    def up(self, alt_up):
        self.altitude = self.altitude + alt_up

    def down(self, alt_down):
        self.altitude = self.altitude - alt_down

    def position(self):
        print(self.altitude)


r1 = Rocket(altitude=0)
r1.up(10)
r1.down(20)
r1.position()

r1.up(100)
r1.down(70)
r1.position()

r1.up(200)
r1.down(0)
r1.position()



#----- build up function phone using class
class phone:
    def __init__(self, battery):
        self.battery = battery
    
    def charge(self, charge):
        self.update_battery(2 * charge)

    def call(self, call):
        self.update_battery(-1 * call)

    def sms(self, sms):
        self.update_battery(-1 * ((sms)/100))

    def play(self, play):
        self.update_battery(-5 * play)

    def update_battery(self, change):
        self.battery = self.battery + change
        if self.battery < 0:
            self.battery = 0
        elif self.battery > 100:
            self.battery = 100


    def data(self):
        print(str(self.battery) + ' % ')

bt = phone(battery=0)
bt.charge(120)
bt.data()
bt.call(30)
bt.data()
bt.sms(1000)
bt.data()
bt.charge(30)
bt.data()
bt.play(30)
bt.data()
