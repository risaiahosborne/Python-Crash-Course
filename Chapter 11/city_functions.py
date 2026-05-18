def city_country(city, country, population=None):
    """Return a string of the form 'City, Country'."""
    if population:
        return f"{city.title()}, {country.title()} - Population: {population}"
    else:
        return f"{city.title()}, {country.title()}"
