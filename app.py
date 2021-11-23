from flask import Flask, redirect, url_for, render_template, request
from urlparse import urlparse
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
#This fun function returns link_content which for now is just the link given as input by user derived to this program by POST method
def fun():
    if request.method == "POST":
        link_content = request.form['link']
        if predict(getLink(link_content))==1:
            return  render_template('phishing.html')
        else:
            return render_template('legitimate.html')

    else:
        return render_template('index.html')



#This function return a list of 55 variable which will be calculated in this or in other function by the help of string link which contains a webpage
def getLink(link):
    pt=urlparse(url).path
    nl=urlparse(url).netloc
    prms=urlparse(url).params
    qry=urlparse(url).query



    ls =[]
    return ls 
def predict(ls):
    return 0


if __name__ == '__main__':
    app.run(debug=True)













