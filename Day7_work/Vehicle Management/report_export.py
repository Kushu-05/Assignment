import csv

def export_vehicle_data(filename, vehicles):
    """Export vehicle data to a csv file."""
    with open(filename, mode='w', newline='') as file:
        writer =csv.writer(file)
        writer.writerow(['Brand','Model','year','Owner','Battery Capacity'])

        for v in vehicles:
            owner =v.get_owner()
            if owner is None:
                owner ="No owner assignment"
            battery_capacity = getattr(v, 'battery_capacity', 'N/A')
            writer.writerow([v.brand, v.model,v.year,owner,battery_capacity])
    return f"Vehicle data exported to {filename} successfully."
