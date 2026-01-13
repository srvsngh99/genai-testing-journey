class PromptTemplate:
    def __init__(self, template: str):
        self.template = template    
    
    def fill(self, **kwargs):
        return self.template.format(**kwargs)   

    