import sys
from src.logger import logging

def error_message_detail(error , error_detail:sys):

    _,_,exception_tb = error_detail.exc_info()
    file_name = exception_tb.tb_frame.f_code.co_filename
    error_message = "An error occured in the python script [{0}] in the line [{1}] \nError message : [{}]".format(
        file_name,exception_tb.tb_lineno, str(error)
    )

    return error_message


class CustumException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self) -> str:
        return self.error_message

    