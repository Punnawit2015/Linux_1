#!/usr/bin/env python3

print("Welcome! Choose a shape using 1, 2, or 3.")


def rectangle_area():
    print("\nRectangle Area")
    width = float(input("Enter the width: "))
    length = float(input("Enter the length: "))
    area = width * length
    print(f"Rectangle area = width x length = {width} x {length} = {area}")


def square_area():
    print("\nSquare Area")
    length = float(input("Enter the length: "))
    area = length * length
    print(f"Square area = length x length = {length} x {length} = {area}")


def triangle_area():
    print("\nTriangle Area")
    print("Formula: 1/2 x base x height")
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"Triangle area = 1/2 x {base} x {height} = {area}")


while True:
    try:
        print("\nMenu")
        print("[1] Rectangle area")
        print("[2] Square area")
        print("[3] Triangle area")

        choice = input("Press 1, 2, or 3: ").strip()

        if choice == "1":
            rectangle_area()
        elif choice == "2":
            square_area()
        elif choice == "3":
            triangle_area()
        else:
            print("Invalid choice. Please press 1, 2, or 3.")
    except EOFError:
        print("\nInput ended. Goodbye!")
        break
