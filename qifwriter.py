import csv

FILE_BEGIN = "!Type:Invst\n"
DELIMITER_TRANSACTION = "^"
CARACTERE_POURRI = "\xa0"


class QIFWriter(object):
    """Write file for money."""

    def __init__(self, qiffile, correspondances):
        """
        Initialise la classe
        :param qiffile: Fichier où l'on souhaite écrire
        :param correspondances: Tableau de correspondance pour le champ "Y"
        """
        super(QIFWriter, self).__init__()
        self.output = open(qiffile, 'w')
        self.output.write(FILE_BEGIN)
        self.correspondances = correspondances

    @staticmethod
    def _tofloat(number):
        """
        Convertit un nombre au format texte vers un format flottant
        :param number: texte a convertir
        :return: nombre converti
        """
        return float(number.replace(CARACTERE_POURRI, "").replace(",", "."))

    def _to_english_notation(self, number):
        """
        Convertit un nombre avec la notation englaise
        :param number: Nombre a convertir
        :return: Nombre convertit au format chaine de caractère (str)
        """
        # Pour avoir 2 chiffres après la virgule
        number = list("%.2f" % self._tofloat(number))
        number.reverse() # On lit depuis la fin
        english = []
        # On ajoute des "," tout les 3 chiffres
        for n in range(len(number)):
            # Offset a cause des chiffres après la virgule
            if n > 2 and n-2 % 3 == 0:
                english.append(",")
            english.append(number[n])
        english.reverse() # On remet a l'endroit
        return "".join(english) # On transforme en texte

    def write_transaction(self, transaction):
        """
        Ecrit une transaction dans le fichier de sortie
        :param transaction: une transaction (comme retourné par le CSV reader)
        :return: rien
        """
        valeur_d = transaction['date'].replace("/20", "'20")
        valeur_t = str(abs(self._tofloat(transaction['montant_net'])))
        # C'est du ternaire: "valeur vrai" if condition else "valeur fausse"
        valeur_n = "Sell" if self._tofloat(transaction['montant_net']) > 0 else "Buy"
        valeur_y = self.correspondances[transaction['valeur']]
        valeur_i = str(self._tofloat(transaction['cours']))
        valeur_q = transaction['qte']
        valeur_o = str(
            abs(
                abs(self._tofloat(transaction['montant_net'])) - abs(self._tofloat(transaction['montant_brut']))
            )
        )

        self.output.write("D" + valeur_d + "\n")
        self.output.write("T" + self._to_english_notation(valeur_t) + "\n")
        self.output.write("N" + valeur_n + "\n")
        self.output.write("Y" + valeur_y + "\n")
        self.output.write("I" + self._to_english_notation(valeur_i) + "\n")
        self.output.write("Q" + valeur_q + "\n")
        self.output.write("O" + self._to_english_notation(valeur_o) + "\n")
        self.output.write(DELIMITER_TRANSACTION + "\n")

    def close(self):
        self.output.close()