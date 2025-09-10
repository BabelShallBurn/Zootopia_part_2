import data_fetcher

def load_html(file_path:str):
    """ Loads a HTML file """
    with open(file_path, "r", encoding="utf-8") as fileobj:
        html_content = fileobj.read()
        return html_content


def serialize_animal(animal:dict):
    """serializes animal and returns necessary data in list form

    Args:
        animal (dict): holds information of one animal

    Returns:
        list: list with easy to access information
    """
    animal_obj = []
    animal_obj.append(animal["name"])
    animal_obj.append(["Diet: ", animal["characteristics"]["diet"]])
    animal_obj.append(["Locations: ", animal['locations']])
    if "type" in animal['characteristics']:
        animal_obj.append(["Type: ", animal["characteristics"]["type"]])
    if "distinctive_feature" in animal['characteristics']:
        animal_obj.append(["Distinctive feature: ", animal["characteristics"]["distinctive_feature"]])
    if "temperament" in animal['characteristics']:
        animal_obj.append(["Temperament: ", animal["characteristics"]["temperament"]])
    if "lifespan" in animal['characteristics']:
        animal_obj.append(["Lifespan: ", animal["characteristics"]["lifespan"]])
    return animal_obj


def create_html(serialized_animal:list):
    """creates html string from serialized animal

    Args:
        serialized_animal (list): list with animal information

    Returns:
        string: html string
    """
    animal_obj = ''
    animal_obj += '<li class="cards__item">\n'
    animal_obj += f'  <div class="card__title">{serialized_animal[0]}</div>\n'
    animal_obj += '  <div class="card__text">\n'
    animal_obj += '    <ul>\n'
    for item in serialized_animal:
        if len(item) == 2:
            if isinstance(item[1],list):
                animal_obj += f'      <li><strong>{item[0]}</strong>{", ".join(item[1])}\n'
            else:
                animal_obj += f'      <li><strong>{item[0]}</strong>{item[1]}\n'
    animal_obj += "    </ul>\n"
    animal_obj += "  </div>\n"
    animal_obj += '</li>\n'
    animal_obj += '\n'
    return animal_obj

def main():
    animal_name = input("Please enter an animal: ")
    html_data = load_html('animals_template.html')
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        html_data = html_data.replace("My Animal Repository", f"{animal_name} doesn't exist.")
        html_data = html_data.replace('''<ul class="cards">\n            __REPLACE_ANIMALS_INFO__\n        </ul>''', "Here would be your animal's info.")

    animals_data_string = ""
    if animals_data != []:
        for animal in animals_data:
            serialized_animal = serialize_animal(animal)
            animals_data_string += create_html(serialized_animal)
        html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)

    with open("animals_data.html", "w", encoding="utf-8") as handle:
        handle.write(html_data)

if __name__ == "__main__":
    main()