from flask import Flask, render_template



app = Flask(__name__)





@app.route('/')
def dashboard():
    return render_template('dashboard.html', plot_html=plot_html)

@app.route('/map')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)