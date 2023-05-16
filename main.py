from flask import Flask
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def flaskdemo():
    return 'this is flask demo'
if __name__== "__main__":
    app.run()
