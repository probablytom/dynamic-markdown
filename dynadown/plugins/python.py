from dynadown import register_plugin

class PythonPlugin:
    def __init__(self):
        pass
    def evaluate(self, block):
        return str(eval(block))

register_plugin('python', PythonPlugin)
