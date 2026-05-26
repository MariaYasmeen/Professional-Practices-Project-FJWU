import pandas as pd

# 1. Load your actual file using read_excel (NOT read_csv)
# This fixes the UnicodeDecodeError completely!
file_path = 'behavioral_integrity_analysis.xlsx'
df = pd.read_excel(file_path)

# Clean up column names to eliminate hidden spaces or errors
df.columns = df.columns.str.strip()

# 2. Define the exact behavioral columns from your file
col_mindset = "Be honest, what describes you the best?"
col_internship = "Respond to the following Questions. [Completed any internship?]"
col_projects = "Respond to the following Questions. [Worked on real-world projects (outside coursework)?]"
col_freelance = "Respond to the following Questions. [Done freelancing or any paid work?]"

col_skills_lacking = "What skills do you think you are lacking for a job?"
col_uni_change = "If you could change one thing in your university system to better prepare students for jobs, what would it be?"

# 3. Create a fully automated function to classify the rows safely
def automate_student_type(row):
    # Check if they have done out-of-class practical work
    has_experience = (
        str(row[col_internship]).strip().lower() == 'yes' or
        str(row[col_projects]).strip().lower() == 'yes' or
        str(row[col_freelance]).strip().lower() == 'yes'
    )
    
    # Check if they actively focus on extra skills
    is_active_mindset = "actively work on skills" in str(row[col_mindset]).lower()
    
    if has_experience and is_active_mindset:
        return "Proactive Segment"
    else:
        return "Exam-Focused Segment"

# Apply the automatic grouping to a new column
df['Student_Market_Segment'] = df.apply(automate_student_type, axis=1)

# 4. Generate the exact summary table your Project Manager wants to see
print("\n" + "="*50)
print("       EXECUTIVE SUMMARY: STUDENT ANALYSIS REPORT")
print("="*50)

# Calculate totals and percentages
counts = df['Student_Market_Segment'].value_counts()
percentages = df['Student_Market_Segment'].value_counts(normalize=True) * 100

for segment in counts.index:
    print(f"\n📊 {segment}: {counts[segment]} Students ({percentages[segment]:.1f}%)")
    print("-" * 45)
    print("  Commonly reported skill gaps & university complaints:")
    
    # Extract top 3 real samples from your dataset for this group
    sample_rows = df[df['Student_Market_Segment'] == segment].head(3)
    for idx, r in sample_rows.iterrows():
        lack_text = str(r[col_skills_lacking]).strip().replace('\n', ' ')
        change_text = str(r[col_uni_change]).strip().replace('\n', ' ')
        print(f"   • Lacks: '{lack_text}' | Demands: '{change_text}'")

print("\n" + "="*50)

# 5. Save the final completed spreadsheet back out cleanly
df.to_excel('Automated_Student_Analysis_Final.xlsx', index=False)
print("Saved final data as 'Automated_Student_Analysis_Final.xlsx'")