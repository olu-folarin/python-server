from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# store the captured data
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# grab and store form data in a text file
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():  
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'something is broken!!'
    else:
        return 'something went wrong. Resubmit!'
    
# store data in a csv file
def write_to_csv(data):
    with open('database.csv',  newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# @app.route("/works.html")
# def projects():
#     return render_template("./works.html")

# @app.route("/about.html")
# def about():
#     return render_template("./about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")

# @app.route("/components.html")
# def components():
#     return render_template("./components.html")