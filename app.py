from flask import Flask,redirect,render_template,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('cv.html')

@app.route('/assignment8')
def assign_func():  # put application's code here
    name = 'ori'
    uni = 'BGU'
    second_name = 'milbauer'
    # simulate like search in the DB
    found = True
    if found:
        return render_template('assignment8.html', name=name, uni=uni, second_name=second_name,
                               musics=['hip-hop', 'R&B', 'Soul'])
    else:
        # without name-> so not get into logged in section
        return render_template('assignment8.html', uni=uni, second_name=second_name, musics=['hip-hop', 'R&B', 'Soul'])

if __name__ == '__main__':
    app.run()
