#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com
   
   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/
   
   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
from mtgsdk import Type

types = Type.all()

# Define our "base" API
API = "https://docs.magicthegathering.io/#api_v1types_list" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}types")   # this "f" string reads: API + "types"
                                        # OR, https://docs.magicthegathering.io/#api_v1types_list

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cardsets = resp.json().get("types")

    for type in types:  # loop across ALL of the sets of MTG cards (they are stored as dict objects)
        print(type)  # each dictionary represents a set of cards

if __name__ == "__main__":
    main()

