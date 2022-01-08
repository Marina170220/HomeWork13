from flask import Flask, request, render_template, send_from_directory, abort, url_for
from functions import *
import os

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

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
    if request.method == "GET":
        return render_template('post_form.html')
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        abort(400, "Ошибка загрузки")
    post = {'pic': url_for('static_dir', path=picture.filename),
            'content': content
            }
    picture.save(os.path.join(BASE_DIR, UPLOAD_FOLDER, f'{picture.filename}'))
    add_new_post(POST_PATH, post)
    return render_template('post_uploaded.html', post=post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)


app.run(debug=True)
