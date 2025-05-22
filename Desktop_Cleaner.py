import os
import shutil

# Get the OneDrive desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
print(f"Desktop path: {desktop_path}")

# Verify the path exists
if not os.path.exists(desktop_path):
    print(f"OneDrive Desktop not found, trying regular Desktop...")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop_path):
        print(f"Error: Desktop path not found!")
        exit(1)

file_list = []
i = 1
cleanup_directory = os.path.join(desktop_path, 'cleanup')

while os.path.exists(cleanup_directory):
    cleanup_directory = os.path.join(desktop_path, f'cleanup_{i}')
    i += 1

os.makedirs(cleanup_directory)

# Create subdirectories for different file types
documents_dir = os.path.join(cleanup_directory, 'Documents')
images_dir = os.path.join(cleanup_directory, 'Images')
videos_dir = os.path.join(cleanup_directory, 'Videos')
audio_dir = os.path.join(cleanup_directory, 'Audio')
installers_dir = os.path.join(cleanup_directory, 'Installers')
folders_dir = os.path.join(cleanup_directory, 'Folders')
shortcuts_dir = os.path.join(cleanup_directory, 'Shortcuts')
other_files_dir = os.path.join(cleanup_directory, 'Other_Files')

# Create subdirectories
for directory in [documents_dir, images_dir, videos_dir, audio_dir, installers_dir, folders_dir, shortcuts_dir, other_files_dir]:
    os.makedirs(directory, exist_ok=True)

# Define installer extensions and common installer names
installer_extensions = ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.appimage', '.run']
installer_keywords = [
    'setup', 'install', 'installer', 'steam', 'discord', 'chrome', 'firefox', 
    'vlc', 'zoom', 'skype', 'spotify', 'office', 'adobe', 'winrar', '7zip',
    'nvidia', 'amd', 'intel', 'driver', 'update', 'launcher', 'wallpaper',
    'visual studio', 'intellij', 'mcafee'
]

def is_installer(filename):
    """Check if a file is likely an installer"""
    filename_lower = filename.lower()
    
    # Check if it has installer extension
    has_installer_ext = any(filename_lower.endswith(ext) for ext in installer_extensions)
    
    # Check if filename contains installer keywords
    has_installer_keyword = any(keyword in filename_lower for keyword in installer_keywords)
    
    return has_installer_ext and (has_installer_keyword or filename_lower.endswith('.exe') or filename_lower.endswith('.msi'))

# Get all items on desktop
file_list = os.listdir(desktop_path)
moved_count = 0
skipped_count = 0

print(f"\nFound {len(file_list)} items on desktop:")
for item in file_list:
    print(f"  - {item}")

print(f"\nStarting cleanup process...")

for item in file_list:
    print(f"\nProcessing: {item}")
    
    item_path = os.path.join(desktop_path, item)
    
    # Skip the cleanup directory itself and the current script
    script_name = os.path.basename(__file__) if '__file__' in globals() else 'Desktop_Cleaner.py'
    if (item.startswith('cleanup') and os.path.isdir(item_path)) or item == script_name:
        print(f"  -> Skipping: {item}")
        skipped_count += 1
        continue
    
    try:
        # Handle directories (folders)
        if os.path.isdir(item_path):
            print(f"  -> Moving folder to Folders: {item}")
            destination = os.path.join(folders_dir, item)
            # Handle duplicate folder names
            counter = 1
            while os.path.exists(destination):
                destination = os.path.join(folders_dir, f"{item}_{counter}")
                counter += 1
            shutil.move(item_path, destination)
            moved_count += 1
            
        # Handle files
        else:
            # Check for shortcuts first
            if item.lower().endswith(('.lnk', '.url')):
                print(f"  -> Moving to Shortcuts: {item}")
                destination = os.path.join(shortcuts_dir, item)
            # Check if it's an installer
            elif is_installer(item):
                print(f"  -> Moving to Installers: {item}")
                destination = os.path.join(installers_dir, item)
            # Move files based on their extensions
            elif item.lower().endswith(('.txt', '.doc', '.docx', '.pdf', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv')):
                print(f"  -> Moving to Documents: {item}")
                destination = os.path.join(documents_dir, item)
            elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico')):
                print(f"  -> Moving to Images: {item}")
                destination = os.path.join(images_dir, item)
            elif item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v')):
                print(f"  -> Moving to Videos: {item}")
                destination = os.path.join(videos_dir, item)
            elif item.lower().endswith(('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a')):
                print(f"  -> Moving to Audio: {item}")
                destination = os.path.join(audio_dir, item)
            else:
                print(f"  -> Moving to Other Files: {item}")
                destination = os.path.join(other_files_dir, item)
            
            # Handle duplicate file names
            counter = 1
            original_destination = destination
            while os.path.exists(destination):
                name, ext = os.path.splitext(os.path.basename(original_destination))
                parent_dir = os.path.dirname(original_destination)
                destination = os.path.join(parent_dir, f"{name}_{counter}{ext}")
                counter += 1
                
            shutil.move(item_path, destination)
            moved_count += 1
            
    except PermissionError:
        print(f"  -> Permission denied: {item} (file may be in use)")
        skipped_count += 1
    except Exception as e:
        print(f"  -> Error moving {item}: {str(e)}")
        skipped_count += 1

print(f"\n" + "="*50)
print(f"DESKTOP CLEANUP COMPLETED!")
print(f"="*50)
print(f"Total items processed: {len(file_list)}")
print(f"Items moved: {moved_count}")
print(f"Items skipped: {skipped_count}")
print(f"\nAll your desktop items are now organized in:")
print(f"📁 {cleanup_directory}")
print(f"├── 🗂️  Folders (phone stuff, Games, etc.)")
print(f"├── 🔧 Installers (Steam, Discord, etc.)")
print(f"├── 📄 Documents")
print(f"├── 🖼️  Images") 
print(f"├── 🎥 Videos")
print(f"├── 🎵 Audio")
print(f"├── 🔗 Shortcuts (.lnk files)")
print(f"└── 📋 Other Files")
print(f"\n🎉 Your desktop should now be completely clean!")