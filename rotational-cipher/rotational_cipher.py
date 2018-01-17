from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    lower_rotate = "".maketrans({k: chr((ord(k) + key)) if (ord(k) + key) <=122 else chr((ord(k)+key -26)) for k in ascii_lowercase})
    upper_rotate = "".maketrans({k: chr((ord(k) + key)) if (ord(k) + key) <=90 else chr((ord(k)+key -26)) for k in ascii_uppercase})
    text = text.translate(lower_rotate).translate(upper_rotate)
    return text
