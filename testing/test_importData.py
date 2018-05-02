import unittest
import os
from controllers import importData


class TestImport(unittest.TestCase):

    def test_import_values(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'pca_evec')
        importer = importData.ImportData()
        importer.import_values(file_path)

        print(len(importer.subject_list))
        i = 0
        for subject in importer.subject_list:
            self.assertEqual(subject.id_num, 'subject:{}'.format(i))
            self.assertEqual(subject.values, ['pc1', 'pc2', 'pc3'])
            i += 1

    if __name__ == '__main__':
        unittest.main()