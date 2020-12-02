from random import choices

with open("new_mp3.mp3", "w", encoding="Macintosh") as new_file, \
        open("base_file.txt", "r", encoding="Macintosh") as old_mp3_txt:

    mp3_text = old_mp3_txt.read().split("\n")
    song_line_len = len(mp3_text)
    average_chunk_length = 1000

    start_text = "\n".join(mp3_text[:100])
    end_text = "\n".join(mp3_text[-100:])

    chunk_options = ["\n".join(mp3_text[x:x + average_chunk_length])
                     for x in range(50, song_line_len-2000, average_chunk_length)]
    new_text = "\n".join(choices(chunk_options, k=int(song_line_len/(average_chunk_length/2))))

    new_file.write(start_text + new_text + end_text)
