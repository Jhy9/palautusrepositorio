from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        di = toml.loads(content, _dict = dict)
        di = di[list(di.keys())[0]]
        di = di[list(di.keys())[0]]
        di4 = di[list(di.keys())[7]]
        di4 = di4[list(di4.keys())[0]]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(di['name'], di['description'],di['license'], di['dependencies'], di4['dependencies'], di['authors'])
