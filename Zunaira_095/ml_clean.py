import pandas as pd

# 1. Load the Excel file (Notice the .xlsx extension)
file_path = 'ML_Categorized_Separated.xlsx'
df = pd.read_excel(file_path)

# 2. Fix typos and standardize names for Skills
skills_map = {
    'pactical': 'practical',
    'soft': 'soft skills',
    'others': 'other'
}
df['category_skills'] = df['category_skills'].replace(skills_map)

# 3. Fix typos and standardize names for University
uni_map = {
    'techniacl': 'technical',
    'communication': 'soft skills',
    'other': 'other'
}
df['category_uni'] = df['category_uni'].replace(uni_map)

# 4. Final cleanup: Strip any accidental spaces and make lowercase
df['category_skills'] = df['category_skills'].str.lower().str.strip()
df['category_uni'] = df['category_uni'].str.lower().str.strip()

# 5. Save the final, polished version
df.to_excel('FINAL_Capstone_Data.xlsx', index=False)

print("--- Cleanup Complete! ---")
print("New category counts for Skills:")
print(df['category_skills'].value_counts())
print("\nNew category counts for University:")
print(df['category_uni'].value_counts())