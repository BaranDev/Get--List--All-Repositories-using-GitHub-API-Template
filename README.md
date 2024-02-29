### Directions:

1. **Setting up GitHub API Token:**
   - Make sure you have a GitHub API token. You can obtain one by following [GitHub's instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
   - Once you have the token, create a `.env` file in the root directory of your project.
   - Inside the `.env` file, edit the following line:
     ```
     GITHUB_API_TOKEN="your_github_api_key"
     ```

2. **Dependencies:**
   - Make sure to install the required dependencies by running:
     ```
     pip install -r requirements.txt
     ```

3. **Running the Application:**
   - Execute the script by running:
     ```
     python main.py
     ```
   - This will start the Flask application on `http://127.0.0.1:8080/`.

4. **Using the Application:**
   - Navigate to `http://127.0.0.1:8080/` in your web browser.
   - Enter a GitHub username and submit the form.
   - The application will fetch and display the repositories of the entered GitHub user.

### Additional Information:

- The application uses Flask to create a web server.
- It fetches the repositories of a GitHub user using the GitHub API.
- The `fetch_repositories` function sends a request to the GitHub API with the provided username and API token.
- The fetched repository data is then passed to the HTML template for rendering.

![GitHub language count](https://img.shields.io/github/languages/count/barandev/List-Repositories-using-GitHub-API-Template)
![GitHub repo size](https://img.shields.io/github/repo-size/barandev/List-Repositories-using-GitHub-API-Template)
[![License](https://img.shields.io/github/license/barandev/List-Repositories-using-GitHub-API-Template)](https://github.com/barandev/List-Repositories-using-GitHub-API-Template/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/barandev/List-Repositories-using-GitHub-API-Template)](https://github.com/barandev/List-Repositories-using-GitHub-API-Template/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/barandev/List-Repositories-using-GitHub-API-Template)](https://github.com/barandev/List-Repositories-using-GitHub-API-Template/pulls)
[![GitHub stars](https://img.shields.io/github/stars/barandev/List-Repositories-using-GitHub-API-Template)](https://github.com/barandev/List-Repositories-using-GitHub-API-Template/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/barandev/List-Repositories-using-GitHub-API-Template)](https://github.com/barandev/List-Repositories-using-GitHub-API-Template/network)