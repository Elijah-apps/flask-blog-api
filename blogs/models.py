class Post:
    posts = {}

    @staticmethod
    def create_post(post_id, title, content):
        if post_id in Post.posts:
            raise ValueError("Post already exists.")
        Post.posts[post_id] = {'title': title, 'content': content}

    @staticmethod
    def get_post(post_id):
        return Post.posts.get(post_id)

    @staticmethod
    def update_post(post_id, title=None, content=None):
        if post_id not in Post.posts:
            raise ValueError("Post does not exist.")
        if title:
            Post.posts[post_id]['title'] = title
        if content:
            Post.posts[post_id]['content'] = content

    @staticmethod
    def delete_post(post_id):
        if post_id in Post.posts:
            del Post.posts[post_id]
