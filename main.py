from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

blog_url = "https://api.npoint.io/d6a237e8f73e6b93d7ed"
blog_response = requests.get(blog_url)
all_blog_posts = blog_response.json()

email_contact_form = "YOUR_OWN_EMAIL"
password_contact_form = "YOUR_OWN_PASSWORD"

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

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_email_from_from(data["name"], data["email"], data["message"])

        print(data["name"])
        print(data["email"])
        print(data["message"])
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)

def send_email_from_from(name, email, email_message):
    email_message = f"Subject: Blog Message \n\nName:{name}\nEmail:{email}\nMessage: {email_message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email_contact_form, password_contact_form)
        connection.sendmail(
            from_addr=email_contact_form,
            to_addrs=email_contact_form,
            message=email_message
        )




@app.route("/post/<int:num>")
def post_page(num):
    picked_post = all_blog_posts[num - 1]
    return render_template("post.html", post=picked_post)