from enum import Enum


class Roles(Enum):
    PO = "PRODUCT OWNER"
    SM = "MASTER"
    ST = "TEAM"

    def __lt__(self, other):
        """`sort` function will use self.value to sort a list of enums of type Roles"""
        return self.value < other.value
