import socket
import struct
import textwrap

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '


# Main Function - Loops Infinitely Listening to Packets
def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, address = connection.recvfrom(65536)
        dest_mac, src_mac, ethernet_protocol, data = ETHERNET_FRAME(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, ethernet_protocol))

        # Protocol: 8 = IPv4
        if ethernet_protocol == 8:
            version, header_length, time_to_live, protocol, src, target, data = IPv4_PACKET(data)
            print(TAB_1 + 'IPv4 Packet:')
            print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(version, header_length, time_to_live))
            print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(protocol, src, target))

            # Protocol: 1 = ICMP
            if protocol == 1:
                icmp_type, code, checksum, data = ICMP_PACKET(data)
                print(TAB_1 + 'ICMP Packet:')
                print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(icmp_type, code, checksum))
                print(TAB_2 + 'ICMP Data:')
                print(FORMAT_DATA(DATA_TAB_3, data))

            # Protocol: 6 = TCP
            elif protocol == 6:
                src_port, dest_port, sequence, acknowledgement, flag_urgent, flag_acknowledge, flag_push, flag_reset, \
                    flag_synchronize, flag_finish, data = TCP_SEGMENT(data)
                print(TAB_1 + 'TCP Segment:')
                print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(src_port, dest_port))
                print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(sequence, acknowledgement))
                print(TAB_2 + 'Flags:')
                print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}'.format(flag_urgent, flag_acknowledge, flag_push))
                print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(flag_reset, flag_synchronize, flag_finish))
                print(FORMAT_DATA(DATA_TAB_3, data))

            # Protocol: 17 = UDP
            elif protocol == 17:
                src_port, dest_port, size, data = UDP_SEGMENT(data)
                print(TAB_1 + 'UDP Segment:')
                print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(src_port, dest_port, size))

            # Extra IPv4 Data
            else:
                print(TAB_1 + 'Extra IPv4 Data:')
                print(FORMAT_DATA(DATA_TAB_2, data))

        # Extra Ethernet Data
        else:
            print('Ethernet Data:')
            print(FORMAT_DATA(DATA_TAB_1, data))


# Extract Ethernet Frame Function
def ETHERNET_FRAME(data):
    dest_mac, src_mac, protocol = struct.unpack('! 6s 6s H', data[:14])
    return GET_MAC_ADDR(dest_mac), GET_MAC_ADDR(src_mac), socket.htons(protocol), data[14:]


# Format MAC Address Function (XX:XX:XX:XX:XX:XX)
def GET_MAC_ADDR(bytes_addr):
    bytes_string = map('{:02x}'.format, bytes_addr)
    return '.'.join(bytes_string).upper()


# Extract IPv4 Packet Function
def IPv4_PACKET(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    time_to_live, protocol, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, time_to_live, protocol, IPv4(src), IPv4(target), data[header_length:]


# Format IPv4 Address Function (000.000.000.000)
def IPv4(addr):
    return '.'.join(map(str, addr))


# Extract ICMP Packet Function
def ICMP_PACKET(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]


# Extract TCP Segment Function
def TCP_SEGMENT(data):
    src_port, dest_port, sequence, acknowledgement, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urgent = (offset_reserved_flags & 32) >> 5
    flag_acknowledge = (offset_reserved_flags & 16) >> 4
    flag_push = (offset_reserved_flags & 8) >> 3
    flag_reset = (offset_reserved_flags & 4) >> 2
    flag_synchronize = (offset_reserved_flags & 2) >> 1
    flag_finish = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgement, flag_urgent, flag_acknowledge, flag_push, flag_reset, \
        flag_synchronize, flag_finish, data[offset:]


# Extract UDP Segment Function
def UDP_SEGMENT(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]


# Data Formatter Function
def FORMAT_DATA(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()
