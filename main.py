from Display_response import display_response
from get_user_input import get_user_guess
from random_response import get_random_response
from play_again import play_again

def magic_8_ball():

    print("🎱 Welcome to the Magic 8-Ball! 🎱")
    while True:
        question = get_user_guess()
        if question is None:
            break
        response = get_random_response()
        display_response(response)
        if not play_again():
            break

if __name__ == "__main__":

    magic_8_ball()