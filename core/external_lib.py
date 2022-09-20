import spacy.cli
import en_core_web_md
import nltk


spacy.cli.download("en_core_web_md")
spacy.cli.download("en_core_web_sm")
nlp = en_core_web_md.load()
nltk.download('stopwords')
