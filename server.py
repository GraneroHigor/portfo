from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def cap_informations(data):
    with open('database.txt', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        cap_informations(data)
        return redirect('/thanks.html')
    else:
        return 'teste2'

                    


"""
@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def components():
    return render_template('components.html')
#@app.route('/teste')
#def teste():
#    return render_template('index.html')
"""
