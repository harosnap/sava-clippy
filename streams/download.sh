#!/bin/bash
yt-dlp -r 5M -f bestvideo+bestaudio --write-thumbnail --write-info-json -o '%(upload_date)s__%(id)s__%(title)s.%(ext)s' $*
