import socket
import struct

MCAST_GRP = '224.0.1.60'
MCAST_PORT = 427

#        message size - vv  vv                                          vv  vv
message = ( b'\x01\x07\x01\x4C\x00\x00\x65\x6E\x00\x03\x00\x00\x00\x00\x01\x3C'
            b'(x-hp-ver=01)(x-hp-prod_id=CE841A)(x-hp-mac=08EDB912EE61)'
            b'(x-hp-guid=08EDB912EE61)(x-hp-num_port=01)(x-hp-ip=192.168.001.034)'
            b'(x-hp-hn=NPI12EE61)(x-hp-p1=MFG:Hewlett-Packard;'
            b'MDL:HP LaserJet Professional M1212nf MFP;'
            b'CMD:ZJS,HBS,URF,PCLm,PJL,ACL,HTTP;CLS:PRINTER;'
            b'DES:HP LaserJet Professional M1212nf MFP;FWVER:20110826;)' )

#        message size - vv  vv                                          vv  vv
messagE = ( b'\x01\x07\x01\x48\x00\x00\x65\x6E\x00\x03\x00\x00\x00\x00\x01\x38'
            b'(x-hp-ver=01)(x-hp-prod_id=CE841A)(x-hp-mac=08EDB912EE61)'
            b'(x-hp-guid=08EDB912EE61)(x-hp-num_port=01)(x-hp-ip=192.168.001.034)'
            b'(x-hp-hn=AVL-P)(x-hp-p1=MFG:Hewlett-Packard;'
            b'MDL:HP LaserJet Professional M1212nf MFP;'
            b'CMD:ZJS,HBS,URF,PCLm,PJL,ACL,HTTP;CLS:PRINTER;'
            b'DES:HP LaserJet Professional M1212nf MFP;FWVER:20110826;)' )


sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
#sock.setsockopt( socket.SOL_IP, socket.IP_MULTICAST_TTL, 64 )
#mreq = struct.pack( '4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY )
mreq = socket.inet_aton(MCAST_GRP) + socket.inet_aton('192.168.1.34')
sock.setsockopt( socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, mreq )
sock.setsockopt( socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1 )
sock.bind( ('', MCAST_PORT) ) # ( ('192.168.1.35', MCAST_PORT) )


while True:
    data, addr = sock.recvfrom( 4096 )
    print( 'Request from address:', addr )
    sock.sendto( message, addr )






#*******************************     END OF FILE     ***************************
