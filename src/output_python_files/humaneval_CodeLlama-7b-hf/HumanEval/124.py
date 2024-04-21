def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    if date == '':
        return False
    else:
        if date[2] == '-':
            date = date.replace('-', '/')
        if date[5] == '-':
            date = date.replace('-', '/')
        if date[8] == '-':
            date = date.replace('-', '/')
        if date[1] == '/' or date[4] == '/' or date[7] == '/':
            return False
        else:
            if date[0] == '0':
                return False
            else:
                if date[0] == '1' and date[1] == '0':
                    if int(date[2]) > 3:
                        return False
                    else:
                        if int(date[3]) > 1:
                            return False
                        else:
                            if int(date[4]) > 1:
                                return False
                            else:
                                if int(date[5]) > 1:
                                    return False
                                else:
                                    if int(date[6]) > 1:
                                        return False
                                    else:
                                        if int(date[7]) > 1:
                                            return False
                                        else:
                                            if int(date[8]) > 1:
                                                return False
                                            else:
                                                if int(date[9]) > 1:
                                                    return False
                                                else:
                                                    if int(date[10]) > 1:
                                                        return False
                                                    else:
                                                        if int(date[11]) > 1:
                                                            return False
                                                        else:
                                                            if int(date[12]) > 1:
                                                                return False
                                                            else:
                                                                return True
                if date[0] == '1' and date[1] == '1':
                    if int(date[2]) > 1:
                        return False
                    else:
                        if int(date[3]) > 1:
                            return False
                        else:
                            if int(date[4]) > 1:
                                return False
                            else:
                                if int(date[5]) > 1:
                                    return False
                                else:
                                    if int(date[6]) > 1:
                                        return False
                                    else:
                                        if int(date[7]) > 1:
                                            return False
                                        else:
                                            if int(date[8]) > 1:
                                                return False
                                            else:
                                                if int(date[9]) > 1:
                                                    return False
                                                else:
                                                    if int(date[10]) > 1:
                                                        return False
                                                    else: