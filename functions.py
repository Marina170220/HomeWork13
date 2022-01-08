import json


def read_json(file):
    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)


def get_tags(data):
    tags = set()
    for post in data:
        words_in_post = post['content'].split()
        for word in words_in_post:
            if word.startswith('#'):
                tags.add(word.lstrip('#'))
    return tags


def get_posts_by_tag(data, tag):
    results = [post for post in data if f'#{tag}' in post['content']]
    return results


def add_new_post(file, post):
    data = read_json(file)
    data.append(post)
    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
