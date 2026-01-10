from . import transacoes_bp
from flask import render_template


@transacoes_bp.route("/adicionar_transacao", methods=["GET"])
def adicionar_transacao():
    return render_template("adicionar_transacao.html")


@transacoes_bp.route("/movimentacoes", methods=["GET"])
def movimentacoes():
    return render_template("movimentacoes.html")


@transacoes_bp.route("/categorias", methods=["GET"])
def categorias():
    return render_template("categorias.html")
