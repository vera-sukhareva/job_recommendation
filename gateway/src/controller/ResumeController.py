from flask import request
from flask_restful import Resource

from src.servicies.ResumeService import resumeService


class ResumeController(Resource):
    def post(self):
        resume_pdf = request.files['resume']
        response = resumeService.sent_resume(resume_pdf)
        return response
