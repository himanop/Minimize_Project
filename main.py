import database_creation, database_functions
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "hello"

user_reg_data = {}
db_name = "minimize.db"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register_account():
    msg=""
    user_info = {}
    if request.method == "POST":
        user_email = request.form["user_email"]
        user_firstName = request.form["user_firstName"]
        user_lastName = request.form["user_lastName"]
        user_password = request.form["user_password"]
        user_password_verify = request.form["user_password_verify"]
        #Gather user info in json object which will be passed to render template to display data user has already entered.
        user_info = {'email' : user_email, 'fname' : user_firstName, 'lname' : user_lastName}
        if user_password != user_password_verify:
            msg = "Passwords do not match. Please confirm passwords"
            return render_template("register.html", msg=msg, user_info=user_info)
        elif not user_email or not user_firstName or not user_lastName or not user_password:
            msg = "Please fill out all fields of the form"
            return render_template("register.html", msg=msg, user_info=user_info)
        elif database_functions.user_exists(user_email, db_name) == True:
            msg = "Account Already Exists. Please log in through link below"
            return render_template("register.html", msg=msg, user_info=user_info)
        # session["user_email"] = user_email
        # session["user_firstName"] = user_firstName
        # session["user_lastName"] = user_lastName
        # session["user_password"] = user_password
        user_reg_data["user_email"] = user_email
        user_reg_data["user_firstName"] = user_firstName
        user_reg_data["user_lastName"] = user_lastName
        user_reg_data["user_password"] = user_password
        #There are three ways to approach sending information to the function
        #1.) simply saving all the registration information as a session.
        #2.) passing the user registration information as a parameter through URL FOR. This means we need to display the user information in the URL and this is not secure
        #3.) create a global dictionary and use that. I believe that this won't allow for multiple users. We will go with this approach for right now
        #user_email = user_email, user_firstName = user_firstName, user_lastName = user_lastName, user_password = user_password
        return redirect(url_for("validate_email"))

    return render_template("register.html", user_info=user_info)

# @app.route("/validate_registration/<user_email>/<user_firstName>/<user_lastName>/<user_password>", methods=["POST", "GET"])
@app.route("/validate_email", methods=["POST", "GET"])
#user_email, user_firstName, user_lastName, user_password
def validate_email():
    # user_email = session["user_email"]
    # user_password = session["user_password"]
    return render_template("validate_email.html", user_email=user_reg_data["user_email"], user_firstName = user_reg_data["user_firstName"],
                           user_lastName = user_reg_data["user_lastName"], user_password = user_reg_data["user_password"])


def main():
    database_creation.creating_database_user_table('minimize.db')

if __name__ == '__main__':
    main()
    app.run(debug=True)
