import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import ast

# Download the "dictionary" for lemmatization
nltk.download('wordnet')
nltk.download('omw-1.4')

# 1. Load the data with keywords
input_file = 'final_keywords_data.xlsx'
df = pd.read_excel(input_file)

# The columns containing our clean lists of words
keyword_cols = [
    'What skills do you think you are lacking for a job?_final_keywords', 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?_final_keywords'
]

# 2. Initialize the Lemmatizer
lemmatizer = WordNetLemmatizer()

# 3. Lemmatization Function
def lemmatize_tokens(token_list):
    # Ensure it's a list (Excel sometimes reads it as a string)
    if isinstance(token_list, str):
        try:
            token_list = ast.literal_eval(token_list)
        except:
            return []
    
    # Convert words to their root form (e.g., 'projects' -> 'project')
    return [lemmatizer.lemmatize(word) for word in token_list]

# 4. Apply Lemmatization
for col in keyword_cols:
    new_col_name = col.replace('_final_keywords', '_lemmatized')
    df[new_col_name] = df[col].apply(lemmatize_tokens)

# 5. Save the final processed data
output_file = 'fully_processed_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Lemmatization complete! Your data is now perfectly clean.")
print(f"Final file saved as: {output_file}")

# Example of the change
print("\n--- Lemmatization Example ---")
print("Before:", ['skills', 'projects', 'learning'])
print("After :", [lemmatizer.lemmatize(w) for w in ['skills', 'projects', 'learning']])