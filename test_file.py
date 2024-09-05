from flask import Flask,request
app = Flask(__name__)

@app.get("/")
def fun():
    name = request.args.get("name")
    if name is None:
        return "helloworld"
    return "hello mr "+name+" nice to meet u"
app.run(host=0.0.0.0,port=5000)
