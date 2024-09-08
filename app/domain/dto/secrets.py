from pydantic import BaseModel

class Secret(BaseModel):
    secret_key : str
    secret_value : str
    
class ProtectedSecret(BaseModel):
    secret_key : str
    secret_value : str
    password : str