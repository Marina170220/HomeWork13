import json


def read_json(file):
    with open(file, encoding='UTF-8') as f:
        return json.load(f)


# print(read_json('posts.json'))


def get_tags(data):
    tags = set()
    for post in data:
        words_in_post = post['content'].split()
        for word in words_in_post:
            if word.startswith('#'):
                tags.add(word.lstrip('#'))
    return tags

# return [cand for cand in dict_ if name in cand.get("name")]
# print(get_tags(read_json('posts.json')))


def get_posts_by_tag(data, tag):
    results = [post for post in data if f'#{tag}' in post['content']]
    return results

#
# print(get_posts_by_tag(read_json('posts.json'), 'пирог'))
