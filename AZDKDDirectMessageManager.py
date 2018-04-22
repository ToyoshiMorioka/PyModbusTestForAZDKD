from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import AZDKDDirectParameter

method = AZDKDDirectParameter.ControlMethod_Default
position = AZDKDDirectParameter.Position_Default
speed = AZDKDDirectParameter.Speed_Default
changeSpeed = AZDKDDirectParameter.ChangeSpeed_Default
stop = AZDKDDirectParameter.Stop_Default
motionSupply = AZDKDDirectParameter.MotionSupply_Default
feedbuckTrigger = AZDKDDirectParameter.FeedbackTrigger_Default
transportDestination = AZDKDDirectParameter.TransportDestination_Default

def makeMotionParameter():
    # Direct運転 P.292, P.351
    builder = BinaryPayloadBuilder(byteorder=Endian.Big)
    builder.add_32bit_int(0)
    builder.add_32bit_int(method)
    builder.add_32bit_int(position)
    builder.add_32bit_int(speed)
    builder.add_32bit_int(changeSpeed)
    builder.add_32bit_int(stop)
    builder.add_32bit_int(motionSupply)
    # builder.add_32bit_int(feedbackTrigger)
    builder.add_32bit_int(AZDKDDirectParameter.FeedbackTrigger["AllDataFeedback"])
    builder.add_32bit_int(transportDestination)

    # builder.add_32bit_int(0)
    # builder.add_32bit_int(1)
    # builder.add_32bit_int(8500)
    # builder.add_32bit_int(2000)
    # builder.add_32bit_int(1500)
    # builder.add_32bit_int(1500)
    # builder.add_32bit_int(100)
    # builder.add_32bit_int(1)
    return  builder.build()

def getAddress():
    return AZDKDDirectParameter.MotionNumAdress_Min # hex: 0x0058
