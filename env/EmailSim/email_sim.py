from contact_sim import *
from email_export import *
from jinja2 import Template

class EmailSimulator:
    def __init__(self, cfg):
        self._cfg = cfg
        
        self._company_sim = CompanySimulator()
        self._contact_sim = ContactSimulator()
        self._exporter = EmailExporter(cfg)
        self._email_bodies = RandomizedData('data/email_body.csv')

    def generate(self):
        
        if self._cfg:
            max_count = self._cfg.get('maxcount',0)
        else:
            max_count = 10

        employees = 0
        company = None
        
        for i in range(int(max_count)):
            if employees <= 0:
                company,t = self._company_sim.random_company()
                employees = (int)( random.gammavariate(alpha=7.5, beta=1.0) )

                signature_format = Template(t['signature_format'])
                email_format = Template(t['email_format'])
                phone_format = Template(t['phone_format'])
                address_format = Template(t['street_address_format'])
            employees = employees - 1
                
            contact = self._contact_sim.random_contact()
            contact.update(company)
            
            street_address = address_format.render( **contact )
            fax = phone_format.render( tel_subscriber_number = contact.get('tel_fax_subscriber_number'), **contact )
            main = phone_format.render( tel_subscriber_number = contact.get('tel_main_subscriber_number'), **contact )
            direct = phone_format.render( tel_subscriber_number = contact.get('tel_direct_subscriber_number'), **contact )
            contact['street_address'] = street_address
            contact['fax'] = fax
            contact['main_phone'] = main
            contact['direct_phone'] = direct
            
            contact['business_email'] = email_format.render(**contact)
            contact['signature'] = signature_format.render(**contact)

            y = self._email_bodies.random()
            t = Template(y['Email Body'])
            
            email_body = t.render(**contact)
            
            self._exporter.export(email_body,contact)

