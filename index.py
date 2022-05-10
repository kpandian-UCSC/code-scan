import requests

res = requests.get("https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml")
print(res.text)

# 


    # "https://raw.github.com/kpandian-ucsc/dummy-ci/main/cloud-formation.yaml"
    # Received
    # https://api.github.com/kpandian-UCSC/dummy-ci/blob/main/cloud-formation.yaml
    # Rename to use api.github url


    # "https://github.com/kpandian-UCSC/code-scan/blob/main/index.py"
print(lambda_handler({"body": {"repo": "https://github.com/kpandian-UCSC/code-scan/blob/0ea3e6d361f940e3496ad2803730511ce13e0b19/index.py"}, "requestContext": {"http": {"method": "PUT"}} }, None))
print(lambda_handler({"body": {"repo": "https://github.com/kpandian-UCSC/code-scan/blob/no-token/index.py"}, "requestContext": {"http": {"method": "PUT"}} }, None))
print(lambda_handler({"body": {"repo": "https://github.com/kpandian-UCSC/code-scan/blob/main/index.py"}, "requestContext": {"http": {"method": "PUT"}} }, None))
print(lambda_handler({"body": {"repo": "https://github.com/kpandian-UCSC/code-scan/blob/main/index.py"}, "requestContext": {"http": {"method": "GET"}} }, None))
print(lambda_handler({"body": {"repo": "https://github.com/kpandian-UCSC/CSE138_Assignment1/blob/main/index.js"}, "requestContext": {"http": {"method": "PUT"}} }, None))