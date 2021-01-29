from flask import Flask, request, jsonify, render_template
from Payment import PaymentGateway
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ProcessPayment',methods=['POST'])
def ProcessPayment():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    print(features)
    obj = PaymentGateway(features[0],features[1],features[2],features[3],int(features[4]))
    output = obj.process()
    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)
