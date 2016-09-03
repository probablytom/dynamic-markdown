'''
    A preprocessor to evaluate code embedded in Markdown documents.
    The evaluation is done by interpreter plugins. The preprocessor will:
        1. Collect all plugin modules it knows about
        2. Register the plugin modules with an evaluator class
        3. Peruse a Markdown document and evalute blocks that it finds.
'''

import os.path as op
import os
from dynadown import evaluator
import CommonMark as cm

def collect_plugins():
    dynadown_path = op.dirname(op.realpath(__file__))
    plugin_directory = dynadown_path + '/plugins/'
    for path, _, files in os.walk(plugin_directory):  # Recursive walk
        for currfile in files:
            if currfile[-3:] == '.py':  # If the file ext is .py
                exec(open(path + '/' + currfile, 'r').read())  # Execute the plugin code

    
def translate(markdown_filepath):
    markdown_file = open(markdown_filepath, 'r')
    output = ''
    block_type = ''
    block_content = ''
    in_block = False  # We're not currently in a block of code
    for line in markdown_file.read().split('\n'):
        if line[:3] == "```" and not in_block:  # Three backticks starts block
            in_block = True  # We found something to evaluate!
            block_type = line[3:]
            block_content = ''
            # TODO: Finish this
        elif line[:3] == "```" and in_block:
            in_block = False
            output += evaluator.evaluate(block_type, block_content) + '\n'
        elif in_block:
            block_content += '\n' + line
        else:
            output += line + '\n'

    # TODO: Now, translate the markdown in `output`!
    print(cm.commonmark(output))
