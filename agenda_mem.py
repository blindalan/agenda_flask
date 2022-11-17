#!/usr/bin/env python
# -*- coding: utf-8 -*-

contatos = []


def adicionar_contato(name, lastName, address, city, phone, email):
    contatos.append(
        {
            'id': len(contatos)+1,
            'name': name,
            'lastName': lastName,
            'address': address,
            'city': city,
            'phone': phone,
            'email': email
        }
    )


def obter_contatos():

    return contatos


def filtrar_contatos(filtro=''):
    filtro = filtro.lower()
    if filtro == '':
        return contatos
    else:
        contatos_filtrados = []
        for c in contatos:
            if c['name'].lower().find(filtro) != -1 or c['lastName'].lower().find(filtro) != -1:
                contatos_filtrados.append(c) 
        return contatos_filtrados


def eliminar_contato(id_contato):
    for i in range(0, len(contatos)):
        if contatos[i]['id'] == int(id_contato):
            contatos.pop(i)
            return
    

def obter_contato(id_contato):
    for c in contatos:
        if c['id'] == id_contato:
            return c
    return None


def editar_contato(id_contato, name, lastName, address, city, phone, email):
    for c in contatos:
        if c['id'] == int(id_contato):
            c['name'] = name
            c['lastName'] = lastName
            c['address'] = address
            c['city'] = city
            c['phone'] = phone
            c['email'] = email
            return

