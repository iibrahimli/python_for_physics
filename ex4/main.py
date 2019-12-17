import requests
from bs4 import BeautifulSoup


nist_url = "https://webbook.nist.gov/cgi/cbook.cgi?Name={}"

def get_info(name):
    resp = requests.get(nist_url.format(name))
    resp_soup = BeautifulSoup(resp.text, 'html.parser')
    info = {}

    formula_a_text = "Formula"
    formula_text = str(resp_soup.find('a', text=formula_a_text).parent.parent.text)
    info['formula'] = formula_text[formula_text.find(": ")+1:].strip()

    weight_a_text = "Molecular weight"
    info['weight'] = resp_soup.find('a', text=weight_a_text).parent.next_sibling.strip()

    return info


names = ["glucose", "ethanol", "caffeine", "octane", "cyclohexane"]

for name in names:
    res = get_info(name)
    print(f"{name:14} - ", end='')
    for k, v in res.items():
        print(f"{v:>12}   ", end='')
    print()