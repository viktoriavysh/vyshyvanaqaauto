import requests

class GitHub:

    def get_user(self, username):
        r=requests.get(f"https://api.github.com/users/{username}")
        body = r.json()
        return body
    
    def search_repo(self, name):
        r=requests.get(f"https://api.github.com/search/repositories?q={name}")
        body = r.json()
        return body
    
    def get_project_id(self, project_id):
        r=requests.get(f"https://api.github.com/projects/{project_id}")
        body = r.json()
        return body
        print(body)
    
    def get_commit(self, owner, repo):
        r=requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        body = r.json()
        return body 