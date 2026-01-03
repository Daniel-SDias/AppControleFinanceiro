from . import transacoes_bp
from flask import render_template


@transacoes_bp.route("/adicionar_transacao", methods=["GET"])
def adicionar_transacao():
    return render_template("adicionar_transacao.html")
