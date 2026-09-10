
def lift (air_density,velocity,wing_area,cl):
    l = 0.5 * air_density * velocity**2 * wing_area * cl
    return l
def drag (air_density,velocity,wing_area,cd):
    d = 0.5*air_density*velocity**2*wing_area*cd
    return d
def lift_drag_ratio (cl,cd):
    ratio = (cl/cd)
    return ratio
def weight (mass):
    total_weight = mass*9.81
    return total_weight
def dynamic_pressure (air_density,velocity):
    pressure = 0.5 * air_density * velocity**2
    return pressure

def get_aircraft_inputs ():
    try:
        mass = float(input("Enter the mass of the aircraft (kg): "))
        wing_area = float(input("Enter the area of the wing of the aircraft (m^2): "))
        velocity = float(input("Enter the velocity (m/s): "))
        air_density = float(input("Enter the air density (kg/m^3): "))
        cl = float(input("Enter the coefficient of lift: "))
        cd = float(input("Enter the coefficient of drag: "))
        return mass, wing_area,velocity,air_density,cl,cd
    
    except ValueError:
        print("Invalid input!! Please input only numerical values.")
        return None

while True:
    
    user_data = get_aircraft_inputs()
    if user_data is None:
        continue
    mass,wing_area,velocity,air_density,cl,cd = user_data

    print("="*4,"AIRCRAFT PERFORMANCE CALCULATOR","="*4)
    print("1. Calculate Lift")
    print("2. Calculate drag")
    print("3. Calculate weight")
    print("4.Calculate dynamic pressure")
    print("5. Calculate lift/drag ratio")
    print("6. Calculate All")
    print("7. Exit")

    choice = input("Choose an option (from 1-7): ")
    if choice == "1":
        t_lift = lift (air_density,velocity,wing_area,cl)
        print(f"The total lift force is: {t_lift:.4f}N")
    elif choice == "2":
        t_drag = drag(air_density,velocity,wing_area,cd)
        print (f"The total drag force is: {t_drag:.4f}N")
    elif choice == "3":
        total_weight = weight(mass)
        print(f"The total weight of the aircraft is: {total_weight:.4f}N")
    elif choice == "4":
        d_pressure = dynamic_pressure(air_density,velocity)
        print (f"The dynamic pressure is: {d_pressure:.4f}Pa")
    elif choice == "5":
        try:
            ratio = lift_drag_ratio(cl,cd)
            print (f"The lift drag ratio is: {ratio:.4f}")
        except ZeroDivisionError:
            print ("The drag is zero !! hence can't calculate the ratio.")
    elif choice == "6":
        t_lift = lift (air_density,velocity,wing_area,cl)
        print(f"The total lift force is: {t_lift:.4f}N")
        t_drag = drag(air_density,velocity,wing_area,cd)
        print (f"The total drag force is: {t_drag:.4f}N")
        total_weight = weight(mass)
        print(f"The total weight of the aircraft is: {total_weight:.4f}N")
        d_pressure = dynamic_pressure(air_density,velocity)
        print (f"The dynamic pressure is: {d_pressure:.4f}Pa")
        try:
            ratio = lift_drag_ratio(cl,cd)
            print (f"The lift drag ratio is: {ratio:.4f}")
        except ZeroDivisionError:
            print ("The drag is zero !! hence can't calculate the ratio.")
    elif choice == "7":
        print("Thankyou ! Exiting calculator, goodbye.")
        break
    else:
        print("Invalid choice!! Please choose between (1-7)")
    
    
    
    
        

    
