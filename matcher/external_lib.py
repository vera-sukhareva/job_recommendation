import spacy.cli
import nltk


spacy.cli.download("en_core_web_md")
spacy.cli.download("en_core_web_sm")
nltk.download('stopwords')