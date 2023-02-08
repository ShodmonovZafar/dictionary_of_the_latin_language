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

def eratosfen_elagi(n: int) -> list[int]:
    """1 dan n gacha mavjud tub sonlarni topish algoritmi."""
    kv_il = math.sqrt(n)
    nums = list(range(2, n + 1))
    i = 0
    j = i + 1
    while nums[i] <= kv_il:
        if nums[j] == nums[-1]:
            if nums[j] % nums[i] == 0:
                del nums[j]
            i += 1
            j = i + 1
            continue
        if nums[j] % nums[i] == 0:
            del nums[j]
        else:
            j += 1
    return nums

#print(eratosfen_elagi(100000))
