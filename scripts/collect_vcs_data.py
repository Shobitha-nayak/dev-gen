# # import requests
# # import json

# # GITHUB_TOKEN = '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'
# # GITHUB_REPO = 'Shobitha-nayak/dev-gen'

# # headers = {
# #     "Authorization": f"token {GITHUB_TOKEN}"
# # }

# # def get_commits():
# #     url = f'https://api.github.com/repos/{GITHUB_REPO}/commits'
# #     response = requests.get(url, headers=headers)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         print("Failed to fetch commits:", response.status_code)

# # def get_pull_requests():
# #     url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls?state=all'
# #     response = requests.get(url, headers=headers)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         print("Failed to fetch pull requests:", response.status_code)

# # if __name__ == "__main__":
# #     commits = get_commits()
# #     prs = get_pull_requests()
# #     with open('scripts/data/commits.json', 'w') as f:
# #         json.dump(commits, f, indent=4)
# #     with open('scripts/data/prs.json', 'w') as f:
# #         json.dump(prs, f, indent=4)
# #     print("Data collected successfully.")



import requests
import json

# Hardcoded GitHub personal access token
GITHUB_TOKEN = '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'  # Replace this with your actual token
GITHUB_REPO = 'Shobitha-nayak/dev-gen'

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_commits():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/commits'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch commits:", response.status_code, response.text)
        return []

def get_pull_requests():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls?state=all'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch pull requests:", response.status_code, response.text)
        return []

if __name__ == "__main__":
    # Fetch data
    commits = get_commits()
    prs = get_pull_requests()
    
    # Ensure the data directory exists
    import os
    os.makedirs('scripts/data', exist_ok=True)

    # Save the collected data
    with open('scripts/data/commits.json', 'w') as f:
        json.dump(commits, f, indent=4)

    with open('scripts/data/prs.json', 'w') as f:
        json.dump(prs, f, indent=4)

    print("Data collected successfully.")




# import requests
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")  # Set your token in the environment

# def get_commit_data(repo_name):
#     headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
#     url = f"https://api.github.com/repos/{repo_name}/commits"
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()  # Raise an error for bad responses
#     return response.json()

# def get_build_status(repo_name):
#     headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
#     url = f"https://api.github.com/repos/{repo_name}/actions/runs"
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     runs = response.json()
#     success_rate = sum(run['conclusion'] == 'success' for run in runs['workflow_runs']) / len(runs['workflow_runs']) * 100
#     return success_rate

# if __name__ == "__main__":
#     repo_name = "Shobitha-nayak/dev-gen"  # Replace with your GitHub repo
#     commits = get_commit_data(repo_name)
#     build_success_rate = get_build_status(repo_name)

#     # Save data to file for report generation
#     with open('outputs/commit_data.json', 'w') as f:
#         f.write(str(commits))
#     with open('outputs/build_success_rate.txt', 'w') as f:
#         f.write(str(build_success_rate))






import requests
import json
import os

# Hardcoded GitHub personal access token
GITHUB_TOKEN = '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' 
# GITHUB_TOKEN = os.getenv('MY_GITHUB_TOKEN')            # Replace this with your actual token
GITHUB_REPO = 'Shobitha-nayak/dev-gen'

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def get_commits():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/commits'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch commits:", response.status_code, response.text)
        return []

def get_pull_requests():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls?state=all'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch pull requests:", response.status_code, response.text)
        return []

if __name__ == "__main__":
    # Fetch data
    commits = get_commits()
    prs = get_pull_requests()
    
    # Ensure the data directory exists
    os.makedirs('scripts/data', exist_ok=True)

    # Save the collected data
    with open('scripts/data/commits.json', 'w') as f:
        json.dump(commits, f, indent=4)

    with open('scripts/data/prs.json', 'w') as f:
        json.dump(prs, f, indent=4)

    print("Data collected successfully.")      


