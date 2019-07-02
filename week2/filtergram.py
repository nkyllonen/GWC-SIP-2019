import filters

def main():
    file = "cube.jpg"

    myimage = filters.load_img(file)
    filters.show_img(myimage)

    #filtered = filters.obamicon(myimage)
    #filters.save_img(filtered, "filtered_" + file)

if __name__ == '__main__':
    main()
