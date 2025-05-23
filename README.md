# Desktop_Cleaner

automatically organizes your cluttered desktop by categorizing and moving files into organized folders.<br />

# 🚀**Features**<br />
Automatic file categorization - Sorts files by type (documents, images, videos, audio, etc.)<br />
Smart installer detection - Identifies and separates installer files from regular applications<br />
Folder organization - Moves desktop folders into a dedicated directory<br />
Duplicate handling - Automatically renames files if duplicates exist<br />
Cross-platform support - Works on Windows (OneDrive Desktop) and standard desktop locations<br />
Safe operation - Skips system files and the script itself<br />
Detailed logging - Shows exactly what's being moved where<br />

# 📁 **File Categories**<br />
The script organizes files into the following categories:<br />
| Category | File Extensions | Description |
|----------|----------------|-------------|
| :page_facing_up: **Documents** | `.txt`, `.doc`, `.docx`, `.pdf`, `.rtf`, `.odt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv` | Text documents, spreadsheets, presentations |
| :framed_picture: **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`, `.ico` | Pictures and graphics |
| :movie_camera: **Videos** | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v` | Video files |
| :musical_note: **Audio** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a` | Music and sound files |
| :wrench: **Installers** | `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm` | Application installers |
| :link: **Shortcuts** | `.lnk`, `.url` | Desktop shortcuts |
| :file_folder: **Folders** | N/A | Any directory on the desktop |
| :clipboard: **Other Files** | All others | Files that don't fit other categories |

# 🔧 **Installation**<br />
- **Prerequisites**<br />
    - Python 3.6 or higher
    - No additional packages required (uses built-in modules)
- Setup<br />
    Clone or download the script
    ```
    git clone https://github.com/yourusername/Desktop-Cleaner.git
    cd Desktop-cleaner
    ```
# 💻**Usage**<br />
**Basic Usage**<br />
```python/python3 desktop_cleanup.py```

**How It Works**<br />

Desktop Detection: Automatically finds your desktop location

:white_check_mark: First tries OneDrive Desktop (~/OneDrive/Desktop)<br />
:white_check_mark: Falls back to regular Desktop (~/Desktop)<br />

Cleanup Directory Creation: Creates a new folder called cleanup<br />
File Processing: Scans and categorizes all desktop items<br />
Progress Reporting: Shows real-time progress<br />

📊 **Output Structure**<br />
After running, your desktop will contain a new organized folder:<br />
📁 C:\Users\YourName\OneDrive\Desktop\cleanup<br />
├── 🗂️  Folders (My Projects, etc.)<br />
├── 🔧 Installers (Steam, Discord, etc.)<br />
├── 📄 Documents (PDFs, Word docs, etc.)<br />
├── 🖼️  Images (Photos, screenshots, etc.)<br />
├── 🎥 Videos<br />
├── 🎵 Audio<br />
├── 🔗 Shortcuts (.lnk files)<br />
└── 📋 Other Files<br />
    
# 🛡️ **Safety Features**<br />

Skips the cleanup directory - Won't move the folder it creates<br />
Skips the script itself - Won't move the cleanup script<br /><br />
Handles permissions errors - Gracefully handles files that can't be moved<br />
Duplicate prevention - Automatically renames files to prevent overwrites<br />
Non-destructive - Only moves files, never deletes them<br />

# **🎯 Smart Installer Detection**<br />
The script uses intelligent detection for installer files by checking:<br />

File extensions: ```.exe```, ```.msi```, ```.dmg```, ```.pkg```, etc.
```
installer_keywords = [
    'setup', 'install', 'installer', 'steam', 'discord', 'chrome', 'firefox', 
    'vlc', 'zoom', 'skype', 'spotify', 'office', 'adobe', 'winrar', '7zip',
    'nvidia', 'amd', 'intel', 'driver', 'update', 'launcher', 'wallpaper',
    'visual studio', 'intellij', 'mcafee'
]
```
📝 **Example Output**<br />
Desktop path: C:\Users\YourName\OneDrive\Desktop

Found 25 items on desktop:
  - important_document.pdf
  - vacation_photo.jpg
  - setup_steam.exe
  - My Projects

Starting cleanup process...

Processing: important_document.pdf<br />
  -> Moving to Documents: important_document.pdf<br />

Processing: vacation_photo.jpg<br />
  -> Moving to Images: vacation_photo.jpg<br />

Processing: setup_steam.exe<br />
  -> Moving to Installers: setup_steam.exe<br />

Processing: My Projects<br />
  -> Moving folder to Folders: My Projects<br />

==================================================
DESKTOP CLEANUP COMPLETED!
==================================================
Total items processed: 25
Items moved: 23
Items skipped: 2

All your desktop items are now organized in:<br />
📁 C:\Users\YourName\OneDrive\Desktop\cleanup<br />
├── 🗂️  Folders (phone stuff, Games, etc.)<br />
├── 🔧 Installers (Steam, Discord, etc.)<br />
├── 📄 Documents<br />
├── 🖼️  Images<br />
├── 🎥 Videos<br />
├── 🎵 Audio<br />
├── 🔗 Shortcuts (.lnk files)<br />
└── 📋 Other Files<br />

🎉 Your desktop should now be completely clean!
⚠️ Important Notes

Backup recommended: While the script is safe, consider backing up important files first
File permissions: Some files may be skipped if they're currently in use or lack permissions
System files: The script avoids moving system files and shortcuts to critical applications
Undo process: To restore files, simply move them back from the cleanup folder

#🐛 **Troubleshooting**<br />
Common Issues
Desktop not found: If the script can't find your desktop, it will show an error. Make sure you're running it on a system with a standard desktop folder structure.
Permission errors: Some files may be skipped due to permission issues. This is normal and safe - the script will continue with other files.
Files still on desktop: Check the output log to see if files were skipped and why.<br />

#**🤝 Contributing**<br />
Feel free to submit issues or suggestions for improvements. 

#**📄 License**<br />
This script is provided as-is for personal use. Feel free to modify and distribute as needed.
