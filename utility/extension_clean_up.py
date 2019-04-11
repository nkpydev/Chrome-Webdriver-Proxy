import os
from utility.config import BASE_DIR

class cleanup:
    
    def extensionCleanup(self,extension_name):
        target_file = os.path.join(BASE_DIR,extension_name)
        os.remove(target_file)