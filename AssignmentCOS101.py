def velocity():
    print("Calculating velocity...")
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    print(f"Velocity = {distance / time} m/s")


def force():
    print("Calculating force...")
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    print(f"Force = {mass * acceleration} N")


def kinetic_energy():
    print("Calculating kinetic energy...")
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    print(f"Kinetic Energy = {0.5 * mass * velocity ** 2} J")


def potential_energy():
    print("Calculating potential energy...")
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    gravity = 9.8  # acceleration due to gravity
    print(f"Potential Energy = {mass * gravity * height} J")


def power():
    print("Calculating power...")
    work = float(input("Enter work done (J): "))
    time = float(input("Enter time taken (s): "))
    print(f"Power = {work / time} W")


def main():
    print("Choose a physics operation:")
    print("a. Velocity")
    print("b. Force")
    print("c. Kinetic Energy")
    print("d. Potential Energy")
    print("e. Power")

    choice = input("Enter your choice (a-e): ").lower()
    if choice == 'a':
        velocity()
    elif choice == 'b':
        force()
    elif choice == 'c':
        kinetic_energy()
    elif choice == 'd':
        potential_energy()
    elif choice == 'e':
        power()
    else:
        print("Invalid choice. Please enter a valid option.")


# Call the main function to start the program