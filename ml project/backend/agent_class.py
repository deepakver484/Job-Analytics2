import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def job_class(data):
    train_data = data[['involvement', 'workplace_type', 'employee_count',
                       'followers_count', 'applicants']]
    train_data = pd.get_dummies(train_data, columns = ['involvement', 'workplace_type'],
                                drop_first= True)
    train_data['employee_count'] = pd.to_numeric(train_data['employee_count'], errors = 'coerce')
    train_data['followers_count'] = pd.to_numeric(train_data['followers_count'], errors = 'coerce')
    train_data['applicants'] = pd.to_numeric(train_data['applicants'], errors = 'coerce')
    train_data['employee_count'] = train_data['employee_count'].fillna(train_data['employee_count'].median())
    train_data['followers_count'] = train_data['followers_count'].fillna(train_data['followers_count'].mean())
    train_data['applicants'] = train_data['applicants'].fillna(train_data['applicants'].mean())
    
    #n_cluster value is 4 
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(train_data)
    class_ = kmeans.predict(train_data)
    data['job_class'] = class_
    data['job_class'] = data['job_class'].map({0:'Class 1',1:'Class 2',2: 'Class 3',3: 'Class 4'})
    return data
    
def log_class():
    log_text = f'''Class added successfully done........
    ------------------------------------------------
    '''
    return log_text