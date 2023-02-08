import math

def lotinchadan_ozbekchaga(lotincha: str, lugat: dict):
    for key in lugat.keys():
        if key[0] == lotincha:
            return lugat[key]
    return 0

def ozbekchadan_lotinchaga(ozbekcha: str, lugat: dict):
    for key in lugat:
        if ozbekcha == lugat[key]:
            return key
    return 0

