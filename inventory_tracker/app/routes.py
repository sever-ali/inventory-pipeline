from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, InventoryItem

main = Blueprint('main', __name__)

@main.route('/')
def index():
    query = request.args.get('query', '').strip()

    if query:
        items = InventoryItem.query.filter(
            (InventoryItem.t2t_code.ilike(f"%{query}%")) |
            (InventoryItem.branch_code.ilike(f"%{query}%"))
        ).order_by(InventoryItem.id.desc()).all()
    else:
        items = InventoryItem.query.order_by(InventoryItem.id.desc()).all()

    return render_template('index.html', items=items)



@main.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        t2t_code = request.form.get('t2t_code')
        branch_code = request.form.get('branch_code')
        quantity = request.form.get('quantity')

        if t2t_code and branch_code and quantity:
            new_item = InventoryItem(
                t2t_code=t2t_code.strip(),
                branch_code=branch_code.strip(),
                quantity=int(quantity)
            )
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('add.html')

@main.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)

    if request.method == 'POST':
        item.t2t_code = request.form.get('t2t_code')
        item.branch_code = request.form.get('branch_code')
        item.quantity = int(request.form.get('quantity'))
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit.html', item=item)

@main.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))
