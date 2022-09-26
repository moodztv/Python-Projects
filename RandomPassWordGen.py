import random

def main():

    
    firstpwd = random.choice(['fgHr', "ogyh", "edkg", "jgkn"])

    secondpwd = random.choice(["hawks", "lions", "eagles", "dolphins"])

    thirdpwd = random.choice(["432","968","374","903","145"])

    print("YOUR PASSWORD:")
    print(firstpwd+secondpwd+thirdpwd)


main()