import re
import asyncio

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


"""def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name"""


def normalize(name: str) -> str:
    p_name = name.translate(TRANS)
    t_name = name.translate(TRANS)
    p_name = re.findall(r'^[^.]+', p_name)
    p_name = re.sub(r'\W', '_', p_name[0])
    t_name = re.sub(r'^[^.]+', '', t_name)
    return p_name + t_name
