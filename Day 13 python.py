# data
data = [
    {'name': 'John',
     'surname': 'Smith',
     'follower_count': 100,
     'description': 'Python developer',
     'country': 'USA'
     },
    {'name': 'Jane',
     'surname': 'Doe',
     'follower_count': 200,
     'description': 'Java developer',
     'country': 'Canada'
     },
    {'name': 'Bob',
     'surname': 'Johnson',
     'follower_count': 300,
     'description': 'C# developer',
     'country': 'UK'
     },
    {'name': 'Alice',
     'surname': 'White',
     'follower_count': 400,
     'description': 'PHP developer',
     'country': 'France'
     },
    {'name': 'David',
     'surname': 'Brown',
     'follower_count': 500,
     'description': 'C++ developer',
     'country': 'Germany'
     },
    {'name': 'Emily',
     'surname': 'Green',
     'follower_count': 600,
     'description': 'Ruby developer',
     'country': 'Italy'
     },
    {'name': 'Frank',
     'surname': 'Purple',
     'follower_count': 700,
     'description': 'Scala developer',
     'country': 'Spain'
     },
    {'name': 'Gary',
     'surname': 'Yellow',
     'follower_count': 800,
     'description': 'Javascript developer',
     'country': 'Austria'
     },

    {'name': 'Harry',
     'surname': 'Pink',
     'follower_count': 900,
     'description': 'C# developer',
     'country': 'India'
     },
    {'name': 'Isabella',
     'surname': 'Orange',
     'follower_count': 1000,
     'description': 'Java developer',
     'country': 'Germany'
     },

    {'name': 'Jacob',
     'surname': 'Black',
     'follower_count': 1100,
     'description': 'Python developer',
     'country': 'USA'
     },

    {'name': 'Karen',
     'surname': 'White',
     'follower_count': 1200,
     'description': 'Java developer',
     'country': 'Canada'
     },

    {'name': 'Lisa',
     'surname': 'Pink',
     'follower_count': 1300,
     'description': 'C# developer',
     'country': 'UK'
     },

    {'name': 'Mia',
     'surname': 'Orange',
     'follower_count': 1400,
     'description': 'PHP developer',
     'country': 'France'
     },

    {'name': 'Nancy',
     'surname': 'Green',
     'follower_count': 1500,
     'description': 'C++ developer',
     'country': 'Germany'
     }

]

# create higher or lower game with previous dataset
import random
# import clear in order to clear page when answer is found
import time


def get_random_person(data):
    """
    Returns a randomly selected person from the data.
    """
    person = random.choice(data)
    return person

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
    score = 0
    game_should_continue = True
    person_a = get_random_person(data)
    person_b = get_random_person(data)
    while game_should_continue:
        person_a=person_b
        person_b  = get_random_person(data)
        while person_a == person_b:
            person_b = get_random_person(data)


        if person_a == person_b:
            person_b = get_random_person(data)

        print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}")
        print(f"Compare B: {person_b['name']}, {person_b['description']}, from {person_b['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = person_a['follower_count']
        b_follower_count = person_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
game()
