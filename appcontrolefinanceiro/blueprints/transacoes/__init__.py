from flask import Blueprint

transacoes_bp = Blueprint("transacoes", __name__, static_folder="static", template_folder="templates")

from . import routes