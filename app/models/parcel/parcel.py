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

    def cancel_parcel_Order(self):
        """Cancels a parcel delivery order"""
        if self.status =='Pending':
            #cancel Order
            self.status = 'Cancelled'

            return True
        # Order is already delivered,Cancelled,or In transit
        return False




    def __str__(self):
        return
        "parcels:{ id:'%d',item:'%s', pickUp:'%s',destination:'%s',status:'%s',ownerId:'%s'" \
        % (self.id, self.item, self.pickUp, self.destination, self.status, self.ownerId)


def parcel_table():
    return {parcel.id: parcel for parcel in PARCELS}

# returns the reference of the PARCEL Object Instance from memory
def get_parcel_reference(id):
    """parameter: expects an integer id
    :returns: memory address of the parcel object"""
    return parcel_table()[id]


def get_parcel_by_id(id):
    return parcel_table()[id].parcel_details()

PARCELS.extend ([
    # PARCEL(id, 'item' 'pickUp', 'destination', 'status', ownerId),
    PARCEL('Laptop', 'Kampala', 'Moroto', 'Pending', 1),
    PARCEL('Office Cabin', 'Kole', 'Otuke', 'In Transit',2),
    PARCEL('HMIS FORMS', 'Kitgum', 'Agago', 'Delivered', 1),
    PARCEL('HRH PLANS' ,'Yumbe', 'Koboko', 'Cancelled', 1),
    PARCEL('DJ Mavic Air Beats' ,'Mwanza', 'Bukoba', 'Cancelled', 1),
    PARCEL('APPRAISAL FORMS', 'Mwanza', 'Bukoba', 'Pending', 2)

])

if __name__ == "__main__":
    # pass
    # add a parcel
    # PARCELS.append(PARCEL('item', 'pickUp', 'destination', 'status', 'owner5'))

    # print(get_parcel_by_id(1))
    # parcelIds = parcel_table().keys()
    # print('parcelId=',parcelIds)
    # parcelStatus = get_parcel_by_id(1)['status']
    # print('parcelstatus=',parcelStatus)
    # parcelS# from app.dummy_data import (
#     PARCELS,
#     # USERS
#
# )tatus = get_parcel_by_id(1)
    # print(PARCELS[3].parcel_details())
    #  for xparcel in parcel_table():
     for xparcel in PARCELS:

         print(xparcel.ownerId)
         # for parcel in PARCELS:
             # if parcel.parcel_details()['ownerId'] ==1:
            # print(parcel)
