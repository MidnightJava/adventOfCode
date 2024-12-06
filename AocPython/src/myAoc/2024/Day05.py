""" 
Input is in two parts:

records like: x|Y represent a rule specifying that page y cannot be added to a list until page x is already in the list

records like x,y,z... represent a list of pages in a manual update

Part 1:

Determine which update lists are valid wrt any rules specified for the pages in the list. For each valid update, determine
the page in the middle of the update list. Add up all the middle page numbers and report that as the solution.

Part 2:

Collect all the updates that are not valid per instructions in Part 1. For each uf these, correct the order of the pages so
the update follows all the rules.  determine the middle page of each update list, add them up, and report that as the solution.
"""

from collections import defaultdict

def update_valid(update, rules):
    valid = True
    for page in update:
      for prior in rules[page]:
        if prior in update and update.index(prior) > update.index(page):
          valid = False
          break
    return valid

def correct_update(input, rules):
  """
  - Iterate over pages in the input list
    - For any page with no rule assigned, move it from the input the output list
  - Iterate through the input list until it's empty
    - Move to the output list each pages whose priors already exist in the output list
  """
  output = []
  for page in input:
    if not page in rules:
      output.append(input.pop(input.index(page)))
  while len(input):
    for page in input:
      priors = filter(lambda x: x not in output, rules[page])
      if all(map(lambda x: x in output or x not in input, priors)):
        output.append(input.pop(input.index(page)) if page  in input else page)
  return output

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
            update = line.split(",")
            updates.append(list(map(lambda x: int(x), update)))

count = 0
for update in updates:
    if update_valid(update, rules):
        count += middle_page(update)
    else:
        bad_updates.append(update)

print(f"Part 1: {count}")

count = 0
for update in bad_updates:
    corrected = correct_update(update, rules)
    count +=  middle_page(corrected)

print(f"Part 2: {count}")
# Part 1: 6951
# Part 2: 4121