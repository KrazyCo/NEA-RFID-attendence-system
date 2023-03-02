import time
import json

from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

from cardDataTest import dataTest

import sys
sys.path.insert(0, '../database')

from logStudentAction import logStudentAction

# define the apdus used in this script
apdu = [0xFF, 0xCA, 0x00, 0x00, 0x04] # UID request hex code


# a simple card observer that tries to select DF_TELECOM on an inserted card
class selectDFTELECOMObserver(CardObserver):
    def __init__(self):
        self.observer = ConsoleCardConnectionObserver() 

    def update(self, observable, actions): # called when the card is inserted/removed
        (addedcards, removedcards) = actions 
        for card in addedcards:
            card.connection = card.createConnection() # create connection to the card
            card.connection.connect() 

            response, sw1, sw2 = card.connection.transmit(apdu) # transmit hex code for UID and save response and status

            if sw1 == 144: # if transmission was successful
                response = toHexString(response) # convert response to hex string from byte
                reader = card.reader[-4] # Take single digit from reader name - shown with [] - ACS ACR122U 0[1] 00
                dataTest(response, findReader(reader), time.time()) # send UID, reader type and time to dataTest function
                logStudentAction(response, findReader(reader), time.time()) # send UID, reader type and time to logStudentAction function

def findReader(reader):
    with open('inputConfig.json', 'r') as f:
        config = json.load(f)
        return "In" if config["inReader"]== reader else "Out" # return In or Out depending on reader type

if __name__ == '__main__':
    print("Started")
    print("")

    # setup the observer 
    cardmonitor = CardMonitor() # create a card monitor
    selectobserver = selectDFTELECOMObserver() # create an observer
    cardmonitor.addObserver(selectobserver) # add the observer to the monitor
    try:
        while True:
            input() # wait for keyboard interrupt as program needs to be running to detect card
    except KeyboardInterrupt:
        cardmonitor.deleteObserver(selectobserver) # remove the observer on keyboard interrupt
        print(" detected, closed")
