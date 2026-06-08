def parser(line):
    result = {
        "claim_id": line[0:10].strip(),
        "customer_name": line[10:38].strip(),
        "claim_date": line[38:46].strip(),
        "hospital": line[46:74].strip(),
        "amount": line[74:83].strip(),
        "policy_number": line[83:106].strip()
    }
    return result