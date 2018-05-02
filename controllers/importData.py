from models.subject import Subject
from models.pcaGroup import PCAGroup


class ImportData:

    def __init__(self):
        self.subject_list = []
        self.group_list = []
        self.group_names = []

    def import_values(self, file_path):

        with open(file_path, 'r') as f:
            # List of all lines in the file
            all_lines = f.readlines()

            # Splitting each line and populating subject list
            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = line[0]
                if subject_id == '#eigvals:':   # check to omit the top line of the evec file
                    continue

                subject_values = line[1:(len(line)-1)]  # this omits the last value in the line

                individual = Subject(id_num=subject_id, values=subject_values)
                self.subject_list.append(individual)

        return self.subject_list

    def import_pca_pheno(self, file_path):
        # group_names = []

        with open(file_path, 'r') as f:

            all_lines = f.readlines()

            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = '{}:{}'.format(line[0], line[1])
                subject_group_name = '{}:{}'.format(line[2], line[3])

                for subject in self.subject_list:
                    if subject.id_num == subject_id:

                        # if the group doesnt exist create a new one
                        if subject_group_name not in self.group_names:
                            self.group_names.append(subject_group_name)
                            population_group = PCAGroup(name=subject_group_name)
                            self.group_list.append(population_group)

                        else:
                            group_pos = self.group_names.index(subject_group_name)
                            population_group = self.group_list[group_pos]

                        population_group.add_subject(subject)

        return self.group_list

