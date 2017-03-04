"""
Generates simulated emails. The emails are written into individual files in the
specified output directory.

Usage:
    email_gen.py [options]
    email_gen.py

Options:
    -h --help                    Show this screen.
    --max-count=COUNT            Number of simulated emails to generate
    -o DIR --output=DIR          Output directory for the simluated emails
"""

from docopt import docopt
from configparser import ConfigParser
# This is new in Python 3.3
from collections import ChainMap

from email_sim import *

import sys
import logging
import logging.config

def _main(argv=None):
    # read initial config file
#    logging.config.fileConfig('logging.conf')
    
    args = docopt(__doc__, argv=argv, help=True)
    
    # Make a dictionary of supplied option values
    # Take care to remove None values without removing False's or O's
    siphon_off = ['--help']
    opt_values = [ (k.replace('-',''),v) for k,v in args.items() if v is not None and k.startswith('--') and k not in siphon_off ]
    opt_values = dict(opt_values)

    cfg_file_name = 'email_gen.cfg'
    try:
        config = ConfigParser()
        # Definitely use with-blocks to limit resource acquisition.
        with open(cfg_file_name,'r') as cf:
            config.read_file(cf)
        cfg_values = dict(config['Default'])
    except Exception:
        logging.warn("Could not read configuration file", exc_info=True)
        # We will exit without the cfg.
        # IT IS BEST TO FAIL-FAST HERE. You don't want to think too much about
        # second-guessing the contents of a missing CFG without somehow involving
        # a human.
        #   You can always put in code to auto-generate a defaulted CFG TEMPLATE
        # to help the human.
        sys.exit()

    # Now we are happy from operational perspective: there are two ways to source
    # configuration settings: via command line options, and via a configuration file.
    # You'll find that having both is necessary when you have highly configurable
    # software.
    cfg = ChainMap(opt_values,cfg_values)
    
    sim = EmailSimulator(cfg)
    sim.generate()
    
    
if __name__ == '__main__':
    # Put the 'main' logic into its own function. This allows us to repeatedly call
    # the 'main' logic from a REPL terminal.
    
    _main()    
    
