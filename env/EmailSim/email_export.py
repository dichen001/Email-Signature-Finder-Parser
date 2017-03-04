import os.path
import datetime

class EmailExporter:
    def __init__(self,cfg):
        if not cfg:
            return
        self._out_dir = cfg['output']
    
    def export(self,email_body,contact):
        fn = contact['first_name'].strip().lower()
        ln = contact['last_name'].strip().lower()
        d = datetime.datetime.now().strftime('%Y%m%d_%I%M%S')
        
        p = '%s_%s_%s.txt'%(fn,ln,d)
        if self._out_dir:
            p = os.path.join(self._out_dir, p)

        with open(p,'w') as f:
            f.write(email_body)

        return