import unittest
import jinja2
import util


class TestRunConfig(unittest.TestCase):

    def setUp(self):

        self.test_yml = util.load_run_config('files/test_yaml.yml')
        self.test_tempalate = util.load_templates(template_file='myfile.jinja2', search_path='templates')
        self.test_generate = util.generate_file(template='myfile.jinja2',
                                                config='files/test_yaml.yml',
                                                search_path='templates',
                                                artifact_name='manifest',
                                                output_file='/tmp/myfile')
        self.test_template_execpt = util.load_templates(template_file='myfi.jina', search_path='blah')

    def test_run_open(self):

        self.assertIsInstance(self.test_yml, dict)

    def test_load_template(self):

        self.assertIsInstance(self.test_tempalate, jinja2.Template)

    def test_generate_file(self):

        self.assertIsInstance(self.test_generate, dict)











