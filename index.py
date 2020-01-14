#!/usr/bin/env python3

from flask import Flask, render_template
from services import*
from services.service import get_categories, get_category

app = Flask(__name__)

def find_category(id):
    for category in get_categories(): 
        if id == category['id']:
            name_category = category['name']
    return name_category

@app.route('/')
def categories():
    categories = get_categories()
    return render_template('home.html', categories=categories)

@app.route('/category/<id>')
def category(id):
    category = get_category(id)
    name_category = find_category(id)
    
    return render_template('category.html', category=category, name_category=name_category)

if __name__ == '__main__':
        app.run(debug=True)
