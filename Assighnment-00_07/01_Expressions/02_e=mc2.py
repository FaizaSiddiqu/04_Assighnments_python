
c = 299792458 
m = 100.0


def main():
   mass_in_kg = float(input("Enter the mass in kg: "))
   energy_in_joules : float = mass_in_kg * (c ** 2)
    
 
 
   print("e = m * c^2...")
   print("m = " + str(mass_in_kg) + " kg")
   print("c = " + str(c) + " m/s")
   
   print(str(energy_in_joules) + " joules in energy!")
 
 
if __name__ == '__main__':
    main()