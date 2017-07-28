from jinja2 import Environment, FileSystemLoader

def fill_template(file_infos):
    """
    Render Jinja2 mail template
    """
    j2_env = Environment(loader=FileSystemLoader("templates"),
                         trim_blocks=True)
    return j2_env.get_template('mailtemplate.html').render(
        files=file_infos, time=str(datetime.datetime.now())
    )
