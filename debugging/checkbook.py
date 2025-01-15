#!/usr/bin/python3

"""
Application de gestion de compte bancaire simple permettant de gérer un solde
avec des opérations de dépôt et de retrait.

Ce programme offre une interface en ligne de commande pour:
- Effectuer des dépôts
- Effectuer des retraits
- Consulter le solde
"""

class Checkbook:
    """
    Classe représentant un compte bancaire avec des opérations basiques.

    Attributes:
        balance (float): Le solde actuel du compte, initialisé à 0.0
    """

    def __init__(self):
        """
        Initialise un nouveau compte bancaire avec un solde de 0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Effectue un dépôt sur le compte.

        Args:
            amount (float): Le montant à déposer

        Returns:
            None

        Note:
            Affiche un message d'erreur si le montant est négatif ou nul.
            Affiche le montant déposé et le nouveau solde en cas de succès.
        """
        if amount <= 0:
            print("Le montant du dépôt doit être positif.")
            return
        self.balance += amount
        print("Déposé ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Effectue un retrait sur le compte.

        Args:
            amount (float): Le montant à retirer

        Returns:
            None

        Note:
            Affiche un message d'erreur si :
            - Le montant est négatif ou nul
            - Le solde est insuffisant
            Affiche le montant retiré et le nouveau solde en cas de succès.
        """
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
            return
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retiré ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.

        Returns:
            None
        """
        print("Solde actuel : ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale qui gère l'interface utilisateur du programme.
    
    Crée une instance de Checkbook et entre dans une boucle interactive
    permettant à l'utilisateur de:
    - Faire des dépôts
    - Faire des retraits
    - Consulter le solde
    - Quitter le programme
    
    La boucle continue jusqu'à ce que l'utilisateur choisisse 'exit'.
    Gère les erreurs de saisie pour les montants non numériques.
    """
    cb = Checkbook()
    while True:
        # Affiche le menu et obtient le choix de l'utilisateur
        action = input("Que souhaitez-vous faire ? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                cb.deposit(amount)
            except ValueError:
                print("Veuillez entrer un montant valide.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                cb.withdraw(amount)
            except ValueError:
                print("Veuillez entrer un montant valide.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
