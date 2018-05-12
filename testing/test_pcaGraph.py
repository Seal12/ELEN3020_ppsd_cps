#!/usr/bin/env python

"""test_pcaGraph.py: Testing for the pcaGraph.py file"""

__author__ = "Phatho Pukwana"
__credits__ = ["Phatho Pukwana"]
__email__ = "1388857@students.wits.ac.za"
__status__ = "Development"

import unittest
import os
import wx

from controllers import pcaGraph


class TestPCAGraph(unittest.TestCase):

    def setUp(self):
        evec_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_evec')
        pheno_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pca_pheno')

        self.graph = pcaGraph.PCAGraph()
        self.graph.import_data(evec_file_path,pheno_file_path)

    def test_find_subject(self):
        for i in range(0, len(self.graph.importer.subject_list)-1):
            subject = self.graph.find_subject('subject:{}'.format(i))
            self.assertEqual(subject.id_num,'subject:{}'.format(i))

    def test_find_group(self):
        for i in range(0, len(self.graph.groups)-1):
            group = self.graph.find_group('country{}:continent{}'.format(i,i))
            self.assertEqual(group.name,'country{}:continent{}'.format(i,i))

    if __name__ == '__main__':
        unittest.main()