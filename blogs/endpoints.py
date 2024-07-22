from flask_restful import Resource, reqparse
from blog.models import Post

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
post_parser.add_argument('content', type=str, required=True, help="Content cannot be blank!")

update_parser = reqparse.RequestParser()
update_parser.add_argument('title', type=str, help="Title cannot be blank!")
update_parser.add_argument('content', type=str, help="Content cannot be blank!")

class PostAPI(Resource):
    def get(self, post_id):
        post = Post.get_post(post_id)
        if not post:
            return {'message': 'Post not found'}, 404
        return post, 200

    def post(self, post_id):
        args = post_parser.parse_args()
        title = args['title']
        content = args['content']
        try:
            Post.create_post(post_id, title, content)
            return {'message': 'Post created'}, 201
        except ValueError as e:
            return {'message': str(e)}, 400

    def put(self, post_id):
        args = update_parser.parse_args()
        title = args.get('title')
        content = args.get('content')
        try:
            Post.update_post(post_id, title, content)
            return {'message': 'Post updated'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def delete(self, post_id):
        try:
            Post.delete_post(post_id)
            return {'message': 'Post deleted'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

class PostListAPI(Resource):
    def get(self):
        return Post.posts, 200
