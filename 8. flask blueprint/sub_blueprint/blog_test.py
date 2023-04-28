from flask import Blueprint

blog_ab = Blueprint('blog', __name__)

@blog_ab.route('/blog1')
def blog():
    return 'Test Blueprint'

@blog_ab.route('/blog2')
def blog2():
    return 'Test Blueprint 2'