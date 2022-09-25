from src.extractor.Extractor import extractor
from src.loader.Loader import loader
from src.transformer.Transformer import transformer


class Etl:
    def execute(self, file_name):
        data = extractor.extract(file_name)
        print('extracted')
        transformed_data = transformer.transform(data)
        print('transformed')
        loader.load(transformed_data)
        print('loaded')


etl = Etl()