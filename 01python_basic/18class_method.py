class Methods:
    value = 100
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def static_m():
        print("static_method")
    
    @classmethod
    def class_m(cls):
        print(cls.value)

    def instance_m(self):
        print(self.name)
    
Methods.static_m()
Methods.class_m()

obj = Methods("Lee")
obj.instance_m()
obj.class_m()
obj.static_m()