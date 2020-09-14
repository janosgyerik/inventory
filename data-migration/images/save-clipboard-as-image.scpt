use AppleScript version "2.4" -- Yosemite (10.10) or later
use framework "Foundation"
use framework "AppKit"
use scripting additions

set thePasteboard to current application's NSPasteboard's generalPasteboard()
-- make bitmap rep of existing clipboard image
set imageRep to current application's NSBitmapImageRep's imageRepWithPasteboard:thePasteboard
-- extract jpeg data
set theData to imageRep's representationUsingType:(current application's NSJPEGFileType) |properties|:{NSImageCompressionFactor:0.7}
-- write to temp file
set thePath to POSIX path of (path to temporary items) & "Temp.jpg"
theData's writeToFile:thePath atomically:true
-- put the URL on the clipboard, ready for pasting into Mail
set theURL to current application's NSURL's fileURLWithPath:thePath
thePasteboard's clearContents()
thePasteboard's writeObjects:{theURL}
