# How to get "Ganesha's Big Race" onto your laptop

Everything lives on GitHub, in the folder `ganesha-video/09_final` of your repository **HimanshuKamat/Firmware**, branch **claude/amazing-pasteur-y5im4h**. You need to be signed in to GitHub in your browser.

Folder page: https://github.com/HimanshuKamat/Firmware/tree/claude/amazing-pasteur-y5im4h/ganesha-video/09_final

## Download these two files (that is all you need)

| # | File | What it is | Direct download |
|---|---|---|---|
| 1 | `Ganesha_Big_Race_1080p_download.mp4` | The whole video in one file: 4:40, 1920x1080, with sound. Plays on any laptop and can be uploaded to YouTube as is. | https://github.com/HimanshuKamat/Firmware/raw/claude/amazing-pasteur-y5im4h/ganesha-video/09_final/Ganesha_Big_Race_1080p_download.mp4 |
| 2 | `Ganesha_Big_Race_package.zip` | The Shorts video (1080x1920), the three thumbnails, captions (`captions.srt`), the YouTube title/description/tags (`youtube_metadata.md`) and the summary. Unzip it and everything is inside. | https://github.com/HimanshuKamat/Firmware/raw/claude/amazing-pasteur-y5im4h/ganesha-video/09_final/Ganesha_Big_Race_package.zip |

Click the link, or open the folder page, click the file name, then the **Download raw file** button (the down-arrow icon at the top right of the file).

## About quality

- File 1 is a one-file version sized to fit GitHub's 100 MB limit (about 2.6 Mbps video, 1080p). It looks clean on a laptop and YouTube re-compresses everything on upload anyway.
- The untouched master (about 12 Mbps, 427 MB) is stored as five pieces in `parts/`. If you want the master for archive or editing, download the five `part00` to `part04` files into one folder and join them (on Mac or Linux: `cat Ganesha_Big_Race_1080p.mp4.part* > Ganesha_Big_Race_1080p.mp4`; on Windows PowerShell: `cmd /c copy /b Ganesha_Big_Race_1080p.mp4.part* Ganesha_Big_Race_1080p.mp4`). Details in `parts/JOIN.md`.

## Get everything at once (optional)

Open https://github.com/HimanshuKamat/Firmware/tree/claude/amazing-pasteur-y5im4h, click the green **Code** button, then **Download ZIP**. That ZIP holds the whole project (scripts, scenes, pictures, audio, all of `09_final`), which is large, so for just the video and extras use the two files above.
