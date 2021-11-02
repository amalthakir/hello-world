from flask_bootstrap import Bootstrap

app = Flask(_name_)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if _name_ == '_main_':
    app.run()
