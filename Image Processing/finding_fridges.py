from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import json


class ApplianceType(Enum):
    """Enumeration of appliance types"""

    FRIDGE = "fridge"
    WASHER = "washing_machine"
    DRYER = "dryer"
    OVEN = "oven"
    DISHWASHER = "dishwasher"


@dataclass
class Appliance:
    """
    Represents an appliance with its properties

    Attributes:
        name: Name/model of appliance
        type: Type of appliance
        brand: Manufacturing brand
        price: Price in dollars
        capacity: Storage capacity (for fridges)
    """

    name: str
    type: ApplianceType
    brand: str
    price: float
    capacity: Optional[float] = None


class FridgeFinder:
    """
    Class to find and filter fridges from appliance collections

    Example:
        >>> finder = FridgeFinder()
        >>> fridges = finder.find_fridges(appliances)
    """

    def find_fridges(self, appliances: List[Appliance]) -> List[Appliance]:
        """Find all fridges in appliance list"""
        return [
            appliance
            for appliance in appliances
            if appliance.type == ApplianceType.FRIDGE
        ]

    def find_fridges_by_brand(
        self, appliances: List[Appliance], brand: str
    ) -> List[Appliance]:
        """Find fridges of specific brand"""
        return [
            appliance
            for appliance in appliances
            if appliance.type == ApplianceType.FRIDGE
            and appliance.brand.lower() == brand.lower()
        ]

    def find_fridges_in_price_range(
        self, appliances: List[Appliance], min_price: float, max_price: float
    ) -> List[Appliance]:
        """Find fridges within price range"""
        return [
            appliance
            for appliance in appliances
            if appliance.type == ApplianceType.FRIDGE
            and min_price <= appliance.price <= max_price
        ]

    def find_fridges_by_capacity(
        self, appliances: List[Appliance], min_capacity: float
    ) -> List[Appliance]:
        """Find fridges with minimum capacity"""
        return [
            appliance
            for appliance in appliances
            if appliance.type == ApplianceType.FRIDGE
            and appliance.capacity
            and appliance.capacity >= min_capacity
        ]

    def get_fridge_statistics(self, appliances: List[Appliance]) -> Dict:
        """Get statistics about fridges"""
        fridges = self.find_fridges(appliances)

        if not fridges:
            return {"count": 0, "avg_price": 0, "min_price": 0, "max_price": 0}

        prices = [fridge.price for fridge in fridges]

        return {
            "count": len(fridges),
            "avg_price": sum(prices) / len(prices),
            "min_price": min(prices),
            "max_price": max(prices),
        }

    def export_fridges_to_json(
        self, appliances: List[Appliance], filename: str
    ) -> None:
        """Export fridge data to JSON file"""
        fridges = self.find_fridges(appliances)
        fridge_data = [
            {
                "name": fridge.name,
                "brand": fridge.brand,
                "price": fridge.price,
                "capacity": fridge.capacity,
            }
            for fridge in fridges
        ]

        with open(filename, "w") as f:
            json.dump(fridge_data, f, indent=4)


def load_appliances_from_json(filename: str) -> List[Appliance]:
    """Load appliances from JSON file"""
    with open(filename, "r") as f:
        data = json.load(f)

    return [
        Appliance(
            name=item["name"],
            type=ApplianceType(item["type"]),
            brand=item["brand"],
            price=item["price"],
            capacity=item.get("capacity"),
        )
        for item in data
    ]


if __name__ == "__main__":
    # Create sample appliances
    appliances = [
        Appliance("Frost-Free 500L", ApplianceType.FRIDGE, "Whirlpool", 999.99, 500),
        Appliance("Front Load 8kg", ApplianceType.WASHER, "LG", 699.99),
        Appliance("Smart Fridge", ApplianceType.FRIDGE, "Samsung", 1499.99, 700),
        Appliance("Electric Range", ApplianceType.OVEN, "GE", 899.99),
        Appliance("French Door", ApplianceType.FRIDGE, "LG", 1299.99, 600),
    ]

    finder = FridgeFinder()

    # Find all fridges
    fridges = finder.find_fridges(appliances)
    print("\nAll Fridges:")
    for fridge in fridges:
        print(f"{fridge.brand} {fridge.name} - ${fridge.price}")

    # Find fridges by brand
    lg_fridges = finder.find_fridges_by_brand(appliances, "LG")
    print("\nLG Fridges:")
    for fridge in lg_fridges:
        print(f"{fridge.name} - ${fridge.price}")

    # Get statistics
    stats = finder.get_fridge_statistics(appliances)
    print("\nFridge Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    # Export to JSON
    finder.export_fridges_to_json(appliances, "fridges.json")
