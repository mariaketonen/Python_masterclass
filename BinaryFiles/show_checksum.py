import hashlib

published_hash = '08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44'

filename = 'colorama-0.4.6.tar.gz'

with open(filename, 'rb') as downloaded_file:
    contents = downloaded_file.read()

file_hash = hashlib.sha256(contents).hexdigest()
print(file_hash)

if file_hash != published_hash:
    print(f'The file {filename} has been modified')
else:
    print(f'file {filename} hash is correct')