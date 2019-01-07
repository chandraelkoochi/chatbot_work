from services.Leave import Leave_check

leave = Leave_check()
leave.user_leave_type = "Leave"

class NormalLeave(Leave_check):
    def regularLeave(req):
        # if "leave" in req:
        #     print("Please enter the dates:")
        # else:
        #     print("What kind of leave do you want?")

        if (not leave.extract_Months or not leave.extract_dates):
             leave.monthManipulation(req)
             leave.dateManipulation(req)
             if (not leave.extract_Months and len(leave.extract_dates) >= 1):
                 return "Enter months say dec to jan"
             elif not leave.extract_dates and len(leave.extract_Months) >= 1:
                 return "Enter dates say 26 to 28"
             if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                 leave.dateFormatConstruction()
                 return "Enter the reason for leave"
        elif (len(leave.extract_Months)>=1 and len(leave.extract_dates)>=1 and leave.user_leave_type is not None):
             if req == "bye" or req == "cancel" or req == "end" or req == 'exit':
                 leave.leaveSession = None
                 return "Hope to serve you again"
             elif req == "yes":
                 if (len(leave.extract_Months) >= 1 and len(
                         leave.extract_dates) >= 1 and leave.user_leave_type is not None and leave.reason_leave is not None):
                     return "Your leave request has been raised."
             elif req == "no":
                 if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1):
                     leave.clearDates()
                     return "Do you wish to change dates?Please enter dates"
             elif req == "bye" or req == "cancel" or req == "end" or req == 'exit':
                 leave.session['leave_type'] = "Leave"
                 leave.leaveSession = None
                 return "Hope to serve you again"
             else:
                 print("hello")
                 leave.reason_leave = req
                 if (len(leave.extract_Months) >= 1 and len(leave.extract_dates) >= 1 and leave.user_leave_type is not None and leave.reason_leave is not None):
                      return "your leaves summary" + "\n" + "from date:" + leave.from_dateString + "\n" + "to date: " + leave.to_dateString + "\n" + "reason: " + leave.reason_leave + "Leave type:" + leave.user_leave_type

        # elif req == "bye" or req == "cancel" or req == "end" or req == 'exit':
        #         leave.leaveSession = None
        #         return "Hope to serve you again"
        #     else:
        #         return "Please provide all the details before you apply for leave or want to change mode say cancel"
