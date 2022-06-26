import sys

names = ["Matheus", "Gabriel", "Thiago", "Marco", "Henry", "Guillermo", "Joao"]

if "Guillermo" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
