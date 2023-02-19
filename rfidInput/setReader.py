import time

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
                response = toHexString(response)
                reader = card.reader[-4]



if __name__ == '__main__':
    print("Tap the in reader to set the correct number in config")
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