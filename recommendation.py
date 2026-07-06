movies = {
    "Action": ["Avengers", "John Wick", "Batman"],
    "Comedy": ["3 Idiots", "Hera Pheri", "Golmaal"],
    "Horror": ["The Conjuring", "Annabelle", "IT"],
    "Romance": ["Titanic", "The Notebook", "DDLJ"],
    "Sci-Fi": ["Interstellar", "Inception", "Avatar"]
}

print("===== Movie Recommendation System =====")
print("Available Categories:")
for category in movies:
    print("-", category)

choice = input("\nEnter your favorite category: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("•", movie)
else:
    print("\nSorry! Category not found.")