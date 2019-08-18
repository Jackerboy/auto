import json

from  werkzeug.exceptions import HTTPException

class JsonHTTPException(HTTPException):
    def get_description(self,environ=None):

        return self.description

    def get_body(self,environ=None):

        return json.dumps(
            {"code":self.code,"name":self.name,"msg":self.get_description(environ)}
        )

    def get_headers(self,environ=None):

        return[("Content-Type","application/json")]



class JsonValidateError(JsonHTTPException):
    """验证不通过"""
    code = 400


class JsonDatabaseError(JsonHTTPException):
    """验证不通过"""
    code = 500