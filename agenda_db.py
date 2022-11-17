#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
DB_HOST     = ''
DB_USER     = ''
DB_PASSWORD = ''
DB_DBNAME   = ''
conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_DBNAME, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


def adicionar_contato(name, lastName, address, city, phone, email):
    '''
    adiciona um contato na base de dados
    '''
    # TODO: armazena a instrução sql na variável de consulta
    #       para adicionar o contato com os dados fornecidos
    query = ''
    cur.execute(query)


def obter_contatos():
    '''
    devolve a lista completa de contatos
    '''
    # TODO: armazena a instrução sql na variável de consulta
    #       para obter todos os contatos
    query = ''
    
    try:
        cur.execute(query)
        contatos = []
        for c in cur.fetchall():
            contatos.append(
                {
                    'id': c['id'],
                    'name': c['name'],
                    'lastName': c['lastName'],
                    'address': c['address'],
                    'city': c['city'],
                    'phone': c['phone'],
                    'email': c['email'],
                }
            )
        return contatos
    except pymysql.err.InternalError as e:
        if e.args[1] == 'Query was empty':
            return []
        else:
            raise e
    
    


def filtrar_contatos(filtro=''):
    '''
    devolve a lista de contatos que o nome
    coencida com o filtro
    '''
    # TODO: armazena a instrução sql na variável de consulta
    #       para obter os contatos de acordo com o criterio de filtro
    query = ''
    try:
        cur.execute(query)
        contatos = []
        for c in cur.fetchall():
            contatos.append(
                {
                    'id': c['id'],
                    'name': c['name'],
                    'lastName': c['lastName'],
                    'address': c['address'],
                    'city': c['city'],
                    'phone': c['phone'],
                    'email': c['email'],
                }
            )
        return contatos
    except pymysql.err.InternalError as e:
        if e.args[1] == 'Query was empty':
            return []
        else:
            raise e


def eliminar_contato(id_contacto):
    '''
    Elimina um contato através da base de dados pelo id
    '''
    # TODO: armazena a instrução sql na variável de consulta
    # eliminar o contato con id: id_contato
    query = ''
    cur.execute(query)
    

def obter_contato(id_contato):
    '''
    Devolve os dados de un contato da lista a partir de seu id
    '''
    # TODO: armazena a instrução sql na variável de consulta
    # para obter os dados do contato con id: id_contato
    query = ''
    cur.execute(query)
    c = cur.fetchall()[0]
    contato = {
        'name': c['name'],
        'lastName': c['lastName'],
        'address': c['address'],
        'city': c['city'],
        'phone': c['phone'],
        'email': c['email'],
    }
    return contatos


def editar_contato(id_contato, name, lastName, address, city, phone, email):
    '''
    Modifica a informação do contato com o id relacionado ao contato
    '''
    # TODO: armazena a instrução sql na variável de consulta
    # para modificar o contato con id: id_contato de acordo aos dados subministrados
    query = ''
    cur.execute(query)

    