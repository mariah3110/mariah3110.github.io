from flask import Flask, render_template
from posts import posts

app = Flask(__name__)

def get_categories():
    return sorted(set(post["category"] for post in posts))

@app.route("/")
def index():
    latest_posts = sorted(posts, key=lambda x: x["date"], reverse=True)[:3]
    return render_template(
        "index.html",
        intro="Willkommen auf meinem Blog. Hier analysiere ich aktuelle Themen aus Politik, Wirtschaft und Gesellschaft – klar, sachlich und unabhängig.",
        posts=latest_posts,
        categories=get_categories()
    )

@app.route("/post/<slug>")
def post(slug):
    post = next((p for p in posts if p["slug"] == slug), None)
    return render_template(
        "post.html",
        post=post,
        categories=get_categories()
    )

@app.route("/category/<category>")
def category(category):
    filtered = [p for p in posts if p["category"] == category]
    return render_template(
        "category.html",
        posts=filtered,
        category=category,
        categories=get_categories()
    )

if __name__ == "__main__":
    app.run(debug=True)