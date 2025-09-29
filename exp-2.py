import os

def copy_file(src, dst):
    # Open source file (read-only)
    src_fd = os.open(src, os.O_RDONLY)
    
    # Open/Create destination file (write-only, create if not exists, truncate if exists)
    dst_fd = os.open(dst, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

    while True:
        # Read 1024 bytes at a time
        data = os.read(src_fd, 1024)
        if not data:
            break
        os.write(dst_fd, data)  # Write to destination file

    # Close both files
    os.close(src_fd)
    os.close(dst_fd)
    print(f"Copied content from {src} to {dst}")

# Example usage
copy_file("C:/Users/Hp/OneDrive/Desktop/source.txt",
          "C:/Users/Hp/OneDrive/Desktop/destination.txt")
