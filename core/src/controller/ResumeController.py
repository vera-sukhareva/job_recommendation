from flask import request
from flask_restful import Resource

from src.dao.ResumeDao import resumeDao
from src.dao.UserDao import userDao
from src.model.UserStatus import UserStatus
from src.producer.MessageProducer import messageProducer
from src.servicies.ResumeService import resumeService
from src.servicies.UserService import userService


class ResumeController(Resource):
    def post(self):
        resume_pdf = request.files['resume']
        parsed_resume = resumeService.parse(resume_pdf)
        user = userService.get_by_email(parsed_resume.email)
        if not user:
            user = userDao.save_user(parsed_resume)
        elif user.status == UserStatus.PROCESSING:
            return {'message': 'wait, your previous resume is processing'}
        saved_resume = resumeDao.save_resume(parsed_resume)
        user.status = UserStatus.PROCESSING
        user.resume_id = saved_resume.id
        updated_user = userService.update_user(user)
        messageProducer.publish(parsed_resume, user.id)
        return {'message': 'status for {} is {}'.format(saved_resume.email, updated_user.status.value)}
