from abc import ABC, abstractclassmethod

class Command(ABC):

    @abstractclassmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):

    def __init__(self) -> None:
        super().__init__()

    
    def execute(self) -> None:
        print("Simple Command Execute")

class Receiver:
    def do_sth(self):
        print("Receiver Do sth")

class ComplexCommand(Command):

    def __init__(self, receiver: Receiver) -> None:
        super().__init__()

        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.do_sth()




class Invoker:

    _on_start = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def do_task(self) -> None:
        if(self._on_start):
            self._on_start.execute()

if __name__ == "__main__":
    
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand())
    invoker.do_task()

    receiver = Receiver()
    invoker.set_on_start(ComplexCommand(receiver))
    invoker.do_task()

    