from dao_product import DaoProduct

class Product(DaoProduct):

    def __init__(self, name: str, description: str, value: float) -> None:
        self.name = name
        self.description = description
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} - {self.description} - {self.value}"



