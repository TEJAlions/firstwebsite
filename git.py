import requests

def fetch_pull_request_info(pr_url, token):
    api_url = pr_url.replace("https://github.com/", "https://api.github.com/repos/")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        pr_data = response.json()
        site_name = pr_data["title"]
        site_url = pr_data["html_url"]
        repo_name = pr_data["base"]["repo"]["name"]
        repo_branch = pr_data["base"]["ref"]
        source_branch = pr_data["head"]["ref"]
        target_branch = pr_data["base"]["ref"]
        creator_username = pr_data["user"]["login"]
        creator_timestamp = pr_data["created_at"]
        
        return {
            "site_name": site_name,
            "site_url": site_url,
            "repo_name": repo_name,
            "repo_branch": repo_branch,
            "source_branch": source_branch,
            "target_branch": target_branch,
            "creator_username": creator_username,
            "creator_timestamp": creator_timestamp
        }
    else:
        return None

# Example usage
pr_url = "https://github.com/TEJAlions/myMovies/pull/5"  # Replace with actual PR URL
token = "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"
pr_info = fetch_pull_request_info(pr_url, token)

if pr_info:
    print("Pull Request Information:")
    print(f"Site Name: {pr_info['site_name']}")
    print(f"Site URL: {pr_info['site_url']}")
    print(f"Repository Name: {pr_info['repo_name']}")
    print(f"Repository Branch: {pr_info['repo_branch']}")
    print(f"Source Branch: {pr_info['source_branch']}")
    print(f"Target Branch: {pr_info['target_branch']}")
    print(f"Creator Username: {pr_info['creator_username']}")
    print(f"Creation Timestamp: {pr_info['creator_timestamp']}")
else:
    print("Failed to fetch pull request information.")
