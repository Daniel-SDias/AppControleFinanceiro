from datetime import datetime

from flask import render_template, request, jsonify

from . import transacoes_bp
from webapp.models import Transaction, Category


@transacoes_bp.route("/adicionar_transacao", methods=["GET"])
def adicionar_transacao():
    categories = Category.query.all()
    return render_template("adicionar_transacao.html", categories=categories)


@transacoes_bp.route("/movimentacoes", methods=["GET"])
def movimentacoes():
    return render_template("movimentacoes.html")


@transacoes_bp.route("/categorias", methods=["GET"])
def categorias():
    return render_template("categorias.html")


@transacoes_bp.route("/add_transaction", methods=["POST"])
def add_transaction():
    data = request.get_json()

    date_string = data["data"]
    date_datetime = datetime.strptime(date_string, "%Y-%m-%d")


    new_transaction = Transaction(
        type=data["tipo"],
        description=data["descricao"],
        date=date_datetime,
        amount=data["valor"],
        category_id=data["categoria"]
    )

    new_transaction.add_transaction()

    return jsonify({"status": "success", "message": "Transação recebida"})