import unittest
import os
from controllers import pcaGraph


class TestPCAGraph(unittest.TestCase):

    def test_find_subject(self):
        # Create PCAGraph instance
        graph = pcaGraph.PCAGraph()
        # Import test evec values
        fam_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_evec')
        graph.import_fam_file(fam_file_path)
        # Import test phenotype data
        pheno_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_pheno')
        graph.import_pheno_file(pheno_file_path)

        for i in range(0, len(graph.importer.subject_list)-1):
            subject = graph.find_subject('subject:{}'.format(i))
            self.assertEqual(subject.id_num,'subject:{}'.format(i))

    def test_find_group(self):
        # Create PCAGraph instance
        graph = pcaGraph.PCAGraph()
        # Import test evec values
        fam_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_evec')
        graph.import_fam_file(fam_file_path)
        # Import test phenotype data
        pheno_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_pheno')
        graph.import_pheno_file(pheno_file_path)

        for i in range(0, len(graph.groups)-1):
            group = graph.find_group('country{}:continent{}'.format(i,i))
            self.assertEqual(group.name,'country{}:continent{}'.format(i,i))

    if __name__ == '__main__':
        unittest.main()