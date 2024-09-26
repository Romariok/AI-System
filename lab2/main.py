from prolog_query import PrologQuery
from user_interface import UserInterface

def main():
    base_path = 'lab2/base.pl'
    prolog_query = PrologQuery(base_path)
    hero_selector = UserInterface(prolog_query)

    print("""
    Welcome to the Dota 2 Hero program!
    You will be asked a few questions to find matching heroes.
    """)

    user_roles = hero_selector.learn_user_roles()
    user_attributes = hero_selector.learn_user_attributes()
    user_types = hero_selector.learn_user_types()

    matching_heroes = prolog_query.look_for_matching_heroes(user_attributes, user_types, user_roles)
    matching_heroes = list(set(matching_heroes))

    if len(matching_heroes) == 0:
        print("Sorry, but there are no matching heroes for your preferences.")
    else:
        print("Here are the heroes that match your preferences:")
        for hero in matching_heroes:
            print(f"- {hero}")

if __name__ == "__main__":
    main()