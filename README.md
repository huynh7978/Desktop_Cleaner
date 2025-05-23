# Desktop_Cleaner

automatically organizes your cluttered desktop by categorizing and moving files into organized folders.
🚀 Features

Automatic file categorization - Sorts files by type (documents, images, videos, audio, etc.)
Smart installer detection - Identifies and separates installer files from regular applications
Folder organization - Moves desktop folders into a dedicated directory
Duplicate handling - Automatically renames files if duplicates exist
Cross-platform support - Works on Windows (OneDrive Desktop) and standard desktop locations
Safe operation - Skips system files and the script itself
Detailed logging - Shows exactly what's being moved where

📁 File Categories
The script organizes files into the following categories:
CategoryFile TypesDocuments.txt, .doc, .docx, .pdf, .rtf, .odt, .xls, .xlsx, .ppt, .pptx, .csvImages.jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp, .icoVideos.mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4vAudio.mp3, .wav, .flac, .aac, .ogg, .wma, .m4aInstallers.exe, .msi, .dmg, .pkg, .deb, .rpm (with installer keywords)Shortcuts.lnk, .urlFoldersAny directory on the desktopOther FilesEverything else that doesn't fit the above categories
🔧 Installation
Prerequisites

Python 3.6 or higher
No additional packages required (uses built-in modules)

Setup

Download the script file
Save it to your desired location (doesn't need to be on desktop)
Run the script

💻 Usage
Basic Usage
bashpython desktop_cleanup.py
What Happens When You Run It

Desktop Detection: The script automatically finds your desktop location

First tries OneDrive Desktop (~/OneDrive/Desktop)
Falls back to regular Desktop (~/Desktop)


Cleanup Directory Creation: Creates a new folder called cleanup (or cleanup_1, cleanup_2, etc.)
File Processing: Scans all desktop items and moves them to appropriate subdirectories
Progress Reporting: Shows real-time progress of what's being moved

📊 Output Structure
After running, your desktop will contain a new organized folder:
Desktop/
└── cleanup/
    ├── Documents/
    ├── Images/
    ├── Videos/
    ├── Audio/
    ├── Installers/
    ├── Folders/
    ├── Shortcuts/
    └── Other_Files/
🛡️ Safety Features

Skips the cleanup directory - Won't move the folder it creates
Skips the script itself - Won't move the cleanup script
Handles permissions errors - Gracefully handles files that can't be moved
Duplicate prevention - Automatically renames files to prevent overwrites
Non-destructive - Only moves files, never deletes them

🎯 Smart Installer Detection
The script uses intelligent detection for installer files by checking:

File extensions: .exe, .msi, .dmg, .pkg, etc.
Filename keywords: setup, install, installer, steam, discord, chrome, firefox, vlc, zoom, etc.
Combined logic: Must have installer extension AND contain relevant keywords

📝 Example Output
Desktop path: C:\Users\YourName\OneDrive\Desktop

Found 25 items on desktop:
  - important_document.pdf
  - vacation_photo.jpg
  - setup_steam.exe
  - My Projects

Starting cleanup process...

Processing: important_document.pdf
  -> Moving to Documents: important_document.pdf

Processing: vacation_photo.jpg
  -> Moving to Images: vacation_photo.jpg

Processing: setup_steam.exe
  -> Moving to Installers: setup_steam.exe

Processing: My Projects
  -> Moving folder to Folders: My Projects

==================================================
DESKTOP CLEANUP COMPLETED!
==================================================
Total items processed: 25
Items moved: 23
Items skipped: 2

All your desktop items are now organized in:
📁 C:\Users\YourName\OneDrive\Desktop\cleanup
├── 🗂️  Folders (phone stuff, Games, etc.)
├── 🔧 Installers (Steam, Discord, etc.)
├── 📄 Documents
├── 🖼️  Images
├── 🎥 Videos
├── 🎵 Audio
├── 🔗 Shortcuts (.lnk files)
└── 📋 Other Files

🎉 Your desktop should now be completely clean!
⚠️ Important Notes

Backup recommended: While the script is safe, consider backing up important files first
File permissions: Some files may be skipped if they're currently in use or lack permissions
System files: The script avoids moving system files and shortcuts to critical applications
Undo process: To restore files, simply move them back from the cleanup folder

🐛 Troubleshooting
Common Issues
Desktop not found: If the script can't find your desktop, it will show an error. Make sure you're running it on a system with a standard desktop folder structure.
Permission errors: Some files may be skipped due to permission issues. This is normal and safe - the script will continue with other files.
Files still on desktop: Check the output log to see if files were skipped and why.
🤝 Contributing
Feel free to submit issues or suggestions for improvements. Common enhancement ideas:

Additional file type categories
Custom organization rules
GUI interface
Scheduling capabilities

📄 License
This script is provided as-is for personal use. Feel free to modify and distribute as needed.
