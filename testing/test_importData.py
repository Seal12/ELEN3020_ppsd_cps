import unittest
import os
from controllers import importData


class TestImport(unittest.TestCase):

    def test_import_pca_evec(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pca_evec')
        importer = importData.ImportPCAData()
        importer.import_pca_evec(file_path)

        i = 0
        for subject in importer.subject_list:
            self.assertEqual(subject.id_num, 'subject:{}'.format(i))
            self.assertEqual(subject.values, ['pc1', 'pc2', 'pc3'])
            i += 1

    def test_import_admix_fam(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'admix_fam')
        importer = importData.ImportAdmixData()
        importer.import_admix_fam(file_path)

        i = 0
        for subject in importer.subject_list:
            self.assertEqual(subject.id_num, 'subject:{}'.format(i))
            i += 1

    if __name__ == '__main__':
        unittest.main()