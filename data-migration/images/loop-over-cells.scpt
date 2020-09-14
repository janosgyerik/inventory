use AppleScript version "2.4" -- Yosemite (10.10) or later
use framework "Foundation"
use framework "AppKit"
use scripting additions

tell application "Numbers"
    activate
    tell first table of the active sheet of the front document
        
        -- set the value of cell "B3" to the value of the cell "A2"
        
        (*
        tell application "System Events" to keystroke "c" using command down
        delay 1
        
        set selection range to cell "B2"
        
        tell application "System Events" to keystroke "v" using command down
        *)
        
        
        -- ... to count columns / rows
        repeat with r from 5 to 6
            
            if the value of cell r of column 2 is not missing value then
                set imagePath to "/tmp/" & the value of cell r of column 2 & ".png"
                set selection range to cell r of column 1
                --set the clipboard to (value of cell r of column 1) as TIFF picture
                tell application "System Events" to keystroke "c" using {command down}
                delay 1
                clipboard info
                --set the clipboard to (the clipboard as TIFF picture)
                
                (* https://macscripter.net/viewtopic.php?id=46946
                set thePasteboard to current application's NSPasteboard's generalPasteboard()
                -- make bitmap rep of existing clipboard image
                set imageRep to (current application's NSBitmapImageRep's imageRepWithPasteboard:thePasteboard)
                -- extract jpeg data
                set theData to (imageRep's representationUsingType:(current application's NSJPEGFileType) ¬
                    |properties|:{NSImageCompressionFactor:0.7})
                -- write to temp file
                set thePath to POSIX path of (path to temporary items) & "Temp.jpg"
                (theData's writeToFile:thePath atomically:true)
                -- put the URL on the clipboard, ready for pasting into Mail
                set theURL to (current application's NSURL's fileURLWithPath:thePath)
                thePasteboard's clearContents()
                (thePasteboard's writeObjects:{theURL})
                *)
                
                (*
                tell application "System Events" to keystroke "c" using {command down}
                delay 1
                
                set imageData to get the clipboard
                
                set outFile to POSIX file ("/tmp/foo.png")
                tell application "Image Events"
                    launch
                    set thisImage to get the clipboard
                    save thisImage in outFile
                end tell
                *)
                
                (*
                set fh to open for access file imagePath with write permission
                set eof of the fh to 0
                write imageData to fh starting at 0
                close access fh
                *)
                
                (*
                tell application "Image Events"
                    launch
                    set thisImage to get the clipboard
                    save thisImage as TIFF in imagePath
                end tell
                *)
                
                --set selection range to cell 5 of column i
                --tell application "System Events" to keystroke "v" using command down
                --delay 1
                --do shell script "pbpaste > " & imagePath
                --delay 1
                --exit repeat
                --do shell script ("echo $(date) > " & imagePath)
            end if
            
        end repeat
        
    end tell
    
    -- set p to "/tmp/foo.png" as string
    -- set data to get the clipboard as "class PNG"
    -- set the clipboard to p
    -- set result to my writeToFile(data, path, false)
end tell

(*
on writeToFile(data, path)
    tell current application
        try
            return true
        on error msg
            log("script error: " & msg)
            return false
        end try
    end tell
end writeToFile *)
