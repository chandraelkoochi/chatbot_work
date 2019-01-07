from services.Leave import Leave_check

leave = Leave_check()

leave.reason_leave = "Sick"
leave.user_leave_type = "Sick"


class Sick_check():
    def sick(req):

        if "sick" in req:
            leave.monthManipulation(req)
            leave.dateManipulation(req)
            if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                leave.dateFormatConstruction()
                return "from date:" + leave.from_dateString + "\n" + ", to date:" + leave.to_dateString + ", leave-type: " + leave.user_leave_type + ", reason for leave: " + leave.reason_leave
            else:
                return "Please tell me the dates"
        elif (not leave.extract_Months and not leave.extract_dates):
            leave.monthManipulation(req)
            leave.dateManipulation(req)
            if (not leave.extract_Months and len(leave.extract_dates) >= 1):
                return "Enter months say dec to jan"
            elif not leave.extract_dates and len(leave.extract_Months) >= 1:
                return "Enter dates say 26 to 28"
            if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                leave.dateFormatConstruction()
                return "your leaves summary" + "\n" + "from date:" + leave.from_dateString + "\n" + "to date: " + leave.to_dateString + "\n" + "reason: " + leave.reason_leave + "Leave type:" + leave.user_leave_type
            elif req == "bye" or req == "cancel" or req == "end" or req == 'exit':
                return "Hope to serve you again"
            else:
                return "Please provide all the details before you apply for leave"
        elif req == "yes":
            if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                return "Your leave request has been raised."
        elif req == "no":
            if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                leave.clearDates()
                return "Do you wish to change dates?Please enter dates"
        elif req == "bye" or req == "cancel" or req == "end" or req == 'exit':
            return "Hope to serve you again"
            # use session.clear()



