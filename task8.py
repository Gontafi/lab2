from abc import ABC, abstractmethod
from enum import Enum


class CurrencyUSDExchangeRate(Enum):
    USD = 1.0
    KZT = 465.5
    RUB = 60.5


class BankOperations(ABC):

    @abstractmethod
    def add_to_bank_account(self, amount: float) -> None:
        pass

    @abstractmethod
    def subtract_from_bank_account(self, amount: float) -> None:
        pass


class Converter(ABC):

    @abstractmethod
    def convert_money(self, amount: int, currency_from: str, currency_to: str) -> float:
        pass


class BankAccountUSD(BankOperations, Converter):

    def __init__(self):
        self.user_wallet = 0.0

    def add_to_bank_account(self, amount: float) -> None:
        self.user_wallet += amount

    def subtract_from_bank_account(self, amount: float) -> None:
        self.user_wallet -= amount

    #@staticmethod
    def convert_money(self, amount: float, currency_from: str, currency_to: str) -> float:
        return amount / CurrencyUSDExchangeRate[currency_from].value * CurrencyUSDExchangeRate[currency_to].value

    def __repr__(self) -> str:
        return str(self.user_wallet)


account = BankAccountUSD()

print(f'Bank account wallet: {account}$\n')

account.add_to_bank_account(500)

print(f'Bank account wallet after adding 500$: {account}$\n')

account.subtract_from_bank_account(300)

print(f'Bank account wallet after subtracting 300$: {account}$\n')

print(f'Convert 300 USD to KZT: {account.convert_money(300, "USD", "KZT")} KZT')
print('1 USD is 465.5KZT\n')

print(f'Convert 200 RUB to KZT: {account.convert_money(200, "RUB", "KZT")} KZT')
print('1 RUB is 7,69KZT\n')

print(f'Convert 465500KZT to USD: {account.convert_money(465500, "KZT", "USD")} USD')
