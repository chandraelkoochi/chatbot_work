
from chatterbot import ChatBot
from difflib import SequenceMatcher
import datetime


class Leave_check():
    module = "leave2"

    chatterbot = ChatBot(
        "SQLMemoryTerminal",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=("mysql+pymysql://root:mysql@localhost:3306/{}".format(module)),
        read_only=True,
    )
    previousResponse = " "
    response = " "
    reply = " "
    leaveQuestion = "What kind of leave"

    s1 = 'mark me absent on 27 dec'

    mylist = ['on', 'from', 'to']

    session = {'leave_type': 'leave'}
    leaveSession = None
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
    reason_leave = None
    count = 0
    mode = None
    months = ["jan", "january", "feb", "February", "march", "april", "apr","may", "june", "jun", "july", "jul", "aug",
              "august", "september", "sep", "sept", "oct",
              "october", "nov", "november", "dec", "december"]
    leave_type = ["Loss of pay", "Compensatory","Maternity","Wedding","Sick","Paternity"]
    matern = "maternity"
    patern = "paternity"
    wedding_leave = "wedding"
    sick_leave = "sick"
    leave_type2 = ["Leave","Loss of pay", "Compensatory","Maternity","Wedding","Sick","Paternity"]
    user_leave_type = " "
    req = ["work from home","hometown"]

    noise_free_words = None
    noise_free_text = None
    nsf = None



    def process(self):
        print("processing")

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def monthManipulation(self, msg):
        self.splitMsg = msg.split(" ")
        i = 0
        j = 0
        while i < len(self.splitMsg):
            j = 0
            while j < len(self.months):
                result = Leave_check.similar(self.splitMsg[i], self.months[j])
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

    def clearDates(self):
        self.extract_Months = []
        self.extract_dates = []
        self.from_month = None
        self.to_month = None
        self.from_date = None
        self.to_date = None
        self.from_dateString = None

    def getSessionType1(self,request):
        splitrequest = request.split(" ")
        i = 0
        j = 0
        while i < len(splitrequest):
            j = 0
            while j < len(self.leave_type):
                if splitrequest[i][:1].upper() == self.leave_type[j][0][:1]:
                    result = Leave_check.similar(splitrequest[i],self.leave_type[j])
                    if result >= 0.80:
                        self.leaveSession = self.leave_type[j]
                j = j+1
            i = i+1

        return self.leaveSession

    def getSessionType2(self,request):
        splitrequest = request.split(" ")
        i = 0
        j = 0
        while i < len(splitrequest):
            j = 0
            while j < len(self.leave_type2):
                if splitrequest[i][:1].upper() == self.leave_type2[j][0][:1]:
                    result = Leave_check.similar(splitrequest[i],self.leave_type2[j])
                    if result >= 0.80:
                        self.leaveSession = self.leave_type2[j]
                j = j+1
            i = i+1

        return self.leaveSession

# if __name__ == '__main__':
#     leave = Leave_check()
#     result =  leave.getSession("Maternity")
#     print(result)
