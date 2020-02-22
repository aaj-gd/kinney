from config import config

# COMMON config
DEBUG = "True" == config["COMMON"]["DEBUG"]
SUCCESS = 100

#Constants 
SEPARATOR = "*"

# Error Constants
ERR_ENV_VAR_MISSING = 100  
ERR_ENV_VAR_MISSING_USERNAME = 101
ERR_ENV_VAR_MISSING_PASSWORD = 102
ERR_ENV_VAR_MISSING_SGID_OR_STATIONID = 103

ERR_CONNECTION=400

ERR_INVALID_VALUE = 300
ERR_INVALID_VALUE_CURTAIL_ABS_AMT = 301
ERR_INVALID_VALUE_CHARGE_POINT = 302
ERR_MISSING_AMOUNT = 303

