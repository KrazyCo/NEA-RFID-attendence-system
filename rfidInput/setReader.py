import json

from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

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
                reader = card.reader[-4]
                with open('inputConfig.json', 'w') as f:
                    config = {
                        "inReader": reader
                    }
                    json.dump(config, f, indent=4)
                print("IN reader set to: " + reader)
                print("Press ctrl+c to close")


if __name__ == '__main__':
    print("Tap the IN reader to set the correct number in config")
    print("")
    cardmonitor = CardMonitor()
    selectobserver = selectDFTELECOMObserver()
    cardmonitor.addObserver(selectobserver)
    try:
        while True:
            input()
    except KeyboardInterrupt:
        cardmonitor.deleteObserver(selectobserver)
        print(" detected, closed")
