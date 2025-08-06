from flask import Flask, render_template

app = Flask(__name__)

# Data for portfolio projects
projects = [
    {
        "name": "Project Alpha",
        "description": "A web application that analyzes data and provides insights.",
        "tech_stack": ["Python", "Flask", "HTML", "CSS"],
        "github": "https://github.com/yourusername/project-alpha"
    },
    {
        "name": "Project Beta",
        "description": "A machine learning project that predicts outcomes using scikit-learn.",
        "tech_stack": ["Python", "scikit-learn", "Pandas"],
        "github": "https://github.com/yourusername/project-beta"
    }
]

@app.route("/")
def index():
    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
