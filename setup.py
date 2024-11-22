from setuptools import setup, find_packages

# Graceful fallback for README.md
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python package for rendering pixelated text in the console or terminal."

setup(
    name="pixel_pretender",
    version="1.0.0",
    author="Anasse Gassab",
    author_email="anasse.gsb@gmail.com",
    description="Render pixelated text in the console using customizable symbols and colors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnasseGX/Pixel_pretender",
    packages=find_packages(),  # Finds all packages within your module folder
    include_package_data=True,  # Include additional files if needed
    install_requires=[
        "colorama>=0.4.6",
        "rich>=13.9.0,<14.0.0",  # Flexible pinning for `rich`
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ASCII Unicode pixel art terminal text rendering color formatting",
    python_requires=">=3.8.0",
)
