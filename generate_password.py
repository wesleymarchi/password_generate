import random
import string


def generate_password(length):
    """
    Generate a random passwords

    :return: dataframe
    """

    min_length = length
    max_length = length
    length = random.randint(min_length, max_length)

    str_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    generated_string = ''.join(random.choice(str_characters) for _ in range(length))
    # generated_string = ''.join(random.choices(str_characters, k=length))

    return generated_string
