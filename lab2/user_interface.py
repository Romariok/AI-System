class UserInterface:
    learn_user_roles_message_format = "I prefer roles:"
    learn_user_attributes_message_format = "I like attributes:"
    learn_user_types_message_format = "I prefer types:"

    def __init__(self, prolog_query):
        self.prolog_query = prolog_query

    def validate_user_message(self, message: str, message_start_format):
        return len(message) > 0 and message.lower().startswith(message_start_format.lower())

    def check_user_choice(self, chosen_items, available_items):
        checked_items = []
        for chosen_item in chosen_items:
            if chosen_item not in available_items:
                print(f"Warning: '{chosen_item}' is unknown.")
            else:
                checked_items.append(chosen_item)
        return checked_items

    def read_user_message(self, message_start_format):
        while True:
            message = input("> ").strip().replace("  ", " ").lower()
            if message == "exit":
                exit(1)
            if self.validate_user_message(message, message_start_format):
                return message
            print("Invalid input. Please try again.")

    def learn_user_preferences(self, message_format, get_available_items, item_type):
        print(f"Enter hero {item_type}s you prefer. List of available {item_type}s:\n")
        available_items = get_available_items()
        for available_item in available_items:
            print(f"- {available_item}")
        print(f"\nEnter a message of format: \"{message_format} <your {item_type}s>\"")
        print(f"Example: {message_format} {', '.join(available_items[:2])}\n")
        
        while True:
            message = self.read_user_message(message_format)
            user_choices = message[len(message_format):].strip().replace(" ", "").split(",")
            user_choices = self.check_user_choice(user_choices, available_items)
            if len(user_choices) != 0:
                return user_choices
            print(f"Not enough hero {item_type}s selected. Please try again.")

    def learn_user_roles(self):
        return self.learn_user_preferences(
            self.learn_user_roles_message_format,
            self.prolog_query.get_available_roles,
            "role"
        )

    def learn_user_attributes(self):
        return self.learn_user_preferences(
            self.learn_user_attributes_message_format,
            self.prolog_query.get_available_attributes,
            "attribute"
        )

    def learn_user_types(self):
        return self.learn_user_preferences(
            self.learn_user_types_message_format,
            self.prolog_query.get_available_types,
            "type"
        )