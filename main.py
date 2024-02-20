from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)



@app.route('/')
def home():
    # # Get the apple data using yfinance
    # apple = yf.Ticker("aapl")
    # info = apple.info
    # return render_template('home.html', apple_info=info)
    companies = (
('Shell', 'SHEL'),
('AstraZeneca', 'AZN'),
('HSBC Holdings', 'HSBA'),
('BHP Group', 'BHP'),
('Unilever', 'ULVR'),
('Rio Tinto', 'RIO'),
('GlaxoSmithKline', 'GSK'),
('Diageo', 'DGE'),
('RELX', 'REL'),
('British American Tobacco', 'BATS'),
('Glencore', 'GLEN'),
('London Stock Exchange Group', 'LSEG'),
('Reckitt Benckiser Group', 'RB'),
('BAE Systems', 'BA'),
('Compass Group', 'CPG'),
('National Grid', 'NG'),
('Experian', 'EXPN'),
('Flutter Entertainment', 'FLTR'),
('Haleon', 'HLN'),
('Lloyds Banking Group', 'LLOY'),
('Rolls-Royce Group', 'RR'),
('Anglo American', 'AAL'),
('3i Group', 'III'),
('Ashtead Group', 'AHT'),
('Prudential', 'PRU')
)

    companies_info = []
    for company, symbol in companies:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        if info.get('symbol') is not None:
            companies_info.append({'name': company, 'info': info})

    return render_template('home.html', companies_info=companies_info)

@app.route('/company/<symbol>')
def company(symbol):
    return render_template('company.html', symbol=symbol)


if __name__ == '__main__':
    app.run(debug=True)
