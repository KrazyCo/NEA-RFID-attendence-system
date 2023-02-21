import time
import json

from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

from cardDataTest import dataTest

# define the apdus used in this script
apdu = [0xFF, 0xCA, 0x00, 0x00, 0x04]


# a simple card observer that tries to select DF_TELECOM on an inserted card
class selectDFTELECOMObserver(CardObserver):
    def __init__(self):
        self.observer = ConsoleCardConnectionObserver()

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            card.connection = card.createConnection()
            card.connection.connect()

            response, sw1, sw2 = card.connection.transmit(apdu)

            if sw1 == 144: # if transmission was successful
                response = toHexString(response) # convert response to hex string from byte
                reader = card.reader[-4]
                print(card.reader)
                dataTest(response, findReader(reader), time.time())

def findReader(reader):
    with open('inputConfig.json', 'r') as f:
        config = json.load(f)
        return "In" if config["inReader"]== reader else "Out"

if __name__ == '__main__':
    print("Started")
    print("")

    # setup the observer 
    cardmonitor = CardMonitor()
    selectobserver = selectDFTELECOMObserver()
    cardmonitor.addObserver(selectobserver)
    try:
        while True:
            input()
    except KeyboardInterrupt:
        cardmonitor.deleteObserver(selectobserver) # remove the observer on keyboard interrupt
        print(" detected, closed")
