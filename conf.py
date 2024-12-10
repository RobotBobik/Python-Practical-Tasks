import yaml
from jinja2 import Environment, FileSystemLoader
import os

def generate_vhosts():
    try:
        if os.path.exists('vhosts.conf'):
            print("Removing existing vhosts.conf...")
            os.remove('vhosts.conf')
        
        print("Loading data from data.yml...")
        with open('data.yml', 'r') as file:
            data = yaml.safe_load(file)
        print("Data loaded successfully:", data)
        
        print("Setting up Jinja2 environment...")
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('vhosts.j2')
        print("Template loaded successfully.")

        print("Rendering template...")
        output = template.render(hosts=data['hosts']).strip()
        print("Template rendered successfully.")

        print("Writing to vhosts.conf...")
        with open('vhosts.conf', 'w') as f:
            f.write(output)
        print("vhosts.conf has been generated.")
        
        if os.path.exists('vhosts.conf'):
            print("vhosts.conf exists and is ready for use.")
        else:
            print("Error: vhosts.conf was not created.")
    
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except yaml.YAMLError as yaml_error:
        print(f"Error parsing YAML file: {yaml_error}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    generate_vhosts()