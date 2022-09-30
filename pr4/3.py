class Time:
    def __init__(self, sec):
        self.sec = sec
    def convert_to_minutes(self):
        min = self.sec //60 
        remainder = self.sec%60
        return str(f'{min}:{remainder}')
    def convert_to_hours(self):
        hour = self.sec//3600
        min = (self.sec%3600)//60
        remainder = self.sec%60
        return str(f'{hour}:{min}:{remainder}') 
    
value = Time(280)
print(value.convert_to_minutes())

new_value = Time(19808)
print(new_value.convert_to_hours())
print(new_value.convert_to_minutes())