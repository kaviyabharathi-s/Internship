from music21 import stream, note, meter, tempo
import random

# Function to generate a random melody
def generate_random_melody(num_notes=16):
    melody = stream.Stream()
    
    # Define note choices (C4 to B4)
    pitches = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
    
    for _ in range(num_notes):
        pitch = random.choice(pitches)  # Randomly select a pitch
        dur = random.choice([1.0, 0.5, 0.25])  # Randomly select a duration
        melody.append(note.Note(pitch, quarterLength=dur))
    
    return melody

# Function to create a simple score with tempo and meter
def create_score(melody):
    score = stream.Score()
    part = stream.Part()
    
    # Add a time signature and tempo
    part.append(meter.TimeSignature('4/4'))
    part.append(tempo.MetronomeMark(number=120))
    
    # Add melody notes to part
    part.append(melody)
    
    # Add part to score
    score.append(part)
    
    return score

# Main program
if __name__ == "__main__":
    random_melody = generate_random_melody()
    score = create_score(random_melody)
    
    # Show the score
    score.show('text')  # Displays in text format
    score.show('midi')  # Play the generated melody as MIDI
    