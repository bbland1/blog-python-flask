from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
all_blog_posts = blog_response.json()

posts = []
for post in all_blog_posts:
    post_item =  Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(post_item)


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:num>")
def post_page(num):
    picked_post = all_blog_posts[num - 1]
    return render_template("post.html", post=picked_post)