from flask import Flask,render_template, url_for,request ,redirect
app =Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def load(page_name):
    return  render_template(page_name)


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method =="POST":
        data = request.form.to_dict()
        print(data)
        write(data)
        return redirect("/thanku.html")
    else:
        return "something went wrong"
def write(data):
    with open("text.txt" , mode="a") as da:
        email =data["email"]
        subject = data["subject"]
        message = data["message"]
        file = da.write(f"\n{email},{subject},{message}")

if __name__=="__main__":
    app.run(debug=True)