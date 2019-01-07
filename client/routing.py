import flask
import flask_cors
# from services.NormalLeave import normalLeave_check
from services.RegularLeave import NormalLeave

app = flask.Flask(__name__)
cors = flask_cors.CORS(app)
from flask import Flask, session
from services.Maternity import Maternity_check
from services.WeddingLeave import Wedding_check
from services.Leave import Leave_check
from services.Paternity import Paternity_check
from services.SickLeave import Sick_check
leave = Leave_check()

noise_list = ["absent", "ooo", "out of office","pto"]

class Leave_Demo():



    @app.route('/<request>')
    def leaveType(request):

        words = request.split()
        leave.noise_free_words = [word for word in words if word in noise_list]
        leave.noise_free_text = " ".join(leave.noise_free_words)
        leave.nsf = str(leave.noise_free_text)



        if leave.leaveSession is None:
            leave.getSessionType1(request)
            print(leave.leaveSession)


        if "Maternity" == leave.leaveSession  or leave.session['leave_type'] == "Maternity":
                leave.session['leave_type'] = "Maternity"
                return Maternity_check.maternity(request)
        elif "Paternity" == leave.leaveSession or leave.session['leave_type'] == "Paternity":
                leave.session['leave_type'] = "Paternity"
                return Paternity_check.paternity(request)
        elif "Sick" == leave.leaveSession  or leave.session['leave_type'] == "Sick":
                leave.session['leave_type'] = "Sick"
                return Sick_check.sick(request)
        elif "Wedding" == leave.leaveSession or leave.session['leave_type'] == "Wedding":
                leave.session['leave_type'] = "Wedding"
                return Wedding_check.wedding(request)
        elif leave.nsf is not None or "Leave" == leave.leaveSession or leave.session['leave_type'] == "Leave":
            leave.session['leave_type'] = "Leave"
            return NormalLeave.regularLeave(request)
        elif request == 'bye' or request == 'exit' or request == 'cancel':
                return "Hope to serve you again."

        else:

            leave.response = leave.chatterbot.get_response(request)
            leave.reply = leave.response.confidence
            if leave.response == leave.leaveQuestion:
                leave.previousResponse = leave.response
            try:
                if leave.reply > 0.65:

                    return str(leave.response)

                else:
                    if str(leave.previousResponse) == leave.leaveQuestion:
                        leave.getSessionType2(request)
                    if leave.leaveSession is not None and not leave.extract_dates and not leave.extract_Months:
                        leave.previousResponse = " "
                        return "please tell me the dates"
                    else:
                        if request == "no":
                            return "hope to serve you again"
                        else:
                         return "Did you mean this?1. Apply for leave OR 2.Get leaves summary"

                    # print("Did you mean this?")
                    # print("1. Apply for leave")
                    # print("OR")
                    # print("2.Get leaves summary")

            except:
                return ""


if __name__ == '__main__':
    app.secret_key = 'SECRET KEY'
    app.run(debug=True)
