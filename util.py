import os

import jinja2
import yaml


def load_run_config(run_config=None):

    with open(run_config) as config_run:
        try:
            run_yaml = yaml.load(config_run)
            return run_yaml
        except (yaml.YAMLError, FileExistsError, FileNotFoundError) as e:
            print(e)


def load_templates(tmpl_file):

    try:
        template_loader = jinja2.FileSystemLoader(searchpath='/')
        template_env = jinja2.Environment(loader=template_loader)

        return template_env.get_template(tmpl_file)

    except (Exception, jinja2.TemplateAssertionError, jinja2.TemplateSyntaxError) as templ_ex:
        print(templ_ex)


def render_templates(templ, data):
    pass



# print(load_run_config('run_config.yaml'))