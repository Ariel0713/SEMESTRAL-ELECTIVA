import mido
from mido import MidiFile, MidiTrack, Message
import random
import os

# Función para generar una secuencia de notas aleatorias
def generate_random_notes(num_notes, note_range=(60, 80), velocity_range=(50, 100), duration_range=(0.1, 1.0)):
    notes = []
    for _ in range(num_notes):
        note = random.randint(note_range[0], note_range[1])
        velocity = random.randint(velocity_range[0], velocity_range[1])
        duration = random.uniform(duration_range[0], duration_range[1])
        notes.append((note, velocity, duration))
    return notes

# Función para agregar notas a una pista
def add_notes_to_track(track, notes, start_time=0):
    time = start_time
    for note, velocity, duration in notes:
        track.append(Message('note_on', note=note, velocity=velocity, time=int(time * 480)))
        track.append(Message('note_off', note=note, velocity=0, time=int(duration * 480)))
        time += duration

# Crear un archivo MIDI
mid = MidiFile()

# Crear la primera pista con un instrumento de piano
track1 = MidiTrack()
mid.tracks.append(track1)
track1.append(Message('program_change', program=0, time=0))  # Instrumento de piano

# Crear la segunda pista con un instrumento de guitarra
track2 = MidiTrack()
mid.tracks.append(track2)
track2.append(Message('program_change', program=24, time=0))  # Instrumento de guitarra

# Generar y agregar notas a las pistas
notes1 = generate_random_notes(20, note_range=(60, 72))  # Notas más bajas para el piano
add_notes_to_track(track1, notes1)

notes2 = generate_random_notes(20, note_range=(72, 84))  # Notas más altas para la guitarra
add_notes_to_track(track2, notes2)

# Guardar el archivo MIDI
output_file = 'random_music.mid'
mid.save(output_file)
print(f"Archivo MIDI generado: {output_file}")

# Reproducir el archivo MIDI automáticamente
try:
    import pygame
    from time import sleep

    # Inicializar pygame
    pygame.init()
    pygame.mixer.init()

    # Cargar y reproducir el archivo MIDI
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

    # Esperar hasta que la música termine
    while pygame.mixer.music.get_busy():
        sleep(1)
except ImportError:
    print("Pygame no está instalado. Instálalo usando 'pip install pygame' para reproducir el archivo MIDI automáticamente.")
