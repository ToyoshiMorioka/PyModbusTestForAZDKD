# 運転No.
MotionNum_Min = 0 # Dec:6144, Hex:0x1800
MotionNum_Default = 0
MotionNum_Max = 255  # Dec:22464, Hex:0x57c0 255*64+6144
MotionNumAdress_Min = 6144
MotionNumAdress_Max = 22464
MotionNumAdress_Pitch = 64

# 方式（基準アドレス+0,1）: default:2
ControlMethod = {
    "AbsolutePosition" : 1, # 1:絶対位置決め
    "RelativePositionBasedOnOrderPosition" : 2, # 2:相対位置決め（指令位置基準）
    "RelativePositionBasedOnDetectPosition" : 3, # 3:相対位置決め（検出位置基準）
    "ContinusOperation" : 7 ,    # 7:連続運転（位置制御）
    "RoundAbsolutePositionOrder" : 8, # 8:ラウンド絶対位置決め
    "RoundNearPositionOrder" : 9, # 9:ラウンド近回り位置決め
    "RoundForwardAbsolutePositionOrder" : 10, # 10:ラウンドFWD方向絶対位置決め
    "RoundForwardReversePositionOrder" : 11, # 11:ラウンドRVS方向絶対位置決め
    "RoundAbsolutePress" : 12, # 12:ラウンド絶対押し当て
    "RoundNearPress" : 13, # 13:ラウンド近回り押し当て
    "RoundForwardPress" : 14, # 14:ラウンドFWD方向押し当て
    "RoundReversePress" : 15, # 15:ラウンドRVS方向押し当て
    "ContinusOperationWithSpeed" : 16, # 16:連続運転（速度制御）
    "ContinusOperationWithPress" : 17, # 17:連続運転（押し当て）
    "ContinusOperationWithTorque" : 18, # 18:連続運転（トルク）
    "AbsolutePositionPress" : 20, # 20:絶対位置決め押し当て
    "RerativePositionWithOrderPosition" : 21, # 21:相対位置決め押し当て（指令位置基準）
    "RerativePositionWithDetectPosition" : 22 # 22:相対位置決め押し当て（検出位置基準）
}
ControlMethod_Default = ControlMethod["RelativePositionBasedOnOrderPosition"]

# 位置（基準アドレス+2, 3）:default:0
# -2147483648 to 2147483647 step
Position_Max = 2147483647
Position_Default = 0
Position_Min = -2147483648

# 速度（基準アドレス+4, 5）:default:1000
# -4000000 to 4000000 Hz
Speed_Max = 4000000
Speed_Default = 1000
Speed_Min = -4000000

# 起動・変速（基準アドレス+6, 7）:default:1000000
# 1 to 1000000000 (1=0.01Khz/sec or 1= 0.001ms/Khz)
ChangeSpeed_Max = 1000000000
ChangeSpeed_Default = 1000000
ChangeSpeed_Min = 1

# 停止（基準アドレス+8, 9）:default:1000000
# 1 to 1000000000 (1=0.01Khz/sec or 1= 0.001ms/Khz)
Stop_Max = 1000000000
Stop_Default = 1000000
Stop_Min = 1

# 運転電流（基準アドレス+10 11） : default: 1000
# 0 to 1000(1=0.1%)
MotionSupply_Max = 1000
MotionSupply_Default = 1000
MotionSupply_Min = 0

# 運転終了遅延（基準アドレス+12, 13） : default:0
# 0 to 65535(1=0.001s)
MotionFinishDelay_Max = 65535
MotionFinishDelay_Default = 0
MotionFinishDelay_Min = 0

# 結合（基準アドレス+14, 15） : default:0
MergeMethod = {
    "NoMerge" : 0,    # 0:結合無
    "SelfSend" : 1,    # 1:手動順送
    "AutoSend" : 2,    # 2:自動順送
    "SurfaceSend" : 3    # 3:形状接続
}
Merge_Default = MergeMethod["NoMerge"]

# 結合先（基準アドレス）+16, 17:default:-1
# -256:STOP, -2:(+2), -1:(+1), 0 to 255:運転データNo
MergeTo_Stop = -256
MergeTo_PlusTwo = -2
MergeTo_PlusOne = -1
MergeTo_Max = 255
MergeTo_Default = MergeTo_PlusOne
MergeTo_Min = 0

# オフセット（エリア）（基準アドレス+18, 19）：default : 0
# -2147483648 to 2147483647 step
OffsetArea_Max = 2147483647
OffsetArea_Default = 0
OffsetArea_Min = -2147483648

# 幅（エリア）（基準アドレス+20, 21） default:-1
# -1:無効
# 0 to　4194303 step
WidthArea_Disable = -1
WidthArea_Max = 4194303
WidthArea_Default = WidthArea_Disable
WidthArea_Min = 0

# カウント（loop） （基準アドレス+22, 23） default:0
# 0:無し
# 2 to 255:ループ回数
CountLoop_Max = 255
CountLoop_Default = 0
countLoop_Min = 2

# 位置オフセット（基準アドレス+24, 25） default : 0
# -4194304 to 4194303 step
PositionOffset_Max = 4194303
PositionOffset_Default = 0
PositionOffset_Min = -4194304

# 終了（loop）（基準アドレス+26, 27） default:0
FinishLoop = {
    "Enable":0, # 0：なし
    "End":1 # 1: end
}

FinishLoop_Default = FinishLoop["Enable"]

# 弱イベント（基準アドレス+28, 29） default:-1
# -1:無し
# 0 to 31運転ioイベント
WeakEvent_Disable = -1
WeakEvent_Max = 31
WeakEvent_Default = WeakEvent_Disable
WeakEvent_Min = 0

# 強イベント（基準あdレス+30, 31） default:-1
# -1:無し
# 0 to 31運転ioイベント
StrongEvent_Disable = -1
StrongEvent_Max = 31
StrongEvent_Default = StrongEvent_Disable
StrongEvent_Min = 0
