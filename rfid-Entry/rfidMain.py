from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util
from cardDataTest import dataTest


if __name__ == '__main__':
    while True:
        # respond to the insertion of any type of smart card
        card_type = AnyCardType()

        # create the request. Wait forever for a card to be attached. Only activate when new card is placed on reader
        request = CardRequest(newcardonly=True, timeout=None, cardType=card_type)

        # listen for the card
        print("Place card on reader")
        service = None
        try:
            service = request.waitforcard()
        except CardRequestTimeoutException:
            print("ERROR: No card detected")
            exit(-1)

        # when a card is attached, open a connection
        conn = service.connection
        conn.connect()

        # get and print the ATR and UID of the card
        get_uid = util.toBytes("FF CA 00 00 00")
        ATR = util.toHexString(conn.getATR())
        data, sw1, sw2 = conn.transmit(get_uid)
        uid = util.toHexString(data)
        status = util.toHexString([sw1, sw2])
        dataTest(ATR, uid, status)