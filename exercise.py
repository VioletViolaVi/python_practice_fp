def calculate_population_density(ppl_num, land_area):
    return ppl_num / land_area


def sentence(home_town_name="peru"):
    print(
        f"the population density of {home_town_name} is {calculate_population_density(70, 2)}")


sentence("Japan")
