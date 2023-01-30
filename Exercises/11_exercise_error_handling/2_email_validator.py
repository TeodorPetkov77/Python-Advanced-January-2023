import re

class NameTooShortError(Exception):
    """"Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


email_pattern = re.compile(r"(?P<name>\w+)@\w+.(?P<domain>\w+)")

email_input = input()
while email_input != "End":
    if re.match(email_pattern, email_input):
        name = re.match(email_pattern, email_input).group("name")
        domain = re.match(email_pattern, email_input).group("domain")
        if len(name) < 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if domain not in ["bg", "org", "com", "net"]:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if "@" not in email_input:
        raise MustContainAtSymbolError("Email must contain @")
    print("Email is valid")
    email_input = input()