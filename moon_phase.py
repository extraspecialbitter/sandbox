#!/usr/bin/python3

import ephem

# Calculate and print moon phase

def get_moon_phase():
    moon = ephem.Moon()
    moon.compute()
    illumination = moon.phase  # percentage illuminated (0-100)

    # Determine phase name from the lunar cycle
    previous_new = ephem.previous_new_moon(ephem.now())
    next_new = ephem.next_new_moon(ephem.now())
    cycle_length = next_new - previous_new
    days_into_cycle = ephem.now() - previous_new
    fraction = days_into_cycle / cycle_length

    if fraction < 0.0625:
        phase_name = "New Moon"
    elif fraction < 0.1875:
        phase_name = "Waxing Crescent"
    elif fraction < 0.3125:
        phase_name = "First Quarter"
    elif fraction < 0.4375:
        phase_name = "Waxing Gibbous"
    elif fraction < 0.5625:
        phase_name = "Full Moon"
    elif fraction < 0.6875:
        phase_name = "Waning Gibbous"
    elif fraction < 0.8125:
        phase_name = "Last Quarter"
    elif fraction < 0.9375:
        phase_name = "Waning Crescent"
    else:
        phase_name = "New Moon"

    return phase_name, round(illumination, 1)

moon_phase, moon_illumination = get_moon_phase()
print(" Moon: %s (%s%% illuminated)" % (moon_phase, moon_illumination))
