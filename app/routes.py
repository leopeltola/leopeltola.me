from flask import request, render_template, redirect, url_for, abort
from app import app
from app.models import Blog, Project


@app.get("/")
def index():
	dark_mode = True if request.cookies.get('dark') == "true" else False
	return render_template("index.html", stylesheet="css/index.css", dark_mode=dark_mode)

@app.route("/blog")
def blog():
	dark_mode = True if request.cookies.get('dark') == "true" else False
	posts = Blog.get_posts()
	return render_template("blog.html", stylesheet="css/blog.css", dark_mode=dark_mode, title="Blog", posts=posts)

@app.route("/blog/<string:name>")
def blog_post(name):
	dark_mode = True if request.cookies.get('dark') == "true" else False
	if not Blog.does_post_exist(name):
		abort(404)
	post = Blog.get_post(name)
	return render_template("blog_post.html", stylesheet="css/blog_post.css", dark_mode=dark_mode, title=post["title"], description=post["title"], post=post)

@app.get("/projects")
def portfolio():
	dark_mode = True if request.cookies.get('dark') == "true" else False
	return render_template("portfolio.html", stylesheet="css/portfolio.css", dark_mode=dark_mode, title="Portfolio", projects=Project.get_all())

@app.get("/projects/<string:name>")
def project(name):
	dark_mode = True if request.cookies.get('dark') == "true" else False
	if not Project.exists(name):
		abort(404)
	project = Project.get(name)
	return render_template("project.html", stylesheet="css/project.css", dark_mode=dark_mode, title=project["title"], description=project["title"], project=project)



# Error handlers
@app.errorhandler(404)
def error_404(e):
	dark_mode = True if request.cookies.get('dark') == "true" else False
	return render_template("404.html", stylesheet="css/index.css", dark_mode=dark_mode)