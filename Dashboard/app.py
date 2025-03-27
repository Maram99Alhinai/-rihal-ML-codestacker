from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import folium


app = Flask(__name__)

df = pd.read_csv('Competition_Dataset.csv')
df['Dates'] = pd.to_datetime(df['Dates'])
df['hour'] = df['Dates'].dt.hour


# Count crimes per hour
crime_by_hour = df.groupby('hour').size().reset_index(name='crime_count')
# Create histogram with adjustable bins
fig_1 = px.histogram(df, x='hour', nbins=12,  
                   title='Crime Traffic During the Day',
                   labels={'hour': 'Hour of the Day', 'count': 'Number of Crimes'},
                   color_discrete_sequence=['skyblue'])
fig_1.update_traces(marker=dict(line=dict(color='black', width=1.5)))
plot_html = fig_1.to_html(full_html=False)



@app.route('/')
def dashboard():
    return render_template('dashboard.html', plot_html=plot_html)

@app.route('/map')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)