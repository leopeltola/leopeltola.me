from pathlib import Path
from app import app

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
	def get_posts(number=None):
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
	def does_post_exist(name):
		try:
			with open(Blog.path / f"{name}.txt", encoding="utf-8") as file:
				return True
		except:
			return False

	@staticmethod
	def process_raw_post(text):
		post = {}
		post["title"] = find_between(text, "<title>", "</title>")
		post["h1"] = find_between(text, "<h1>", "</h1>")
		post["desc"] = find_between(text, "<desc>", "</desc>")
		post["body"] = find_between(text, "<--->", "</--->")
		post["link"] = "/blog/" + find_between(text, "<link>", "</link>")
		return post



