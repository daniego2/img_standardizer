from PIL import Image
import json
import os
import colorlog

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    fmt="%(log_color)s%(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "white",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)
handler.setFormatter(formatter)
logger = colorlog.getLogger()
logger.setLevel("INFO")
logger.addHandler(handler)


def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"


def get_data():
    with open("config.json") as config:
        data = json.load(config)
    return data


def is_image(input_file):
    return input_file.lower().endswith(
        (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
    )


def convert_color_model(input_path, data):
    img = Image.open(input_path)
    if data["format"] == "png":
        img = img.convert("RGBA")
    elif data["format"] == "jpg":
        img = img.convert("RGB")
    return img


def parse_filename(filename):
    return "std_" + os.path.splitext(filename)[0]


def resize_img(img, width, height):
    img = img.resize((width, height))
    return img


def main():
    data = get_data()
    i = 0
    data["format"] = data["format"].lower()

    if not os.path.exists(data["input_path"]):
        logger.error(f"Input path '{data['input_path']}' does not exist.")
        return

    input_list = [file for file in os.listdir(data["input_path"]) if is_image(file)]
    os.makedirs(data["output_path"], exist_ok=True)

    logger.info(colorize(f"Attempting to process {len(input_list)} image(s)", "yellow"))
    logger.info(f"Config: {data['width']}x{data['height']}.{data['format']}")
    logger.info(f"Input: {data['input_path']} → Output: {data['output_path']}")

    for i, input_file in enumerate(input_list, 1):
        try:
            img = convert_color_model(
                os.path.join(data["input_path"], input_file), data
            )
            img = resize_img(img, data["width"], data["height"])
            filename = f"{parse_filename(input_file)}.{data['format']}"
            img.save(os.path.join(data["output_path"], filename), format=data["format"])
            logger.info(
                f"[{i}/{len(input_list)}] {colorize(filename, 'blue')} \u2714"
            )
        except Exception as e:
            logger.error(f"Error processing {colorize(input_file, 'red')}: {e}")

    logger.info(
        f"{colorize(f'{i}/{len(input_list)} image(s) processed successfully!', 'green')}"
    )


if __name__ == "__main__":
    main()
