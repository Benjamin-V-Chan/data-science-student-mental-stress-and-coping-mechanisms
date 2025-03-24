# data-science-student-mental-stress-and-coping-mechanisms

## Project Overview
This project performs data cleaning, exploratory analysis, feature engineering, visualization, and predictive modeling on a dataset of students' mental stress levels and coping mechanisms. The goal is to explore relationships between academic, social, and lifestyle factors and understand what contributes to student stress.

## Folder Structure
```
project-root/
├── data/                     # Original raw dataset (CSV format)
├── outputs/                  # Cleaned data, plots, models, metrics
├── scripts/                  # Python scripts for each stage of the pipeline
│   ├── 01_load_and_clean.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   └── 05_visualizations.py
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Run the Scripts:
Each script should be executed from the project-root directory.

```bash
# Clean and prepare the data
python scripts/01_load_and_clean.py

# Generate summary statistics and categorical distributions
python scripts/02_eda.py

# Create dummy variables and new features
python scripts/03_feature_engineering.py

# Train and evaluate a logistic regression model
python scripts/04_modeling.py

# Generate plots and visualizations
python scripts/05_visualizations.py
```

## Requirements
- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install using:
```bash
pip install -r requirements.txt
```

## Acknowledgments
**Dataset Name**: Student Mental Stress and Coping Mechanisms  
**Dataset Author**: Salahuddin Ahmed  
**Dataset Source**: https://www.kaggle.com/datasets/salahuddinahmedshuvo/student-mental-stress-and-coping-mechanisms