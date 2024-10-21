import openai
import json

# Replace with your actual API key
openai.api_key = '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'

def analyze_commit_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze this commit message: {message}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Load your commit data
with open('scripts/data/commits.json', 'r') as f:
    commits = json.load(f)

# Process and analyze each commit message
for commit in commits:
    message = commit['commit']['message']
    analysis = analyze_commit_message(message)
    print(f"Commit: {message}\nAnalysis: {analysis}\n")

# import openai
# import os
# import json

# openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI key in the environment

# def analyze_commit_messages(commit_messages):
#     prompt = f"Analyze the following commit messages and provide insights: {commit_messages}"
#     response = openai.Completion.create(
#         engine="gpt-4",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# if __name__ == "__main__":
#     # Load commit messages
#     with open('outputs/commit_data.json', 'r') as f:
#         commit_data = json.load(f)

#     commit_messages = [commit['commit']['message'] for commit in commit_data]
#     insights = analyze_commit_messages(commit_messages)

#     # Save insights for report generation
#     with open('outputs/insights.txt', 'w') as f:
#         f.write(insights)
