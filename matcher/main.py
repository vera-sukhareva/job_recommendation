import spacy.cli

spacy.cli.download("en_core_web_md")

from src.model.Resume import Resume

if __name__ == '__main__':
    resume = Resume('Po', 'e@m.ru', ['a', 'b', 'c'], ['d', 'e', 'f'])
