#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, render_template, redirect, abort, flash, session

from connexion_db import get_db

client_panier = Blueprint('client_panier', __name__,
                        template_folder='templates')


@client_panier.route('/client/panier/add', methods=['POST'])
def client_panier_add():
    mycursor = get_db().cursor()
    id_client = session['id_utilisateur']
    id_jean = request.form.get('id_jean')
    quantite = request.form.get('quantite')
    sql="select * from ligne_panier where id_jean =%s and id_utilisateur =%s"
    mycursor.execute(sql,(id_jean, id_client))
    article_panier = mycursor.fetchone()

    mycursor.execute("select * from jean where id_jean =%s",(id_jean))
    jean = mycursor.fetchone()

    if not (article_panier is None) and article_panier['quantite']>=1:
        tuple_update =(quantite, id_client, id_jean)
        sql="update ligne_panier set quantite= quantite +%s where id_utilisateur =%s"
        mycursor.execute(sql, tuple_update)
    else:
        tuple_insert = (id_client, id_jean, quantite)
        sql="update ligne_panier set quantite = quantite+%s where id_utilisateur=%s"
        mycursor.execute(sql, tuple_insert)

    get_db().commit()
    return redirect ('/client/article/show')
@client_panier.route('/client/panier/delete', methods=['POST'])
def client_panier_delete():
    mycursor = get_db().cursor()
    id_client = session['id_user']
    id_article = request.form.get('id_article','')
    quantite = 1

    # ---------
    # partie 2 : on supprime une déclinaison de l'article
    # id_declinaison_article = request.form.get('id_declinaison_article', None)

    sql = ''' selection de la ligne du panier pour l'article et l'utilisateur connecté'''
    article_panier=[]

    if not(article_panier is None) and article_panier['quantite'] > 1:
        sql = ''' mise à jour de la quantité dans le panier => -1 article '''
    else:
        sql = ''' suppression de la ligne de panier'''

    # mise à jour du stock de l'article disponible
    get_db().commit()
    return redirect('/client/article/show')





@client_panier.route('/client/panier/vider', methods=['POST'])
def client_panier_vider():
    mycursor = get_db().cursor()
    client_id = session['id_user']
    sql = ''' sélection des lignes de panier'''
    items_panier = []
    for item in items_panier:
        sql = ''' suppression de la ligne de panier de l'article pour l'utilisateur connecté'''

        sql2=''' mise à jour du stock de l'article : stock = stock + qté de la ligne pour l'article'''
        get_db().commit()
    return redirect('/client/article/show')


@client_panier.route('/client/panier/delete/line', methods=['POST'])
def client_panier_delete_line():
    mycursor = get_db().cursor()
    id_client = session['id_user']
    #id_declinaison_article = request.form.get('id_declinaison_article')

    sql = ''' selection de ligne du panier '''

    sql = ''' suppression de la ligne du panier '''
    sql2=''' mise à jour du stock de l'article : stock = stock + qté de la ligne pour l'article'''

    get_db().commit()
    return redirect('/client/article/show')


@client_panier.route('/client/panier/filtre', methods=['POST'])
def client_panier_filtre():
    filter_word = request.form.get('filter_word', None)
    filter_prix_min = request.form.get('filter_prix_min', None)
    filter_prix_max = request.form.get('filter_prix_max', None)
    filter_types = request.form.getlist('filter_types', None)
    # test des variables puis
    # mise en session des variables
    return redirect('/client/article/show')


@client_panier.route('/client/panier/filtre/suppr', methods=['POST'])
def client_panier_filtre_suppr():
    # suppression  des variables en session
    print("suppr filtre")
    return redirect('/client/article/show')
