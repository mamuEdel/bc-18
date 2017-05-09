""" Demonstrates virtual wallet """


class Wallet(object):
    """ Defines blue print for digital wallet """
    def _init_(self):
    	self.balance = 0

    def deposit(self, amount):
        """ Adds money to wallet 
         1. Get amount to be deposited
         2. Update balance with amount
         3. Output = updated balance"""
        if not isinstance( amount, int):
        	return "Numbers only Please!"
        self. balance += amount
        return self.balance

    def withdraw(self):
        """ Withdraws money from wallet """
        pass
