# demonstrate template strings

from string import Template




def main():
    # usual string formation with format()
    str1 = "You're watching {0} by {1}".format("advanced python", "andrew marks")
    print(str1)

    # TODO: create a template with placeholders
    templ = Template("watching ${title} by ${author}")


    # TODO: use the substitute method with keyword args
    str2 = templ.substitute(title="Adv Py", author="andrew")
    print(str2)


    # TODO: use the substitute method with a dictionary
    data = {
        "author": "andrew",
        "title": "Adv Py"
    }
    str3 = templ.substitute(data)
    print(str3)
    

if __name__ == "__main__":
    main()