import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the survey data into a Pandas DataFrame (you can use a CSV file if available)
data = [
    {
        'Timestamp': '14/10/2023 14:32',
        'Your Name': 'James Kityo',
        'Years of Experience': '4 to 7 years',
        'Role in Software Development': 'Software Developer',
        'Question 1 Response': 'Strongly Agree',
        'Question 2 Response': 'Strongly Agree',
        # The rest of the data here
    },
    # Add data for other participants
]

df = pd.DataFrame(data)

# Create a list of survey questions (adjust as needed)
questions = [
    'Question 1 Response',
    'Question 2 Response',
    'Question 3 Response',
    'Question 4 Response',
    'Question 5 Response',
    'Question 6 Response',
    'Question 7 Response',
    'Question 8 Response',
    'Question 9 Response',
    'Question 10 Response',
    'Question 11 Response',
    'Question 12 Response'
]

# Create a dictionary to store the results for each question
survey_results = {}

# Analyze each question
for question in questions:
    # Count the number of responses for each answer option
    response_counts = df[question].value_counts().reset_index()
    response_counts.columns = ['Response', 'Count']
    
    # Sort the responses by count in descending order
    response_counts = response_counts.sort_values(by='Count', ascending=False)
    
    # Store the results in the survey_results dictionary
    survey_results[question] = response_counts

# Display the results for each question
for question, result in survey_results.items():
    print(f"Results for {question}:\n")
    print(result)
    print("\n")

# Create bar plots to visualize the results for each question
for question, result in survey_results.items():
    plt.figure(figsize=(10, 6))
    sns.barplot(data=result, x='Count', y='Response', palette="viridis")
    plt.title(f"Survey Results for {question}")
    plt.xlabel("Count")
    plt.ylabel("Response")
    plt.show()
