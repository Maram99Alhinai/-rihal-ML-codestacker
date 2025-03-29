import os
import PyPDF2
import pandas as pd 
import joblib
import re
import string



# Ensure you have a folder for uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           

def extract_pdf_data(filename):
    """
    Extract data from PDF with generalized handling for multi-line fields.
    """
    try:
        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Extract text from first page
            first_page = reader.pages[0]
            text = first_page.extract_text()
            lines = [line.strip() for line in text.split('\n')]
            extracted_data = {}
            
            # List of all expected field names
            expected_fields = [
                "Report Number", "Date & Time", "Reporting Officer", 
                "Incident Location", "Coordinates", "Detailed Description",
                "Police District", "Resolution", "Suspect Description", 
                "Victim Information"
            ]
            
            current_field = None
            current_value = []
            
            for line in lines:
                # Check if this line contains a field name
                found_field = False
                for field in expected_fields:
                    if line.startswith(field + ":"):
                        # Save the previous field if there was one
                        if current_field:
                            extracted_data[current_field] = ' '.join(current_value).strip()
                        
                        # Start a new field
                        current_field = field
                        value_part = line[len(field) + 1:].strip()  # +1 for the colon
                        current_value = [value_part]
                        found_field = True
                        break
                
                # If no field name was found, append to the current value
                if not found_field and current_field:
                    current_value.append(line)
            
            # Don't forget to add the last field
            if current_field:
                extracted_data[current_field] = ' '.join(current_value).strip()
            
            return extracted_data
    except Exception as e:
        print(f"Error extracting PDF data: {e}")
        return {}





#load the models 
rf_model = joblib.load("Models/crime_classification_model.pkl")
vectorizer = joblib.load("Models/tfidf_vectorizer.pkl")
    


def classify_crime_severity(category):
    """
    Function that takes the crime category as input
    and classifies it into the corresponding severity level.
    """

    # Define severity levels using a dictionary
    severity_dict = {
        'severity level 1': {'NON-CRIMINAL', 'SUSPICIOUS', 'OCCURRENCE', 'MISSING PERSON', 'RUNAWAY', 'RECOVERED VEHICLE'},
        'severity level 2': {'WARRANTS', 'OTHER OFFENSES', 'VANDALISM', 'TRESPASS', 'DISORDERLY CONDUCT', 'BAD CHECKS'},
        'severity level 3': {'LARCENY/THEFT', 'VEHICLE THEFT', 'FORGERY/COUNTERFEITING', 'DRUG/NARCOTIC', 'STOLEN PROPERTY', 'FRAUD', 'BRIBERY', 'EMBEZZLEMENT'},
        'severity level 4': {'ROBBERY', 'WEAPON LAWS', 'BURGLARY', 'EXTORTION'},
        'severity level 5': {'KIDNAPPING', 'ARSON'}
    }

    # Find the severity level
    for severity, categories in severity_dict.items():
        if category in categories:
            return severity

    return "Sorry, this crime severity level is not defined."
        
        
        
def clean_text(text):
    text = text.lower()  # Lowercase text
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = text.strip()  # Remove extra spaces
    return text


def crime_category_and_severity(description):
    """
    Predicts the crime category and severity level based on a given crime description.
    """
    clean_description = clean_text(description)
    vectorized_description = vectorizer.transform([clean_description])
    category = rf_model.predict(vectorized_description)
    severity = classify_crime_severity(category[0])
    
    print(f"This crime belongs to the category '{category[0]}' with {severity}.")
    return category[0], severity