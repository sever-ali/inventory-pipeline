from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import InventoryItem
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    search_query = request.args.get('q')
    if search_query:
        items = InventoryItem.query.filter(
            InventoryItem.name.ilike(f'%{search_query}%') |
            InventoryItem.location.ilike(f'%{search_query}%')
        ).all()
    else:
        items = InventoryItem.query.all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['POST'])
def add_item():
    name = request.form['name'].strip()
    quantity = request.form['quantity']
    location = request.form['location'].strip()

    if not name or not quantity or not location:
        flash('All fields are required.', 'error')
        return redirect('/')

    item = InventoryItem(name=name, quantity=quantity, location=location)
    db.session.add(item)
    db.session.commit()
    flash('Item added successfully!', 'success')
    return redirect('/')


@main.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully.', 'success')
    return redirect('/')


@main.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)

    if request.method == 'POST':
        item.name = request.form['name'].strip()
        item.quantity = request.form['quantity']
        item.location = request.form['location'].strip()

        if not item.name or not item.quantity or not item.location:
            flash('All fields are required.', 'error')
            return redirect(f'/edit/{item_id}')

        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect('/')

    return render_template('edit.html', item=item)


