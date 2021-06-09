from pathlib import Path

from flask import url_for


# https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        print("models.py:find_between: Can't find substring between substrings.")
        return ""


class Blog:
    path = Path("posts/blog/")

    @staticmethod
    def get_posts(page=0, page_size=20):
        post_paths = Blog.path.iterdir()
        posts = []
        for post_path in post_paths:
            try:
                with open(post_path, encoding="utf-8") as file:
                    text = file.read()
                    posts.append(Blog.process_raw_post(text))
            except FileNotFoundError:
                # Should never happen.
                print("models.py:Blog:get_posts: This should never print :^)")
                return []
        return posts

    @staticmethod
    def get_post(name):
        try:
            with open(Blog.path / f"{name}", encoding="utf-8") as file:
                text = file.read()
                return Blog.process_raw_post(text)
        except FileNotFoundError:
            return None

    @staticmethod
    def does_post_exist(name):
        try:
            with open(Blog.path / f"{name}", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def process_raw_post(text):
        post = {}
        post["title"] = find_between(text, "<title>", "</title>")
        post["h1"] = find_between(text, "<h1>", "</h1>")
        post["desc"] = find_between(text, "<desc>", "</desc>")
        post["body"] = (
            find_between(text, "<--->", "</--->")
            .replace("\n<p>\n", "<p>")
            .replace("\n</p>\n", "</p>")
            .replace("\n", "<br>")
        )
        post["link"] = "/blog/" + find_between(text, "<link>", "</link>")
        return post


class Project:
    path = Path("posts/projects/")

    @staticmethod
    def get_all(page=0, page_size=20):
        post_paths = Project.path.iterdir()
        posts = []
        for post_path in post_paths:
            try:
                with open(post_path, encoding="utf-8") as file:
                    text = file.read()
                    posts.append(Project._process_raw_post(text))
            except FileNotFoundError:
                # Should never happen.
                print("models.py:Project:get: This should never print :^)")
                return []
        return posts

    @staticmethod
    def get(name):
        try:
            with open(Project.path / f"{name}", encoding="utf-8") as file:
                text = file.read()
                return Project._process_raw_post(text)
        except FileNotFoundError:
            return None

    @staticmethod
    def exists(name):
        try:
            print("opening:", str(Project.path / f"{name}"))
            with open(Project.path / f"{name}", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False
            print("Doesn't exist!")

    @staticmethod
    def _process_raw_post(text):
        post = {}
        post["title"] = find_between(text, "<title>", "</title>")
        post["h1"] = find_between(text, "<h1>", "</h1>")
        post["desc"] = find_between(text, "<desc>", "</desc>")
        post["body"] = (
            find_between(text, "<--->", "</--->")
            .replace("\n<p>\n", "<p>")
            .replace("\n</p>\n", "</p>")
            .replace("\n", "<br>")
        )
        post["link"] = url_for("project", name=find_between(text, "<link>", "</link>"))
        post["tags"] = find_between(text, "<tags>", "</tags>").split(",")
        post["img"] = url_for(
            "static",
            filename="img/"
            + find_between(text, "<img>", "</img>").replace("[PIXEL]", ""),
        )
        post["pixel"] = (
            True if "[PIXEL]" in find_between(text, "<img>", "</img>") else False
        )
        return post
