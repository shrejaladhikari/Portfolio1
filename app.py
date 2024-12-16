from flask import Flask, render_template
from flask_cors import CORS  # Import Flask-Cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/projects')
def projects():
    project_data = [
        {
            "title": "Song Recommendation System",
            "description": "A Machine Learning-powered system that recommends songs based on user input. The backend is built with Flask and integrated with Spotify's API for album covers, while the React.js frontend displays personalized recommendations interactively.",
            "links": [
                {"name": "Backend", "url": "https://songrecommendation-final.onrender.com"},
                {"name": "Frontend", "url": "https://songrecommendation-final-1.onrender.com"}
            ]
        },
        {
            "title": "Movie Recommendation System",
            "description": "A Machine Learning-based system to suggest movies based on user preferences, enhancing personalized viewing experiences.",
            "links": [
                {"name": "View Project", "url": "https://movierecommendationsystem-xfk7.onrender.com"}
            ]
        },
        {
            "title": "Query Relevance and Similarity",
            "description": "An NLP-based tool to analyze query relevance and measure document similarity for efficient search and retrieval.",
            "links": [
                {"name": "View Project", "url": "https://similarityreport-queryrelevance.onrender.com"}
            ]
        }
    ]
    return render_template('projects.html', projects=project_data)


# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
