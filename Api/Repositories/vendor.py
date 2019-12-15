from Api.Models.vendor import Vendor


def get_by_id(id) -> Vendor:
    return Vendor(id, id, "description", "website")


def get_all():
    vendors = [
        Vendor(1, "vendor 1", "provides service", "website"),
        Vendor(2, "vendor 2", "different service", "website"),
        Vendor(3, "vendor 3", "does something else", "website")
    ]
    return vendors
