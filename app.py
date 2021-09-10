from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def fun():
    if request.method == "POST":
        link_content = request.form['link']
        return link_content 

    else:
        return render_template('index.html')


def getLink(link):
    ls =[]
    return ls 




if __name__ == '__main__':
    app.run(debug=True)













