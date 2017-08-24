import jinja2
import yaml


def load_run_config(run_config=None):

    with open(run_config) as config_run:
            run_yaml = yaml.load(config_run)
            return run_yaml


def load_templates(template_file=None, search_path=None):

    try:
        template_loader = jinja2.FileSystemLoader(searchpath='/'.join([search_path]))
        template_env = jinja2.Environment(loader=template_loader)

        return template_env.get_template(template_file)

    except (jinja2.TemplateAssertionError, jinja2.TemplateNotFound) as templ_ex:
        print("Something went wrong trying to load template: {}".format(templ_ex))
        return None


def generate_file(template, config=None, search_path=None, artifact_name=None, output_file=None):

    run_config = load_run_config(config)
    template_load = load_templates(template_file=template, search_path=search_path)

    if run_config is not None or template_load is not None:

        try:
            run_file_meta = run_config['run_info']['project_files'][artifact_name]
            with open(output_file, 'w') as templ_output:

                templ_output.write(template_load.render(run_file_meta))

                return {'output_file': output_file, 'status': 'success', 'artifact_name': artifact_name}

        except jinja2.UndefinedError as je:
            print("Template data in {0} is errored because {1}".format(template, je))






