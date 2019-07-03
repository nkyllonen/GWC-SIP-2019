'''
PY file for getting started with my analysis of the Cars data set

CORGIS Source:
https://think.cs.vt.edu/corgis/python/cars/cars.html
'''
import cars

def main():
    # import all of the car dataset as a list
    # list_of_cars = cars.get_cars()

    # import a subset of the entire dataset
    list_of_cars = cars.get_cars(test=True)

if __name__ == '__main__':
    main()
