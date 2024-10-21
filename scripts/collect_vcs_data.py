import requests
import json

GITHUB_TOKEN = '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'
GITHUB_REPO = 'Shobitha-nayak/devops-genome'

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_commits():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/commits'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch commits:", response.status_code)

def get_pull_requests():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls?state=all'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch pull requests:", response.status_code)

if __name__ == "__main__":
    commits = get_commits()
    prs = get_pull_requests()
    with open('data/commits.json', 'w') as f:
        json.dump(commits, f, indent=4)
    with open('data/prs.json', 'w') as f:
        json.dump(prs, f, indent=4)
    print("Data collected successfully.")
