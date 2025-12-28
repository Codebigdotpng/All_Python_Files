class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level  # 0 to 100

    def say_hello(self):
        print("Beep boop! I'm " + self.name + "!")

    def show_battery(self):
        print(self.name + "'s battery level is " + str(self.battery_level) + "%.")

    def recharge(self, hours):
        # Each hour adds 10% battery
        added_percent = hours * 10
        self.battery_level += added_percent
        # Make sure battery doesn't go over 100%
        if self.battery_level > 100:
            self.battery_level = 100
        print(self.name + " recharged for " + str(hours) + " hour(s). Battery is now " + str(self.battery_level) + "%.")

# Test it!
my_robot = Robot("RoboBuddy", 50)
my_robot.say_hello()
my_robot.show_battery()
my_robot.recharge(3)  # Adds 30%
my_robot.show_battery()