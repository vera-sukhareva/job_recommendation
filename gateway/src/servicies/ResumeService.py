import json

import requests
from werkzeug.datastructures import FileStorage

from src.constants import Urls

HEADERS = {
# 'Accept': "multipart/form-data",
'Content-Type': "multipart/form-data"
}


class ResumeService():

    def send_resume(self, resume_file: FileStorage):

        file = {'resume':(resume_file.filename,
                          resume_file.stream,
                          resume_file.mimetype)}
        res = requests.post(Urls.CORE_RESUME_URL,
                            files=file)
        return json.loads(res.content)


resumeService = ResumeService()
