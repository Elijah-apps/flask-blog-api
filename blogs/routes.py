from flask_restful import Api
from blog.endpoints import PostAPI, PostListAPI

def initialize_routes(app):
    api = Api(app)
    api.add_resource(PostAPI, '/posts/<string:post_id>')
    api.add_resource(PostListAPI, '/posts')
