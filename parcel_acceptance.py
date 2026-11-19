def is_parcel_accepted(weight_grams, length_cm):
    """Determine whether a parcel meets both measurement limits."""
    if type(weight_grams) is not int or type(length_cm) is not int:
        raise TypeError("invalid argument type")

    if weight_grams < 0 or length_cm < 0:
        raise ValueError("argument outside permitted range")
        
    return 1 <= weight_grams <= 20000 and 1 <= length_cm < 200
