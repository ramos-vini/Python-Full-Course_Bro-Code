# def loud(text):
#     return text.upper()
#
#
# def quite(text):
#     return text.lower()
#
#
# def hello(function):
#     return print(function("Hello!"))
#
#
# hello(loud)
#
# hello(quite)

def scream(text):
    return f"{text.upper()}!!!"


def aggressive_hello(name):
    return f"HELLO, {scream(name)}"


print(aggressive_hello("user"))
