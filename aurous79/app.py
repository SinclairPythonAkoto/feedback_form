import os
from aurous79 import app, init_mail
from typing import List, Dict
from flask import render_template, url_for, request, redirect, flash, session
from functools import wraps
from datetime import datetime
from flask_mail import Message
from time import strftime
from aurous79.extension import init_db, SessionLocal
from aurous79.models import FeedbackForm, EmailLibrary
from aurous79.utils.validate_email import validate_email, find_email, is_email_valid
from aurous79.utils.create_feedback import create_feedback
from aurous79.utils.validate_age import minimum_age, check_age
from aurous79.utils.create_email import send_email, send_one_email
from aurous79.utils.mass_email_from_feedback import send_batch_emails_from_feedback
from aurous79.utils.mass_email_from_email_library import (
    send_batch_emails_from_email_lib,
)
from aurous79.utils.add_to_email_library import add_to_email_library
from aurous79.utils.report_functions import (
    get_male_report,
    get_female_report,
    get_first_visit_report,
    get_return_visit_report,
    get_shisha_report,
    get_all_reports,
)
from aurous79.utils.graph_functions import (
    male_x,
    male_y,
    female_x,
    female_y,
    first_visit_x,
    first_visit_y,
    return_visit_x,
    return_visit_y,
    shisha_x,
    shisha_y,
    service_x,
    service_y,
    speed_x,
    speed_y,
    clean_x,
    clean_y,
)
from dotenv import load_dotenv
import dash
import dash_core_components as dcc
import dash_html_components as html

load_dotenv()

init_db()


# config your db
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["AUROUS79_DB"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

title = os.environ["AUROUS79_TITLE"]

# secret key for session
app.secret_key = os.environ["AUROUS79_SECRET_KEY"]


from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get("logged_in") is None:
            flash("You need to log in first")
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return decorated_function


@app.route("/")
def home():
    session: SessionLocal = SessionLocal()
    feedback: List[FeedbackForm] = session.query(FeedbackForm).first()
    if feedback is None:
        message: str = "The feedback board is empty."
        return render_template("home.html", message=message, title=title)
    else:
        feedback: List[FeedbackForm] = session.query(FeedbackForm).all()
        return render_template("home.html", feedback=feedback, title=title)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html", title=title)
    name: str = request.form["name"]
    age: str = request.form["age"]
    sex: str = request.form["sex"]
    first_visit: str = request.form["first_visit"]
    return_visit: str = request.form["return_visit"]
    cleanliness: str = request.form["cleanliness"]
    customer_service: str = request.form["customer_service"]
    service_speed: str = request.form["speed"]
    food_quality: str = request.form["food_quality"]
    shisha: str = request.form["shisha"]
    customer_comment: str = request.form["customer_comment"]
    customer_email: str = request.form["customer_email"]
    confirm_email: str = request.form["confirm_email"]

    # check if customer is < 16
    verified_age: bool = minimum_age(int(age))
    if verified_age is False:
        message: str = "You must be 16 or older to complete this form."
        return render_template("home.html", message=message, title=title), 308
    else:
        # use regex to check valid email 1st before anything
        # if not valid send error message
        # check if customer is >= 18
        over_18: bool = check_age(int(age))
        if over_18 is True:
            # check if email already exists in db
            email_exists: bool = find_email(customer_email)
            if email_exists is True:
                # add feedback to db with 5% email
                new_feedback: FeedbackForm = create_feedback(
                    name,
                    int(age),
                    sex,
                    first_visit,
                    return_visit,
                    int(cleanliness),
                    int(customer_service),
                    int(service_speed),
                    int(food_quality),
                    shisha,
                    customer_comment,
                    customer_email,
                )
                discount: str = "5%"
                send_customer_email: Message = send_email(
                    name, customer_email, discount
                )
                flash(f"Thank you {name} for your feedback!")
                return redirect(url_for("home")), 201
            else:
                # if email does not exist, add feedback to db with 10% email
                validate_customer_email: bool = validate_email(
                    customer_email, confirm_email
                )
                if validate_customer_email is True:
                    new_feedback: FeedbackForm = create_feedback(
                        name,
                        int(age),
                        sex,
                        first_visit,
                        return_visit,
                        int(cleanliness),
                        int(customer_service),
                        int(service_speed),
                        int(food_quality),
                        shisha,
                        customer_comment,
                        customer_email,
                    )
                    discount: str = "10%"
                    send_customer_email: Message = send_email(
                        name, customer_email, discount
                    )
                    flash(f"Thank you {name} for your feedback!")
                    return redirect(url_for("home")), 201
                # if invalid emails, return error message
                error_message: str = "The email you entered does not match. Please try again to recieve your discount."
                return (
                    render_template(
                        "feedback.html", error_message=error_message, title=title
                    ),
                    400,
                )
        else:
            # if customer is under 18, send 5% email
            validate_customer_email: bool = validate_email(
                customer_email, confirm_email
            )
            if validate_customer_email is True:
                new_feedback: FeedbackForm = create_feedback(
                    name,
                    int(age),
                    sex,
                    first_visit,
                    return_visit,
                    int(cleanliness),
                    int(customer_service),
                    int(service_speed),
                    int(food_quality),
                    shisha,
                    customer_comment,
                    customer_email,
                )
                discount: str = "5%"
                send_customer_email: Message = send_email(
                    name, customer_email, discount
                )
                # check if email has been sent (True/False)
                # if true proceed to flash message
                # if False return error message
                flash(f"Thank you {name} for your feedback!")
                return redirect(url_for("home")), 201
            # if invalid emails, return error message
            error_message: str = "The email you entered does not match. Please try again to recieve your discount."
            return (
                render_template(
                    "feedback.html", error_message=error_message, title=title
                ),
                400,
            )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        admin = request.form["username"]
        admin_password = request.form["password"]
        if admin == os.getenv("ADMIN_USERNAME") and admin_password == os.getenv(
            "ADMIN_PASSWORD"
        ):
            session["logged_in"] = True
            flash("Welcome back to Aurous79!")
            return redirect(url_for("admin"))
        else:
            error: str = "Invalid username and/or password. You must be management of Aurous79 to login."
    return render_template("login.html", error=error)


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    session: SessionLocal = SessionLocal()
    feedback: List[FeedbackForm] = session.query(FeedbackForm).first()
    if feedback is None:
        message: str = "The feedback board is empty."
        return render_template("admin.html", message=message, title=title)
    else:
        data: List[FeedbackForm] = session.query(FeedbackForm).all()
        return render_template("admin.html", data=data, title=title)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("See you soon!")
    return redirect(url_for("home"))


@app.route("/get-report", methods=["GET", "POST"])
@login_required
def get_report():
    session: SessionLocal = SessionLocal()
    if request.method == "GET":
        return render_template("get_report.html", title=title)
    elif "run_rpt" in request.form:
        run_report: str = request.form["run_rpt"]
        if run_report == "male":
            male_entries: List[FeedbackForm] = get_male_report()
            return render_template(
                "get_report.html", title=title, male_entries=male_entries
            )
        elif run_report == "female":
            female_entries: List[FeedbackForm] = get_female_report()
            return render_template(
                "get_report.html", title=title, female_entries=female_entries
            )
        elif run_report == "n_visit":
            first_visit_entries: List[FeedbackForm] = get_first_visit_report()
            return render_template(
                "get_report.html", title=title, first_visit_entries=first_visit_entries
            )
        elif run_report == "r_visit":
            return_visit_entries: List[FeedbackForm] = get_return_visit_report()
            return render_template(
                "get_report.html",
                title=title,
                return_visit_entries=return_visit_entries,
            )
        elif run_report == "shisha":
            shisha_entries: List[FeedbackForm] = get_shisha_report()
            return render_template(
                "get_report.html", title=title, shisha_entries=shisha_entries
            )
        elif run_report == "clean":
            clean_entries: List[FeedbackForm] = get_all_reports()
            return render_template(
                "get_report.html", title=title, clean_entries=clean_entries
            )
        elif run_report == "service":
            service_entries: List[FeedbackForm] = get_all_reports()
            return render_template(
                "get_report.html", title=title, service_entries=service_entries
            )
        elif run_report == "speed":
            speed_entries: List[FeedbackForm] = get_all_reports()
            return render_template(
                "get_report.html", title=title, speed_entries=speed_entries
            )
        else:
            flash(f"You need to select a report to run.")
            return redirect(url_for("get_report"))
    else:
        flash(f"The database is empty.")
        return redirect(url_for("get_report"))


@app.route("/send-email", methods=["GET", "POST"])
@login_required
def send_single_email():
    if request.method == "GET":
        return render_template("single_email.html", title=title)
    else:
        email: str = request.form["name"]
        email_subject: str = request.form["sub"]
        email_content: str = request.form["email_content"]
        create_email: bool = send_one_email(email, email_subject, email_content)

        # check if the email is valid
        if is_email_valid(email) is False:
            flash("Please enter a valid email.")
            return redirect(url_for("send_single_email"))

        # check if email has been sent
        if create_email is False:
            flash("The email did not send. Please check the credentials and try again.")
            return redirect(url_for("send_single_email"))
        session: SessionLocal = SessionLocal()
        data: List[EmailLibrary] = (
            session.query(EmailLibrary).order_by(EmailLibrary.id).all()
        )
        flash(f"Your email has been sent to {email}.")
        return render_template("single_email.html", title=title, data=data)


@app.route("/mass-emails", methods=["GET", "POST"])
def send_mass_emails():
    if request.method == "GET":
        return render_template("mass_emails.html")
    else:
        email_subject: str = request.form["sub"]
        content: str = request.form["email_content"]
        if request.form["massEmail"] == "feedback_lib":
            feedback_batch_emails: bool = send_batch_emails_from_feedback(
                email_subject, content
            )
            if feedback_batch_emails is False:
                flash("Could not send email. There are no emails stored in database.")
                return redirect(url_for("send_mass_emails"))
            flash("Your email has been sent!")
            return render_template("mass_emails.html", title=title)
        elif request.form["massEmail"] == "email_lib":
            email_lib_batch_emails: bool = send_batch_emails_from_email_lib(
                email_subject, content
            )
            if email_lib_batch_emails is None:
                flash("Could not send email. There are no emails stored in database.")
                return redirect(url_for("send_mass_emails"))
            flash("Your email has been sent!")
            return render_template("mass_emails.html", title=title)
        else:
            if request.form["massEmail"] == None:
                flash("You forgot to select an email source.")
                return redirect(url_for("send_mass_emails"))


@app.route("/email-library", methods=["GET", "POST"])
@login_required
def email_library():
    if request.method == "GET":
        return render_template("email_library.html", title=title)
    else:
        session: SessionLocal = SessionLocal()
        name: str = request.form["name"]
        email: str = request.form["email"]
        new_entry: EmailLibrary = add_to_email_library(name, email)
        session.add(new_entry)
        session.commit()
        # get all email entries
        data: EmailLibrary = session.query(EmailLibrary).order_by(EmailLibrary.id).all()
        flash(f"You have stored {name}'s email to the Aurous79® Email Library")
        # display all entries
        return render_template("email_library,html", title=title, data=data)


# creating dash graph
aurous_graph: dash = dash.Dash(
    __name__, server=app, routes_pathname_prefix="/aurous-graph/"
)
aurous_graph.layout = html.Div(
    children=[
        html.H1(children="Aurous79 Customer Analysis"),
        html.Div(
            children="""
        Aurous79 Customer Analysis
    """
        ),
        dcc.Graph(
            id="aurous-graph-1",
            figure={
                "data": [
                    {"x": [1], "y": [male_y()], "type": "bar", "names": "Males"},
                    {"x": [2], "y": [female_y()], "type": "bar", "name": "Females"},
                ],
                "layout": {"title": "Aurous79 Visitors by Gender"},
            },
        ),
        html.Div(
            """This graph displays the contrast between male & female customers who complete the Aurous79 feedback form."""
        ),
        dcc.Graph(
            id="aurous-graph-2",
            figure={
                "data": [
                    {
                        "x": [1],
                        "y": [first_visit_y()],
                        "type": "bar",
                        "name": "New Visitors",
                    },
                    {
                        "x": [2],
                        "y": [return_visit_y()],
                        "type": "bar",
                        "name": "Customer Services",
                    },
                    {
                        "x": [3],
                        "y": [shisha_y()],
                        "type": "bar",
                        "name": "Tried Shihsa",
                    },
                ],
                "layout": {"title": "Aurous79 Customer Relations"},
            },
        ),
        html.Div(
            """This graph displays the number of customers that were first time customers, customers that would return and customers that tried the shisha."""
        ),
        dcc.Graph(
            id="aurous-graph-3",
            figure={
                "data": [
                    {
                        "x": [clean_x()],
                        "y": [clean_y()],
                        "type": "bar",
                        "name": "Cleaniness Rating",
                    },
                    {
                        "x": [service_x()],
                        "y": [service_y()],
                        "type": "bar",
                        "name": "Customer Service Rating",
                    },
                    {
                        "x": [speed_x()],
                        "y": [speed_y()],
                        "type": "bar",
                        "name": "Speed Rating",
                    },
                ],
                "layout": {"title": "Overall Aurous79 Customer Rating"},
            },
        ),
        html.Div(
            """This graph displays the average ranking (out of 5) for Cleaniness, Customer Service and Speed by customers."""
        ),
    ]
)

if __name__ == "__main__":
    aurous_graph.run_server(debug=True)


# status codes
# 200 - ok
# 201 - created
# 202 - accepted
# 204 - no content
# 301 - moved permanently
# 302 - found
# 304 - not modified
# 307 - temporary redirect (same as 302)
# 308 - permanent redirect (same as 301)

# 400 - bad request
# 401 - unauthorized
# 403 - forbidden
# 404 - not found
# 405 - method not allowed
# 500 - internal server error
# 501 - not implemented
