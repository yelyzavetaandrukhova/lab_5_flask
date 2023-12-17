from flask import Blueprint
from app_blueprint.views import index, transfer, addaccount, addpost, about

# Create a Blueprint for the views
bp = Blueprint('app_blueprint', __name__)

# Define routes
bp.route('/index')(index)
bp.route('/about')(about)
bp.route('/post/<int:post_id>')(transfer)
bp.route('/addaccount', methods=['POST'])(addaccount)
bp.route('/addpost', methods=['POST'])(addpost)
