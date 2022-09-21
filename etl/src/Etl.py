from src.extractor.Extractor import extractor
from src.loader.Loader import loader
from src.transformer.Transformer import transformer


class Etl:
    def execute(self, file_name):
        data = extractor.extract(file_name)
        transformed_data = transformer.transform(data)
        loader.load(transformed_data)


etl = Etl()