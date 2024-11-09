from flask import Flask,request
import json

app=Flask(__name__)

@app.route('/')
def home():
    dict_a={
        "name" : "batman"
    }
    return json.dumps(dict_a,indent=4)


@app.route('/user')
def users():
    name=request.args["name"]
    age=request.args["age"]

    return "<h1>UserName is {} and age is {}</h1>".format(name,age)

if __name__=="__main__":
    app.run("0.0.0.0",5000)
    print("Hello World")

