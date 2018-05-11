from models.subject import Subject
from models.pcaGroup import PCAGroup
from models.populationGroup import PopulationGroup


class ImportPCAData:

    def __init__(self):
        self.subject_list = []
        self.group_list = []
        self.group_names = []

    def import_pca_evec(self, file_path):

        with open(file_path, 'r') as f:
            # List of all lines in the file
            all_lines = f.readlines()

            # Splitting each line and populating subject list
            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = line[0]
                if subject_id == '#eigvals:':   # check to omit the top line of the pca_evec file
                    continue

                subject_values = line[1:(len(line)-1)]  # this omits the last value in the line

                individual = Subject(id_num=subject_id, values=subject_values)
                self.subject_list.append(individual)

        return self.subject_list

    def import_pca_pheno(self, file_path, column):
        # group_names = []

        with open(file_path, 'r') as f:

            all_lines = f.readlines()

            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = '{}:{}'.format(line[0], line[1])
                subject_group_name = line[column]

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


class ImportAdmixData:

    def __init__(self):
        self.subject_list = []
        self.group_list = []
        self.group_names = []

    def import_admix_fam(self,file_path):
        with open(file_path, 'r') as f:
            # List of all lines in the file
            all_lines = f.readlines()

            # Splitting each line and populating subject list
            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = '{}:{}'.format(line[0], line[1])

                individual = Subject(id_num=subject_id, values=[])
                self.subject_list.append(individual)

        return self.subject_list


    def import_admix_pheno(self, file_path, column):
        # Create groups and populate them with subjects
        with open(file_path, 'r') as f:

            # List of all lines in the file
            all_lines = f.readlines()

            for i in range(0, len(all_lines)):
                line = all_lines[i].split()

                subject_id = '{}:{}'.format(line[0], line[1])
                subject_group_name = line[column]

                for subject in self.subject_list:
                    if subject.id_num == subject_id:

                        # if the group doesnt exist create a new one
                        if subject_group_name not in self.group_names:
                            self.group_names.append(subject_group_name)
                            population_group = PopulationGroup(name=subject_group_name)
                            self.group_list.append(population_group)

                        else:
                            group_pos = self.group_names.index(subject_group_name)
                            population_group = self.group_list[group_pos]

                        population_group.add_subject(subject)

        # Making an dictionary of the different ancestry heights per group
        for group in self.group_list:
            # Populate the dictionary with ancestry values
            for subject in group.subjects:
                # Calculate the height of the ancestry bar graphs
                for key in range(0, len(subject.values)):
                    value = 0
                    for j in range(key, len(subject.values)):
                        value += subject.values[j]
                    # Store the heights in a dictionary of lists
                    group.ancestries[key].append(value)

        return self.group_list

    def import_admix_Q(self,file_path):
        with open(file_path, 'r') as f:
            all_lines = f.readlines()

            if len(all_lines) == len(self.subject_list):  # Check that the lines in the Q file match the lines in the fam
                i = 0

                for line in all_lines:
                    # Following line of code splits the line into a list of ratios,casts the list to a list of floats then normalizes the values
                    ratios = self.normalize_ratios([float(j) for j in line.split()])
                    self.subject_list[i].values = ratios
                    i += 1

                return self.subject_list

            else:
                return 'fam file and Q file do not match'

    def normalize_ratios(self, ratios):
        total = sum(ratios)

        for i in range(0, len(ratios)):
            ratios[i] = ratios[i]/total * 100

        return ratios
