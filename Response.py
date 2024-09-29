from random import choice , randint

def get_response(useer_input: str) -> str:
    lowered:str = useer_input.lower()

    if lowered == '':
        print("Well you are afully slient")
    elif "hello" in lowered:
        return 'Hello there !'
    elif 'how are you' in lowered:
        return 'Good Thanx'
    elif 'bye' in lowered:
        return 'see you'
