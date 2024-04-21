def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    max_strength = -1
    max_extension = ''
    for extension in extensions:
        strength = ord('Z') - ord('A') #ord('A') #ord('Z')
        for letter in extension:
            if letter.islower():
                strength -= ord(letter)
        if strength > max_strength:
            max_strength = strength
            max_extension = extension
    return class_name + '.' + max_extension

# Testing
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9', 'Extension10']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9', 'Extension10', 'Extension11']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9', 'Extension10', 'Extension11', 'Extension12']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9', 'Extension10', 'Extension11', 'Extension12', 'Extension13']))
print(Strongest_Extension('my_class', ['Extension1', 'Extension2', 'Extension3', 'Extension4', 'Extension5', 'Extension6', 'Extension7', 'Extension8', 'Extension9', 'Extension