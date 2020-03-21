import csvreader
import qifwriter

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


CSV = csvreader.CSVReader(ENTREE)
QIF = qifwriter.QIFWriter(SORTIE, CORRESPONDANCES)

transactions = CSV.read_transactions()
for transaction in transactions:
    if transaction['operation'] not in TO_IGNORE:
        QIF.write_transaction(transaction)

QIF.close()