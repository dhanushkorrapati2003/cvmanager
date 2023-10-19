from django.core.exceptions import ValidationError

#1MB in bytes
mega_byte = 1048576

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 5 * mega_byte:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value
