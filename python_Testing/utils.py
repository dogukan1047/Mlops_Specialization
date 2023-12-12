def str_to_bool(val):

    """
    convert a string representation of truth to True or False
    """

    true_vals=["yes","y",""]
    false_vals=["no","n"]

    try:
        val=val.lower()
    except AttributeError:
        val=str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False       
    else:
        raise ValueError("Invalid input value :%s" % val)    