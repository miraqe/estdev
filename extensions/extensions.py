def get_media_type(file_name):
    """Given a file name, returns the corresponding media type based on the file's extension."""
    extensions = {'.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.pdf': 'application/pdf', '.txt': 'text/plain', '.zip': 'application/zip'}
    file_extension = '.' + file_name.split('.')[-1].lower()  # Get the file extension (if any), convert to lowercase, and add a period
    if file_extension in extensions:
        return extensions[file_extension]
    else:
        return 'application/octet-stream'

# Prompt the user for a file name and print the corresponding media type
file_name = input('Enter a file name: ')
media_type = get_media_type(file_name)
print(f'The media type for {file_name} is {media_type}.')
