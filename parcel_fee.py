def delivery_fee(weight_grams):
    """Calculate the delivery fee using two weight bands."""
    if type(weight_grams) is not int:
        raise TypeError("invalid argument type")

    if not 1 <= weight_grams <= 20000:
        raise ValueError("argument outside permitted range")

    if weight_grams < 1000:
        return 500
        
    return 1000
