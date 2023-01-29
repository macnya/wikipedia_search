import wikipedia

# Fetch a random article from Wikipedia
article = wikipedia.random(pages=1)

# Ask the user if they want to read the article
answer = input("Would you like to read the article '" + article + "'? (Y/N)")

if answer == 'Y':
    # Print the article
    print(wikipedia.page(article).content)

elif answer == 'N':
    # Fetch a different article
    article = wikipedia.random(pages=1)
    # Ask the user if they want to read the new article
    answer = input("Would you like to read the article '" + article + "'? (Y/N)")
    if answer == 'Y':
        # Print the article
        print(wikipedia.page(article).content)
    else:
        # Exit program
        print("Goodbye.")
        exit()
