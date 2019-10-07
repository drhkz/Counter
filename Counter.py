from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    count = 0
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1


    return render_template("index.html", count = count)
@app.route('/count', methods=['Post','Get'])
def counter():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['Post', 'Get'])
def reset():
    session.clear()
    return redirect('/')

# @app.route('/counted', methods=['Post'])
# def counted():
#     return redirect

if __name__=="__main__":
    app.run(debug=True)