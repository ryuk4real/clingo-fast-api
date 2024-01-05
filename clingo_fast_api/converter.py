from typing import Iterable
from clingo import Model, SymbolType


def to_atoms(model: Model) -> Iterable[str]:
    answer_set = []

    for atom in model.symbols(shown=True):
        answer_set.append(str(atom))

    return answer_set