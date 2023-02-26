import json
import lugat

path1 = "json_files/json_file1.json"
with open(path1, "w") as f:
    json.dump(lugat.data1, f, indent=4, sort_keys=True)
