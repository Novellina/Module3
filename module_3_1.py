calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list):
    count_calls()
    string = string.upper()
    for i in list:
        if i.upper() == string:
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)