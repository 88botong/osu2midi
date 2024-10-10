from midiutil.MidiFile import MIDIFile
from osupyparser import OsuFile, Circle

# Load the OSU beatmap file
osu_beatmap = OsuFile("beatmap.osu").parse_file()
# Create a new MIDI file
midi_file = MIDIFile(1)

# Define variables
track = 0
time = 0
channel = 0
track_name = "osu! beatmap"
tempo = osu_beatmap.timing_points[0].bpm

# Add track and tempo to the MIDI file
midi_file.addTrackName(track, time, track_name)
midi_file.addTempo(track, time, tempo)

# Map the timing and note information to the MIDI file
for hit_object in osu_beatmap.hit_objects:

    if hit_object.__class__ == Circle:  # Hit circle
        note_time = hit_object.start_time / 60000 * tempo  # Convert note time in ms to beat number
        note_pitch = 60  # Set the note pitch to middle C
        note_duration = 1  # Set the note duration to 1 beat
        note_velocity = 127
        midi_file.addNote(track, channel, note_pitch, note_time, note_duration, note_velocity)

# Save the MIDI file to disk
with open("output.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
