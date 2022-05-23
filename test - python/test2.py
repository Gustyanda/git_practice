class phone:
    def __init__(self, battery):
        self.battery = battery
    
    def charge(self, charge):
        if self.battery == 0 or self.battery < 100:
            self.battery = self.battery + (2 * charge)
            if self.battery > 100:
                self.battery = 100

    def call(self, call):
        if self.battery > 0:
            self.battery = self.battery - (1 * call)
            if self.battery < 0:
                self.battery = 0

    def sms(self, sms):
        if self.battery > 0:
            self.battery = self.battery - (1 * ((sms)/100))
            if self.battery < 0:
                self.battery = 0

    def play(self, play):
        if self.battery > 0:
            self.battery = self.battery - (5 * play)
            if self.battery < 0:
                self.battery = 0

    def data(self):
        print(str(self.battery) + ' % ')

bt = phone(battery=0)
bt.charge(120)
bt.call(30)
bt.sms(1000)
bt.charge(30)
bt.play(30)
bt.data()

