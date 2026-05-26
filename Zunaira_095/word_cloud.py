import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 1. Load your frequency data
df = pd.read_excel('Keyword_Frequency_Analysis.xlsx', sheet_name='Lacking_Skills_Analysis')

# --- THE FIX: Clean the data before making the cloud ---
# Remove any rows where Keyword might be empty (NaN)
df = df.dropna(subset=['Keyword'])

# Force Keywords to be strings (this prevents the 'float' error)
df['Keyword'] = df['Keyword'].astype(str)
# -------------------------------------------------------

# 2. Convert the dataframe into a dictionary
data = dict(zip(df['Keyword'], df['Frequency']))

# 3. Generate the Word Cloud
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    colormap='viridis'
).generate_from_frequencies(data)

# 4. Display
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 5. Save
wordcloud.to_file("final_wordcloud.png")
print("Word Cloud generated successfully!")