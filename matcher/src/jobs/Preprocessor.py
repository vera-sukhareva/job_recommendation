import en_core_web_md
from src.dao.VacancyDao import vacancyDao
import numpy as np


class Preprocessor:
    nlp = None
    VECTORS_LEN = 300

    def __init__(self):
        self.nlp = en_core_web_md.load()

    def process_job_data(self):
        descriptions = vacancyDao.find_all_descriptions()
        description_vectors = np.zeros((len(descriptions), self.VECTORS_LEN))
        for i, desc in enumerate(self.nlp.pipe(descriptions)):
            vector = np.zeros(self.VECTORS_LEN )
            valid_tokens = 0
            for token in desc:
                if not token.is_stop and not token.is_punct and token.has_vector:
                    vector += token.vector
                    valid_tokens += 1
            vector = vector / valid_tokens if valid_tokens > 1 else vector
            description_vectors[i, :] = vector
        with open('data/job_descr_vectors.npy', 'wb') as f:
            np.save(f, description_vectors)


preprocessor = Preprocessor()
