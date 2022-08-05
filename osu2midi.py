from midiutil.MidiFile import MIDIFile

directory = input("Directory: ")
beatmap = open(directory, "r")
# check if file is readable
if not beatmap.readable():
    print("File cannot be read")
else:
    print("Reading TimingPoints...")
    line = beatmap.readline()
    # checks for "HitObjects" section
    while "[TimingPoints]" not in line:
        line = beatmap.readline()
    print("TimingPoints Section Found...")
    line = beatmap.readline()
    # check for ","
    while "," in line:
        # "items" as each item in the line
        items = line.split(',')
        # "time" set as the third item in the line
        beat_length = float(items[1])
        if beat_length > 0:
            global_beat_length = beat_length
            tempo = round(60000 / beat_length)
        print("The tempo is: " + str(tempo))
        line = beatmap.readline()

    print("Reading HitObjects...")
    line = beatmap.readline()
    # checks for "HitObjects" section
    while "[HitObjects]" not in line:
        line = beatmap.readline()
    print("HitObject Section Found...")

    timing_list_ms = []  # Create a list of timings

    line = beatmap.readline()  # Move to the next line
    while "," in line:  # check for ","
        items = line.split(',')  # "items" as list of each item in the line
        time = int(items[2])  # "time" as the third item in the line
        timing_list_ms.append(time)  # Append the time to the list
        line = beatmap.readline()
    print(timing_list_ms)
beatmap.close()
print("Reading complete")

timing_list_beats = [item / global_beat_length for item in timing_list_ms]     # Convert from milliseconds to beats
print(timing_list_beats)
# Create a midi file with 1 track
midi_file = MIDIFile(1)
track = 0  # Track number
time = 0  # Start time
name = "osu"  # Name of track
midi_file.addTrackName(track, time, name)
midi_file.addTempo(track, time, tempo)
# Set channel, volume, and pitch
channel = 0
volume = 100
pitch = 36  # C1

# Add notes

for index in range(len(timing_list_beats)):
    time = timing_list_beats[index]  # Starting time in beats
    duration = 1  # Length in beats
    midi_file.addNote(track, channel, pitch, time, duration, volume)

with open("output.mid", 'wb') as output:
    midi_file.writeFile(output)

# Conversion
# Tempo (BPM) = 60000 / BeatLength (millisecond)
# Beat = BeatTiming / BeatLength

# Todo
# AudioLeadIn
# changes in tempo
# calculate duration of sliders
# length of note match slider and spinner
# track name as song name

# Timing points
# time,beatLength,meter,sampleSet,sampleIndex,volume,uninherited,effects
# Hit objects
# x,y,time,type,hitSound,objectParams,hitSample
# Sliders
# x,y,time,type,hitSound,curveType|curvePoints,slides,length,edgeSounds,edgeSets,hitSample
