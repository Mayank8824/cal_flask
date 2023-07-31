from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    return "<h1>Welcome to the Flask</h1>"

@app.route('/cal',methods=["GET"])
def math_operate():
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    
    if operation=='add':
        results=num1+num2
    elif operation=='multiply':
        result=num1*num2
    elif operation=='sub':
        result=num1-num2
    else:
        result=num1/num2    
    return result


if __name__=="__main__":
    app.run(debug=True)