import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import ast

# 1. Load your data
df = pd.read_excel('fully_processed_data.xlsx')

def prepare_text(tokens):
    if isinstance(tokens, str):
        try: tokens = ast.literal_eval(tokens)
        except: return ""
    return " ".join(tokens)

# Function to run the ML classifier for a specific column
def run_ml_for_column(dataframe, text_col, label_col):
    # Prepare text
    temp_text = dataframe[text_col].apply(prepare_text)
    
    # Split into Labeled (to train) and Unlabeled (to predict)
    train_df = dataframe.dropna(subset=[label_col])
    predict_df = dataframe[dataframe[label_col].isnull()]
    
    if len(train_df) < 5:
        print(f"Skipping {label_col}: Not enough labels (need at least 5-10).")
        return dataframe[label_col]

    # Vectorize and Train
    tfidf = TfidfVectorizer()
    X_train = tfidf.fit_transform(temp_text[train_df.index])
    y_train = train_df[label_col]
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Predict
    X_predict = tfidf.transform(temp_text[predict_df.index])
    predictions = model.predict(X_predict)
    
    # Fill in the results
    result_col = dataframe[label_col].copy()
    result_col.loc[predict_df.index] = predictions
    return result_col

# 2. Run ML for the Skills Column
print("Classifying Skills Lacking...")
df['category_skills'] = run_ml_for_column(
    df, 
    'What skills do you think you are lacking for a job?_lemmatized', 
    'category_skills'
)

# 3. Run ML for the University Changes Column
print("Classifying University Changes...")
df['category_uni'] = run_ml_for_column(
    df, 
    'If you could change one thing in your university system to better prepare students for jobs, what would it be?_lemmatized', 
    'category_uni'
)

# 4. Save Final Results
df.to_excel('ML_Categorized_Separated.xlsx', index=False)
print("Finished! Check 'ML_Categorized_Separated.xlsx'.")