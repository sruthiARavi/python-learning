def calculate_love_score(name1, name2):
    # combine the names so that the calculation is easier
    combined_name = name1 + name2
    # convert to upper so that the matches don't fail
    combined_name = combined_name.upper()
    # count the letter repetition
    tcount = combined_name.count("T")
    rcount = combined_name.count("R")
    ucount = combined_name.count("U")
    ecount = combined_name.count("E")
    lcount = combined_name.count("L")
    ocount = combined_name.count("O")
    vcount = combined_name.count("V")

    num1 = tcount + rcount + ucount + ecount
    num1_str = str(num1)

    num2 = lcount + ocount + vcount + ecount
    num2_str = str(num2)

    num = num1_str + num2_str

    print(num)
