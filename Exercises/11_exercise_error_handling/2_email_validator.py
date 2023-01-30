class NameTooShortError(Exception):
    """"Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


email_input = input()
while email_input != "End":
    name = email_input.split("@")[0]
    domain = email_input.split(".")[-1]
    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email_input:
        raise MustContainAtSymbolError("Email must contain @")
    if domain not in ["bg", "org", "com", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email_input = input()