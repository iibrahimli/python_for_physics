import re
import pandas as pd


def parse_formula(formula):
    """
    Parse formula string and return a dict of atom name -> number of atoms
    """
    formula_re = re.compile(r"[A-Z][a-z]?[0-9]+")
    char_re = re.compile(r"[A-Z][a-z]?")
    digit_re = re.compile(r"[0-9]+")
    res = {}

    for m in formula_re.finditer(formula):
        m_m = m.group(0)
        atom_name = char_re.findall(m_m)[0]
        n_atoms = digit_re.findall(m_m)
        n_atoms = list(filter(lambda x: len(x) > 0, n_atoms))
        if atom_name not in res:
            res[atom_name] = 0
        if len(n_atoms) == 0:
            res[atom_name] += 1
        else:
            res[atom_name] += int(n_atoms[0])

    return res


formulas = pd.read_csv("formula.csv", sep=';', names=['name', 'formula'])
for i in range(len(formulas)):
    name = formulas.loc[i, 'name']
    formula = formulas.loc[i, 'formula']
    counts = parse_formula(formula)
    if counts.get('H') == 4:
        print(f"4 Hydrogen atoms:  {name} - {formula}")
    if counts.get('Br') == 3:
        print(f"3 Bromine atoms:  {name} - {formula}")