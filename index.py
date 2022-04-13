import requests

res = requests.get("https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml")
print(res.text)

# 


    # "https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml"
    # Received
    # https://api.github.com/kpandian-UCSC/dummy-ci/blob/main/cloud-formation.yaml
    # Rename to use api.github url


    # "https://github.com/kpandian-UCSC/code-scan/blob/main/index.py"