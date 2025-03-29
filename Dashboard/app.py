from flask import Flask, render_template
from flask import  render_template, request, redirect
import os
import PyPDF2
from utilize import *





app = Flask(__name__)

# Add this to your app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload_report', methods=['GET', 'POST'])
def upload_report():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If no file is selected, redirect back
        if file.filename == '':
            return redirect(request.url)
        
        # If file is allowed, process it
        if file and allowed_file(file.filename):
            # Save the file
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            
            # Extract data from PDF
            extracted_data = extract_pdf_data(filename)
            
            crime_sv = crime_category_and_severity(extracted_data["Detailed Description"])
            # Render template with extracted data
            return render_template('report_data.html', data=extracted_data ,crime_category_and_severity= crime_sv)
    crime_sv = 'It will appear after the upload'
    # GET request - show upload form
    return render_template('report_data.html',crime_category_and_severity= crime_sv)



if __name__ == '__main__':
    app.run(debug=True)