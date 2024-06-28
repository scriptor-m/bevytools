import click
from core import gdr as gdr_helper , gpn as gpn_helper , grn as grn_helper , templates as t_helper , gcm as gcm_helper , gdocs as gdocs_helper , sdocs as sdocs_helper
from root_utils import save_config , load_config

@click.group()
def main():
   pass

# generate daily report
@click.command(name='gdr' , help='Generate a daily project report using your local git repo history.') 
@click.option('--path', "-p", help='Project directory path' , type=click.Path(exists=True))
def gdr(path):
   gdr_helper.generate_daily_report(path)

@click.command(name='gpn' , help='Generate a project name for your project using code') 
@click.option("--path" , "-p" , help='Project directory path' , type=click.Path(exists=True))
def gpn(path):
   gpn_helper.generate_project_name(path)


# generate release notes
@click.command(name='grn' , help='Generate a release notes using your local git repo history.') 
@click.option('--path', "-p", help='Project directory path' , type=click.Path(exists=True))
def grn(path):
   grn_helper.generate_release_notes(path)


# templates
@click.command(name='template' , help="Work with templates using this command. For more type 'bt template --help'")
@click.option('--list' , '-l' , help='List all the templates', type=bool , is_flag=True)
@click.option('--create' , '-c' , help='Create a new template', type=bool , is_flag=True)
@click.option('--load' , help='Load a template into current dir', type=bool , is_flag=True)
@click.option('--delete' , '-d' , help='Delete a template', type=bool , is_flag=True)
@click.option('--search' , '-s' , help='Search for a template', type=bool , is_flag=True)

@click.argument('path' , type=click.Path(exists=True) , required=False)
@click.argument ('name' , type=str , required=False)
def templates(list , create , path , load , name ):
   if list:
      t_helper.list_all_templates()
   elif create:
      if path is None or name is None:
         raise click.UsageError('Please specify the paths and name beside --create')
      else:
         t_helper.create_new_template(name,path)
   elif load:
      if name is None:
         raise click.UsageError('Please specify name of the template beside --load')
      else:
         t_helper.load_template()
   else:
      raise click.UsageError('Please specify a valid option')


# generate commit message
@click.command(name='gcm' , help='Generate a commit message using your local git repo history.')
@click.option('--path', "-p", help='Project directory path' , type=click.Path(exists=True))
def gcm(path):
   gcm_helper.generate_commit_message(path)


# generate documentation
@click.command(name="gdocs" , help="Generate documentation for your project")
@click.option('--path', "-p", help='Project directory path' , type=click.Path(exists=True))
def gdocs(path):
   gdocs_helper.generate_docs(path)


# serve documentation
@click.command(name="sdocs" , help="Serve documentation for your project in your local server")
@click.argument('port', type=int , required=False)
@click.option('--path', "-p", help='Project directory path' , type=click.Path(exists=True))
def sdocs(path,port=4576):
   sdocs_helper.serve_docs(path,port)

# configuration
@click.command(name="config" , help="Configure the tool")
@click.option('--ollama_model' , '-m' , help='Ollama model name' , type=str)
@click.option('--ollama_server_url' , '-u' , help='Ollama server url', default='http://localhost:11434/' , type=str)
@click.option('--show' , '-s' , help='Show current config' , type=bool , is_flag=True)
def config(ollama_model, show , ollama_server_url):
   if ollama_model:
      config_data = {
         'ollama_model' : ollama_model,
         'ollama_server_url' : ollama_server_url
      }
      save_config(config_data)
      click.echo("Config saved!")
   elif show:
      config = load_config()
      click.echo(config)
   else: 
      raise click.UsageError('Please provide valid options')


# main command group
main.add_command(config)
main.add_command(sdocs)
main.add_command(gdocs)
main.add_command(gcm)
main.add_command(templates)
main.add_command(grn)
main.add_command(gdr)
main.add_command(gpn)

# init tool
if __name__ == '__main__':
    main()