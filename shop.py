import csv
import locale
from dataclasses import dataclass

@dataclass
class WondrousItem:
  """
  Class representing a wondrous item from the CSV data.
  """
  name: str
  slot: str
  description: str
  view_desc: str
  price: int
  half_price: int
  upgrade: str
  cl: int
  weight: float
  strength: str
  school: str
  crafting_feat: str
  spells_needed: str
  other_reqs: str
  base_crafting_dc: int
  num_req: int
  source: str
  url: str
  notes: str

def read_wondrous_items(filename):
  """
  Reads a CSV file containing wondrous item data and returns a list of WondrousItem objects.

  Args:
      filename: The path to the CSV file.

  Returns:
      A list of WondrousItem objects.
  """
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  items = []
  with open(filename, 'r') as csvfile:
    # Skip the header row
    next(csvfile)

    reader = csv.reader(csvfile)
    for row in reader:
      # Convert values to appropriate types
      name, slot, description, view_desc = row[0], row[1], row[2], row[3]
      price = locale.atoi(row[4]) if row[4] else None
      half_price = locale.atoi(row[5]) if row[5] else None
      upgrade = row[6]
      cl = int(row[7])
      weight = float(row[8])
      strength = row[9]
      school = row[10]
      crafting_feat = row[11]
      spells_needed = row[12]
      other_reqs = row[13]
      base_crafting_dc = int(row[14])
      num_req = int(row[15])
      source = row[16]
      url = row[17]
      notes = row[18]

      # Create a WondrousItem object and append it to the list
      item = WondrousItem(name, slot, description, view_desc, price, half_price, upgrade, cl, weight, strength, school, crafting_feat, spells_needed, other_reqs, base_crafting_dc, num_req, source, url, notes)
      items.append(item)
  return items

if __name__ == "__main__":
  filename = "Pathfinder_WondrousItems.csv"
  items = read_wondrous_items(filename)

  # Access item data
  for item in items:
    print(f"Name: {item.name}")
    print(f"Description: {item.description[:50]}...")  # Print first 50 characters of description
    print(f"Price: {item.price} gp")
    print("-" * 20)

