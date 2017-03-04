import random
import os.path

from sim_util import RandomizedData, csv_to_dict_list

class CompanySimulator:
    def __init__(self):
        self._postal_codes = RandomizedData(os.path.join('data','postal_code_us.csv'))
        
        x = csv_to_dict_list(os.path.join('data','tel_area_code_us.csv'))
        self._tel_area_code = dict( [ ( x0['State'], x0['Area Codes'].split(';') ) for x0 in x ] )

        self._company_names = RandomizedData(os.path.join('data','company_name.csv'))
        self._street_names = RandomizedData(os.path.join('data','street_name.csv'))
        self._street_types = RandomizedData(os.path.join('data','street_type.csv'))
        self._directionals = RandomizedData(os.path.join('data','directional.csv'))
        
        self._address_formats = RandomizedData(os.path.join('data','address_format.csv'))
        self._email_formats = RandomizedData(os.path.join('data','email_format.csv'))
        self._signature_formats = RandomizedData(os.path.join('data','signature_format.csv'))
        self._phone_formats = RandomizedData(os.path.join('data','phone_format.csv'))
        

    def random_company(self):
        t = {}
        t['email_format'] = self._email_formats.random()['Email Format']
        t['signature_format'] = self._signature_formats.random()['Signature Format']
        t['phone_format'] = self._phone_formats.random()['Phone Format']

        y = self._address_formats.random()
        t['street_address_format'] = y['Address Format']
        uses_directional = False
        if y['Directional']:
            uses_directional = True
        
        d = {}
        y = self._company_names.random()
        d['company_name'] = y['Company Name']
        d['domain_name'] = y['Domain']

        y = self._postal_codes.random()
        d['postal_code'] = y['Postal Code']
        d['city'] = y['City']
        d['state_abbrev'] = y['State Abbrev']
        d['state'] = y['State']

        tacl = self._tel_area_code[ d['state']]
        d['tel_area_code'] = tacl[0]
        d['tel_exchange_code'] = int(random.uniform(0.100,0.999) * 1000.0)
        
        d['tel_fax_subscriber_number'] = '9999'
        d['tel_main_subscriber_number'] = '0000'

        d['street_number'] =  int(random.uniform(0.100,0.999) * 1000.0)
        d['street_name'] =  self._street_names.random()['Street Name']
        d['street_type'] =  self._street_types.random()['Street Type']
        if uses_directional:
            d['directional'] = self._directionals.random()['Directional']
        return d,t

class ContactSimulator:
    def __init__(self):
        self._first_names_male = RandomizedData(os.path.join('data','first_name_male.csv'))
        self._first_names_female = RandomizedData(os.path.join('data','first_name_female.csv'))
        
        self._last_names = RandomizedData(os.path.join('data','last_name.csv'))
        self._job_titles = RandomizedData(os.path.join('data','job_title.csv'))
        
    def random_contact(self):
        d = {}
        x = random.random()*2.00
        if x <= 1.0:
            d['first_name'] = self._first_names_male.random(x)['First Name']
        else:
            x = x - 1.0
            d['first_name'] = self._first_names_female.random(x)['First Name']

        d['last_name'] = self._last_names.random()['Last Name']
        d['job_title'] = self._job_titles.random()['Job Title']

        return d

