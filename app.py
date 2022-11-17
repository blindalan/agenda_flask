#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import agenda_mem as agenda
#import agenda_db as agenda

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

class ContactForm(FlaskForm):
    name        = StringField('nome', validators=[DataRequired()])
    lastName    = StringField('Sobrenome', validators=[DataRequired()])
    address     = StringField('Endereço', validators=[DataRequired()])
    city        = StringField('Cidade', validators=[DataRequired()])
    phone       = StringField('Telefone', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('list.html', contacts=agenda.obter_contatos())

@app.route('/filter/<string:term>')
def filter(term):
    return render_template('list.html', contacts=agenda.filtrar_contatos(term), filter_term=term)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        agenda.adicionar_contato(form.name.data, form.lastName.data, form.address.data, form.city.data, form.phone.data, form.email.data)
        return redirect(url_for('index'))
    return render_template('add_edit.html', form=form, title="Novo contato", action=url_for('add'), action_label="adicionar")


@app.route('/edit/<int:id_contact>', methods=['GET', 'POST'])
def edit(id_contact):
    contact = agenda.obter_contato(id_contact)
    form = ContactForm(data=contact)
    if request.method == 'POST' and form.validate():
        agenda.editar_contato(id_contact, form.name.data, form.lastName.data, form.address.data, form.city.data, form.phone.data, form.email.data)
        return redirect(url_for('index'))
    return render_template('add_edit.html', form=form, title="Editar contato", action=url_for('edit', id_contact=id_contact), action_label="Guardar")


@app.route('/remove', methods=['POST'])
def remove():
    agenda.eliminar_contato(request.form['id_contact'])
    return redirect(url_for('index'))

