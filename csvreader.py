import csv

CHAMP_DATE = 'Date'


class CSVReader(object):
    """Decode csv file from easy bourse."""

    def __init__(self, csvfile):
        """
        Initialise la classe
        :param csvfile: Fichier a lire
        """
        super(CSVReader, self).__init__()
        self.csv = csv.reader(open(csvfile, 'r'), delimiter=';')

    def read_transactions(self):
        """
        Lis le fichier d'entrée
        :return: Liste de transactions interpretable par qifwriter
        """
        is_transaction = False
        liste_transactions = []
        for row in self.csv:
            if is_transaction:
                transaction = {
                    "date": row[0],
                    "valeur": row[1],
                    "isin": row[2],
                    "place_cotation": row[3],
                    "operation": row[4],
                    "qte": row[5],
                    "cours": row[6],
                    "montant_brut": row[7],
                    "montant_net": row[8]
                }
                liste_transactions.append(transaction)

            if row[0] == CHAMP_DATE:
                is_transaction = True
        return liste_transactions
