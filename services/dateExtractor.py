import datetime
from difflib import SequenceMatcher


class DateExtractor():

    x = datetime.datetime.now()

    today = x.strftime("%d")
    tomorrow = int(today) +1
    yesterday = int(today) -1
    print("today is "+today)

    mylist = ['on', 'from', 'to']
    months = ["jan", "january", "feb", "February", "march", "april", "apr", "may", "june", "jun", "july", "jul", "aug",
              "august", "september", "sep", "sept", "oct",
              "october", "nov", "november", "dec", "december"]
    splitmsg = []
    extract_Months = []
    extract_dates = []
    now = datetime.datetime.now()
    current_year = now.year
    previous_year = current_year - 1
    from_month = None
    to_month = None
    from_date = None
    to_date = None
    from_dateString = None
    to_dateString = None

    @staticmethod
    def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()


    def monthManipulation(self, msg):
        self.splitMsg = msg.split(" ")
        i = 0
        j = 0
        while i < len(self.splitMsg):
            j = 0
            while j < len(self.months):
                result = DateExtractor.similar(self.splitMsg[i], self.months[j])
                if result >= 0.80:
                    self.extract_Months.append(str(self.months[j]))
                    # print(self.extract_Months)
                j = j + 1
            i = i + 1


    def dateManipulation(self, msg):
        for s in msg.split(" "):
            if s.isdigit():
                self.extract_dates.append(str(int(s)))


    def dateFormatConstruction(self):
        if len(self.extract_Months) > 1:
            self.from_month = self.extract_Months[0]
            self.to_month = self.extract_Months[1]
        else:
            self.from_month = self.extract_Months[0]
            self.to_month = self.extract_Months[0]

        if len(self.extract_dates) > 1:
            self.from_date = self.extract_dates[0]
            self.to_date = self.extract_dates[1]
        else:
            self.from_date = self.extract_dates[0]
            self.to_date = self.extract_dates[0]

        self.from_dateString = str(self.from_date) + "-" + self.from_month + "-" + str(self.current_year)
        self.to_dateString = str(self.to_date) + "-" + self.to_month + "-" + str(self.current_year)
        print(self.from_dateString + "\n" + self.to_dateString)

    def hello(self,s):
        if 'mark absent' and 'from' and 'to' in s:
            self.monthManipulation(s)
            self.dateManipulation(s)
            self.dateFormatConstruction()

        elif ('mark absent 'and 'today') or ('today' or 'tomorrow' or 'yesterday') in s:
            print("entering")

        else:
            mysplit = s.split(" ")

            for i in mysplit:

                if i in self.mylist:
                    self.monthManipulation(s)
                    self.dateManipulation(s)
                    self.dateFormatConstruction()


if __name__ == '__main__':
    extractor = DateExtractor()
    req = input("Enter message here: ")
    extractor.hello(req)

