
# Cell Painting Analysis

This repository provides a Python package for analyzing morphological features from Cell Painting data using PCA and perturbation ranking.

## Features:
- Fetch data from an S3 bucket (Cell Painting Gallery)
- Perform PCA on morphological features
- Rank perturbations based on similarity to control group
- Visualize PCA results and perturbation rankings

## Usage:
1. Install the required dependencies using `pip install -r requirements.txt`
2. Run the analysis using `python analysis.py`

## Dependencies:
- pandas
- numpy
- matplotlib
- scikit-learn
- boto3
- scipy
