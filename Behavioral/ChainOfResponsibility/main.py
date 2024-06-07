from abc import ABC, abstractmethod


class IChecker(ABC):
    @abstractmethod
    def set_next_checker(self, checker: 'IChecker') -> "IChecker":
        pass

    @abstractmethod
    def check(self, password: str) -> str:
        pass


class Checker(IChecker):
    def __init__(self):
        self.next_checker = None

    def set_next_checker(self, checker: 'IChecker') -> IChecker:
        self.next_checker = checker
        return checker

    def check(self, password: str) -> str:
        if self.next_checker is not None:
            return self.next_checker.check(password)
        return "valid"


class CheckIsVoid(Checker):
    def check(self, password: str) -> str:
        if password == "":
            return "Password is void."
        else:
            return super().check(password)


class CheckIsAlpha(Checker):
    def check(self, password: str) -> str:
        is_alpha = False
        for char in password:
            if char.isalpha():
                is_alpha = True
                break
        if is_alpha:
            return super().check(password)
        else:
            return "Password has`t alpha"


class NumericChecker(Checker):
    def check(self, password: str) -> str:
        is_number = False
        for char in password:
            if char.isnumeric():
                is_number = True
                break
        if is_number:
            return super().check(password)
        else:
            return "Password has`t number"


def check_password(checker: IChecker, password: str):
    result = checker.check(password)
    if result == "valid":
        print("Password is valid")
    else:
        print(result)


void_checker = CheckIsVoid()
alpha_checker = CheckIsAlpha()
number_checker = NumericChecker()

void_checker.set_next_checker(alpha_checker).set_next_checker(number_checker)

check_password(void_checker, "Qw")
check_password(void_checker, "")
check_password(void_checker, "11")

check_password(void_checker, "Qw11")
