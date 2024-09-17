
# Cell Painting Analysis

This repository provides a Python package for analyzing morphological features from Cell Painting data using PCA and perturbation ranking.

## Introduction to Cell Painting
Cell Painting is an image-based, high-content screening method used to study the effects of various treatments (such as drugs or genetic modifications) on cells. By staining cells with multiple dyes, Cell Painting captures detailed images of cellular structures, allowing for the extraction of morphological features. These features can be used to identify and classify biological perturbations and predict drug mechanisms of action.

## Data Description
The data used in this analysis comes from the JUMP-Cell Painting dataset, available via the Cell Painting Gallery. This dataset contains morphological features extracted from cellular images after being treated with various perturbations, such as drugs or gene knockdowns. Each sample contains a set of features describing different aspects of the cell morphology, and the goal is to rank the perturbations based on their similarity to a control group.

## Running the Vignette
To run the analysis vignette:
1. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the analysis using the following command:
   ```bash
   python analysis.py
   ```

The script will:
1. Download the dataset from the S3 bucket.
2. Perform PCA to reduce the dimensionality of the morphological feature data.
3. Calculate the similarity of each perturbation to the control group.
4. Visualize the PCA results and generate a ranked list of perturbations based on their distance from the control group.

## What the Analysis Achieves
The analysis performs dimensionality reduction using PCA to identify the most significant morphological changes caused by various perturbations. It calculates the similarity between each perturbation and the control group, ranking them based on their distance from the control centroid. The perturbations that cause the most significant changes in morphology are ranked highest, helping identify treatments with the largest biological effect.

## Summary of Results
The results include:
- A PCA plot showing how the perturbations group based on their morphological features.
- A ranked list of perturbations showing which treatments have the largest morphological deviation from the control group.

This information can be used to infer the biological activity of various treatments and gain insights into their potential mechanisms of action.
