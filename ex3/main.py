import re
import warnings
import numpy as np
import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)



def parse_formula(formula):
    """
    Parse formula string and return a dict of atom name -> number of atoms
    """
    formula_re = re.compile(r"[A-Z][a-z]?[0-9]?")
    char_re = re.compile(r"[A-Z][a-z]?")
    digit_re = re.compile(r"[0-9]")
    res = {}

    for m in formula_re.finditer(formula):
        m_m = m.group(0)
        atom_name = char_re.findall(m_m)[0]
        n_atoms = digit_re.findall(m_m)
        if atom_name not in res:
            res[atom_name] = 0
        if len(n_atoms) == 0:
            res[atom_name] += 1
        else:
            res[atom_name] += int(n_atoms[0])
    return pd.Series(res)


df = pd.read_csv("aminoacids.csv", index_col='Name')

print("Heaviest molecule: ")
print("   ", df['Molecular Weigth'].idxmax())

print()
print("Positively charged molecules: ")
print("   ", ", ".join(df.index[df['Polarization'] == 'positive'].tolist()))

print()
print("Counts of molecules by polarization type: ")
tmp = df['Polarization'].value_counts()
names = tmp.index.tolist()
vals  = tmp.values
for n, c in zip(names, vals):
    print(f"    {n:12}: {c}")

print()
print("Names of heaviest molecules by polarization types:")
tmp = df.groupby('Polarization', sort=False)['Molecular Weigth'].idxmax()
names = tmp.index.tolist()
heaviest  = tmp.values
for n, c in zip(names, heaviest):
    print(f"    {n:12}: {c}")


print()
print("Means and standard deviations of molecules by polarization types:")
res = df.groupby('Polarization', sort=False)['Molecular Weigth'].mean()
res = pd.concat([res, df.groupby('Polarization', sort=False)['Molecular Weigth'].std()], axis=1)
names = res.index.tolist()
means = res.values[:, 0]
stds = res.values[:, 1]
print(f"    {'name':12}:   mean      std")
print(f"    --------------------------------")
for n, m, s in zip(names, means, stds):
    print(f"    {n:12}:   {m:.3f}   {s:.3f}")


print()
print("Counts of H, N, C, and O:")
df_new = df['Molecular Formula'].apply(parse_formula)
df_final = pd.concat([df, df_new], axis=1)
df_final = df_final.drop(columns=['S'])
print(df_final)

df_final.to_csv("NewAminoAcids.csv")
