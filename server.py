from flask import Flask,render_template,request, flash, session, redirect
app = Flask(__name__)
app.secret_key = "twinjuan"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    form_name = request.form['form_name']
    if len(form_name) < 1:
        flash("Name cannot be empty!")
        return redirect("/")
    form_location = request.form['form_location']
    form_lang = request.form['form_lang']
    form_description = request.form['form_description']
    if len(form_description) < 1:
        flash("Description cannot be empty!")
        return redirect("/")
    elif len(form_description) > 120:
        flash("Description cannot be more than 120")
        return redirect("/")
    return render_template('result.html',web_name = form_name, web_location = form_location, web_lang = form_lang, web_description = form_description)

app.run(debug=True)