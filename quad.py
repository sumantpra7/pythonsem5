import cmath 


a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))


if a == 0:
    print("This is not a quadratic equation (a should not be 0)")
else:
    
    D = b**2 - 4*a*c
    print(f"Discriminant (D) = {D}")

   
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)

    # Display roots based on D
    if D > 0:
        print("Roots are real and distinct.")
    elif D == 0:
        print("Roots are real and equal")
    else:
        print("Roots are complex ")

    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
