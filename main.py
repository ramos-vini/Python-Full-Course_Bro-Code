class Car():
    def turn_on(self):
        print("This car turns on.")
        return self

    def drive(self):
        print("This car drives.")
        return self

    def brake(self):
        print("This car brakes.")
        return self

    def turn_off(self):
        print("This car turns off.")
        return self


car = Car()

# car.turn_on().drive().brake().turn_off()

# car.turn_on(). \
#     drive(). \
#     brake(). \
#     turn_off()

(car.turn_on().
 drive().
 brake().
 turn_off())

