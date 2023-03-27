# WebP Image HTML Generator

This Python script generates HTML `<img>` tags for all the .webp image files in a specified directory. It assumes your image file names have dashes between the words in the filename.

## Usage

1. Clone the repository to your local machine.

2. Install Python 3 (if not already installed).

3. Open a terminal or command prompt and navigate to the cloned repository directory.

4. Modify the `directory` variable at the top of the `generate_html.py` file to specify the directory where your .webp images are located.

5. Run the `generate_html.py` script using Python by typing `python generate_html.py` in the terminal/command prompt.

6. The script will output the HTML <img> tags to the console. For example, if the file `Green-Mythic-ElephantEars-Alocasia-Baginda.webp` is in your directory, the script generates `<img src="Green-Mythic-ElephantEars-Alocasia-Baginda.webp" alt="Green Mythic ElephantEars Alocasia Baginda" title="Green Mythic ElephantEars Alocasia Baginda">` after the script is run. The same will happen to all .webp files in the directory. You can copy and paste these tags into your website or HTML document.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.