import os
from fuzzywuzzy import fuzz

from dotenv import load_dotenv

load_dotenv()

def ratio():
    mot1=(
        os.environ["MOT_UN"]
        if "MOT_UN" in os.environ
        else "conception_logicielle"
    )
    mot2=(
        os.environ["MOT_DEUX"]
        if "MOT_DEUX" in os.environ
        else "configuration"
    )
    return fuzz.ratio(mot1, mot2)