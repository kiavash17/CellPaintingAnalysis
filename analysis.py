
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
import boto3
import os

def fetch_data_from_s3(bucket_name, file_key, local_file):
    # Initialize a session using boto3 to access the S3 bucket
    s3 = boto3.client('s3')
    
    # Download the file from S3 to local directory
    if not os.path.exists(local_file):
        s3.download_file(bucket_name, file_key, local_file)
    return pd.read_csv(local_file)

def preprocess_data(data):
    features = data.columns[:-1]  # Assuming last column is 'perturbation'
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[features])
    return scaled_data

def perform_pca(scaled_data, data, n_components=2):
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(scaled_data)
    data['PCA1'] = pca_result[:, 0]
    data['PCA2'] = pca_result[:, 1]
    
    # Plotting the PCA result
    plt.figure(figsize=(8,6))
    for perturbation in data['perturbation'].unique():
        subset = data[data['perturbation'] == perturbation]
        plt.scatter(subset['PCA1'], subset['PCA2'], label=perturbation)
    plt.title('PCA of Morphological Features by Perturbation')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
    
def calculate_similarity(data):
    control_group = data[data['perturbation'] == 'control'][['PCA1', 'PCA2']]
    treated_groups = data[data['perturbation'] != 'control'][['PCA1', 'PCA2', 'perturbation']]
    control_centroid = control_group.mean().values.reshape(1, -1)
    treated_groups['distance_from_control'] = cdist(treated_groups[['PCA1', 'PCA2']], control_centroid, metric='euclidean')
    
    # Ranking perturbations based on distance from control
    treated_groups = treated_groups.sort_values(by='distance_from_control', ascending=False)
    return treated_groups

def visualize_ranking(treated_groups):
    # Visualization of Rankings
    plt.figure(figsize=(10,6))
    top_10_perturbations = treated_groups[['perturbation', 'distance_from_control']].head(10)
    plt.barh(top_10_perturbations['perturbation'], top_10_perturbations['distance_from_control'], color='skyblue')
    plt.xlabel('Distance from Control (Euclidean)')
    plt.title('Top 10 Perturbations by Distance from Control Group')
    plt.gca().invert_yaxis()
    plt.show()
    
def main():
    # Example usage with actual S3 data path
    bucket_name = 'cellpainting-gallery'
    file_key = 'cpg0016-jump-assembled/source_all/workspace/profiles/jump-profiling-recipe_2024_a917fa7/your_file.csv'  # Replace with actual path
    local_file = 'jump_profiles.csv'
    
    # Fetch and preprocess data
    data = fetch_data_from_s3(bucket_name, file_key, local_file)
    scaled_data = preprocess_data(data)
    
    # Perform PCA and visualize
    perform_pca(scaled_data, data)
    
    # Calculate similarity and visualize ranking
    treated_groups = calculate_similarity(data)
    visualize_ranking(treated_groups)

if __name__ == '__main__':
    main()
