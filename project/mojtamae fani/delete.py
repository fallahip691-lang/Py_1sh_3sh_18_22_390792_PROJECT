

def delete(shomare_class, class_mojtama, classes,code):
    if shomare_class in class_mojtama:

        class_mojtama.pop(shomare_class)
        code.remove(shomare_class)

        for i in classes:
            if i["shomare class"] == shomare_class:
                classes.remove(i)
                break

        print("class deleted")

    else:
        print("class not found")

        