from string import ascii_letters, digits


class User:
    """Represents a user of service"""
    _local_symbols = ascii_letters + digits + "!#$%&'*+-/=?^_`{|}~."
    _domain_symbols = ascii_letters + digits + '-'

    def __init__(self, email: str, passw: str, username: str):
        self.passw = passw
        self.username = username
        if User.validate(email):
            self.email = email
        else:
            raise ValueError("Email string must be a correct email address")

    @classmethod
    def validate(cls, mail: str) -> bool:
        """Checks email name for compliance with the RFC 5321.
        Quoted 'local-part' and [ip.addr] domain are not supported"""
        if mail.count('@') != 1:
            return False
        local_part, domain = mail.split('@')
        local_dots_check = local_part[0] != '.' and local_part[-1] != '.' and '..' not in local_part
        local_symbols_check = all([c in cls._local_symbols for c in local_part])
        local_len_check = len(local_part) <= 64
        total_local_check = local_dots_check and local_symbols_check and local_len_check
        domain_len_check = len(domain) <= 255 and len(domain.split('.')[-1]) >= 2
        domain_dots_check = '.' in domain and domain[0] != '.' and domain[-1] != '.' and '..' not in domain
        subcheckers = []
        for subdom in domain.split('.'):
            symbols_check = all([c in cls._domain_symbols for c in subdom])
            len_check = len(subdom) <= 63
            hyphen_check = subdom[0] != '-' and subdom[-1] != '-'
            digits_check = not all([c in digits for c in subdom])
            subcheckers.append((symbols_check and len_check and hyphen_check and digits_check))
        subdoms_check = all(subcheckers)
        total_domain_check = domain_len_check and domain_dots_check and subdoms_check
        return total_domain_check and total_local_check
