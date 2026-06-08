def is_valid(record):

    if not record["claim_id"]:
        return False

    if not record["policy_number"]:
        return False

    if not record["customer_name"]:
        return False

    if not record["claim_date"]:
        return False

    if not record["amount"]:
        return False

    return True