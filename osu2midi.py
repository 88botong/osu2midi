directory = input("Directory: ")
beatmap = open(directory, "r")
# check if file is readable
if not beatmap.readable():
    print("File cannot be read")
else:
    print("Reading...")
    line = beatmap.readline()
    # checks for "HitObjects" section
    while "[HitObjects]" not in line:
        line = beatmap.readline()
    print("HitObject Section Found...")
    line = beatmap.readline()
    # check for ","
    while "," in line:
        # "items" as each item in the line
        items = line.split(',')
        # "time" set as the third item in the line
        time = int(items[2])
        print(time)
        line = beatmap.readline()
beatmap.close()
print("complete")

# print(line, end="")

# millisecond to beat
# change in tempo
# legato
# calculate duration of sliders
# write to a midi file

# Timing points
# time,beatLength,meter,sampleSet,sampleIndex,volume,uninherited,effects
# Hit objects
# x,y,time,type,hitSound,objectParams,hitSample
# Sliders
# x,y,time,type,hitSound,curveType|curvePoints,slides,length,edgeSounds,edgeSets,hitSample

# c:\users\88bot\appdata\local\osu!\Songs\62852 fripSide - only my railgun (TV size)\fripSide - only my railgun (TV size) (Chewin) [cRyo's Hard].osu