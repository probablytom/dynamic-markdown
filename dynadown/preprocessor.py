'''
    A preprocessor to evaluate code embedded in Markdown documents.
    The evaluation is done by interpreter plugins. The preprocessor will:
        1. Collect all plugin modules it knows about
        2. Register the plugin modules with an evaluator class
        3. Peruse a Markdown document and evalute blocks that it finds.
'''

import os.path as op

def collect_plugins():
    dynadown_path = op.dirname(op.realpath(__file__))
    plugin_directory = dynadown_path + '/plugins/'
    
