from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
@app.route('/')
def fun():
    return render_template('index.html')

# @app.route('/ <link>')
# def getLink(link):
#     return link 




if __name__ == '__main__':
    app.run(debug=True)













