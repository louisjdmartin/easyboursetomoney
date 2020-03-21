# How to use
Change main.py variables then execute main.py
```
ENTREE = "Fichier export easy bourse.csv"
SORTIE = "export.qif"


# Pour ignorer certaines opérations, faut le nom exact
TO_IGNORE = [
    "Retrait par Virement"
]

# Si une correspondance manque, ça plante !
CORRESPONDANCES = {
    "LLYX.CAC 40 DAIL.DBLE SH.UC.ET": "CAC40 DD SHORT",
    "THE BLOCKCHAIN GROUP": "blockchain group"
}
```