def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_word = "true"
    love_word = "love"
    true_score = 0
    love_score = 0
    for letter1 in true_word:
        for letter2 in name1:
            if letter1 == letter2:
                true_score += 1
        for letter2 in name2:
            if letter1 == letter2:
                true_score += 1
    for letter1 in love_word:
        for letter2 in name1:
            if letter1 ==  letter2:
                love_score += 1
        for letter2  in name2:
            if letter1 == letter2:
                love_score += 1
    true_love_score = str(true_score) + str(love_score)
    print(true_love_score)


calculate_love_score("Richard Granados", "Angela Miralda")
