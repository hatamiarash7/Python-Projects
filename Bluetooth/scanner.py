import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for address, name in nearby_devices:
    print("  %s - %s" % (address, name))
