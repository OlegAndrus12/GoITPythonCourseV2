from abc import ABC, abstractmethod, ABCMeta


# Developer(ABC) and Developer(metaclass=ABCMeta) is the same
class Developer(ABC):
    @abstractmethod
    def code(self):
        raise NotImplementedError
    
    def debug(self):
        raise NotImplementedError

    def review_prs(self):
        raise NotImplementedError

class HTMLDeveloper(Developer):
    pass


class PythonDeveloper(Developer):
    def code(self):
        print("\n Python \n print('Hello world!')")

class ScalaDeveloper(Developer):
    def code(self):
        code = """
            object Hello {
                def main(args: Array[String]) = {
                    println("Hello, world")
                }
            }
        """
        print(" \n Scala \n" + code)


python = PythonDeveloper()
python.code()

scala = ScalaDeveloper()
scala.code()


html = HTMLDeveloper()
html.code()