from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__, static_folder="static", template_folder="templates")

from . import routes