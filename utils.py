def match_to_user(measure, usernames):
    matched_dict = {}
    for idx, username in enumerate(usernames):
        matched_dict[username] = measure.get(str(idx))
    matched_dict = {k: v for k, v in sorted(matched_dict.items(), key=lambda item: item[1])}
    return matched_dict