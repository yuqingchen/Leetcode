class Solution:
    def leapyear(self, year) :
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
            return True
        else :
            return False
    
    def countday(self, day, month, year) :
        monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        for i in range(1971, year) :
            if self.leapyear(i):
                days += 366
            else :
                days += 365
        days += sum(monthday[:month - 1])
        days += day
        if self.leapyear(year) and month > 2:
            return days + 1
        return days
                
        
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        days = self.countday(day, month, year)
        now = self.countday(3, 5, 2020)
        print(days - now)
        print((days - now) % 7)
        print(week[(days - now) % 7])
        return week[(days - now) % 7]