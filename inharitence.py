class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def arrangeDate(self):
        date = "The date is " + str(self.day)+'-' + \
            str(self.month)+'-'+str(self.year)
        return date


birthdate = Date(1998, 12, 12)

print(birthdate.arrangeDate())
