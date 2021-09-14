from flask import Flask, request, jsonify
import flask

app=Flask(__name__)

@app.route("/",methods=["GET"])
def inicio():
    return jsonify({"mensaje":"Server levantado"})

if __name__ == "__main__":
    app.run(port=3000, debug=True)    
