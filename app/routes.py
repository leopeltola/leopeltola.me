from flask import render_template, redirect, url_for, abort
from app import app
from app.models import Blog

@app.get("/")
def index():
	return render_template("index.html", stylesheet="css/index.css")

@app.route("/blog")
def blog():
	posts = Blog.get_posts()
	return render_template("blog.html", stylesheet="css/blog.css", title="Blog", posts=posts)

@app.route("/blog/<string:name>")
def blog_post(name):
	if not Blog.does_post_exist(name):
		abort(404)
	post = Blog.get_post(name)
	return render_template("blog_post.html", stylesheet="css/blog_post.css", title=post["title"], description=post["title"], post=post)

@app.get("/portfolio")
def portfolio():
	return render_template("portfolio.html", stylesheet="css/portfolio.css", title="Portfolio", posts=Blog.get_posts())

# Redirects
@app.get("/p")
@app.get("/projects")
@app.get("/work")
@app.get("/works")
def portfolio_redirect():
	return redirect(url_for("portfolio"), code=301)

@app.get("/b")
def blog_redirect():
	return  redirect(url_for("blog"), code=301)


# Error handlers
@app.errorhandler(404)
def error_404(e):
	return render_template("404.html", stylesheet="css/index.css")