from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
#This fun function returns link_content which for now is just the link given as input by user derived to this program by POST method
def fun():
    if request.method == "POST":
        link_content = request.form['link']
        return link_content 

    else:
        return render_template('index.html')
#This function return a list of 55 variable which will be calculated in this or in other function by the help of string link which contains a webpage
def getLink(link):
    ls =[]
    return ls 

if __name__ == '__main__':
    app.run(debug=True)













