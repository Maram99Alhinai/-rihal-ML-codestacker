# Rihal-ML-codestacker

## 🏆 Crime Analytics Dashboard

This project was developed for the competition organized by the Rihal team. It combines exploratory data analysis, machine learning, and interactive visualization to analyze crime data and provide actionable insights.

## 📊 Project Overview

This repository contains a comprehensive crime analysis solution with:

- **Data Exploration**: In-depth analysis of crime patterns and trends
- **Machine Learning Models**: For crime classification and severity prediction
- **Interactive Dashboard**: A Flask-based web application for visualization and reporting

## 📁 Repository Structure

```
Rihal-ML-codestacker/
├── EDA with Geo-Spatial Mapping.ipynb    # Exploratory data analysis with geographic visualizations
├── Crime Classification.ipynb            # ML models for classifying crime types
├── Crime Severity.ipynb                  # ML models for predicting crime severity
├── Dashboard/                            # Web application directory
│   ├── app.py                            # Main Flask application
│   ├── templates/                        # HTML templates
│   ├── static/                           # CSS, JS, and assets
│   └── uploads/                          # Directory for uploaded reports
└── requirements.txt                      # Project dependencies
```

## 🔍 Jupyter Notebooks

The repository includes three detailed Jupyter notebooks:

1. **EDA with Geo-Spatial Mapping.ipynb**
   - Comprehensive data exploration
   - Geographic visualization of crime hotspots
   - Temporal analysis of crime patterns

2. **Crime Classification.ipynb**
   - Feature engineering for crime type prediction
   - Comparative analysis of classification algorithms
   - Evaluation metrics and model selection

3. **Crime Severity.ipynb**
   - Methodologies for quantifying crime severity
   - Predictive modeling for severity assessment
   - Model performance and validation

## 🚀 Getting Started

Follow these steps to set up and run the dashboard application:

### Prerequisites

- Python Python 3.11.4
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Maram99Alhinai/-rihal-ML-codestacker.git
   cd Rihal-ML-codestacker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv Renv
   
   # On Windows
   Renv\Scripts\activate
   
   # On macOS/Linux
   source Renv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   cd Dashboard
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 🔧 Features

- **Interactive Maps**: Visualize crime data geographically
- **Real-time Analytics**: Dynamic dashboard with key metrics
- **Predictive Insights**: ML-powered crime classification and severity prediction
- **Report Upload**: Upload and analyze PDF crime reports
- **Data Visualization**: Multiple plot types for comprehensive data representation

## 📊 Dashboard

The web application includes:

- Main dashboard with 4 interactive plots arranged in a grid
- Three key metric boxes displaying important statistics
- Geographic mapping of crime incidents
- Report upload functionality for PDF processing

## 🛠️ Technologies Used

- **Data Analysis**: Pandas, NumPy, 
- **Machine Learning**: Scikit-learn
- **Visualization**: Plotly, Matplotlib, folium, seaborn
- **Web Application**: Flask, HTML, CSS, JavaScript
- **Report Processing**: PyPDF2

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

Special thanks to the Rihal team for organizing this competition and providing the opportunity to work on this challenging problem.