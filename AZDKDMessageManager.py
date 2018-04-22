from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
import AZDKDParameter
import AZDKDDirectParameter

method = AZDKDParameter.ControlMethod_Default # 方式（基準アドレス+0,1）: default:2
position = AZDKDParameter.Position_Default # 位置（基準アドレス+2, 3）:default:0
speed = AZDKDParameter.Speed_Default # 速度（基準アドレス+4, 5）:default:1000
changeSpeed = AZDKDParameter.ChangeSpeed_Default # 起動・変速（基準アドレス+6, 7）:default:1000000
stop = AZDKDParameter.Stop_Default # 停止（基準アドレス+8, 9）:default:1000000
motionSupply = AZDKDParameter.MotionSupply_Default # 運転電流（基準アドレス+10 11） : default: 1000
motionFinishDelay = AZDKDParameter.MotionFinishDelay_Default # 運転終了遅延（基準アドレス+12, 13） : default:0
merge = AZDKDParameter.Merge_Default # 結合（基準アドレス+14, 15） : default:0
mergeTo = AZDKDParameter.MergeTo_Default # 結合先（基準アドレス）+16, 17:default:-1
offsetArea = AZDKDParameter.OffsetArea_Default # オフセット（エリア）（基準アドレス+18, 19）：default : 0
widthArea = AZDKDParameter.WidthArea_Default # 幅（エリア）（基準アドレス+20, 21） default:-1
countLoop = AZDKDParameter.CountLoop_Default # カウント（loop） （基準アドレス+22, 23） default:0
postionOffset = AZDKDParameter.PositionOffset_Default # 位置オフセット（基準アドレス+24, 25） default : 0
finishLoop = AZDKDParameter.FinishLoop_Default # 終了（loop）（基準アドレス+26, 27） default:0
weakEvent = AZDKDParameter.WeakEvent_Default # 弱イ.ベント（基準アドレス+28, 29） default:-1
strongEvent =  AZDKDParameter.StrongEvent_Default # 強イベント（基準あdレス+30, 31） default:-1

def makeMotionParameter():
    builder = BinaryPayloadBuilder(byteorder=Endian.Big)
    builder.add_32bit_int(method) # 方式（基準アドレス+0,1）
    builder.add_32bit_int(position) # 位置（基準アドレス+2, 3）
    builder.add_32bit_int(speed) # 速度（基準アドレス+4, 5）
    builder.add_32bit_int(changeSpeed) # 起動・変速（基準アドレス+6, 7）
    builder.add_32bit_int(stop) # 停止（基準アドレス+8, 9）
    builder.add_32bit_int(motionSupply) # 運転電流（基準アドレス+10 11）
    builder.add_32bit_int(motionFinishDelay)  # 運転終了遅延（基準アドレス+12, 13）
    builder.add_32bit_int(merge) # 結合（基準アドレス+14, 15）
    builder.add_32bit_int(mergeTo)# 結合先（基準アドレス+16, 17）
    builder.add_32bit_int(offsetArea) # オフセット（エリア）（基準アドレス+18, 19）
    builder.add_32bit_int(widthArea) # 幅（エリア）（基準アドレス+20, 21）
    builder.add_32bit_int(countLoop)  # カウント（loop） （基準アドレス+22, 23）
    builder.add_32bit_int(postionOffset) # 位置オフセット（基準アドレス+24, 25）
    builder.add_32bit_int(finishLoop)  # 終了（loop）（基準アドレス+26, 27）
    builder.add_32bit_int(weakEvent) # 弱イ.ベント（基準アドレス+28, 29）
    builder.add_32bit_int(strongEvent) # 強イベント（基準ドレス+30, 31）
    return builder.build()

def getAddress(motionNumber):
    return motionNumber * AZDKDParameter.MotionNumAdress_Pitch + AZDKDParameter.MotionNumAdress_Min
