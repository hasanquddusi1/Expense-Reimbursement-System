from flask import Flask, redirect, url_for, render_template, request, jsonify, flash, make_response
from pyodbc import connect
import os
import logging
app = Flask(__name__)
app.secret_key = "hello"

# application logger
logging.basicConfig(
    filename="C://Users//hasan//project1//log//app_logger.log",
    format='%(asctime)s:%(levelname)s: %(message)s',
    datefmt='%m/%d/%Y')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# db connection env variables
db_url = os.environ['db_url']
db_username = os.environ['db_username']
db_password = os.environ['db_password']
db_name = os.environ['db_name']


def get_connection():
    return connect(
        f"DRIVER={{PostgreSQL UNICODE}};SERVER={db_url};PORT=5432;DATABASE={db_name};UID={db_username};PWD={db_password};Trusted_Connection=no")


@app.route("/")
@app.route("/home")
def homepage():
    return render_template('base.html')


@app.route("/employee")
# employee login portal
def EmployeeLogin():
    return render_template("employee_login_page.html")


@app.route("/admin")
# manager login portal
def ManagerLogin():
    return render_template("manager_login_page.html")


@app.route("/employee/login", methods=['GET', 'POST'])
# employee username and password validation and proceed to employee dashboard
def validate_employee():
    # form = LoginForm('index.html', form = form)
    username = request.form['user_name']
    user_password = request.form['user_password']
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    # print(username)
    # print(user_password)
    db_cursor.execute(
        "SELECT emp_id FROM employees where emp_username = ? and emp_password = ?", (username, user_password))
    query_row = db_cursor.fetchone()
    logger.info(str(query_row))
    db_cursor.close()
    db_connection.close()
    if query_row:
        return render_template("reimbursement_form.html"), flash("logged in")
    else:
        message = "Incorrect username or password"
        return render_template("employee_login_page.html", message=message)


@app.route("/submit-request", methods=['GET', 'POST'])
# submit reimbursement request
def reimbursement_request():
    empid = request.form['emp_id']
    item = request.form['item']
    cost = request.form['cost']
    purpose = request.form['purpose']
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "Insert into reimb_report (emp_id, item, item_cost,purpose) values (?,?,?,?)", (empid, item, cost, purpose))
    db_connection.commit()
    db_connection.close()
    return render_template("reimbursement_form.html")


@app.route("/manager-view", methods=['GET', 'POST'])
# manager username and password validation and proceed to manager view
def validate_manager():
    mgr_username = request.form['mgr_name']
    mgr_password = request.form['mgr_password']
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "SELECT manager_id FROM managers where manager_username = ? and manager_password = ?", (mgr_username, mgr_password))
    query_row = db_cursor.fetchone()
    logger.info(str(query_row))
    # display all requests
    db_cursor.execute("Select * from reimb_report")
    query_rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    if query_row:
        return render_template("manager_view.html", all_requests=query_rows)

    else:
        message = "Incorrect username or password"
        return render_template("manager_login_page.html", message=message)


@app.route("/submitted-requests", methods=['GET'])
def submitted_requests():
    # To redirect manager back to manager view after submitting approve/deny request
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute("Select * from reimb_report")
    query_rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return render_template("manager_view.html", all_requests=query_rows)


@ app.route('/view-requests', methods=['POST'])
# view all reimbursements request past and present by employee id
def view_all_requests():
    employee_id = request.form['emp_id']
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "Select * from reimb_report where emp_id = ?", (employee_id))
    query_rows = db_cursor.fetchall()
    logger.info(str(query_rows))
    db_cursor.close()
    db_connection.close()
    return render_template("reimbursement_table.html", requests=query_rows)


@app.route('/submit-request-decision', methods=['POST', 'PUT'])
def request_decision():
    # Submit request decision form
    request_decision = request.form['mgr_decision']
    manager_name = request.form['manager_name']
    request_id = request.form['request_id']
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "update reimb_report set req_status = ? where request_id =?", (request_decision, request_id))
    db_cursor.execute(
        "update reimb_report set manager_name = ? where request_id =?", (manager_name, request_id))
    db_connection.commit()
    db_connection.close()
    return redirect(url_for('submitted_requests'))


@app.route('/leave-feedback', methods=['POST'])
def manager_feedback():
    # Leave optional manager feedback
    req = request.get_json()
    res = make_response(jsonify(req), 200)
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        "update reimb_report set feedback = ? where request_id =?", (
            req["message"], req["request_id"]))
    db_connection.commit()
    db_connection.close()
    return res


@app.route('/view-statistics', methods=['GET'])
def employee_stats():
    # Pull reimbursement statistics from db
    db_connection = get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute("select * from reimb_stats")
    query_rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return render_template('statistics.html', stats=query_rows)


if __name__ == "__main__":
    app.run(debug=True)
