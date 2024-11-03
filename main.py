def en_polsar_boto_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY), music.PlaybackMode.IN_BACKGROUND)

def en_polsar_boto_b():
    music.play(music.tone_playable(Note.G, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.F, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.E, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.D, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.C, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.D, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.E, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(Note.G, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)

def en_bucle():
    acc_y = input.acceleration(Dimension.Y)
    tempo = 120 + int(acc_y / 10)
    music.set_tempo(tempo)

input.on_button_pressed(Button.A, en_polsar_boto_a)
input.on_button_pressed(Button.B, en_polsar_boto_b)
basic.forever(en_bucle)
