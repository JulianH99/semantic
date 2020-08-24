from lexer import TOKENS
import re

dtypes = TOKENS['PARAM_DTYPE'].replace('(', '').replace(')', '').replace('+', '').split('|')

dtypes_re = {
    'int': re.compile('\d+'),
    'double': re.compile('\d+\.+\d+')
}


def check_data_type(dtype, val):
    if dtype in dtypes:
        if dtype == 'int':
            return dtypes_re['int'].match(val) is not None or val == 'null'
        if dtype == 'varchar':
            return val == 'null' or val == '\''
        if dtype == 'double':
            return dtypes_re['double'].match(val) is not None or val == 'null'
        if dtype == 'bit':
            return val in ['0', '1'] or val == 'null'

        if dtype == 'boolean':
            return val in ['true', 'false'] or val == 'null'

    else:
        return False
