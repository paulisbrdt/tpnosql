from pymongo import MongoClient
import pprint

client = MongoClient('localhost:27017')
db = client.Supermarche

Produits = db.produit

Produit2 = {
    "Intitulé": ["Fraise", "Banane", "Eau", "Lardons"],
    "Quantité": ["200", "70", "230", "40"],
    "End_date": ["04/06/2021", "08/05/2021", "29/11/2023", "14/10/2021"]

}
new_result = db.insert_one([Produit2])

Commande = db.commande

Commande2 = {
    "Nom": ['Dupont', "Isenbrandt", "Gauthier", "Martin"],
    "Prenom": ['Alex', "Fred", "Jean", "Michel"],
    "Num_Commande": ['003', '892', '467', '312'],
    "Description": ["Fraise,Eau,Lardons", "Eau", "Banane,Lardons"],
    "date_commande": ["12/04/2021 19:03", "13/04/2021 16:53", "12/04/2021 11:39", "11/04/2021 08:00"],
}
new_result1 = db.insert_one(Commande2)

InventaireProduits = db.inventaire

InventaireProduits2 = {
    "Description": "Inventaire des produits",
    "Quantité": "540",
}

new_result2 = db.insert_one(InventaireProduits2)

Caisse = db.caisse

Caisse2 = {
    "Num caisse": ['1', '2', '3', '4', '5'],
    "Utilisateur id": ["PI0078", "AP003", "OL019", "DA0923", "TH321"],
    "Description": [" Caisse 1 ", "Caisse 2", "Caisse 3", "Caisse 4", "Caisse 5"],
    "Quantité de vente effectuee": ["35", "123", "43", "95", "918"],
    "Commande effectuee": ["003,892", "312", "", "467", ""],
}
new_result3 = db.insert_one(Caisse2)

Vente_caisse1 = db.caisse.find_one({"Num caisse": "1"})
pprint.pprint(Vente_caisse1)
