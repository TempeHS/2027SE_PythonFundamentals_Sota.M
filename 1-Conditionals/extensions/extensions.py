files = input("Enter file: ")

if ".gif" in files:
    print("image/gif")
elif ".jpg" in files:
    print("image/jpg")
elif ".jpeg" in files:
    print("image/jpeg")
elif ".png" in files:
    print("image/png")
elif ".pdf" in files:
    print("application/pdf")
elif ".txt" in files:
    print("text/txt")
elif ".zip" in files:
    print("archive/zip")
