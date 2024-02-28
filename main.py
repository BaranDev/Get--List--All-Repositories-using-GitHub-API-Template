import os
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/repos"
GITHUB_API_TOKEN = os.environ['GITHUB_API_TOKEN']

def fetch_repositories(username):
    headers = {"Authorization": f"token {GITHUB_API_TOKEN}"}
    response = requests.get(GITHUB_API_URL.format(username), headers=headers)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            # Manually parse and reshape the "last updated" information
            last_updated = repo.get('updated_at')
            if last_updated:
                # Splitting the date and time components
                date, time = last_updated.split('T')
                year, month, day = date.split('-')
                repo['updated_at'] = f"{day}-{month}-{year}"  # Reshaping to DD-MM-YYYY format
        return repos
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def root_route():
    if request.method == "POST":
        username = request.form.get("username")
        repos = fetch_repositories(username)
        if repos is not None:
            return render_template('template.html', repos=repos, username=username)
        else:
            return render_template('template.html', error="Failed to fetch repositories or invalid GitHub API token.")
    return render_template('template.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
