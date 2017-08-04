from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    form_name = request.form['form_name']
    form_location = request.form['form_location']
    form_lang = request.form['form_lang']
    form_description = request.form['form_description']
    return render_template('result.html',web_name = form_name, web_location = form_location, web_lang = form_lang, web_description = form_description)

app.run(debug=True)