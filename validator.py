def validate_string(value, allows_none=False, allows_empty=True, case_sensitive=False, acceptable_values=[]):
    if value == '' and allows_empty == False:
        return False
    if value == None and allows_none == False:
        return False
    if len(acceptable_values) > 0:
        if case_sensitive:
            for ac in acceptable_values:
                if ac == value:
                    break
            else:
                return False
        else:
            for ac in acceptable_values:
                if ac.lower() == value.lower():
                    break;
            else:
                return False
    return True


def validate_number(value, allows_none=False, allows_zero=True, allows_reals=True, allows_negatives=True,
                    allows_positives=True, acceptable_values=[]):
    if value == 0 and allows_zero == False:
        return False
    if value == None and allows_none == False:
        return False
    if value < 0 and allows_negatives == False:
        return False
    if value > 0 and allows_positives == False:
        return False
    if len(acceptable_values) > 0:
        for ac in acceptable_values:
            if ac == value:
                return True
        else:
            return False
    return True