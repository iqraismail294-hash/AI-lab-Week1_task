class ParkingSlot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.vehicle_number = None

    def is_free(self):
        return self.vehicle_number is None

slots = [
    ParkingSlot(1),
    ParkingSlot(2),
    ParkingSlot(3),
    ParkingSlot(4),
    ParkingSlot(5)
]
total_money = 0

def park_vehicle(vehicle_number):
    for slot in slots:
        if slot.vehicle_number == vehicle_number:
            print(vehicle_number, "is already parked.")
            return

    for slot in slots:
        if slot.is_free():
            slot.vehicle_number = vehicle_number
            print(
                vehicle_number,
                "parked in slot",
                slot.slot_number
            )
            return
    print("Parking full. Cannot park", vehicle_number)

def vehicle_leaves(vehicle_number, hours):
    global total_money

    for slot in slots:
        if slot.vehicle_number == vehicle_number:
            if hours < 1:
                print("Parking duration must be at least 1 hour.")
                return

            fee = 60 + (hours - 1) * 40
            slot.vehicle_number = None
            total_money += fee

            print(
                vehicle_number,
                "left slot",
                slot.slot_number,
                "| Fee: Rs.",
                fee
            )
            return

    print(vehicle_number, "is not in the parking lot.")

print("PARKING LOT EVENTS")

park_vehicle("LEB-101")
park_vehicle("ABC-555")
park_vehicle("XYZ-777")
park_vehicle("LEB-101") 

vehicle_leaves("LEB-101", 3)

park_vehicle("KHI-999")
park_vehicle("PQR-222")
park_vehicle("MNO-333")
park_vehicle("DEF-444") 

vehicle_leaves("ZZZ-000", 2)
vehicle_leaves("ABC-555", 1)

print("\nFINAL PARKING STATUS")

for slot in slots:
    if slot.is_free():
        print("Slot", slot.slot_number, ": Free")
    else:
        print(
            "Slot", slot.slot_number, ":",
            slot.vehicle_number
        )

print("\nTotal money earned: Rs.", total_money)



