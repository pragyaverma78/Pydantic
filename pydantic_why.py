from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List ,Dict , Optional , Annotated 

class Patient (BaseModel):


    name: Annotated[str,Field(max_length=50 ,title='name of the patient',description='Give the name of the patient in less  than 50 chars', examples=['nikita', 'kalyani'])]
    email: EmailStr
    linkedin_url : AnyUrl 
    age : int = Field(get=0,lt=50)
    weight : Annotated [ float , Field (get=0, strict = True)]
    married : bool = False  
    allergies : Annotated [Optional[List[str]] , Field (default=None ,max_length=5)]
    contact_details : Dict[str,str]
    


def intsert_patient_data(patient:patient):


    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('intserted')
    
patient_info = {'name':'pragya' ,'email':'abcd@gmail.com', 'linkedin_url':'https://linkedin.com/in/1234', 'age':23 , 'weight':49,  'contact_details':{'phone':'1234567'}}

patient1 = Patient(**patient_info) 

intsert_patient_data(patient1)

