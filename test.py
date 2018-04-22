import serial
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
import AZDKDMessageManager
import AZDKDParameter
import AZDKDDirectMessageManager
import AZDKDDirectParameter
    # modbus rtu commando
    # slave address : 8bit
    # fuction code : 8bit
    # data : N * 8bit
    # error check(CRC-16) : 16bit

    # function code
    # read register : 0x03
    # - register count : 1 - 125
    # write register : 0x06
    # - register count : 1
    # check status : 0x08
    # - register count: -
    # write registers : 0x10
    # - register count : 1 - 123
    # readwrite registers : 0x17
    # - read register count : 1 - 125
    # - write register count : 1 - 121

def normalCommando(client):
    # 運転No更新
    AZDKDMessageManager.position = 1000
    result = client.write_registers(address=AZDKDMessageManager.getAddress(0), values=AZDKDMessageManager.makeMotionParameter(), unit=0x01, skip_encode=True)
    print(result)

    # 運転スタート
    result = client.write_registers(address=0x007c, values=getPayload(8), unit=0x01, skip_encode=True)
    print(result)

    # 運転終了
    result = client.write_registers(address=0x007c, values=getPayload(0), unit=0x01, skip_encode=True)
    print(result)
    return

def directCommando(client):
    # Direct運転 P.292, P.351
    # builder = BinaryPayloadBuilder(byteorder=Endian.Big)
    # builder.add_32bit_int(0)
    # builder.add_32bit_int(1)
    # builder.add_32bit_int(8500)
    # builder.add_32bit_int(2000)
    # builder.add_32bit_int(1500)
    # builder.add_32bit_int(1500)
    # builder.add_32bit_int(100)
    # builder.add_32bit_int(1)
    # client.write_registers(address=0x0058, values=builder.build(), unit=0x01, skip_encode=True)
    AZDKDDirectMessageManager.method = AZDKDParameter.ControlMethod["AbsolutePosition"]
    AZDKDDirectMessageManager.position = 0
    result = client.write_registers(address=AZDKDDirectMessageManager.getAddress(), values=AZDKDDirectMessageManager.makeMotionParameter(), unit=0x01, skip_encode=True)
    print(result)
    return

def getPayload(num):
    builder = BinaryPayloadBuilder(byteorder=Endian.Big)
    builder.add_32bit_int(num)
    return builder.build()

if __name__ == '__main__':
    client = ModbusClient(method = "rtu", port="COM6",stopbits = 1, bytesize = 8, parity = 'E', baudrate= 115200, timeout= 0.02)

    connection = client.connect()
    print('connection result:{0}'.format(connection))

    directCommando(client)

    # 接続終了
    client.close()
    print('connection close.')
