# from Api.Models import Vendor as models_vendor
from Api.Contracts.vendor import Vendor as vendorContract
from Api.Repositories import vendor as vendorRepo


def get_by_id(id) -> vendorContract:
    models_vendor = vendorRepo.get_by_id(id)
    return vendorContract(models_vendor.name, models_vendor.description, models_vendor.website)


def get_all():
    models_vendors = vendorRepo.get_all()
    contracts_vendors = []
    for vendor in models_vendors:
        contracts_vendors.append(vendorContract(vendor.name, vendor.description, vendor.website))
    return contracts_vendors

# def get_all_serialize():
#     models_vendors = get_all()
#     vendors_serialized = []
#     for vendor in models_vendors:
#         vendors_serialized.append()
#     return vendorContract(models_vendors.name, models_vendors.description, models_vendors.website)
