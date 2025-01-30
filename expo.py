class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False ,
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend
        
    def __repr__ (self):
        return '{},{},{}'.format (self.designation, self.frontend, self.backend)

        
    def verifier (self):
        if(self.frontend == True and self.backend == True):
            return 'FullStack'
        elif(self.frontend == True or self.backend == True):
            if(self.frontend == True):
                return 'Frontend {}'.format (self.designation)
            else:
                return 'Backend {}'.format (self.designation)
        else:
            return 'Not a Developer'
      

if __name__ == '__main__':
    firstEmployee = Employee()
    print(firstEmployee.verifier())
