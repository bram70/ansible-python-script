import os
import sys
import yaml

from ansible import playbook
from ansible import inventory
from ansible import callbacks
from ansible import utils

utils.VERBOSITY = 3

ANSIBLE_HOSTS = 'local'
INVENTORY_FILE = 'servers.yml'
PLAYBOOK = 'playbook.yml'
CONFIG_RECIPES_FILE = 'script-config.yml'

playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
stats = callbacks.AggregateStats()
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

inventory = inventory.Inventory(INVENTORY_FILE)
inventory.subset(ANSIBLE_HOSTS)

inventory.set_playbook_basedir(os.path.dirname(PLAYBOOK))
hosts = inventory.list_hosts(ANSIBLE_HOSTS)

if len(hosts)==0:
    raise Exception('Could not find any host to match "%s" in the inventory "%s" file' % (ANSIBLE_HOSTS, INVENTORY_FILE))

stream = open(CONFIG_RECIPES_FILE, 'r')
configurations = yaml.load(stream)

for recipe in configurations:
    print recipe['only_tags']

    dictionary = dict(
            inventory=inventory,
            playbook = PLAYBOOK,
            callbacks=playbook_cb,
            runner_callbacks=runner_cb,
            stats=stats,
            check=False)

    dictionary.update(recipe)

    pb = playbook.PlayBook(**dictionary)
    results = pb.run()
    print results
