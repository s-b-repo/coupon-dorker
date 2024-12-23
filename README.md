

---

# Coupon Dorking Tool 🛒🔍

**Coupon Dorking Tool** is a Python-based utility designed to automate advanced search queries (dorks) for finding coupon codes, promo codes, and discounts across various online platforms. Use this tool responsibly and in compliance with applicable laws and terms of service.

---

## Features 🌟

- **Predefined Dork Generation**: Automatically generates large coupon-related dorks.
- **Custom Dork Loading**: Supports loading dorks from a custom text file.
- **Automated Search**: Performs searches using predefined or custom dorks.
- **Save Results**: Outputs search results to a text file for easy reference.
- **User-Friendly**: Simple prompts for input and flexible configuration options.

---

## Installation 📥

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/coupon-dorking-tool.git
   cd coupon-dorking-tool
   ```

2. **Install dependencies**:
   Ensure Python is installed, then run:
   ```bash
   pip install google
   ```

3. **Run the script**:
   ```bash
   python coupon_dorking_tool.py
   ```

---

## Usage 🛠️

1. **Generate Default Dorks**:
   If no `dorks.txt` file is found, the tool will generate 15 predefined dorks.

2. **Custom Dorks**:
   Create a `dorks.txt` file in the same directory and populate it with your dorks, one per line.

3. **Perform Searches**:
   Follow the prompts to specify:
   - The number of results to retrieve per dork.
   - The dorks file to use (default is `dorks.txt`).

4. **Save Results**:
   Search results are saved in a file named `coupon_dorks_results.txt`.

---

## Example Dorks 📜

Here are a few examples of the dorks used by this tool:

- `site:retailmenot.com inurl:discount`
- `intitle:"promo codes" site:*.gov`
- `site:pastebin.com "coupon code"`
- `"valid coupon code" filetype:txt`

Feel free to customize and expand this list!

---

## Contributing 🤝

Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License 📄

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer ⚠️

This tool is intended for educational and ethical purposes only. The authors are not responsible for any misuse of this tool. Always comply with the terms of service of search engines and target platforms.

---

