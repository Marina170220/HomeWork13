from flask import Flask, request, render_template, send_from_directory, abort
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_tags(read_json(POST_PATH))
    return render_template('index.html', tags=tags)


@app.route("/tag")
def page_tag():
    tag = request.args.get('tag')
    if tag:
        posts = get_posts_by_tag(read_json(POST_PATH), tag)
        return render_template('post_by_tag.html', posts=posts, tag=tag)
    return abort(400, "Вы не выбрали ни одного тега :(")


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

