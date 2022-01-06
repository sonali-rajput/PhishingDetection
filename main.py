from flask import Flask, redirect, url_for, render_template, request
import keras
from src.features import feature
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from src.data import data

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
#This fun function returns link_content which for now is just the link given as input by user derived to this program by POST method
def fun():
    if request.method == "POST":
        link_content = request.form['link']
        phish_value = predict(getLink(link_content))
        objofdata = data(link_content,phish_value)
        if phish_value == 1:
            return  render_template('phishing.html')
        else:
            return render_template('legitimate.html')
    else:
        return render_template('index.html')



#This function return a list of 55 variable which will be calculated in this or in other function by the help of string link which contains a webpage
def getLink(link):
    object1 = feature(link)
    #print(object1.ht)
    lt = [[
        object1.searchingQuestionMark(object1.directory),
        object1.timeActivation(object1.ht),
        object1.emailInUrl(object1.url),
        object1.searchingDot(object1.filename),
        object1.searchingSlash(object1.url),
        object1.searchingDot(object1.directory),
        object1.searchingDot(object1.qry),
        object1.searchingEqual(object1.url),
        object1.searchingQuestionMark(object1.qry),
        object1.searchingUnderline(object1.directory),
        object1.urlShort(object1.url),
        object1.searchingUnderline(object1.qry),
        object1.Length(object1.directory),
        object1.qtyAndUrl(object1.url),
        object1.searchingHyphen(object1.directory),
        object1.searchingHyphen(object1.filename),
        object1.searchingUnderline(object1.url),
        object1.searchingHyphen(object1.qry),
        object1.searchingAt(object1.directory),
        object1.Length(object1.url),
        object1.DomainInIP(object1.ht),
        object1.searchingSlash(object1.qry),
        object1.ssl(object1.url),
        object1.searchingHyphen(object1.url),
        object1.searchingAsterisk(object1.directory),
        object1.searchingHyphen(object1.ht),
        object1.ttlHostname(object1.ht),
        object1.Length(object1.qry),
        object1.searchingDot(object1.url),
        object1.searchingQuestionMark(object1.url),
        object1.Length(object1.filename),
        object1.timeExpiration(object1.ht),
        object1.searchingDot(object1.ht),
        object1.searchingPercent(object1.qry),
        object1.asn(object1.ht),
        object1.searchingAt(object1.url),
        object1.countnameservers(object1.ht),
        object1.searchingTilde(object1.url),
        object1.searchingPercent(object1.directory),
        object1.CountVowels(object1.ht),
        object1.serverClientDomain(object1.ht),
        object1.countmxservers(object1.ht),
        object1.searchingDollar(object1.url),
        object1.lenthTldUrl(object1.url),
        object1.searchingSpace(object1.url),
        object1.countRedirects(object1.url),
        object1.searchingExclamation(object1.url),
        object1.searchingUnderline(object1.ht),
        object1.Length(object1.ht),
        object1.searchingAsterisk(object1.url),
        object1.searchingComma(object1.url),
        object1.ipresolvecount(object1.ht),
        object1.searchingHashtag(object1.url),
        object1.timeResponse(object1.ht)
        ]]
    return lt



#     ls =[]
#     return ls 
def predict(ls):
    """
    first we standardize given user data
    """
    Tf_standarization = ls
    scaler=MinMaxScaler()
    # x= scaler.fit_transform(x)
    scaler.fit(Tf_standarization)
    scaled_f = scaler.transform(Tf_standarization)
    df_tf = pd.DataFrame(scaled_f,columns=Tf_standarization[:])
    df_tf.head()
    obj = keras.models.load_model("final_model")
    obj = keras.models.load_model("final_topFeautures.pb")
    value = obj.predict(ls)[0][0]
    # print(value[0])
    return int(value)


if __name__ == '__main__':
    app.run(debug=True)













