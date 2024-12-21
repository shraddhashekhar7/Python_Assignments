class Time:
    def __init__(self, hours, mins):
        self. hours = hours
        self.mins = mins

    def addTime(self, t2):
        add_hr = self.hours + t2.hours
        add_min = self.mins + t2.mins

        if add_min >= 60:
            add_min -= 60
            add_hr += 1

        return Time(add_hr, add_min)

    def displayTime(self):
        print("{} hr {} min".format(self.hours, self.mins))

    def displayMinute(self):
        total_mins = (self.hours * 60) + self.mins
        print("Total {} min".format(total_mins))


time1 = Time(3,50)
time1.displayTime()
time1.displayMinute()

time2 = Time(2,20)
time2.displayTime()
time2.displayMinute()

added_time = time1.addTime(time2)
print("({} hours and {} min) + ({} hour and {} min) is ({} hr and {} min)".format(time1.hours, time1.mins, time2.hours,
                                                                            time2.mins, added_time.hours, added_time.mins))
