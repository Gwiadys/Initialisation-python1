#Implémenter un programme qui demande à l'utilisateur de saisir un prix unitaire HT,
# un taux de TVA et un nombre d'articles, et qui calcule le montant TTC de l'achat.

#saisir les données
Prix_unitaire_HT=float(input("saisir un prix unitaire_HT"))
Taux_de_TVA=float(input("saisir un taux de TVA"))
nombre_d_articles=int(input("saisir un nombre d'articles"))

#calcul du prix unitaire
montant_TTC_de_l_achat = Prix_unitaire_HT*(1+(Taux_de_TVA)/100)*nombre_d_articles
#Taux de TVA= prix unitaire *(1+(TAUX TVA)/100)

#afficher le resultat
print(f"montant-TTC_de_l_achat est de :{montant_TTC_de_l_achat}euros")
