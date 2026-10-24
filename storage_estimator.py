print("Storage Estimator")
print("------------------")

size_mb = float(input("Enter file size in MB: "))
size_gb = size_mb / 1024

print("File size in MB:", size_mb)
print("File size in GB:", round(size_gb, 2))
print("Storage conversion completed.")
