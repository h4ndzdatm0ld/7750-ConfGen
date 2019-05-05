#!/usr/bin/env python3
import yaml
import jinja2
import time
from netmiko import Netmiko
import threading

# Update the yaml file name for the specific router you wish to connect to.
yaml_file = 'r4-64500.yml'
jinja_template = 'template.j2'

# Generate the configurations and send it to the devices
def confgen(vars):
    # Generate configuration lines with Jinja2
    with open(jinja_template) as f:
        tfile = f.read()
    template = jinja2.Template(tfile)
    cfg_list = template.render(vars)

    # Connect directly to host via SSH on the specified port
    conn = Netmiko(host=vars['hostip'], device_type='alcatel_sros', username="admin", password="admin")

    # Send generated commands to host
    output = conn.send_config_set(cfg_list)

    # Display results
    print('-' * 80)
    print('\nConfiguration applied on ' + vars['host'] + ': \n\n' + output)
    print('-' * 80)

    # Probably a good idea
    conn.disconnect()

# Parse the YAML file
with open(yaml_file) as f:
    read_yaml = yaml.load(f)  # Converts YAML file to dictionary

# Take imported YAML dictionary and start multi-threaded configuration generation.
# You could condense all yaml files into one if you wanted.
for hosts, vars in read_yaml.items():
    # Add host to vars dictionary
    host = {'host': hosts}
    vars.update(host)

    # Send vars dictionary to confgen function using multi-threading, one thread per-host
    threads = threading.Thread(target=confgen, args=(vars,))
    threads.start()
