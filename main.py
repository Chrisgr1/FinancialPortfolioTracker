from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Get the apple data using yfinance
    import yfinance as yf
    apple = yf.Ticker("aapl")
    info = apple.info
    return render_template('home.html', apple_info=info)

@app.route('/company/<symbol>')
def company(symbol):
    return render_template('company.html', symbol=symbol)


if __name__ == '__main__':
    app.run(debug=True)
