# imports

# Slide Parameters
class slide_params:
    def __init__(self, debug=False):
        self.debug = debug
        return

class slide:
    # Present a PsychoPy Slide with Common Features
    def __init__(self, params):
        if params.debug == True:
            print("Slide")
        return