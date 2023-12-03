import json

def answer_set_to_json(answer_set):
  atoms = []

  # Split the answer set by spaces
  answer_set = answer_set.split()

  counter = 0

  # Loop through each element in the answer set
  for element in answer_set:
    # Remove the parentheses and commas
    element = element.replace("(", " ")
    element = element.replace(")", " ")
    element = element.replace(",", " ")
  
    # Split the element by spaces
    element = element.split()

    # Loop through each element in the element
    atoms.append({"predicate": element[0], "arguments": element[1:]})

  return atoms