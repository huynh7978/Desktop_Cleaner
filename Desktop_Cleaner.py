import os
import shutil

file_list = []
i = 1
cleanup_directory = 'C:/Users/denni/Desktop/cleanup'

while os.path.exists(cleanup_directory):
    cleanup_directory = 'C:/Users/denni/Desktop/cleanup_' + str(i)
    i += 1

os.makedirs(cleanup_directory)

# Create subdirectories for different file types
documents_dir = os.path.join(cleanup_directory, 'Documents')
images_dir = os.path.join(cleanup_directory, 'Images')
videos_dir = os.path.join(cleanup_directory, 'Videos')
audio_dir = os.path.join(cleanup_directory, 'Audio')
installers_dir = os.path.join(cleanup_directory, 'Installers')

# Create subdirectories
for directory in [documents_dir, images_dir, videos_dir, audio_dir, installers_dir]:
    os.makedirs(directory, exist_ok=True)

# Define installer extensions and common installer names
installer_extensions = ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.appimage', '.run']
installer_keywords = [
    'setup', 'install', 'installer', 'steam', 'discord', 'chrome', 'firefox', 
    'vlc', 'zoom', 'skype', 'spotify', 'office', 'adobe', 'winrar', '7zip',
    'nvidia', 'amd', 'intel', 'driver', 'update', 'launcher'
]

def is_installer(filename):
    """Check if a file is likely an installer"""
    filename_lower = filename.lower()
    
    # Check if it has installer extension
    has_installer_ext = any(filename_lower.endswith(ext) for ext in installer_extensions)
    
    # Check if filename contains installer keywords
    has_installer_keyword = any(keyword in filename_lower for keyword in installer_keywords)
    
    return has_installer_ext and (has_installer_keyword or filename_lower.endswith('.exe') or filename_lower.endswith('.msi'))

file_list = os.listdir('C:/Users/denni/Desktop')
for file in file_list:
    print(f"Processing: {file}")
    
    # Skip the current script file and directories
    file_path = os.path.join('C:/Users/denni/Desktop', file)
    if file == os.path.basename(__file__) or os.path.isdir(file_path):
        continue
    
    # Check if it's an installer first
    if is_installer(file):
        print(f"  -> Moving to Installers: {file}")
        shutil.move(file_path, installers_dir)
    # Move files based on their extensions
    elif file.endswith(('.txt', '.doc', '.docx', '.pdf', '.rtf', '.odt')):
        print(f"  -> Moving to Documents: {file}")
        shutil.move(file_path, documents_dir)
    elif file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp')):
        print(f"  -> Moving to Images: {file}")
        shutil.move(file_path, images_dir)
    elif file.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v')):
        print(f"  -> Moving to Videos: {file}")
        shutil.move(file_path, videos_dir)
    elif file.endswith(('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a')):
        print(f"  -> Moving to Audio: {file}")
        shutil.move(file_path, audio_dir)
    else:
        print(f"  -> Moving to cleanup (other): {file}")
        shutil.move(file_path, cleanup_directory)

print(f"\nDesktop cleanup completed!")
print(f"Files organized in: {cleanup_directory}")
print(f"Installers moved to: {installers_dir}")
print(f"Documents moved to: {documents_dir}")
print(f"Images moved to: {images_dir}")
print(f"Videos moved to: {videos_dir}")
print(f"Audio moved to: {audio_dir}")