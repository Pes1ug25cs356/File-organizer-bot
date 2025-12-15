# File-organizer-bot
Here is a professional and complete **README.md** description for your GitHub repository.

You can copy the text below directly into your GitHub repository's `README.md` file.

-----

# 📂 Automated File Organizer

A Python automation script that declutters your directories (like "Downloads" or "Desktop") by automatically sorting files into labeled folders based on their **File Type** or **File Size**.

## 🚀 About The Project

Digital clutter is a common problem. This script solves it by scanning a target directory and moving files into sub-directories, keeping your workspace clean and organized. It is built with Python using the `os` and `shutil` modules for efficient file system manipulation.

## ✨ Features

  * **Two Organization Modes:**
      * **By Type:** Sorts files into categories like `Images`, `Documents`, `Audio`, `Video`, `Archives`, and `Code`.
      * **By Size:** Sorts files into `Small_Files` (\<1MB), `Medium_Files` (1MB–100MB), and `Large_Files` (\>100MB).
  * **Safety First:** Includes error handling to prevent crashes if a file is currently in use or has permission issues.
  * **Cross-Platform:** Uses `os.path.join` to work seamlessly on Windows, macOS, and Linux.
  * **Smart Parsing:** Automatically handles case sensitivity (e.g., treats `.jpg` and `.JPG` the same).

## 🛠️ Built With

  * [Python 3.x](https://www.python.org/)
  * **Libraries:** `os`, `shutil` (Standard Python libraries, no external installation required).

## 💻 How to Run

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer
    ```

2.  **Run the Script**

    ```bash
    python file_organizer.py
    ```

3.  **Follow the Prompts**

      * Enter the full path of the folder you want to organize (e.g., `C:\Users\Name\Downloads`).
      * Choose your sorting method:
          * Press `1` for **File Type**
          * Press `2` for **File Size**

## 📂 Folder Structure Logic

The script automatically detects extensions and sorts them as follows:

| Category | Extensions |
| :--- | :--- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| **Documents** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| **Audio** | `.mp3`, `.wav`, `.flac` |
| **Video** | `.mp4`, `.mkv`, `.mov`, `.avi` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar` |
| **Code** | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp` |
| **Others** | Any other file types |

## 🔮 Future Improvements

  * [ ] Add a Graphical User Interface (GUI) for easier folder selection.
  * [ ] Add recursive scanning to organize sub-folders.
  * [ ] Implement a "Undo" feature to reverse changes.

## 👤 Author

**[Your Name]**

  * GitHub: [@pes1ug25cs356](https://github.com/yourusername)
  * GitHub: [@pes1ug25cs354](https://github.com/yourusername)
  * GitHub: [@pes1ug25cs353](https://github.com/yourusername)
  * GitHub: [@pes1ug25am273](https://github.com/yourusername)
