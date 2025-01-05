import random

# Véletlen szavak listája
WORDS = [
    "alma", "kutya", "ház", "autó", "virág", "asztal", "szék", "nap", "hold",
    "tenger", "híd", "madár", "könyv", "zene", "idő", "erdő", "utca", "hó",
    "barát", "szerelem", "történet", "mosoly", "lámpa", "kert", "szív",
    "vár", "folyó", "hegy", "mező", "tér", "tó", "vers", "csillag", "ajtó",
    "ablak", "kép", "térkép", "mese", "csoda", "szín", "szél", "víz", "élet"
]
# Véletlenszám generáló függvény
def random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def random_sentence():
    word_count = random.randint(3, 10)
    return " ".join(random.choice(WORDS) for _ in range(word_count)) + "."

# Bekezdés generáló függvény (3-7 mondat)
def random_paragraph():
    sentence_count = random.randint(3, 7)
    return " ".join(random_sentence() for _ in range(sentence_count))

# Véletlenszerű bekezdésszám generálása (1-től a felhasználó által megadott maxig)
def generate_paragraphs(max_paragraphs):
    paragraph_count = random.randint(1, max_paragraphs)
    return "\n\n".join(random_paragraph() for _ in range(paragraph_count))