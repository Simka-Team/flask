from flask import Flask, render_template, url_for
import time




time_now = time.gmtime(time.time())
##current_time = time.ctime(time.time())
current_time = ""

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html")




@app.route("/about")
def about():
    return "FAQ"





@app.route("/time")
def my_time():
    current_time = time.ctime(time.time())
    return str(current_time)




@app.route("/user/<string:name>/<int:id>")
def user_page(name, id):
    return name + "_" + str(id)



@app.route('/test')
def test_page():
    return render_template('testpage.html')





if __name__ == "__main__":
    app.run(debug=True)
