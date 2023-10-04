import os
import json


d = {
    k: v for k, v in os.environ.items()
    if k.islower()
}

print(
    json.dumps(
        d, 
        indent = 2
    )
)



