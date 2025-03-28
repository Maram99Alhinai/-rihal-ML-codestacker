from flask import Flask, render_template



app = Flask(__name__)




@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload_report')
def map_page():
    return render_template('report_data.html')

if __name__ == '__main__':
    app.run(debug=True)