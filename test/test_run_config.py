import os
import unittest

import jinja2
import yaml
import util

class TestRunConfig(unittest.TestCase):

    def setUp(self):

        self.test_yml = yaml.load('files/test_yaml.yml')

    def test_run_open(self):

        test_var = util.load_run_config(run_config=self.test_yml)
        self.assertIsInstance(test_var, dict)

    def test_load_template(self):

        test_var = util.load_templates(os.getcwd()+'/templates/myfile.jinja2')
        self.assertIsInstance(test_var, jinja2.Template)








