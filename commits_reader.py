import urllib.request, json


def get_branches_from_repository(owner, repository_name):
    with urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repository_name}/branches") as url:
        data = json.loads(url.read().decode())
    names = []

    for branch in data:
        names.append(branch["name"])

    return names


def get_commits_from_branch(owner, repository_name, branch_name):
    with urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repository_name}/commits?sha={branch_name}") as url:
        data = json.loads(url.read().decode())
    commits = []

    for commit in data:
        commits.append([
            commit["commit"]["author"]["name"],
            commit["commit"]["author"]["email"],
            commit["commit"]["author"]["date"],
            commit["commit"]["message"]
        ])

    return commits


if __name__ == "__main__":
    repo_owner = input("Repository owner: ")
    repo_name = input("Repository name: ")
    for branch in get_branches_from_repository(repo_owner, repo_name):
        print(f"Branch {branch}:")
        print(*get_commits_from_branch(repo_owner, repo_name, branch), sep='\n')
