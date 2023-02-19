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

            if sw1 == 144:
                print(type(response))
                response = toHexString(response)
                print(type(response))
                reader = card.reader[-4]
                dataTest(response, findReader(reader), time.time())

def findReader(reader):
    with open('inputConfig.json', 'r') as f:
        config = json.load(f)
        return "In" if config[reader] == reader else "Out"

if __name__ == '__main__':
    print("Insert or remove a SIM card in the system.")
    print("")
    cardmonitor = CardMonitor()
    selectobserver = selectDFTELECOMObserver()
    cardmonitor.addObserver(selectobserver)
    try:
        while True:
            input()
    except KeyboardInterrupt:
        # don't forget to remove observer, or the
        # monitor will poll forever...
        cardmonitor.deleteObserver(selectobserver)
        print("Closed")
