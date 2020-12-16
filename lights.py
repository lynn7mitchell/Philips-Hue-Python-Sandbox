from phue import Bridge
# import philips hue bridge number
from bridge_ip import bridge_ip_address
import sys

b = Bridge(bridge_ip_address)

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# light objects
lights = b.lights

separator = ' '
command = str(separator.join(sys.argv[1:]))

for light in lights:
    print(light.name)



def turn_on_ceiling_lights():
    b.set_light('Ceiling Light', 'on', True)

def turn_off_ceiling_lights():
    b.set_light('Ceiling Light', 'on', False)


if command == 'turn on the ceiling lights in my room':
    turn_on_ceiling_lights()

if command == 'turn off the ceiling lights in my room':
    turn_off_ceiling_lights()

