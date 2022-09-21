from typing import List
import en_core_web_md
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

from src.dao.VacancyDao import vacancyDao
from src.model.Resume import Resume
from src.model.Vacancy import Vacancy


class Matcher:
    nlp = None
    vacancies = []
    VECTORS_LEN = 300

    def __init__(self):
        self.nlp = en_core_web_md.load()
        self.vacancies = vacancyDao.find_all()

    def recommend(self, resume: Resume, num_of_recommendations: int) -> List[Vacancy]:
        description_vectors = None
        with open('data/job_descr_vectors.npy', 'rb') as f:
            description_vectors = np.load(f)
        resume_description = ''.join(resume.experience + resume.skills)
        recommended = self._get_top_similar(description_vectors, resume_description, num_of_recommendations)
        return recommended

    def _sent2vect(self, text):
        vector = np.zeros(self.VECTORS_LEN)
        valid_tokens = 0
        for token in self.nlp(text):
            if not token.is_stop and not token.is_punct and token.has_vector:
                vector += token.vector
                valid_tokens += 1
        vector = vector / valid_tokens if valid_tokens > 1 else vector
        return vector

    def _get_top_similar(self, job_descr_vectors, resume_description, num_of_recommendations=5):
        vector = self._sent2vect(resume_description)
        distances = cosine_distances([vector], job_descr_vectors)
        most_similar = np.argsort(distances).flatten()[:num_of_recommendations]
        recommended = []
        for i in most_similar:
            recommended.append(self.vacancies[i].title)
        return recommended


matcher = Matcher()
