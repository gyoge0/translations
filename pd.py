import pandas as pd
from googletrans import Translator
from english_words import get_english_words_set

translator = Translator()

df = pd.DataFrame()
web2lowerset = get_english_words_set(["web2"], lower=True)
df["english"] = list(web2lowerset)[:250]

languages = {
    "tamil": "ta",
    "malayalam": "ml",
    "telugu": "te",
    "hindi": "hi",
    "latin": "la",
}


def add_language(lang, code):
    translations = translator.translate(list(df["english"]), src="en", dest=code)
    df[lang] = list(map(lambda x: x.text, translations))


for lang, code in languages.items():
    add_language(lang, code)

print(df.head())
df.to_csv("translations.csv", sep=",", encoding="utf-8", index=False)
