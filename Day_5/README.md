# Day 5 - Feature Engineering

## Objective
Prepare the dataset for the recommendation 
model by converting raw data into 
machine learning ready format.

## What I Did
- Encoded categories using OneHotEncoder
- Normalized prices using MinMaxScaler
- Combined both into a Feature Matrix
- Saved feature matrix as CSV

## Why Feature Engineering?
- Model cannot understand text like "SUV"
- Price range was too wide ($68 - $1200)
- Encoding converts text to numbers
- Normalization brings prices to 0-1 range

## Output
feature_matrix.csv saved

## Tools Used
- Python
- Pandas
- Scikit-learn
- NumPy
- Jupyter Notebook