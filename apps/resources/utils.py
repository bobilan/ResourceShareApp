def generate_cat_count_list(cat_cnts):
    res = ""
    for cat_cnt in cat_cnts:
        res += f"<li> {cat_cnt['cat_id__cat']}: {cat_cnt['cnt']}'</li>"
        return res

