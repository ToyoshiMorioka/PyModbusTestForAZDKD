import AZDKDParameter

# 運転No.
MotionNum_Min = 0 # Dec:88, Hex:0x0058
MotionNum_Default = 0
MotionNum_Max = 255  # Dec:16408, Hex: 255*64+88
MotionNumAdress_Min = 88
MotionNumAdress_Max = 16408
MotionNumAdress_Pitch = 64

# 方式（基準アドレス+0,1）: default:2
ControlMethod_Default = AZDKDParameter.ControlMethod["RelativePositionBasedOnOrderPosition"]

# 位置（基準アドレス+2, 3）:default:0
# -2147483648 to 2147483647 step
Position_Max = AZDKDParameter.Position_Max
Position_Default = AZDKDParameter.Position_Default
Position_Min = AZDKDParameter.Position_Min

# 速度（基準アドレス+4, 5）:default:1000
# -4,000,000 to 4,000,000 Hz
Speed_Max = AZDKDParameter.Speed_Max
Speed_Default = AZDKDParameter.Speed_Default
Speed_Min = AZDKDParameter.Speed_Min

# 起動・変速（基準アドレス+6, 7）:default:1,000,000
# 1 to 1,000,000,000 (1=0.01Khz/sec or 1= 0.001ms/Khz)
ChangeSpeed_Max = AZDKDParameter.ChangeSpeed_Max
ChangeSpeed_Default = AZDKDParameter.ChangeSpeed_Default
ChangeSpeed_Min = AZDKDParameter.ChangeSpeed_Min

# 停止（基準アドレス+8, 9）:default:1,000,000
# 1 to 1,000,000,000 (1=0.01Khz/sec or 1= 0.001ms/Khz)
Stop_Max = AZDKDParameter.Stop_Max
Stop_Default = AZDKDParameter.Stop_Default
Stop_Min = AZDKDParameter.Stop_Min

# 運転電流（基準アドレス+10 11） : default: 1,000
# 0 to 1,000(1=0.1%)
MotionSupply_Max = AZDKDParameter.MotionSupply_Max
MotionSupply_Default = AZDKDParameter.MotionSupply_Default
MotionSupply_Min = AZDKDParameter.MotionSupply_Min

# 反映トリガ（基準アドレス+12, 13） : default:0
FeedbackTrigger = {
    "MotionNo" : -7,    # -7:運転データNo
    "Method" : -6,    # -6:方式
    "Position" : -5,    # -5:位置
    "Speed" : -4,    # -4:速度
    "ChangeSpeed" : -3, # -3:起動・変速レート
    "Stop" : -2, # -2:停止レート
    "MotionSupply" : -1, # -1:運転電流
    "Disable" : 0, # 0:無効
    "AllDataFeedback": 1 # 1:全データ反映
}
FeedbackTrigger_Default = FeedbackTrigger["Disable"]

# 転送先（基準アドレス+14, 15） default:0
TransportDestination = {
    "ExecutionMemory":0, # 0：実行メモリ
    "BufferMemory":1 # 1: バッファメモリ
}
TransportDestination_Default = TransportDestination["ExecutionMemory"]
