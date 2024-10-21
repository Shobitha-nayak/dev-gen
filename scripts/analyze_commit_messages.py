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
with open('scripts/data/commit.json', 'r') as f:
    commits = json.load(f)

# Process and analyze each commit message
for commit in commits:
    message = commit['commit']['message']
    analysis = analyze_commit_message(message)
    print(f"Commit: {message}\nAnalysis: {analysis}\n")
