import psutil

print(f"{psutil.disk_usage("C:").free / (1024**3):.3f}")