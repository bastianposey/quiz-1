
import project_Class as pc
# create instances

project1 = pc.Project(1001, "SAP Implementation", 25, "09/30/2022")
project2 = pc.Project(1002, "Migration to CRM", 10, "06/30/2022")


# create dict

project_dic = {project1.get_projid():project1.get_duedate(),project2.get_projid():project2.get_duedate()}

print(project_dic)

