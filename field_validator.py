from pydantic import BaseModel, EmailStr, AnyUrl, Field , field_validator
from typing import List ,Dict , Optional , Annotated 


class Patient (BaseModel):


    name : str
    email: EmailStr
    age : int
    weight : float 
    married : bool 
    allergies : List[str]
    contact_details : dict [str,str]


    @field_validator('email')
    def email_validator(cls, value):
        valid_domains = ['herf.com', 'icic.com']
        # e.g. abc@domain.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')

        return value


    @field_validator('name')
    @classmethod
    def transformer_name(cls , value):
        return value.upper() 
    
    @field_validator('age')
    @classmethod
    def validator_age(cls , value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between o and 100')
       
        
        
  

    def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print(patient.email)
        print('inserted')
        
        patient_info = {
            'name': 'pragya',
            'email': 'icic@icic.com',
            'age': '23',
            'weight': 49,
            'married': True,
            'allergies': ['Dust', 'Pollen'],
            'contact_details': {'phone': '1234567'},
        }

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)
