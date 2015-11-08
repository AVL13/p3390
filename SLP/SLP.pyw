
# RFC 2609

import sys
from PyQt4 import QtCore, QtGui


def addDevice( model, devModel, productID, IPAddress, MACAddress, firmwareVersion ):
    model.insertRow( 0 )
    model.setData( model.index(0,0), devModel )
    model.setData( model.index(0,1), productID )
    model.setData( model.index(0,2), IPAddress )
    model.setData( model.index(0,3), MACAddress )
    model.setData( model.index(0,4), firmwareVersion )

application = QtGui.QApplication( sys.argv )


model = QtGui.QStandardItemModel( 0, 5 )
model.setHorizontalHeaderLabels( ['Model', 'Product ID', 'IP Address', 'MAC Address', 'Firmware version'] )

addDevice( model, 'HP LaserJet Professional M1212nf MFP', 'CE841A', '172.31.100.189',
                  '10604B135C88', '20110826' )


devicesTreeView = QtGui.QTreeView()
devicesTreeView.setModel( model )
devicesTreeView.show()

sys.exit( application.exec_() )
