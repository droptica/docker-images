import os
import sys
from optparse import OptionParser, OptionGroup
from .aliases import __all__ as available_aliases, aliases
import docker_drupal.version

__version__ = docker_drupal.version.__version__

parser = OptionParser(version=__version__)

args = ["-p", "--docker-run-path", "-s", "--docker-shell-run", "-c",
        "--docker-container", "-f", "--force-replace-conf", "-e", "--drush-eval-run-code", "-y"]

for i, arg in enumerate(sys.argv):
    if arg.startswith('-'):
        arg = arg.split('=')[0].strip()
        print arg, i
        dest = "docker_fake_value_" + str(i)
        parser.add_option(arg, action="store")

parser.add_option("-p", "--docker-run-path", dest="docker_run_path",
              help="set path do drupal wrapper with 'docker-compose.yml' files and 'docker' folder", metavar="DOCKER_RUN_PATH")

parser.add_option("-s", "--docker-shell-run", action="store_true", dest="docker_shell_run",
              help="Use with no action or 'shell' action. "
                   "set if you want to run docker shell",)

parser.add_option("-c", "--docker-container", dest="docker_container",
              help="Use with 'shell' action. Set container name to run bash in it.", metavar="DOCKER_CONTAINER")

parser.add_option("-f", "--force-replace-conf", action="store_true", dest="docker_init_replace_conf",
              help="Use with action 'init'. "
                   "Set if you want force replace your existing config files "
                   "docker-compose.yml, docker-compose-jenkins.yml, docker/my.conf, docker/docker_drupal/docker_drupal_overrides.py and docker/docker_drupal/docker_drupal_config_overrides.py."
                   "All your changes in listed files will be irrevocably lost. Other files in wrapper folder and 'docker' folder will stay unchanged.",)

parser.add_option("-e", "--drush-eval-run-code", dest="docker_drush_eval_run_code",
              help="Use with action 'drush'. "
                   "Set if you want run code in drush eval", metavar="DRUSH_EVAL_RUN_CODE")

parser.add_option("-y", action="store_true", dest="docker_yes_all",
              help="yes to all questions where 'confirm_action' is used in action steps",)

parser.set_defaults(docker_shell_run=False)
parser.set_defaults(docker_init_replace_conf=False)
parser.set_defaults(docker_yes_all=False)

group = OptionGroup(parser, "Available aliases", ", ".join('@%s' % alias for alias in available_aliases[:]))
parser.add_option_group(group)

(cmd_options, args) = parser.parse_args()

DOCKER_RUN_PATH = os.getcwd()

for idx, arg in enumerate(args):
    if arg.startswith('@'):
        try:
            DOCKER_RUN_PATH = aliases[arg.lstrip('@')]['path'].rstrip('/')
        except:
            pass
        del args[idx]
        del sys.argv[idx]

if cmd_options.docker_run_path is not None:
    DOCKER_RUN_PATH = cmd_options.docker_run_path.rstrip('/')

sys.path.append(os.path.join(DOCKER_RUN_PATH, 'docker', 'docker_drupal'))

try:
    from docker_drupal_overrides import *
except Exception as exception:
    if "No module named docker_drupal_overrides" in str(exception):
        pass
    else:
        print "Error during docker_drupal_overrides file import: ", exception
