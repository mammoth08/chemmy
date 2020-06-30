from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html', name=username)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    # return 'form rubbmitted hooorayy!'
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def login():
#     return render_template('contact.html')

# @app.route('/register.html')
# def contact():
#     return render_template('register.html')

# @app.route('/favicon.ico')