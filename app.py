def compare_flask_django(project_size):

    flask = {
        "pros": [
            "Easy to learn",
            "Lightweight",
            "Good for small projects"
        ],
        "cons": [
            "Less built-in features",
            "Not suitable for very large apps"
        ]
    }

    django = {
        "pros": [
            "High security",
            "Many built-in features",
            "Good for large projects"
        ],
        "cons": [
            "Harder to learn",
            "Heavy for small projects"
        ]
    }

    print("FLASK")
    for p in flask["pros"]:
        print("✅", p)
    for c in flask["cons"]:
        print("❌", c)

    print("\nDJANGO")
    for p in django["pros"]:
        print("✅", p)
    for c in django["cons"]:
        print("❌", c)

    print("\nTRADE-OFF")
    if project_size == "small":
        print("Choose Flask for simplicity and speed.")
    else:
        print("Choose Django for security and scalability.")


compare_flask_django("small")
