
import numpy as np
import json
def load_tester(path):
    with open(path) as f:
        data = json.load(f)
    print(data)
    return np.asarray(data)

d = load_tester('/home/superadmin/Downloads/via_export_coco (3).json')

print(type(d))

np.save('mask.npy',d)