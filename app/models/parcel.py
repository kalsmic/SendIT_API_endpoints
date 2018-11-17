# parcel.py
from app.models.user import user_id_table


class ParcelOrder:
    parcel_id = 1

    def __init__(self, item, pick_up, destination, status, owner_id):
        self.id = ParcelOrder.parcel_id
        self.item = item
        self.pickUp = pick_up
        self.destination = destination
        self.status = status
        self.ownerId = owner_id

        ParcelOrder.parcel_id += 1

    #
    def parcel_details(self):
        """Returns the details of a parcel delivery order"""

        return {
            'id': self.id,
            "Item": self.item,
            "destination": self.destination,
            "ownerId": user_id_table[self.ownerId].userName,
            "pickUp": self.pickUp,
            "status": self.status
        }

    def cancel_parcel_Order(self):
        """Cancels a parcel delivery order"""
        if self.status.upper() == 'PENDING':
            # cancel Order
            self.status = 'CANCELLED'

            return True

        # Order is already delivered,Cancelled,or In transit
        return False


parcelOrders = [
    ParcelOrder('item', 'pickUp Address', 'Destination Address', 'pending', 1),
    ParcelOrder('Laptop', 'Kampala', 'Moroto', 'Pending', 1),
    ParcelOrder('Office Cabin', 'Kole', 'Otuke', 'In Transit', 2),
    ParcelOrder('HMIS FORMS', 'Kitgum', 'Agago', 'Delivered', 1),
    ParcelOrder('HRH PLANS', 'Yumbe', 'Koboko', 'Cancelled', 1),
    ParcelOrder('DJ Mavic Air Beats', 'Mwanza', 'Bukoba', 'Cancelled', 1),
    ParcelOrder('APPRAISAL FORMS', 'Mwanza', 'Bukoba', 'Pending', 2)

]
parcel_id_table = {parcel.id: parcel for parcel in parcelOrders}
