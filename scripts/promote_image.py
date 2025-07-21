# scripts/promote_image.py
import yaml

with open("manifests/dev/deployment.yaml") as f:
    dev = yaml.safe_load(f)

dev_image = dev['spec']['template']['spec']['containers'][0]['image']

with open("manifests/prod/deployment.yaml") as f:
    prod = yaml.safe_load(f)

prod['spec']['template']['spec']['containers'][0]['image'] = dev_image

with open("manifests/prod/deployment.yaml", "w") as f:
    yaml.dump(prod, f)

print(f"Updated prod image to: {dev_image}")
