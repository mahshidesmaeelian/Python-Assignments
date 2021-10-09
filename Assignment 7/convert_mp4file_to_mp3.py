from moviepy import editor
video = editor.VideoFileClip('BTS (방탄소년단) Permission to Dance Official MV 1080p.mp4')
video.audio.write_audiofile('BTS (방탄소년단) Permission to Dance Official MV 1080p.mp3')
