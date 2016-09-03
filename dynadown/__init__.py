'''
    Initialises the Dynadown module
'''

class Evaluator:
    def __init__(self):
        self.plugins = {}
    def add_plugin(self, block_id, evaluator_class):
        self.plugins[block_id] = evaluator_class()
    def evaluate(self, block_id, block):
        if block_id in self.plugins.keys():
            return self.plugins[block_id].evaluate(block)
        else:
            return None

evaluator = Evaluator()

def register_plugin(block_id, plugin):
    evaluator.add_plugin(block_id, plugin)

from .preprocessor import collect_plugins
