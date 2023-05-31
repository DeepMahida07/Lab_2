"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'name': 'Deep Mahida',

        # TODO: Put student ID into data structure
        'ID': '10291395',

        # TODO: Put list of 3 pizza toppings into data structure
        'topping': [
             'PEPPERONI',
             'MOZZARELLA',
             'MUSHROOM',
        ],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'avenger endgame',
                'genre': 'sci-fi'
            },
            # TODO: Add one more movie
            {
                'title': 'the fast and furious:tokyo drift',
                'genre': 'action'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['BACON', 'PINEAPPLE'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'game of thrones', 'drama')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3 
    # Print sentence containing name
    first_name = my_info['name'].split()[0]
    print(f"My name is {my_info['name']}, but you can call me Sir {first_name}.")

    # Print sentence containing student ID
    print(f"My student ID is {my_info['ID']}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    #Print header "My favourite pizza toppings are:"
    print(f"\nMy favourite pizza toppings are: ")

    # Print bullet list of favourite pizza toppings
    for topping_name in my_info['topping']:
        print(f'- {topping_name}')

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['topping'].extend(toppings)

    # Convert all pizza toppings to lowercase
    for i, topping_name in enumerate(my_info['topping']):
        my_info['topping'][i] = topping_name.lower()

    # Sort toppings list alphabetically
    my_info['topping'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie = {
            'title': 'game of thrones',
            'genre': 'drama'
    }
    my_info['movies'].append(new_movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    #print(f"I like to watch {my_info['']}")
    genre_names = [movies['genre'] for movies in my_info['movies']]
    names= (', '.join(genre_names))
    print(f"\nI like to watch {names} movies.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    movie_names = [movies['title'] for movies in movie_list]
    title_names= (', '.join(movie_names)).title()
    print(f"\nSome of my favourite movies are {title_names}!")

if __name__ == '__main__':
    main()