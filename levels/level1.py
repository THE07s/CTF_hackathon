# Script to create bandito1 user and level environment
import os
import hashlib
from datetime import datetime

# Generate SHA256 hash from todays date YYYYMMDD
user_pass = hashlib.sha256(bytes(datetime.now().strftime('%Y%m%d%H%M'), 'utf-8')).hexdigest()

#os.system("useradd -p" +  + )
