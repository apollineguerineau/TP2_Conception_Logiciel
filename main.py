from ratio.ratio import *
from fuzzywuzzy import fuzz


levenshtein_ratio = ratio()
print(levenshtein_ratio)

print(fuzz.ratio("conception logicielle", "portabilité"))
