# m3u-tools

m3u command line tool(s) to manage m3u music playlist from command line or scripts.

## m3u_fix, Fix File Paths in M3U Playlist

Is a python script which reads the existing m3u playlist, for each song checks whether file path is valid, if not it finds a new path based on the song filename in the media library provided as the 2nd argument.

Typical use cases:

- playlist was migrated from another computer, or
- directories have moved, during your organization or merged.

Example: 

    m3u-fix.py myplaylist.m3u ../../Shared/Music > corrected_playlist.m3u
    
Will replace all invalid file paths with the new Shared/Music library, using the relative paths.
