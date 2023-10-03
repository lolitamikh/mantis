from model.project import Project
import random

def test_delete_some_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name="test"))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_project = app.project.get_projects_list()
    old_projects.remove(project)
    assert old_projects == new_project
    assert sorted(new_project, key=Project.name) == sorted(app.project.get_projects_list(), key=Project.name)