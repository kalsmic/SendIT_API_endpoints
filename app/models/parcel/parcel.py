# parcel.py

PARCELS = []


class PARCEL:
    parcel_id = 1

    def __init__(self, item, pickUp, destination, status, ownerId):
        self.id = PARCEL.parcel_id
        self.item = item
        self.pickUp = pickUp
        self.destination = destination
        self.status = status
        self.ownerId = ownerId

        PARCEL.parcel_id += 1

    def parcel_details(self):
        """Returns the details of a parcel delivery order"""
        return {
            'id': self.id,
            "Item": self.item,
            "destination": self.destination,
            "ownerId": self.ownerId,
            "pickUp": self.pickUp,
            "status": self.status
        }

    def __str__(self):
        return
        "parcels:{ id:'%d',item:'%s', pickUp:'%s',destination:'%s',status:'%s',ownerId:'%s'" \
        % (self.id, self.item, self.pickUp, self.destination, self.status, self.ownerId)


def parcel_table():
    return {parcel.id: parcel for parcel in PARCELS}


def get_parcel_by_id(id):
    return parcel_table()[id].parcel_details()

PARCELS.extend ([
    # PARCEL(id, 'item' 'pickUp', 'destination', 'status', ownerId),
    PARCEL('item' ,'pickUp', 'destination', 'status', 'owner1'),
    PARCEL('Laptop', 'Kampala', 'Moroto', 'pending', 'owner2'),
    PARCEL('Office Cabin', 'Kole', 'Otuke', 'In Transit','owner3'),
    PARCEL('HNIS FORMS', 'Yumbe', 'Koboko', 'Delivered', 'owner4'),
    PARCEL('HNIS FORMS' ,'Yumbe', 'Koboko', 'Delivered', 'owner5'),
    PARCEL('APPRAISAL FORMS' ,'Mwanza', 'Bukoba', 'Cancelled', 'owner6')
])

if __name__ == "__main__":
    # add a parcel
    PARCELS.append(PARCEL('item', 'pickUp', 'destination', 'status', 'owner5'))

    print(get_parcel_by_id(1))
