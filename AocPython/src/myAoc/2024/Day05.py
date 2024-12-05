from collections import defaultdict

def update_valid(update, rules):
    valid = True
    for page in rules.keys():
        if page in update:
            priors = rules[page]
            for prior in priors:
                if prior in update and update.index(prior) > update.index(page):
                    valid = False
                    break
    return valid

def correct_update(update, rules):
    """
    - Add all pages with no priors
    - Recursively add pages whose priors already exist in the list
    - Verify that all the pages got added.
    """

def middle_page(update):
    idx = len(update) // 2
    return update[idx]

with open("2024/data/day05") as f:
    # {y: x}, where x must come before y
    rules = defaultdict(list)
    updates = []
    bad_updates = []
    rules_compelte = False
    for line in f:
        if line.strip() == "":
            rules_compelte = True
            continue
        if not rules_compelte:
            rule = line.split("|")
            rules[int(rule[1])].append(int(rule[0]))
        else:
            update = line.strip().split(",")
            updates.append(list(map(lambda x: int(x), update)))
# print(rules)
# for update in updates:
#     print(update)

count = 0
for update in updates:
    if update_valid(update, rules):
        count += middle_page(update)
    else:
        bad_updates.append(update)

print(f"Part 1: {count}")

count += 0
for update in bad_updates:
    correct_order(update, rules)
    count +=  middle_page(update)

print(f"Part 2: {count}")
# Part 1: 6951
