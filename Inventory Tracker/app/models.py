from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t2t_code = db.Column(db.String(20), nullable=False)
    branch_code = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<InventoryItem {self.t2t_code}>'
