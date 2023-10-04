from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_projects_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for project in projects:
                project_list.append(Project(name=project.name,
                                            description=project.description))
            return project_list
        except WebFault:
            return None
