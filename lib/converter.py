import json

def answer_set_to_json(answer_set) -> dict:
  atoms = []

  # Split the answer set by spaces
  answer_set = answer_set.split()

  # Loop through each element in the answer set
  for element in answer_set:
    # Remove the parentheses and commas
    element = element.replace("(", " ")
    element = element.replace(")", " ")
    element = element.replace(",", " ")

    # Split the element by spaces and add it to an array
    element = element.split()

    # Convert the element to a dictionary with keys "predicate" and "arguments"
    element = {"predicate": element[0], "arguments": element[1:]}

    # Append the element to the atoms list
    atoms.append(element)

  return json.loads(json.dumps(atoms))