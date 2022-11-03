from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/d6a237e8f73e6b93d7ed"
blog_response = requests.get(blog_url)
all_blog_posts = blog_response.json()

posts = []
for post in all_blog_posts:
    post_item =  Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    posts.append(post_item)


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post_page(num):
    picked_post = all_blog_posts[num - 1]
    return render_template("post.html", post=picked_post)