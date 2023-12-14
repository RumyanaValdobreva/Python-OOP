class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{"0" + str(self.hours) if self.hours < 10 else self.hours}:\
{"0" + str(self.minutes) if self.minutes < 10 else self.minutes}:\
{"0" + str(self.seconds) if self.seconds < 10 else self.seconds}"

    def next_second(self):
        if self.seconds == Time.max_seconds and self.minutes != Time.max_minutes:
            self.seconds = 0
            self.minutes += 1
        if self.seconds == Time.max_seconds and self.minutes == Time.max_minutes:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
        if self.minutes == Time.max_minutes and self.hours != Time.max_hours:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == Time.max_minutes and self.hours == Time.max_hours:
            self.minutes = 0
            self.hours = 0
            self.seconds = 0
        if self.hours == Time.max_hours:
            self.hours = 0
            self.minutes = 0
            self.hours = 0

        return self.get_time()


# time = Time(10, 59, 59)
# print(time.next_second())
