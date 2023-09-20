import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# This function takes a DataFrame 'data' as input and performs some data preprocessing and clustering.
def job_class(data):
    # Extracting specific columns from the input DataFrame
    train_data = data[['involvement', 'workplace_type', 'employee_count',
                       'followers_count', 'applicants']]
    
    # Performing one-hot encoding on categorical columns 'involvement' and 'workplace_type'
    train_data = pd.get_dummies(train_data, columns=['involvement', 'workplace_type'],
                                drop_first=True)
    
    # Converting selected columns to numeric values and handling any conversion errors with 'coerce'
    train_data['employee_count'] = pd.to_numeric(train_data['employee_count'], errors='coerce')
    train_data['followers_count'] = pd.to_numeric(train_data['followers_count'], errors='coerce')
    train_data['applicants'] = pd.to_numeric(train_data['applicants'], errors='coerce')
    
    # Filling missing values in numeric columns with median and mean respectively
    train_data['employee_count'] = train_data['employee_count'].fillna(train_data['employee_count'].median())
    train_data['followers_count'] = train_data['followers_count'].fillna(train_data['followers_count'].mean())
    train_data['applicants'] = train_data['applicants'].fillna(train_data['applicants'].mean())
    
    # Creating a KMeans clustering model with 4 clusters
    kmeans = KMeans(n_clusters=4)
    
    # Fitting the KMeans model on the preprocessed data
    kmeans.fit(train_data)
    
    # Predicting cluster labels for each data point
    class_ = kmeans.predict(train_data)
    
    # Mapping cluster labels to human-readable class names
    data['job_class'] = class_
    data['job_class'] = data['job_class'].map({0: 'Class 1', 1: 'Class 2', 2: 'Class 3', 3: 'Class 4'})
    
    # Returning the input DataFrame with an additional 'job_class' column containing class labels
    return data

    
