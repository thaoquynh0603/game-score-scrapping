import os
import pandas as pd
folder_path = r'D:\14. Data Science\[Project - ongoing] Game Score Data Scraping\ign'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
dfs = []
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.columns = ['Index','ign_score', 'ign_user','ign_note']
data = pd.read_csv('data.csv')
combined_df = pd.concat([data, combined_df],axis=1).drop('Index', axis=1)
combined_df.to_csv('finalign.csv', index=False)
