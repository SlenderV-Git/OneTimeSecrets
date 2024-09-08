from beanie import Document


class SecretDocument(Document):
    secret_key : str
    secret_value : str
    
class ProtectedSecretDocument(Document):
    secret_key : str
    secret_value : str
    password : str