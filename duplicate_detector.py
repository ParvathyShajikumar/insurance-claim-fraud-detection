from utils import similarity

def detect_duplicates(records):

    seen = {}
    duplicates = []

    for parsed in records:

        key = parsed["policy_number"]

        if key in seen:

            old_record = seen[key]

            policy_match = (
                old_record["policy_number"] ==
                parsed["policy_number"]
            )

            amount_match = (
                old_record["amount"] ==
                parsed["amount"]
            )

            name_score = similarity(
                old_record["customer_name"],
                parsed["customer_name"]
            )

            hospital_score = similarity(
                old_record["hospital"],
                parsed["hospital"]
            )

            overall_score = (
                name_score + hospital_score
            ) / 2

            if (
                policy_match and
                (
                    amount_match or
                    overall_score > 0.65
                )
            ):

                duplicates.append({
                    "record1": old_record,
                    "record2": parsed,
                    "similarity_score": overall_score
                })

        else:
            seen[key] = parsed

    return duplicates