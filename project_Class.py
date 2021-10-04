class Project:
    
    def __init__(self, ID, desc, consul, due):
        self.projid = ID
        self.projdesc = desc
        self.consultants = consul
        self.duedate = due


    def get_projid(self):
        return self.projid

    def get_projdesc(self):
        return self.projdesc

    def get_consultants(self):
        return self.consultants

    def get_duedate(self):
        return self.duedate
