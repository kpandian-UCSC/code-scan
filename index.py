import requests

res = requests.get("https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml")
print(res.text)

# dapi1a2b3c45d67890e1f234567a8bc9012d
# dapi1a2b3c45d67890e1f234567a8bc9012d
token = 'dapi1a2b3c45d67890e1f234567a8bc911dd'


    # "https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml"
    # Received
    # https://api.github.com/kpandian-UCSC/dummy-ci/blob/main/cloud-formation.yaml
    # Rename to use api.github url


    # "https://github.com/kpandian-UCSC/code-scan/blob/main/index.py"