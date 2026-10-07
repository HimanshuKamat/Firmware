# Rebuild the full-quality video from its parts

GitHub does not accept single files over 100 MB, so the 1080p master is stored in 90 MB pieces.

    cd ganesha-video/09_final
    cat parts/Ganesha_Big_Race_1080p.mp4.part* > Ganesha_Big_Race_1080p.mp4
    sha256sum -c SHA256SUMS.txt        # should print OK for the video

On Windows (PowerShell): `cmd /c copy /b parts\Ganesha_Big_Race_1080p.mp4.part* Ganesha_Big_Race_1080p.mp4`

The 1080p master is 1920x1080, 24 fps, H.264 High, about 12 Mbps, AAC 320 kbps, -14 LUFS, 4:40.
