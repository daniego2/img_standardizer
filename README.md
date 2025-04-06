
# 🖼️ img_standardizer

A simple Python script to resize and convert images from an input folder, based on a user-defined configuration.

---



## 📂 Project Structure

```
img_standardizer/
├── input/            # Place your source images here
├── output/           # Processed images will be saved here
├── config.json       # Set configuration here
├── main.py           # Main script
├── requirements.txt  # Dependencies list
└── README.md         # Documentation
```


---

## ⚙️ Configuration

Edit the `config.json` file to define how images should be processed:

```json
{
  "input_path": "input",
  "output_path": "output",
  "width": 800,
  "height": 800,
  "format": "png"
}
```
Supported formats: "png" and "jpg"

## 🛠️ Installation

    ⚠️ Make sure you have Python 3.7+ installed.

Clone the repo and install dependencies:
```
source venv/bin/activate
pip install -r requirements.txt
```
## ▶️ Usage

Once dependencies are installed, the config is set and your images are in the input folder run:

```
python main.py
```
