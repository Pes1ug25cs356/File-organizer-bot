import os
import shutil

def organize_by_type(directory):
    print(f"\nScanning '{directory}' for files...")
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Video': ['.mp4', '.mkv', '.mov', '.avi'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
    }

    
    misc_folder = "Others"

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories, only move files
        if os.path.isdir(file_path):
            continue
	
		if filename==os.path.basename(__file__):
	    	continue
        

        # Get the file extension (lowercase for easier matching)
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        destination_folder = misc_folder
        for folder, extensions in file_types.items():
            if extension in extensions:
                destination_folder = folder
                break

        # Create the folder if it doesn't exist
        destination_path = os.path.join(directory, destination_folder)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            print(f"Created folder: {destination_folder}")

        # Move the file
        try:
            shutil.move(file_path, os.path.join(destination_path, filename))
            print(f"Moved: {filename} -> {destination_folder}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

def organize_by_size(directory):
    print(f"\nScanning '{directory}' for files...")

    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        # Get file size in bytes
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024) # Convert to Megabytes

        if size_mb < 1:
            folder_name = "Small_Files"
        elif size_mb < 100:
            folder_name = "Medium_Files"
        else:
            folder_name = "Large_Files"

        # Create folder and move file
        destination_path = os.path.join(directory, folder_name)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            print(f"Created folder: {folder_name}")

        try:
            shutil.move(file_path, os.path.join(destination_path, filename))
            print(f"Moved: {filename} -> {folder_name}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

def main():
    print("--------------------------------------------------")
    print("       Welcome to the File Organizer Bot!      ")
    print("--------------------------------------------------")
    print("I can help you tidy up your messy folders.")
    
    while True:
        target_dir = input("\nPlease enter the full path of the folder to organize: ").strip()
        # Remove quotes 
        target_dir = target_dir.replace('"', '')
        
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            break
        else:
            print("That directory doesn't seem to exist. Please try again.")

    print("\nHow would you like to organize your files?")
    print("1. By Type (Images, Docs, etc.)")
    print("2. By Size (Small, Medium, Large)")
    
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            organize_by_type(target_dir)
            break
        elif choice == '2':
            organize_by_size(target_dir)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n--------------------------------------------------")
    print("All done! Your files are now organized.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()

