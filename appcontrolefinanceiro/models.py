from . import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "date": self.date,
            "amount": self.amount,
            "category_id": self.category_id,
            "category_name": self.category.name if self.category else None
        }    

    def add_transaction(self):
        db.session.add(self)
        db.session.commit()

    def update_transaction(self):
        db.session.commit()

    def delete_transaction(self):
        db.session.delete(self)
        db.session.commit()

    def get_month_transactions():
        ...
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    transactions = db.relationship("Transaction", backref="category", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "transactions": [transaction.to_dict() for transaction in self.transactions]
        }

    def add_category(self):
        db.session.add(self)
        db.session.commit()

    def update_category(self):
        db.session.commit()

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()

    def make_visible(self):
        ...