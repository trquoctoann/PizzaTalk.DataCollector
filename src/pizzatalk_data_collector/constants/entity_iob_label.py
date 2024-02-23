from enum import Enum


class EntityIOBLabel(Enum):
    B_PIZZA = "B-PIZZA"
    I_PIZZA = "I-PIZZA"
    B_TOPPING = "B-TOPPING"
    I_TOPPING = "I-TOPPING"
    B_SIZE = "B-SIZE"
    I_SIZE = "I-SIZE"
    B_CRUST = "B-CRUST"
    I_CRUST = "I-CRUST"
    B_QUANTITY = "B-QUANTITY"
    I_QUANTITY = "I-QUANTITY"
    B_CUSTOMER_NAME = "B-CUS"
    I_CUSTOMER_NAME = "I-CUS"
    B_PHONE_NUMBER = "B-PHONE"
    I_PHONE_NUMBER = "I-PHONE"
    B_ADDRESS = "B-ADDRESS"
    I_ADDRESS = "I-ADDRESS"
    B_PAYMENT_METHOD = "B-PAYMENT"
    I_PAYMENT_METHOD = "I-PAYMENT"
    OTHER = "O"