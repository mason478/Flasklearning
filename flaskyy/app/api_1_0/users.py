from flask import jsonify,request,current_app,url_for
from . import api
from ..models import User,Post


@api.route('/users/<int:id>')
def get_user(id):
    user=User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users/<int:id>/posts')
def get_user_posts(id):
    user=User.query.get_or_404(id)
    page=request.args.get('page',1,type=int)
    pagination=user.posts.order_by(Post.timestamp.desc()).paginate(
        page,per_page=15,error_out=False
    )
    posts=pagination.items
    next=None
    prev=None
    if pagination.has_prev:
        prev=url_for('get_user_posts',page=page-1,_external=True)
    if pagination.has_next:
        next=url_for('get_user_posts',page=page+1,_external=True)
    return jsonify({
        'posts':[post.to_json() for post in posts],
        'prev':prev,
        'next':next,
        'count':pagination.total
    })