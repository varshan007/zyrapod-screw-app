def screw_conveyor_selector(feed_rate_kg_hr, biomass_type, bulk_density_kg_m3, particle_size_mm):
    print("=== Screw Conveyor Design Recommendation ===\n")
    
    # STEP 1: Estimate flow rate
    feed_rate_kg_min = feed_rate_kg_hr / 60
    flow_rate_m3_min = feed_rate_kg_min / bulk_density_kg_m3

    # STEP 2: Select screw diameter based on particle size and flow
    if particle_size_mm <= 10:
        screw_dia = 75
    elif particle_size_mm <= 20:
        screw_dia = 100
    else:
        screw_dia = 125

    pitch = screw_dia  # standard
    shaft_dia = int(screw_dia * 0.25)
    
    # STEP 3: Estimate RPM (lower RPM for larger particles)
    rpm = 45 if screw_dia <= 100 else 35
    
    # STEP 4: Estimate motor power (empirical range)
    motor_power_kW = 0.18 if feed_rate_kg_hr <= 25 else 0.37

    # STEP 5: Output recommendation
    print(f"Input Biomass Type      : {biomass_type}")
    print(f"Feed Rate               : {feed_rate_kg_hr} kg/hr")
    print(f"Bulk Density            : {bulk_density_kg_m3} kg/m³")
    print(f"Particle Size           : {particle_size_mm} mm\n")

    print(f"Recommended Screw Dia   : {screw_dia} mm")
    print(f"Pitch                   : {pitch} mm")
    print(f"Shaft Diameter          : {shaft_dia} mm")
    print(f"Length                  : 1 to 1.5 m (based on ZyraPod layout)")
    print(f"Recommended RPM         : {rpm}")
    print(f"Housing Type            : U-trough or closed pipe")
    print(f"Motor Power             : {motor_power_kW:.2f} kW")
    print(f"Gearbox Type            : Worm or helical geared motor")
    print("\n============================================\n")


# Example usage
screw_conveyor_selector(
    feed_rate_kg_hr=50,
    biomass_type="Chopped Paddy Straw",
    bulk_density_kg_m3=140,
    particle_size_mm=10
)