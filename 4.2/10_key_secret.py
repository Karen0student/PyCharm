def secret_replace(text, **kwargs):
    replaced_text = text

    for old_substring, replacement_values in kwargs.items():
        if isinstance(replacement_values, tuple):
            current_value = replaced_text
            count_kwarg_key_in_text = text.count(replacement_values)
            while True:


            for new_value in replacement_values:
                current_value = current_value.replace(old_substring, str(new_value), 1)
                if new_value == replacement_values[-1]:
                    new_value = replacement_values[0]
            replaced_text = current_value
        else:
            replaced_text = replaced_text.replace(old_substring, str(replacement_values), 1)

    return replaced_text

# Example usage
result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)
# result = 'Hehiy123, wzrhid!'
