import serial
from pydub import AudioSegment
from pydub.playback import play

ser = serial.Serial('COM3', 9600, timeout=0)
string10 = AudioSegment.from_file("VIOLIN G3.wav") 
string20 = AudioSegment.from_file("VIOLIN D4.wav") 
string30 = AudioSegment.from_file("VIOLIN A4.wav")
string40 = AudioSegment.from_file("VIOLIN E5.wav")
string11 = AudioSegment.from_file("VIOLIN A3.wav")
string21 = AudioSegment.from_file("VIOLIN E4.wav")
string31 = AudioSegment.from_file("VIOLIN B4.wav")
string41 = AudioSegment.from_file("VIOLIN F5.wav") 

string12 = AudioSegment.from_file("VIOLIN B3.wav")
string22 = AudioSegment.from_file("VIOLIN F4.wav") 
string32 = AudioSegment.from_file("VIOLIN C5.wav")
string42 = AudioSegment.from_file("VIOLIN G5.wav") 

string13 = AudioSegment.from_file("VIOLIN C4.wav")
string23 = AudioSegment.from_file("VIOLIN G4.wav")
string33 = AudioSegment.from_file("VIOLIN D5.wav") 
string43 = AudioSegment.from_file("VIOLIN A5.wav") 

while True:
    ser.flushInput()
    ser.flushOutput()
    try:
        byte = int(ser.read_all().decode())
        byte = str(bin(byte))
        analysis = byte[2:]
        if len(analysis) == 5:
            pot = analysis[0]
            sensors = list(analysis[1:])
        if len(analysis) == 6:
            pot = analysis[0:2]
            sensors = list(analysis[2:])
        if len(analysis) == 7:
            pot = analysis[0:3]
            sensors = list(analysis[3:])
        if len(analysis) == 8:
            pot = analysis[0:4]
            sensors = list(analysis[4:])
        msb = sensors.index('1')
        print(pot, sensors)
        if pot == "1":
            match msb:
                case 0:
                    play(string10)
                case 1:
                    play(string20)
                case 2:
                    play(string30)
                case 3:
                    play(string40)
        if pot == "10":
            match msb:
                case 0:
                    play(string11)
                case 1:
                    play(string21)
                case 2:
                    play(string31)
                case 3:
                    play(string41)
        if pot == "100":
            match msb:
                case 0:
                    play(string12)
                case 1:
                    play(string22)
                case 2:
                    play(string32)
                case 3:
                    play(string42)
        if pot == "1000":
            match msb:
                case 0:
                    play(string13)
                case 1:
                    play(string23)
                case 2:
                    play(string33)
                case 3:
                    play(string43)
    except ValueError:
        continue