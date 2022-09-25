from flask import request
from flask_restful import Resource

from src.model.user.UserStatus import UserStatus
from src.producer.MessageProducer import messageProducer
from src.servicies.ResumeService import resumeService
from src.servicies.UserService import userService


class ResumeController(Resource):
    def post(self):
        resume_pdf = request.files['resume']
        parsed_resume = resumeService.parse(resume_pdf)
        user = userService.get_by_email(parsed_resume.email)
        if not user:
            user = userService.save_user(parsed_resume.email)
        elif user.status == UserStatus.PROCESSING:
            return {'message': 'wait, your previous resume is processing'}
        saved_resume = resumeService.save_resume(parsed_resume)
        updated_user = userService.update_user(user.id, UserStatus.PROCESSING, saved_resume.id)
        messageProducer.publish(saved_resume, user.id)
        return {'message': 'status for {} is {}'.format(saved_resume.email, updated_user.status.value)}
