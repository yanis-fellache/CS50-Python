filename = input("Name of file: ")

filename = filename.lower().strip()

if ".jpg" in filename:
    print("image/jpeg")
elif ".jpeg" in filename:
    print("image/jpeg")
elif ".gif" in filename:
    print("image/gif")
elif ".png" in filename:
    print("image/png")
elif ".pdf" in filename:
    print("application/pdf")
elif ".txt" in filename:
    print("text/plain")
elif ".zip" in filename:
    print("application/zip")
else:
    print("application/octet-stream")
