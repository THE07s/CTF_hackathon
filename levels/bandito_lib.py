# Library to group together common functions
import hashlib
from datetime import datetime


def get_password_hash() -> str:
    '''Return SHA256 string of current datetime YYYYMMDDHHMMSSmmm'''
    return hashlib.sha256(bytes(datetime.utcnow().strftime('%Y%m%d%H%M%s%f'), 'utf-8')).hexdigest()