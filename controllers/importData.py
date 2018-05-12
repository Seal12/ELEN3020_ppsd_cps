#!/usr/bin/env python

"""importData.py: includes classes for importing the data files necessary for creating a PCA plot and Admixture Plot"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana", "Cedrick Platt"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

from models.subject import Subject
from models.pcaGroup import PCAGroup
from models.populationGroup import PopulationGroup


class ImportPCAData:

    def __init__(self):
        self.subject_list = []
        self.group_list = []
        self.group_names = []

    def import_pca_evec(self, file_path):
        """
        Imports the evec file for PCA, creates the subjects and returns a list of these subjects

        Keyword arguments:
            file_path -- the file path of the evec file
        """

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

    def import_pca_pheno(self, file_path, column=2):
        """Imports the phenotype file for PCA, creates the population groups and populates them with subjects

        :Restrictions:
            column argument should either be 2 or 3 if this is not the case the class won'nt throw an exception but rather set the column to a relevant value

            This method requires that the import_pca_evec method to have been run prior to it being called otherwise there won't be any subjects to populate the groups with

        Keyword arguments:
            file_path -- the file path of the phenotype file
            column -- the column which the relevant phenotype data is on (default 2)
        """

        # Ensure that valid phenotype columns are selected
        if column != 2 or column != 3:
            if column < 2:
                column = 2
            elif column > 3:
                column = 3

        # Create groups and populate them with subjects
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

    def import_admix_fam(self, file_path):
        """Imports the fam file necessary for an admixture plot, creates the subjects and returns a list of these subjects

        Keyword arguments:
            file_path -- the file path of the Q file
        """

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

    def import_admix_pheno(self, file_path, column=2):
        """Imports the phenotype file for admixture plots, creates the population groups and populates them with subjects

        :Note:
            This method requires import_admix_fam and import_admix_Q to have been run prior to it being called if not there wont be subjects with relevant data to populate the groups

        Keyword arguments:
            file_path -- the file path of the phenotype file
            column -- the column which the relevant phenotype data is on (default 2)


        """

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
        """Imports the Q file for admixture plot, iterates through the subjects and sets their ratios

        Keyword arguments:
            file_path -- the file path of the Q file

        This method requires the import_admix_fam method to have been called prior to calling this method
        If not there will not be any subjects to fill values with
        """
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
        """Ensures that all the subject ratios add up to 100%

         Keyword arguments:
            file_path -- the file path of the Q file
        """

        total = sum(ratios)

        for i in range(0, len(ratios)):
            ratios[i] = ratios[i]/total * 100

        return ratios
